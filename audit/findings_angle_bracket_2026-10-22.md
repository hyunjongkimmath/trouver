# Findings: LaTeX `<` vs bs4 in the HTML extraction chain (2026-10-22)

## Mechanism (two distinct damages)

1. **Parse-time swallowing** (fixed 2026-10-22, `helper.html`).
   `BeautifulSoup(text, 'html.parser')` treats any `<letter … >` as a tag: LaTeX
   `$a<b$ and $c>d$` becomes a bogus tag named `b$` and everything between `<` and
   the next `>` turns into *attributes*, vanishing from `raw_text`. A math `<`
   inside a real mark (e.g. `<span notation="">$x<y$</span>`) even swallows the
   closing tag, corrupting the span range and its text. The old mitigation
   (`add_space_to_lt_symbols_without_space`) was applied only by the auto-marking
   path — never on the extraction path — and covered only unspaced `<` inside
   `latex_indices`-detected math (fails when `$`-pairing fails).

2. **On-disk corruption** (damage already in 22 vault notes, NOT fixed by code).
   Some past write-back serialized soup into the markdown itself: LaTeX tokens now
   sit in unquoted attribute positions (`$$=""`, `$a<r="" …`) inside the `.md`
   files. The swallowed `<`/`>` delimiters are unrecoverable from the current text;
   repair needs pre-corruption versions (vault history).

## Fix shipped

`escape_lt_symbols_that_do_not_open_html_tags` (nb `01_helper_08.html`, exported),
called by `remove_html_tags_in_text` before parsing, two rules:
1. every `<` inside a `latex_indices` math region escapes unconditionally — math
   never contains HTML, and `$0<b>$` looks exactly like a bare tag (a lookalike
   there would otherwise become an element and silently drop nested real marks);
2. outside math, a `<` survives only when it opens a complete tag (quoted
   attribute values included) whose **unquoted** part contains no `$` or `\` —
   real HTML never contains LaTeX; bs4 garbage always does.

`bs4` decodes `&lt;` back, so `raw_text` is character-exact and span indices stay
consistent. Characterization-first: pins green against old code, then flipped.

Verified (2026-10-22): the 4 known-broken extraction cases round-trip verbatim
(rudin 1992→1992 chars, katz 3698→3698; weibel/li_vhlcp diffs are only genuine
`</b>`/`</span>` markup removals); `$a<b$`, dollar-stripped `a<b$ and c>d`, and
bare lookalikes `$0<b>$` all survive verbatim with no bogus tags; real tags keep
attrs/closing tag/exact text (incl. a mark whose math content contains `<b>`);
entity and typo-attribute flows unchanged. All 8 consumer notebooks green.

**Residual risk (accepted):** non-math prose that genuinely looks like a clean
tag (`a<b> and c>d`, e.g. hypothetical text with *both* delimiting `$` stripped)
is still parsed as HTML — indistinguishable from real markup. In the pipeline,
dollar-stripping augmentation runs at token level *after* parsing, so such a
string never re-enters `bs4`; documented in the notebook.

## 22 vault notes with on-disk garbage (scan `_tmp/scan_disk_garbage_tmp.py`)

hindry_silverman_Theorem D.7.1 · foag_ 16.7.C · foag_page_130 ·
szamuely_gg_6.7.4 Proposition · hartshorne_Proposition 7.6 ·
harris_morrison_moc_3.44 LEMMA · katz_esde_5.5.2 Sublemma_page_175 ·
olsson_ass_ 2.5_page_65_6 · rudin_principles_Theorem 5.13 ·
ellenberg_venkatesh_westerland_ 6.1 · silverman_ 9.10 ·
silverman_1.2 Proposition_page_270 · silverman_Definition_page_271 ·
silverman_5.5 Theorem_page_289 · silverman_3.1 Theorem_page_165 ·
silverman_4.8 Conjecture · silverman_5.3 Theorem_page_382 ·
silverman_AT_Example 6.2.2_3 · silverman_AT_Lemma 9.3 ·
silverman_AT_Theorem 4.2_page_473 · koymans_pagano_omcngi_0. 4. Analytic considerations_3 ·
koymans_pagano_omcngi_0. 4. Analytic considerations_5

## Vault-wide residual-edge-case scan (2026-10-22)

Searched all 159,458 vault notes for `<` the fixed rule still lets parse as HTML
(`_tmp/scan_lt_edge_tmp.py`, `scan_lt_attr_tmp.py`, `scan_lt_punct_tmp.py`,
`scan_lt_loss_tmp.py`; details `_tmp/scan_lt_edge_out.txt`):

- 16,918 notes contain tag-shaped `<`; only **100** hold a survivor that is not
  vault markup: SMILES pseudo-tags (`<smiles>…</smiles>`), placeholder names in
  meta notes (`<source>`, `<subject>` — inside backticks), Magma/Graphviz code
  (`P<x,y,z>` inside ``` fences), GUI key names (`<Ctrl>`).
- Real-chain difflib on all candidates: **zero** non-markup text loss.
- Targeted hunts for the true damage class (prose swallowed as tag attributes,
  incl. punctuation blobs like `<a,b,c>`) across the whole vault, outside math
  and code: **0 hits**.

Conclusion: no live vault content is mis-parsed post-fix; every surviving
tag-lookalike sits inside fenced/inline code (HTML-escaped before `bs4`) or is
intended pseudo-markup whose text bs4 preserves. The residual ambiguity
(`a<b> and c>d` in plain prose) does not occur in the vault today.

## Follow-ups

- **Repair**: no vault history exists for these notes (user confirmed
  2026-10-22) — the delimiters are permanently lost; repair = manual re-typing
  of the mangled lines if ever wanted. Decision: treat the 22 as permanently
  dirty and **exclude them from producer-v2 datasets** (#17) — and therefore
  from the #21 freeze.
- **Write-back gate (#18)**: no pass may serialize soup back into vault markdown
  without escaping non-tag `<` (same helper applies); add the dry-run gate there.
- Dataset regeneration picks the parse fix up automatically (producer calls
  `html_data_from_note` → `remove_html_tags_in_text`).
