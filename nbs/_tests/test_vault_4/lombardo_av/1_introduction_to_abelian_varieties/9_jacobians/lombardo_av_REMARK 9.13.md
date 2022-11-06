---
cssclass: clean-embeds
aliases: []
tags: [_auto/notations_added, _auto/links_added, _meta/literature_note, _reference/lombardo_av, _meta/TODO/change_title, _meta/remark]
---
# Topic[^1]
REMARK 9.13. In fancier language, we have an exact sequence of Galois modules
$$
0 \rightarrow \operatorname{Princ}_{C}(\bar{K}) \rightarrow \operatorname{Div}_{C}^{0}(\bar{K}) \rightarrow \operatorname{Pic}_{C}^{0}(\bar{K}) \rightarrow 0
$$
[^2][^3][^4][^5][^6][^7][^8]
and taking invariants under Gal $(\bar{K} / K)$ we get a long exact sequence in cohomology
$$
0 \rightarrow \operatorname{Princ}_{C}(K) \rightarrow \operatorname{Div}_{C}^{0}(K) \rightarrow \operatorname{Pic}_{C}^{0}(\bar{K})^{\mathrm{Gal}(\bar{K} / K)} \rightarrow H^{1}\left(K, \operatorname{Princ}_{C}(K)\right)
$$
[^2][^3][^4][^5][^6][^7][^9]
where the last arrow may in general not be surjective. More precisely, since we also have
$$
0 \rightarrow \bar{K}^{\times} \rightarrow \bar{K}(C)^{\times} \rightarrow \operatorname{Princ}_{C}(\bar{K}) \rightarrow 0
$$
[^7][^8]
we may again take cohomology to find
$$
\begin{array}{rlrr}
0 & \rightarrow & K^{\times} \rightarrow & K(C)^{\times} \rightarrow & \operatorname{Princ}_{C}(K) \\
& \rightarrow & H^{1}\left(\Gamma_{K}, \bar{K}^{\times}\right)=0 \rightarrow & H^{1}\left(\Gamma_{K}, \bar{K}(C)^{\times}\right) \rightarrow & H^{1}\left(\Gamma_{K}, \operatorname{Princ}_{C}(\bar{K})\right) \\
& \rightarrow & H^{2}\left(\Gamma_{K}, \bar{K}^{\times}\right)=\operatorname{Br}(K) &
\end{array}
$$
[^7][^8][^9]
where we have used Hilbert's theorem $90\left(H^{1}\left(K, \bar{K}^{\times}\right)=0\right)$ and which already shows that the obstruction to surjectivity of the natural map $\operatorname{Pic}_{C}(K) \rightarrow \operatorname{Pic}_{C}(\bar{K})^{\mathrm{Gal}(K / K)}$[^10][^6]               should be measured by elements in the Brauer group of $K$.

To be even more precise (and even fancier), consider the structure map $\pi: C \rightarrow$ $\operatorname{Spec}(k)$. By the usual interpretation of [[lombardo_av_DEFINITION 9.1#Topic 1|divisors]] as [[foag_locally_free_sheaf_on_a_scheme#invertible sheaf 2|line bundles]], one may define the Picard26
1. INTRODUCTION TO ABELIAN VARIETIES
[[foag_scheme_over_a_ring#Scheme over a ring 1|scheme]] of $C$ as $H^{1}\left(C, \mathbb{G}_{m}\right)$; we now see how the Picard schemes of $C$ and $C_{K}$ fit in a natural exact sequence. Recall the following form of the spectral sequence of composed functors: for a morphism of schemes $f: Y \rightarrow X$ and for a sheaf $\mathcal{F}$ on $Y$ there is a second-page spectral sequence $H^{p}\left(X, R^{q} f_{*} \mathcal{F}\right) \Rightarrow H^{p+q}(Y, \mathcal{F}) .$ Taking the sequence of low-[[degree_of_an_algebraic_field_extension|degree]] terms for the case $Y=C, X=\operatorname{Spec}(K)$ and $\mathcal{F}=\mathbb{G}_{m}$ yields
$$
0 \rightarrow H^{1}\left(K, \pi_{*} \mathbb{G}_{m}\right) \rightarrow H^{1}\left(C, \mathbb{G}_{m}\right) \rightarrow H^{0}\left(K, R^{1} \pi_{*} \mathbb{G}_{m}\right) \rightarrow H^{2}\left(K, \pi_{*} \mathbb{G}_{m}\right)
$$
or, in more familiar terms,
$$
0 \rightarrow H^{1}\left(K, \bar{K}^{\times}\right) \rightarrow H^{1}\left(C, \mathcal{O}_{C}^{\times}\right) \rightarrow H^{0}\left(K, H^{1}\left(C_{K}, \mathcal{O}_{C}^{\times}\right)\right) \rightarrow H^{2}\left(K, \bar{K}^{\times}\right)
$$
that is,
$$
0 \rightarrow 0 \rightarrow \operatorname{Pic}_{C}(K) \rightarrow \operatorname{Pic}_{C}(\bar{K})^{\mathrm{Gal}(K / K)} \rightarrow \operatorname{Br}(K)
$$
[^10][^6]
The next term in the exact sequence is the so-called algebraic Brauer group of $C$. Note that we have used the equality $H^{1}\left(C, \mathcal{O}_{C}^{\times}\right)=\operatorname{Pic}_{C}(K)$[^10][^6]              , which follows from the fact (that we haven't proven ) that the Picard group of $C$ can be interpreted as $H^{1}\left(C, \mathbb{G}_{m}\right)$ also over non-algebraically closed fields.


# See Also

# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, REMARK 9.13, Page 25
[^2]: ![[lombardo_av_notation_Div_C]]
[^3]: ![[lombardo_av_notation_Div_C_0]]
[^4]: ![[lombardo_av_notation_Div_C_K]]
[^5]: ![[lombardo_av_notation_Pic_C_0_degree_0_picard]]
[^6]: ![[lombardo_av_notation_Pic_C_picard_group]]
[^7]: ![[lombardo_av_notation_princ_C]]
[^8]: ![[lombardo_av_notation_princ_C_bar_K]]
[^9]: ![[lombardo_av_notation_Princ_C_K]]
[^10]: ![[lombardo_av_notation_Pic_C_K]]