---
cssclass: clean-embeds
aliases: [lombardo_av_adelic_tate_module_of_an_abelian_variety, lombardo_av_rational_tate_module_of_an_abelian_variety]
tags: [_meta/notation, _meta/TODO/change_title, _meta/literature_note, _meta/definition, _reference/lombardo_av]
---
# Adelic Tate module of an abelian variety[^1]

Let $A / K$ be an [[lombardo_av_1.3|abelian variety]].

It is sometimes useful to consider the **adelic Tate module**: by definition, it is the projective limit of the system of $n$ torsion points along the transition maps given by $A[km] \stackrel{[k]}{\longrightarrow} A[m]$. 

We have
$$
\hat{T}(A)=\lim _{n:(n, \operatorname{char}(K))=1} A[n]=\prod_{\ell \neq \operatorname{prime} \atop \ell \neq \operatorname{char}(K)} T_{\ell}(A)
$$
[^2]

[^2]: ![[lombardo_av_notation_T_ell_A]]

# Rational Tate module of an abelian variety

Let $\ell$ be a prime number different from $\operatorname{char}(K)$. 


Another useful variant of the Tate module is the so-called **rational Tate module** $V_{\ell}(A):=T_{\ell}(A) \otimes_{\mathbb{Z}_{\ell}} \mathbb{Q}_{\ell}$[^2]


# See Also
- [[lombardo_av_notation_V_ell_A_rational_tate_module]]
- [[lombardo_av_notation_hat_T_A_adelic_tate_module]]
- [[lombardo_av_REMARK 10.11]]
- [[lombardo_av_THEOREM 2.10|lombardo_av_Tates_conjecture]] - we have the isomorphism ![[lombardo_av_THEOREM 2.10#^fc419c]]
# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, DEFINITION 10.10, Page 34