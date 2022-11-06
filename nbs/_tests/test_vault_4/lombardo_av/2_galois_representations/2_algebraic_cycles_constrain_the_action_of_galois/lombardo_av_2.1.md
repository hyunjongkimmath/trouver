---
cssclass: clean-embeds
aliases: [lombardo_av_The_image_of_Galois_is_contained_in_GSp]
tags: [_reference/lombardo_av, _meta/literature_note, _meta/TODO/change_title, _meta/concept, _meta/narrative]
---
# The image of Galois is contained in $\operatorname{GSp}$[^1]
Let $A/K$ be a [[polarization_of_an_abelian_variety|principally polarised]] abelian variety, so that we may identify $A$ with $A^{\vee}$. 

The $\ell$[[lombardo_av_REMARK 10.11|-adic Weil pairing]]
$$
\langle\cdot, \cdot\rangle_{\ell}: T_{\ell} A \times T_{\ell} A \rightarrow \mathbb{Z}_{\ell}(A)
$$
[^2]

[^2]: ![[lombardo_av_notation_langle_rangle_ell_weil_pairing_ell_adic]]

is Galois-equivariant, that is, for all $\sigma \in \mathrm{Gal}(\bar{K} / K)$ and for all $t_{1}, t_{2} \in T_{\ell}(A)$ we have
$$
\left\langle\sigma\left(t_{1}\right), \sigma\left(t_{2}\right)\right\rangle_{\ell}=\sigma\left(\left\langle t_{1}, t_{2}\right\rangle_{\ell}\right)
$$

This means in particular that $G_{\ell^\infty}$[^3] (respectively $G_{\ell}$[^4]) is contained in the subgroup of $\operatorname{Aut}\left(T_{\ell}(A)\right)$ (resp. of $\operatorname{Aut}(A[\ell])$ ) consisting of those automorphisms $M$ that satisfy
$$
\langle M v, M w\rangle_{\ell}=\lambda(M)\langle v, w\rangle_{\ell}
$$
for some $\lambda(M) \in \mathbb{Z}_{\ell}^{\times}$(respectively $\mathbb{F}_{\ell}^{\times}$). [[lombardo_av_DEFINITION 2.1_page_39|This group deserves a name]]:

[^3]: ![[lombardo_av_notation_G_ell_infty_image_of_ell_adic_galois]]
[^4]: ![[lombardo_av_notation_G_ell_n_image_of_galois]]

# See Also

# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, 2.1, Page 38