---
cssclass: clean-embeds
aliases: [lombardo_av_n_torsion_structure_of_a_complex_abelian_variety]
tags: [_auto/notations_added, _meta/concept, _meta/literature_note, _reference/lombardo_av, _meta/TODO/change_title, _meta/proof]
---
# $n$-torsion structure of a complex abelian variety[^1]

Let $A$ be a complex abelian variety, i.e. an [[lombardo_av_1.3|abelian variety]] over $\mathbb{C}$. Let $n$ be a positive integer. 

The group
$$
A[n]=\{x \in A(\mathbb{C}): n x=\underbrace{x+\cdots+x}_{n \text { times }}=0\}
$$
[^2][^3][^4]
is isomorphic to $(\mathbb{Z} / n \mathbb{Z})^{2 g}$
# Proof
By analytic uniformisation it suffices to understand the $n$-torsion points of the group $\mathbb{C}^{g} / \Lambda \cong \mathbb{R}^{2 g} / \Lambda .$ As an abstract group, this is isomorphic to $\mathbb{R}^{2 g} / \mathbb{Z}^{2 g}$, because up to a change of basis in $\mathbb{R}^{2 g}$ we can assume that $\Lambda$ is the standard lattice $1^{1} \mathbb{Z}^{2 g}$. Thus the group of $n$-torsion points of $A$ is isomorphic to
$$
(\mathbb{R} / \mathbb{Z})^{2 g}[n] \cong\left(\frac{\mathbb{R}}{\mathbb{Z}}[n]\right)^{2 g} \cong\left(\mathbb{S}^{1}[n]\right)^{2 g} \cong(\mathbb{Z} / n \mathbb{Z})^{2 g}
$$
[^4]
where we have denoted by $G[n]$[^4]               the $n$-torsion points of an abstract abelian group $G$.


# See Also
- [[lombardo_av_notation_A_n_complex]]
- [[lombardo_av_DEFINITION 5.12]]

# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, PROPOSITION 4.5, Page 12
[^2]: ![[lombardo_av_notation_A_n_complex]]
[^3]: ![[lombardo_av_notation_A_n_general]]
[^4]: ![[lombardo_av_notation_brackets_n]]