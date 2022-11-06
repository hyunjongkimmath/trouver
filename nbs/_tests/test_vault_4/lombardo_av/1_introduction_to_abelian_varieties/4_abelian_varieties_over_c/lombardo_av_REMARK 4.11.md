---
cssclass: clean-embeds
aliases: [lombardo_av_polarisation_induces_maps, lombardo_av_principal_polarization_of_a_complex_torus]
tags: [_meta/concept, _meta/TODO/change_title, _reference/lombardo_av, _meta/literature_note, _meta/definition]
---
# Polarization induces maps[^1]

Let $V=\mathbb{C}^{g}$ and [[lombardo_av_THEOREM 4.1|write]] $A= V / \Lambda$ where $\Lambda \subset V$ is a lattice. Let $H: V \times V \rightarrow \mathbb{C}$ be a [[hermitian_form#Hermitian form 1|Hermitian form]] (linear in the first argument, antilinear in the second). 


#_meta/TODO/link antilinear map on a complex space, positive-definitine


A [[lombardo_av_DEFINITION 4.8|polarisation]] induces a map


$$\begin{aligned}
\lambda_{H}: & V \rightarrow \bar{V}^{\vee} \\
v & \mapsto H(v, \cdot)
\end{aligned}$$

^931965


[^2]which is surjective and satisfies $\lambda_{H}(\Lambda) \subseteq \Lambda^{\vee}$. 
[^3]

[^2]: ![[lombardo_av_notation_bar_V_vee]]
[^3]: ![[lombardo_av_notation_Lambda_vee_dual_complx_abelian_variety]]



In particular, it induces a surjective analytic homomorphism $\lambda_{H}: V / \Lambda \rightarrow \bar{V}^{\vee} / \Lambda^{\vee}$ which is easily seen to have finite kernel (we will soon call such morphism isogenies). 

#_meta/TODO/link isogeny_

The polarisation $H$ is said to be **principal** if $\lambda_{H}$ is an isomorphism; this happens precisely when $d(H)=1$[^4].

[^4]: ![[lombardo_av_notation_d_H]]


# See Also
- [[lombardo_av_notation_lambda_H]]
- [[lombardo_av_EXERCISE 1.4|lombardo_av_Computing_the_degree_of_the_kernel_of_lambda_H]]

# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, REMARK 4.11, Page 13