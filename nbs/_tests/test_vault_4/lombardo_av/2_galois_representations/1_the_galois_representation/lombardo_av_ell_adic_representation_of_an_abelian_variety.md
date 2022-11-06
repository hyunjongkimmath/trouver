---
cssclass: clean-embeds
aliases: [lombardo_av_image_of_galois]
tags: [_reference/lombardo_av, _meta/definition, _meta/literature_note, _meta/narrative, _meta/notation]
---
# $\ell$-adic Galois representation of an abelian variety[^1]
The general problem we would like to solve is that of describing (as precisely and as concretely as possible) the image of the Galois representations $\rho_{\ell^{n}}$[^2].

[^2]: ![[lombardo_av_DEFINITION 1.1_page_37|lombardo_av_mod_ell_n_galois_representation_of_an_abelian_variety]]

In order to dispense with the dependence on $n$, it is often useful to pass to the limit $n \rightarrow \infty$ and work with the so-called **$\ell$-adic representation**
$$
\rho_{\ell^\infty}: \operatorname{Gal}(\bar{K} / K) \rightarrow \operatorname{Aut}\left(T_{\ell} A\right)
$$
[^3]

[^3]: ![[lombardo_av_notation_T_ell_A]]

This representation is again continuous and will be our main object of study. 

We shall use the informal term **image of Galois** to refer to either the groups
$$
G_{\ell^{n}}:=\rho_{\ell}(\mathrm{Gal}(\bar{K} / K)) \subseteq \operatorname{Aut}\left(A\left[\ell^{m}\right]\right)
$$
or their $\ell$-adic counterpart,
$$
G_{\ell \infty}:=\rho_{\ell ^\infty}(\mathrm{Gal}(\bar{K} / K)) \subseteq \operatorname{Aut}\left(T_{\ell}(A)\right)
$$
These groups do of course depend on $\ell$ but - in a sense that will be made precise later they are conjectured to be very similar to each other.
# See Also
- [[lombardo_av_notation_rho_ell_infty_ell_adic_representation]]
- [[lombardo_av_notation_G_ell_n_image_of_galois]]
- [[lombardo_av_notation_G_ell_infty_image_of_ell_adic_galois]]
- [[lombardo_av_NOTATION 1.4]]
- [[lombardo_av_2.1|lombardo_av_The_image_of_Galois_is_contained_in_GSp]]
- Examples
	- [[lombardo_av_EXAMPLE 2.3|lombardo_av_Image_of_Galois_for_elliptic_curves]]
# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, 2.1, Page 38