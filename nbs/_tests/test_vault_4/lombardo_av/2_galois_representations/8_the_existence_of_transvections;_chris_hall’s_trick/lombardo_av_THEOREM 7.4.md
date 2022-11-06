---
cssclass: clean-embeds
aliases: []
tags: [_auto/notations_added, _meta/concept, _auto/links_added, _meta/literature_note, _reference/lombardo_av, _meta/TODO/change_title]
---
# Topic[^1]
THEOREM 7.4 (Torsion injects in the reductions). Let $A / K$ be an [[lombardo_av_1.3|abelian variety]] over a [[number_field|number field]]. Let $v$ be a [[place_of_a_global_field#Place of a global field 1|place]] of $K$ of characteristic $p$ and let suppose that A has [[lombardo_av_DEFINITION 4.1|good]] reduction at $v .$ Finally, let $A(K)_{\text {tors }}^{\prime}$ denote the subgroup of $A(K)$ tors whose points have order prime to $p .$ Then the natural reduction map
$$
A(K)_{\text {tors }}^{\prime} \rightarrow A\left(\mathbb{F}_{v}\right)
$$
is injective.
SKETCH OF PROOF. It suffices to do this one prime at a time, namely, it suffices to show that for $\ell \neq p$ we have an injection $A(K)\left[\ell^{\infty}\right] \rightarrow A\left(\mathbb{F}_{v}\right)$, where $A(K)\left[\ell^{\infty}\right]$ denotes the \ell-primary component of $A(K)$ tors. By the Mordell-Weil theorem 8.1 the group $A(K)$ tors is [[foag_finite_morphism_of_schemes|finite]], so we can choose $n \gg 0$ such that $A(K)\left[\ell^{\infty}\right]=A(K)\left[\ell^{n}\right] .$ Let $\mathcal{A} \rightarrow \operatorname{Spec}\left(\mathcal{O}_{K, v}\right)$[^2][^3]               be an [[lombardo_av_DEFINITION 2.1|abelian scheme]] extending $A \rightarrow \operatorname{Spec}\left(K_{v}\right) ;$ the extension $\mathcal{A}$ exists since $A$ has [[lombardo_av_DEFINITION 4.1|good]] reduction at $v$

We know that $A\left[\ell^{n}\right]$ is an étale [[lombardo_av_DEFINITION 1.1|group scheme]] over $K_{v}$ (remark 5.7 ), but in fact it is also étale over $\mathcal{O}_{K, v}$[^2][^3]              , because $\ell \neq p$ is invertible in $\mathcal{O}_{K, v} .$[^2][^3]               It follows that $\mathcal{A}[n]$[^4][^5][^6]               has precisely9. RAYNAUD'S THEOREM: THE ACTION OF THE INERTIA AT $\ell$
53
$\ell^{2 n g}$ points over the maximal [[lombardo_av_DEFINITION 5.1_page_47|unramified]] extension $\mathcal{O}_{v}^{\mathrm{nr}}$ of $\mathcal{O}_{K, v}$[^2][^3]               (that is, the [[foag_integral_scheme#Integral scheme 1|integral]] closure of $\mathcal{O}_{K, v}$[^2][^3]               inside the maximal [[lombardo_av_DEFINITION 5.1_page_47|unramified]] extension of $\left.K_{v}\right)$. Similarly, $\mathcal{A}[n]$[^4][^5][^6]               has $\ell^{2 n g}$ rational points over $\overline{\mathbb{F}_{v}}$. By Hensel's lemma (and étaleness), each point in $\mathcal{A}[n]\left(\overline{\mathbb{F}}_{v}\right)$[^4][^5][^6]               lifts to a unique point in $\mathcal{A}[n]\left(\mathcal{O}_{v}^{\mathrm{nr}}\right)$[^4][^5][^6]              , which implies that the reduction map
$$
\mathcal{A}\left[\ell^{n}\right]\left(\mathcal{O}_{v}^{\mathrm{nr}}\right) \rightarrow \mathcal{A}\left[\ell^{n}\right]\left(\overline{\mathbb{F}_{v}}\right)
$$
is a bijection (since it is surjective between sets of the same cardinality). In particular, by restricting to $\mathcal{O}_{K, v} \subseteq \mathcal{O}_{v}^{\mathrm{nr}}$[^2][^3]               we obtain an injective map
$$
A\left[\ell^{n}\right]\left(K_{v}\right)=\mathcal{A}\left[\ell^{n}\right]\left(\mathcal{O}_{K, v}\right) \rightarrow \mathcal{A}\left[\ell^{n}\right]\left(\mathbb{F}_{v}\right)
$$
[^2][^3]
where the first equality follows from the properness of $\mathcal{A}$ and the obvious fact that
$$
A\left[\ell^{n}\right]\left(K_{v}\right)=A\left(K_{v}\right)\left[\ell^{n}\right], \quad \mathcal{A}\left[\ell^{n}\right]\left(\mathcal{O}_{K, v}\right)=\mathcal{A}\left(\mathcal{O}_{K, v}\right)\left[\ell^{n}\right]
$$
[^2][^3]

# See Also

# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, THEOREM 7.4, Page 52
[^2]: ![[lombardo_av_notation_O_K]]
[^3]: ![[lombardo_av_notation_O_K_v]]
[^4]: ![[lombardo_av_notation_A_n_complex]]
[^5]: ![[lombardo_av_notation_A_n_general]]
[^6]: ![[lombardo_av_notation_brackets_n]]