---
cssclass: clean-embeds
aliases: []
tags: [_auto/notations_added, _auto/links_added, _meta/literature_note, _reference/lombardo_av, _meta/TODO/change_title, _meta/definition]
---
# Topic[^1]
EXAMPLE 1.16 (Curve of genus 3 whose [[lombardo_av_THEOREM 9.16|Jacobian]] maps to the square of an elliptic [[foag_11.1.3|curve]]). Consider the genus-3 [[foag_11.1.3|curve]]
$$
C: y^{2}=x^{8}+3 x^{4}+1
$$
and its [[lombardo_av_THEOREM 9.16|Jacobian]] $J .$ Then $\operatorname{Aut}(C)$ contains (at least) the [[foag_hyperelliptic_curve|hyperelliptic]] involution and the two isomorphisms $\alpha_{2}:(x, y) \mapsto(i x, y)$ and $\alpha_{3}:(x, y) \mapsto\left(1 / x, y / x^{4}\right)$. Notice that
$$
\alpha_{2} \alpha_{3}(x, y)=\left(i / x, y / x^{4}\right) \neq\left(-i / x, y / x^{4}\right)=\alpha_{3} \alpha_{2}(x, y)
$$
so that Aut $(C)$ is not commutative. However, we know that Aut $(C)$ embeds in End $(J)^{\times}$; suppose now that $J$ is [[foag_geometric_point#Geometric properties|geometrically]] [[18785_simple_ring|simple]]. Then Albert's classification implies that $D:=\operatorname{End}_{\mathrm{C}}^{0}(J)$ is a field, which contradicts the fact that $D^{\times}$contains the non-commutative group Aut $(C) .$ Hence we recover from Albert's classification the fact (obvious by just staring at the equation of the [[foag_11.1.3|curve]] for three or more seconds!) that $J$ cannot be [[18785_simple_ring|simple]]. But looking at the [[lombardo_av_DEFINITION 5.9|endomorphism]] ring tells us more: indeed it's immediate to see that $C$ admits at least two independent maps towards elliptic curves, so $J$ is ([[foag_geometric_point#Geometric properties|geometrically]]) [[lombardo_av_DEFINITION 5.13|isogenous]] to the product of three elliptic curves $E_{1}, E_{2}, E_{3} .$ Suppose that the $E_{i}$ are pairwise non-[[lombardo_av_DEFINITION 5.13|isogenous]] ([[foag_geometric_point#Geometric properties|geometrically]]): then $D \cong \prod_{i=1}^{3} \operatorname{End}_{\mathbb{C}}^{0}\left(E_{i}\right)$, which is commutative since the [[lombardo_av_DEFINITION 5.9|endomorphism]] ring of an elliptic [[foag_11.1.3|curve]] is always commutative in characteristic zero. Again we find a contradiction with the fact that Aut $C$ embeds in $D^{\times}$! It follows that at least two of the three elliptic curves are [[foag_geometric_point#Geometric properties|geometrically]] [[lombardo_av_DEFINITION 5.13|isogenous]].

Finally, we prove that 2 of these 3 elliptic curves are [[lombardo_av_DEFINITION 5.13|isogenous]], but the third one is not. We compute that $f_{3}(t)=\left(t^{2}-2 t+3\right)\left(t^{2}+3\right)\left(t^{2}+2 t+3\right)$, which means (by theorem 2.14) that $J_{\mathrm{F}_{3}}$ is [[lombardo_av_DEFINITION 5.13|isogenous]] to the product of three elliptic curves $\tilde{E}_{1}, \tilde{E}_{2}, \tilde{E}_{3}$, precisely one of which (say $\tilde{E}_{2}$ ) is supersingular. Since supersingularity is a geometric property (and it depends only on the [[lombardo_av_DEFINITION 5.3|isogeny]] class), we find that even over $\overline{\mathbb{F}_{3}}$ the curves $\tilde{E}_{1}$ and $\tilde{E}_{2}$ cannot become [[lombardo_av_DEFINITION 5.13|isogenous]]. This in turn implies that over $\overline{\mathbb{Q}}$ (or even over $\mathbb{C}$ ) not all the elliptic curves $E_{i}$ are [[lombardo_av_DEFINITION 5.13|isogenous]]. Thus the decomposition of $J_{\bar{Q}}$ up to [[lombardo_av_DEFINITION 5.3|isogeny]] is $E_{1}^{2} \times E_{2}$, with $E_{1}, E_{2}$ not [[lombardo_av_DEFINITION 5.13|isogenous]].

As a final remark, notice that $\tilde{E}_{1}$ and $\tilde{E}_{3}$ are (up to [[lombardo_av_DEFINITION 5.3|isogeny]]) quadratic twists of each other, hence, after a quadratic extension of $\mathbb{F}_{p}$, they become [[lombardo_av_DEFINITION 5.13|isogenous]]. This is consistent with the decomposition $J_{\bar{Q}} \sim E_{1}^{2} \times E_{2}$[^2][^3]              .


# See Also

# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, EXAMPLE 1.16, Page 58
[^2]: ![[lombardo_av_notation_sim]]
[^3]: ![[lombardo_av_notation_sim_linearly_equivalent]]