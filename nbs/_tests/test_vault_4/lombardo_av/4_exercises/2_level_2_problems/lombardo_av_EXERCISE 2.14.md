---
cssclass: clean-embeds
aliases: []
tags: [_auto/notations_added, _auto/links_added, _meta/exercise, _meta/literature_note, _reference/lombardo_av, _meta/TODO/change_title]
---
# Topic[^1]
EXERCISE 2.14. Let $C / \mathbb{Q}$ be the [[foag_11.1.3|curve]] given by the equation $y^{2}=x^{5}+1$ and let $J / \mathbb{Q}$ be its [[lombardo_av_THEOREM 9.16|Jacobian]]. Determine, for every prime $p>5$ with $p \neq 1(\bmod 5)$, the number of $\mathbb{F}_{p}$-points of $J .$ Equivalently, determine the number of $\mathbb{F}_{p^{-}}$and $\mathbb{F}_{p^{2}-p o i n t s}$ of the [[foag_11.1.3|curve]] $y^{2}=x^{5}+1$
Hint. This can be a hard problem. Here is a sketch of solution:
(1) Reduce to working over $K=\mathbb{Q}\left(\zeta_{5}\right)$
(2) the only [[lombardo_av_DEFINITION 4.1|places of bad reduction]] of $C$ are 2 and 5, hence the only [[lombardo_av_DEFINITION 4.1|places of bad reduction]] of $C / K$ are contained in $\left\{2,1-\zeta_{5}\right\}$
(3) the conductor of $C$ over $\mathbb{Q}\left(\zeta_{5}\right)$ is $2^{4}\left(1-\zeta_{5}\right)^{4}$. This implies that $\varphi_{v}($ for $v=2$ or $\left.v=1-\zeta_{5}\right)$ is trivial on the principal units.
(4) if $p \equiv-1(\bmod 5)$ is written in the form $p=(a+b \omega)\left(a+b \omega^{\sigma}\right)$, where $\omega=\frac{-1+\sqrt{5}}{2}$ and $\sigma$ is the generator of $\operatorname{Gal}(\mathbb{Q}(\sqrt{5}) / \mathbb{Q})$, then $(a+b \omega) \equiv \pm 2\left(\bmod 1-\zeta_{5}\right)$
(5) let $c$ be the idèle whose $v$-component is 1 for all $v$, except for $v=a+b \omega$, where it takes the values $a+b \omega$. Then $\rho_{\ell}(c)=\rho_{\ell}\left(c^{\prime}\right)$, where $c^{\prime}$ is the idèle with $v$-component equal to $\frac{1}{a+b \omega}$ for $v \neq a+b \omega$ and $c_{a+b \omega}^{\prime}=1$. Now you are [[foag_reduced_scheme|reduced]] to computing $\psi_{\ell}(a+b \omega)$[^2]               and $\varphi_{v}\left(\frac{1}{a+b \omega}\right)$ for all $v$
(6) for $v=2$, the algebraic number $a+b \omega$ has order dividing 3 in the residue field $\mathbb{F}_{v}$, hence its image via $\varphi_{v}$ is trivial
(7) finally, for $v=1-\zeta_{5}$, the image in $\mathbb{F}_{v} \cong \mathbb{F}_{5}$ of $\frac{1}{a+b \omega}$ is $\pm 2$, which is a generator of $\mathbb{F}_{5}^{\times}$. This should tell you the value of $\varphi_{v}(a+b \omega)$
(8) putting everything together, you should now have a [[18785_simple_ring|simple]] formula for the trace of Frob $_{p}^{2}$

# See Also

# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, EXERCISE 2.14, Page 67
[^2]: ![[lombardo_av_notation_psi_ell]]