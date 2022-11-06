---
cssclass: clean-embeds
aliases: [lombardo_av_Type_of_a_polarization]
tags: [_auto/notations_added, _meta/literature_note, _reference/lombardo_av, _meta/TODO/change_title, _meta/notation, _meta/definition]
---
# Type of a polarization[^1]

Let $V=\mathbb{C}^{g}$ and [[lombardo_av_THEOREM 4.1|write]] $A= V / \Lambda$ where $\Lambda \subset V$ is a lattice. Let $H: V \times V \rightarrow \mathbb{C}$ be a [[hermitian_form#Hermitian form 1|Hermitian form]] (linear in the first argument, antilinear in the second). 


Linear algebra over $\mathbb{Z}$ (essentially the elementary divisors theorem) shows that in a suitable basis of $\Lambda$ the matrix representation of $\left.\Im H\right|_{\Lambda \times \Lambda}$[^2]               takes the form
$$
\left(\begin{array}{cc}
0 & D \\
-D & 0
\end{array}\right), \quad \text { where } \quad D=\left(\begin{array}{llll}
d_{1} & & & \\
& d_{2} & & \\
& & \ddots & \\
& & & d_{g}
\end{array}\right)
$$
with the $d_{i}$ positive integers such that $d_{1}\left|d_{2}\right| \cdots \mid d_{g} .$ The vector $\left(d_{1}, \ldots, d_{g}\right)$ is called the **type of the polarisation**; one also sets $d(H)=\prod d_{i}$[^3]              

# See Also
- [[lombardo_av_notation_d_H]]
- [[lombardo_av_EXERCISE 1.4|lombardo_av_Computing_the_degree_of_the_kernel_of_lambda_H]] - $\lambda_H$[^4]               has degree $d(H)^2$[^3]              .
- [[lombardo_av_REMARK 4.11|lombardo_av_principal_polarization_of_a_complex_torus]] - happens when $d(H) = 1$[^3]              .
# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, DEFINITION 4.10, Page 13
[^2]: ![[lombardo_av_notation_Im]]
[^3]: ![[lombardo_av_notation_d_H]]
[^4]: ![[lombardo_av_notation_lambda_H]]