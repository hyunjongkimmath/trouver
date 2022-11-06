---
cssclass: clean-embeds
aliases: [lombardo_av_Tates_conjecture, lombardo_av_Faltings_Tate_theorem]
tags: [_auto/notations_added, _meta/concept, _auto/links_added, _meta/TODO/change_title, _meta/literature_note, _reference/lombardo_av, _meta/permanent_note]
---
# Tate's conjecture[^1]
(Faltings, Tate). Let $A, B$ be [[lombardo_av_1.3|abelian varieties]] defined over a common field $K$ (either a [[number_field|number field]] or a [[foag_finite_morphism_of_schemes|finite]] field). 

There is a natural isomorphism

$$\operatorname{Hom}_{K}(A, B) \otimes_{\mathbb{Z}} \mathbb{Q}_\ell \cong \operatorname{Hom}_{\mathrm{Gal}(K / K)}\left(\operatorname{V}_{\ell}(A), \operatorname{V}_{\ell}(B)\right)$$
[^2][^3][^4] ^fc419c

where $\mathrm{Hom}_{\mathrm{Gal}(\bar{K} / K)}\left(V_{\ell}(A), V_{\ell}(B)\right)$[^2][^3]               denotes the group of $\mathbb{Q}_{\ell}$-linear homomorphisms
$$
g: V_{\ell}(A) \rightarrow V_{\ell}(B)
$$
[^2][^3]
that satisfy
$$
\sigma(g(v))=g(\sigma(v)) \quad \forall v \in V_{\ell}(A), \forall \sigma \in \operatorname{Gal}(\bar{K} / K)
$$
[^2][^3]

# See Also
- [[lombardo_av_REMARK 2.11]]
# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, THEOREM 2.10, Page 41
[^2]: ![[lombardo_av_notation_V_ell_A]]
[^3]: ![[lombardo_av_notation_V_ell_A_rational_tate_module]]
[^4]: ![[foag_notation_Hom_K_A_B_abelian_varieties]]