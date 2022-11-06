---
cssclass: clean-embeds
aliases: []
tags: [_reference/lombardo_av, _meta/literature_note, _meta/exercise, _auto/links_added, _meta/TODO/change_title]
---
# Topic[^1]
EXERCISE 2.11. Consider the [[lombardo_av_THEOREM 9.16|Jacobian]] $J / \mathbb{Q}$ of the [[foag_11.1.3|curve]] $y^{2}+y=x^{5}-2 x^{4}+2 x^{3}-x^{2}$. Determine for which primes $\ell$ there is a $\mathbb{Q}$-rational [[lombardo_av_DEFINITION 5.3|isogeny]] of [[degree_of_an_algebraic_field_extension|degree]] $\ell$ from $J$ to another [[lombardo_av_1.3|abelian variety]].
Hint. Here is a possible way to attack this problem:
(1) Assume that $J[\ell]$ admits a cyclic submodule $H \cong \mathbb{F}_{\ell}$ which is stable under Galois. This induces a character $\psi: \operatorname{Gal}(\bar{K} / K) \rightarrow \operatorname{Aut}(H) \cong \mathbb{F}_{\ell}^{\times}$which is [[lombardo_av_DEFINITION 5.1_page_47|unramified]] outside $\ell$ and the primes of bad reduction of $J$.
(2) Show that $\psi=\varepsilon \chi_{\ell}^{i}$, where $\varepsilon$ is ramified at most at the primes of bad reduction of $J$ and $i \in 0,1$ (you will need theorem 9.1 ).
(3) It follows (why?) that the conductor of $\rho_{\ell}$ is divisible by $\operatorname{cond}(\varepsilon)^{2}$.
(4) In the case at hand, this implies that $\varepsilon$ is trivial.
(5) Hence we have that for every $p$ of [[lombardo_av_DEFINITION 4.1|good]] reduction the characteristic polynomial of $\rho_{\ell}\left(\right.$ Frob $\left._{p}\right)$ (which is just the reduction modulo $\ell$ of $\left.f_{p}(t)\right)$ has a root of the form $\chi \ell\left(\text { Frob }_{p}\right)^{i}$ for some $i=0,1 .$ Moreover, $\chi_{\ell}\left(\text { Frob }_{p}\right)^{i} \equiv p^{i}(\bmod \ell) .$
(6) This should be enough to reduce the problem to a [[foag_finite_morphism_of_schemes|finite]] list of cases.

# See Also

# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, EXERCISE 2.11, Page 66
