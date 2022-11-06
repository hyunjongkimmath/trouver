---
cssclass: clean-embeds
aliases: [lombardo_av_principally_polarized_abelian_varieties_in_dimension_2_are_equivalent_to_jacobians]
tags: [_auto/notations_added, _meta/concept, _meta/TODO/change_title, _meta/narrative, _meta/literature_note, _reference/lombardo_av, _meta/permanent_note]
---
# Topic[^1]
## Dimension $1$ abelian varieties
In dimension $g=1$, all genus 1 curves with a marked point are elliptic curves; they are all [[lombardo_av_DEFINITION 6.6|principally polarised]] (we proved this for elliptic curves over $\mathbb{C}$ in [[lombardo_av_EXAMPLE 4.12|example 4.12]], but the same holds over any field) and isomorphic to their Jacobian ([[lombardo_av_EXAMPLE 9.20|example 9.20]]). Hence in dimension $1$ the notions of [[lombardo_av_1.3|abelian variety]], [[lombardo_av_DEFINITION 6.6|principally polarised abelian variety]] and [[lombardo_av_THEOREM 9.16|Jacobian]] are all the same.

## Dimension $2$
Starting with dimension 2 there are non-principally polarised abelian varieties, but **any principally polarised abelian variety is a Jacobian** (or the product of two elliptic curves with the product polarisation). 

Furthermore, it's not hard to prove that every genus 2 curve is [[foag_hyperelliptic_curve|hyperelliptic]], so we have
$$
\begin{aligned}
\left\{\begin{array}{c}
\text { Jacobians of genus } 2 \\
\text { hyperelliptic curves }
\end{array}\right\} &=\{\text { genus } 2 \text { Jacobians }\} \\
& \simeq\left\{\begin{array}{c}
\text { principally polarised } \\
\text { abelian surfaces }
\end{array}\right\} \subsetneq\{\text { abelian surfaces }\}
\end{aligned}
$$
[^2][^3]

## Dimension $3$

In dimension 3 one has
$$
\begin{aligned}
\left\{\begin{array}{c}
\text { Jacobians of genus } 3 \\
\text { hyperelliptic curves }
\end{array}\right\} & \subsetneq\{\text { genus } 3 \text { Jacobians }\} \\
& \simeq\left\{\begin{array}{c}
\text { principally polarised } \\
\text { abelian threefolds }
\end{array}\right\} \subsetneq\{\text { abelian threefolds }\}
\end{aligned}
$$
[^2][^3]
where as before $\simeq$[^2][^3]               denotes equality up to the (very thin) subset of principally polarised abelian varieties that are isomorphic (and not just isogenous) to products of PPAVs of smaller dimension. 

## Dimension $4$

Finally, from dimension 4 onward, all 4 sets are genuinely distinct. In a suitable sense, which we cannot make precise here, when considering abelian varieties of dimension $g$ the situation is the following:
(1) the moduli space of hyperelliptic curves of genus $g$ has dimension $2 g-1 ;$
(2) the moduli space of curves of genus $g$ (hence of Jacobians, considered together with their principal polarisation ${ }^{9}$ ) has dimension $3 g-3 ;$
(3) the moduli space of principally polarised abelian varieties of dimension $g$ has dimension $\frac{g(g+1)}{2}$
(4) there exists a (countably) infinite number of different types of polarisations; recall however that over an algebraically closed field any abelian variety is isogenous to a principally polarised one (theorem 6.8).
It is quite clear from the previous list that Jacobians become more and more sparse in the space of all the PPAVs of a given dimension; however, Jacobians are still very interesting to study, for many reasons, including the following perhaps surprising result which unfortunately we won't have the time to prove (the interested reader can find a proof in [Mil12, Theorem 10.1]):


# See Also

# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, 9.2, Page 30
[^2]: ![[lombardo_av_notation_sim]]
[^3]: ![[lombardo_av_notation_sim_linearly_equivalent]]