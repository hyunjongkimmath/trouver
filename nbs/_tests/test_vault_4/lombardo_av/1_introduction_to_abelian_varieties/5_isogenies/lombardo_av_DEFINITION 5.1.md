---
cssclass: clean-embeds
aliases: [lombardo_av_homomorphism_of_group_schemes, lombardo_av_homomorphism_of_abelian_varieties, lombardo_av_kernel_of_a_homomorphism_of_group_schemes]
tags: [_auto/notations_added, _meta/literature_note, _reference/lombardo_av, _meta/TODO/change_title, _meta/notation, _meta/definition]
---
# Group scheme homomorphism[^1]
(Group scheme homomorphism, $\operatorname{Hom}(A, B)) .$ Let $\left(\mathcal{G}_{1}, m_{1}, i_{1}, e_{1}\right)$ and $\left(\mathcal{G}_{2}, m_{2}, i_{2}, e_{2}\right)$ be group schemes over a common base $S .$ A homomorphism of group schemes $f: \mathcal{G}_{1} \rightarrow \mathcal{G}_{2}$ is a morphism of $S$-schemes such that $f \circ e_{1}=e_{2}, m_{2} \circ(f \times f)=f \circ m_{1}$ and $i_{2} \circ f=f \circ i_{1} .$ 

If $f: \mathcal{G}_{1} \rightarrow \mathcal{G}_{2}$ is a group scheme homomorphism then one defines $\ker f$[^2]               in the obvious way, namely as the [[fibered_products_exist_in_the_category_of_schemes|fiber product]]

![[Pasted image 20211115160127.png]]

$\ker f$[^2]               is then a subgroup scheme of $\mathcal{G}_{1}$ (with the obvious definition: a subscheme which inherits a structure of group scheme when endowed with the suitable base changes of the $\left.\operatorname{maps} m_{1}, i_{1}, e_{1}\right)$

When $A, B$ are [[lombardo_av_1.3|abelian varieties]] we shall say that $f$ is a **homomorphism of abelian varieties**, or simply a **homomorphism**. The set of all $K$-homomorphisms $A \rightarrow B$ is a group in the obvious way, and is denoted by $\operatorname{Hom}_{K}(A, B)$[^3]              .


# See Also
- [[foag_notation_Hom_K_A_B_abelian_varieties]]
- [[lombardo_av_DEFINITION 5.3|lombardo_av_isogeny_of_abelian_varieties]]
- [[lombardo_av_THEOREM 2.10|lombardo_av_Tates_conjecture]] - determination of $\operatorname{Hom}_K$ when $K$ is finitely generated over its prime field.
# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, DEFINITION 5.1, Page 15
[^2]: ![[lombardo_av_notation_ker_f_kernel_of_group_scheme_homomorphism]]
[^3]: ![[foag_notation_Hom_K_A_B_abelian_varieties]]