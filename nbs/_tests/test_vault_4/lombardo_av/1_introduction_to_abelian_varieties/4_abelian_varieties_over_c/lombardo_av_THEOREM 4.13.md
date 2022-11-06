---
cssclass: clean-embeds
aliases: [lombardo_av_Complex_abelian_variety_is_isogenous_to_a_principally_polarizable_abelian_variety]
tags: [_auto/notations_added, _meta/concept, _auto/links_added, _meta/literature_note, _reference/lombardo_av, _meta/TODO/change_title, _meta/proof]
---
# Complex abelian variety is isogenous to a principally polarizable abelian variety[^1]
THEOREM 4.13. Every [[lombardo_av_1.3|abelian variety]] $A / \mathbb{C}$ is $\mathbb{C}-$ [[lombardo_av_DEFINITION 5.13|isogenous]] to a [[lombardo_av_DEFINITION 6.6#Polarization of an abelian variety 1|principally polarisable abelian variety]], that is, there is a surjective analytic [[lombardo_av_DEFINITION 5.1|homomorphism]] $\varphi$ from $A$ to a [[lombardo_av_DEFINITION 6.6#Polarization of an abelian variety 1|principally polarisable abelian variety]] $A^{\prime}$ such that $\varphi$ has [[foag_finite_morphism_of_schemes|finite]] [[lombardo_av_DEFINITION 5.1|kernel]].

# Proof
PROOF. Write $A=\mathbb{C}^{g} / \Lambda$, choose any [[lombardo_av_DEFINITION 4.8|polarisation]] $H$ (at least one exists, because $A$ is an [[lombardo_av_1.3|abelian variety]] and not just a [[lombardo_av_DEFINITION 4.2|complex torus]]), and fix a $\mathbb{Z}-\mathrm{basis} \tau_{1}, \ldots, \tau_{g}, \tau_{g+1}, \ldots, \tau_{2 g}$ of $\Lambda$ such that the matrix of $\Im H$[^2]               is of the form
$$
\Im H=\left(\begin{array}{cc}
0 & D \\
-D & 0
\end{array}\right)
$$
[^2]
with $D=\operatorname{diag}\left(d_{1}, \ldots, d_{g}\right) .$ Now consider the [[18785_Definition 5.9|lattice]] $\Lambda^{\prime}:=\bigoplus_{i=1}^{g} \mathbb{Z} \cdot \frac{1}{d_{1}} \tau_{i} \oplus \bigoplus_{i=1}^{g} \mathbb{Z} \cdot \tau_{g+i} .$ It is immediate to see that $\Lambda^{\prime}$ is an over-[[18785_Definition 5.9|lattice]] of $\Lambda$, and that with respect to the obvious basis $\left\{\frac{1}{d_{1}} \tau_{i}, \tau_{g+i}\right\}_{i=1, \ldots, g}$ of $\Lambda^{\prime}$ the matrix representing $S H$ is $\left(\begin{array}{cc}0 & I_{g} \\ -I_{g} & 0\end{array}\right)$, so that the [[lombardo_av_1.3|abelian variety]] $A^{\prime}=\mathbb{C}^{g} / \Lambda^{\prime}$ is [[lombardo_av_DEFINITION 6.6|principally polarised]]. Now simply observe that there is an [[lombardo_av_DEFINITION 5.3|isogeny]] $A=\mathbb{C}^{g} / \Lambda \rightarrow \mathbb{C}^{g} / \Lambda^{\prime}=A^{\prime}$ induced by the identity of $\mathbb{C}^{g}$ (the [[lombardo_av_DEFINITION 5.1|kernel]] is the [[foag_finite_morphism_of_schemes|finite]] group $\left.\Lambda^{\prime} / \Lambda\right)$
5. Isogenies

# See Also

# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, THEOREM 4.13, Page 14
[^2]: ![[lombardo_av_notation_Im]]