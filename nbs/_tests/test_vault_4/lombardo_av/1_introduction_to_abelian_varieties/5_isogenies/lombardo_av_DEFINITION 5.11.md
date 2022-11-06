---
cssclass: clean-embeds
aliases: [lombardo_av_integers_on_abelian_variety, lombardo_av_abelian_variety_with_trivial_endomorphisms]
tags: [_meta/notation, _meta/TODO/change_title, _meta/literature_note, _meta/definition, _reference/lombardo_av]
---
# Integers on abelian variety[^1]
The ring $\operatorname{End}_{K}(A)$[^2] contains a canonical copy of the integers: indeed, for every $n \in \mathbb{N}$ the map
$$
\begin{aligned}
[n] : A & \rightarrow A \\
x & \mapsto \underbrace{x+\cdots+x}_{n \text { times }}
\end{aligned}
$$
is an [[lombardo_av_DEFINITION 5.9|endomorphism]] of $A .$ 

[^2]: ![[lombardo_av_notation_End_K_A]]

We further define $[-1]$ to be the map giving the inverse for the group law, and for $n>1$ we define $[-n]$ as the composition of $[n]$ and $[-1]$. This gives a canonical identification $n \mapsto[n]$ of $\mathbb{Z}$ with a subring of $\operatorname{End}_{K}(A) .$ 

One often says that $A$ has **trivial endomorphisms** over $K$ if $n \mapsto[n]$ induces an isomorphism $\mathbb{Z} \cong \mathrm{End}_{K}(A)$

Once we have the isogenies $[n]$ we can look at their kernels; these will play an important role in what is to follow:


# See Also
- [[lombardo_av_notation_brackets_n]]
- [[lombardo_av_PROPOSITION 5.17|lombardo_av_Multiplication_by_n_map_has_degree_n_2g]]

# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, DEFINITION 5.11, Page 16