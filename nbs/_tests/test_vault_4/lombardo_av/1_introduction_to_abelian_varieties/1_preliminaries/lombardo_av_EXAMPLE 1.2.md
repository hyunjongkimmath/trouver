---
cssclass: clean-embeds
aliases: [lombardo_av_Multiplicative_group, lombardo_av_Additive_group, lombardo_av_Multiplicative_and_additive_groups]
tags: [_auto/links_added, _meta/literature_note, _meta/notation, _auto/notations_added, _meta/example, _reference/lombardo_av, _meta/TODO/change_title, _meta/definition]
---
# Multiplicative and additive groups[^1]
The following are two fundamental examples of [[lombardo_av_DEFINITION 1.1|group schemes]]:

## Multiplicative group
The **multiplicative group** $\mathbb{G}_{m, S}$[^2]              . We start by defining $\mathbb{G}_{m, Z}:$ as a [[foag_scheme_over_a_ring#Scheme over a ring 1|scheme]], it is given by $\mathbb{G}_{m, \mathbb{Z}}=\operatorname{Spec} \mathbb{Z}\left[T, T^{-1}\right] .$ In order to describe its group structure, we need to specify three morphisms $e, i$ and $m$ as above. The identity section $e$ is the map of affine schemes induced by the map of rings
$$
\begin{aligned}
\mathbb{Z}\left[T, T^{-1}\right] & \rightarrow \mathbb{Z} \\
T & \mapsto 1
\end{aligned}
$$
Likewise, the inverse $i$ is induced by the map of rings
$$
\begin{aligned}
\mathbb{Z}\left[T, T^{-1}\right] & \rightarrow \mathbb{Z} \\
T & \mapsto T^{-1}
\end{aligned}
$$
and multiplication $m$ is induced by
$$
\begin{array}{clc}
\mathbb{Z}\left[T, T^{-1}\right] & \rightarrow & \mathbb{Z}\left[T_{1}, T_{2}, T_{1}^{-1}, T_{2}^{-1}\right] \\
T & \mapsto & T_{1} T_{2}
\end{array}
$$
Notice that $\mathbb{Z}\left[T_{1}, T_{2}, T_{1}^{-1}, T_{2}^{-1}\right] \cong \mathbb{Z}\left[T_{1}, T_{1}^{-1}\right] \otimes \mathbb{Z} \mathbb{Z}\left[T_{2}, T_{2}^{-1}\right]$, and the latter is the coordinate ring of $\mathbb{G}_{m, Z} \times_{\text {Spec } \mathbb{Z}} \mathbb{G}_{m, Z}$. One checks immediately that, for any [[foag_scheme_over_a_ring#Scheme over a ring 1|scheme]] $X$, we have
$$
\mathbb{G}_{m, Z}(X)=\operatorname{Hom}_{S \operatorname{ch}}\left(X, \mathbb{G}_{m, Z}\right)=\operatorname{Hom}_{R i n g}\left(\mathbb{Z}\left[T, T^{-1}\right], H^{0}\left(X, \mathcal{O}_{X}\right)\right)=H^{0}\left(X, \mathcal{O}_{X}\right)^{\times}:
$$
here the second equality follows from the fact that $\mathbb{G}_{m, Z}$ is affine, while the third is a consequence of the fact that a ring [[lombardo_av_DEFINITION 5.1|homomorphism]] $\varphi: \mathbb{Z}[T] \rightarrow H^{0}\left(X, \mathcal{O}_{X}\right)$ is uniquely determined by $a=\varphi(T)$, and it factors via $\mathbb{Z}\left[T, T^{-1}\right]$ if and only if $a$ is invertible in $H^{0}\left(X, \mathcal{O}_{X}\right) .$

The previous equalities justify the name multiplicative group: when evaluated on $X=\operatorname{Spec}(A)$, where $A$ is a ring, we get $\mathbb{G}_{m, Z}(X)=A^{\times} .$We may also check that the induced maps $m: \mathbb{G}_{m, \mathbb{Z}}(X) \times \mathbb{G}_{m, Z}(X) \rightarrow \mathbb{G}_{m, \mathbb{Z}}(X)$ and $i: \mathbb{G}_{m, \mathbb{Z}}(X) \rightarrow$ $\mathbb{G}_{m, Z}(X)$ are the obvious ones. Let's do it for the former. We are considering a diagram of the form
and we are interested in the composition $m \circ\left(\varphi_{1}, \varphi_{2}\right) .$ We may assume that $X=\operatorname{Spec}(A)$ is affine, in which case the maps $\varphi_{1}, \varphi_{2}$ are determined by $a_{1}:=$ $\varphi_{1}(T) \in A^{\times}$and $a_{2}:=\varphi_{2}(T) \in A^{\times}$. We would like to describe $m \circ\left(\varphi_{1}, \varphi_{2}\right)$ and check that it corresponds to $a_{1} a_{2} \in A^{\times} .$Indeed, we have a corresponding diagram1. PRELIMINARIES
7
of rings
so that the composite map $\mathbb{Z}\left[T, T^{-1}\right] \stackrel{m}{\rightarrow} \mathbb{Z}\left[T_{1}, T_{1}^{-1}\right] \otimes_{\mathbb{Z}} \mathbb{Z}\left[T_{2}, T_{2}^{-1}\right] \rightarrow A$ sends $T \mapsto T_{1} T_{2} \mapsto a_{1} a_{2}$ as desired. The verification for the inverse is similar, and we leave it to the reader.

The upshot of this discussion is that, for every [[foag_scheme_over_a_ring#Scheme over a ring 1|scheme]] $X$, we may endow the set $\mathbb{G}_{m, \mathbb{Z}}(X)=H^{0}\left(X, \mathcal{O}_{X}\right)^{\times}$with the group structure induced by $e, i$ and $m$, and this group structure agrees with the natural multiplicative structure of $H^{0}\left(X, \mathcal{O}_{X}\right)^{\times}$.
Finally, if $S$ is a general base [[foag_scheme_over_a_ring#Scheme over a ring 1|scheme]], the multiplicative group over $S$ is simply $\mathbb{G}_{m, S}=\mathbb{G}_{m, \mathbb{Z}} \times_{\text {Spec } \mathbb{Z}} S$[^2]              , and for any test $S$-[[foag_scheme_over_a_ring#Scheme over a ring 1|scheme]] $X$ we again have canonical group isomorphisms $\mathbb{G}_{m, S}(X) \cong H^{0}\left(X, \mathcal{O}_{X}\right)^{\times}$[^2]              
## Additive group
(2) In a similar manner, we may also define the **additive group** $\mathbb{G}_{a, S}:$[^3]               again it suffices to define $\mathbb{G}_{a, Z}$, which as a [[foag_scheme_over_a_ring#Scheme over a ring 1|scheme]] is simply Spec $\mathbb{Z}[T] .$ A calculation similar to the above shows that for any test [[foag_scheme_over_a_ring#Scheme over a ring 1|scheme]] $X$ we have $\mathbb{G}_{a, \mathbb{Z}}(X)=H^{0}\left(X, \mathcal{O}_{X}\right)$ (equality as sets). We may then equip $\mathbb{G}_{a, Z}$ with the structure of a [[lombardo_av_DEFINITION 1.1|group scheme]] by endowing it with the morphisms corresponding to the ring maps
$$
\begin{aligned}
e: \mathbb{Z}[T] & \rightarrow \mathbb{Z} \quad i: \mathbb{Z}[T] \rightarrow \mathbb{Z}[T], \quad m: \mathbb{Z}[T] \rightarrow \mathbb{Z}\left[T_{1}, T_{2}\right] \\
T & \mapsto 0
\end{aligned} \quad \rightarrow \quad T \quad \mapsto T_{1}+T_{2}
$$
Finally, one checks that, given elements $\varphi_{1}, \varphi_{2}$ in $\mathbb{G}_{a, Z}(X)$, corresponding to $a_{1}, a_{2} \in H^{0}\left(X, \mathcal{O}_{X}\right)$, the map $m \circ\left(\varphi_{1}, \varphi_{2}\right)$ is the element of $\mathbb{G}_{a, \mathbb{Z}}(X)$ corresponding to $a_{1}+a_{2}$, and $i \circ \varphi_{1}$ is the element corresponding to $-a_{1} .$ In other words, for every [[foag_scheme_over_a_ring#Scheme over a ring 1|scheme]] $X$ we have canonical group isomorphisms $\mathbb{G}_{a, Z}(X) \cong\left(H^{0}\left(X, \mathcal{O}_{X}\right),+\right)$.

# See Also
- [[lombardo_av_notation_G_m_S_multiplicative_group]]
- [[lombardo_av_notation_G_a_S_additive_group]]

# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, EXAMPLE 1.2, Page 5
[^2]: ![[lombardo_av_notation_G_m_S_multiplicative_group]]
[^3]: ![[lombardo_av_notation_G_a_S_additive_group]]