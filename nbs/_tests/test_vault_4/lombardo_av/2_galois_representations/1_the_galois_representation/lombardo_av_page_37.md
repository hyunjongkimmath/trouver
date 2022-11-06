---
cssclass: clean-embeds
aliases: []
tags: [_auto/notations_added, _auto/links_added, _meta/narrative, _meta/literature_note, _reference/lombardo_av]
---
# Topic[^1]

Galois representations
The purpose of this lecture is to (re)describe the family of compatible [[lombardo_av_DEFINITION 1.1_page_37|Galois representation]] attached to an [[lombardo_av_1.3|abelian variety]] over a [[number_field|number field]] and to provide the reader with a bag of tricks that might be useful in determining properties of these Galois representations.
1. The [[lombardo_av_DEFINITION 1.1_page_37|Galois representation]]
It is customary to study Galois representations one prime at a time: while this is not strictly necessary, it often makes matters easier. For this reason, in what follows we shall fix a prime $\ell$ and only consider modulo- $\ell$ and $\ell$-adic representations. From now on, $A$ is a fixed [[lombardo_av_1.3|abelian variety]] over a field $K$ (which will usually be either a [[number_field|number field]] or a [[foag_finite_morphism_of_schemes|finite]] field).

The crucial remark is that the coordinates of the points in the [[foag_finite_morphism_of_schemes|finite]] set $A\left[\ell^{n}\right]$ are algebraic, so that there is a natural action of the absolute Galois group Gal $\bar{K} / K)$ on the points of $A\left[\ell^{n}\right] .$ It is clear that when Galois acts on a point in $A(\bar{K})$ we get a new point in $A(\bar{K})$, and that the fixed points of this action are precisely the $K$-points of $A$ (in particular, $0_{A}$ is fixed under the Galois action).

More precisely, we notice that Galois also acts on the [[foag_finite_morphism_of_schemes|finite]] set $A\left[\ell^{n}\right]$. Since the equations that define $A$ and the group law have coefficients in $K$, one sees easily that
$$
[n] \sigma(P)=\sigma([n] P)
$$
[^2]
for all $\sigma \in \operatorname{Gal}(\bar{K} / K), P \in A(\bar{K})$ and $n \in \mathbb{Z}$. In particular, if $P$ is a $n$-torsion point, then so is $[n] P:$[^2]               it follows that Gal $(\bar{K} / K)$ acts on $A\left[\ell^{n}\right] .$ Moreover, since $\sigma(P+Q)=$ $\sigma(P)+\sigma(Q)$, the Galois action is compatible with the obvious structure of $\mathbb{Z} / \ell^{n} \mathbb{Z}$-module of $A\left[\ell^{n}\right]$. Combining the previous remarks, we see that the [[lombardo_av_DEFINITION 5.7|following definition]] is well-posed:

# See Also

# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, 2, Page 37
[^2]: ![[lombardo_av_notation_brackets_n]]