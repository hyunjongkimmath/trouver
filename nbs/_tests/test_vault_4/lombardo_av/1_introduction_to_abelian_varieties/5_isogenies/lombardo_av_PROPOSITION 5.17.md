---
cssclass: clean-embeds
aliases: [lombardo_av_Multiplication_by_n_map_has_degree_n_2g]
tags: [_meta/proof, _meta/TODO/change_title, _meta/literature_note, _meta/concept, _reference/lombardo_av]
---
# Multiplication by $n$ map has degree $n^{2g}$[^1]

Let $A$ be an [[lombardo_av_1.3|abelian variety]] of dimension $g$.

For every positive integer $n$, the [[lombardo_av_DEFINITION 5.3|degree]] of $[n]$[^2] is $n^{2 g}$.

[^2]: ![[lombardo_av_notation_brackets_n]] 

# Proof
PROOF. In order to compute the degree of $[n]$ we look at its action on a very ample line bundle $\mathcal{L}$. One can always find a symmetric ample line bundle, namely an ample $\mathcal{L}$ such that $[-1]^{*} \mathcal{L} \cong \mathcal{L}$ : indeed, if $\mathcal{M}$ is any ample line bundle, $\mathcal{L}:=\mathcal{M} \otimes[-1]^{*} \mathcal{M}$ is ample and symmetric. Taking a sufficiently large power will make it very ample; we still call $\mathcal{L}$ the resulting line bundle.

COROLLARY 3.3 implies that $[n]^{*} \mathcal{L} \cong \mathcal{L}^{\otimes n^{2}}-$ notice that this is in particular compatible with the assumption $[-1]^{*} \mathcal{L} \cong \mathcal{L}$. It follows that $\left.\left.[n]^{*} \mathcal{L}\right|_{\operatorname{ker}[n]} \cong \mathcal{L}^{\otimes n^{2}}\right|_{\operatorname{ker}[n]}$ is both trivial and very ample, which is only possible if ker $[n]$ is zero-dimensional (hence $[n]$ is an isogeny). Furthermore, writing $\mathcal{L}$ as $\mathcal{O}(D)$, we have
$$
\operatorname{deg}[n](D, \ldots, D)=\left([n]^{*} D, \cdots,[n]^{*} D\right)=\left(n^{2} D, \cdots, n^{2} D\right)=n^{2 g}(D, \ldots, D)
$$
where $(D, \ldots, D)$ denotes the intersection product (of divisors). In order to conclude it suffices to show that $(D, \ldots, D)$ is nonzero, but this is easy, because since $\mathcal{L}$ is very ample (hence it induces an embedding $A \hookrightarrow \mathbb{P}^{N}$ ) we may compute this intersection product as the intersection product of $g$ general hyperplane sections of $A \hookrightarrow \mathbb{P}^{N}$, and this is clearly positive.



# See Also

# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, PROPOSITION 5.17, Page 18