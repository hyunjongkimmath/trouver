---
cssclass: clean-embeds
aliases: []
tags: [_reference/lombardo_av, _meta/example, _meta/literature_note, _auto/links_added, _meta/TODO/change_title]
---
# Topic[^1]
EXAMPLE 6.4. Let us see how this works in practice for the [[foag_11.1.3|curve]] $C: y^{2}=x^{5}+x+2$ defined over $\mathbb{F}_{p}$ for $p=7$. It is useful to write $N_{m}$ for $\# C\left(\mathbb{F}_{p^{m}}\right)$. One may compute directly (that is, using some computer algebra system) that $N_{1}=10$ and $N_{2}=46$ (don't forget that there is a point at infinity!).

Now write $P_{C}(t)=p^{2} t^{4}-p a_{1} t^{3}+a_{2} t^{2}-a_{1} t+1$ (the shape of the polynomial follows from Remark 6.3, and the minus sign in front of the coefficient $a_{1}$ is for consistency with some familiar formulas in the case of elliptic curves, see below). Expanding the ratio $\frac{P_{C}(t)}{(1-t)(1-p t)}$ formally as a power series in $t$ we obtain
$$
Z(C, s)=1+t\left(-a_{1}+p+1\right)+t^{2}\left(-a_{1} p-a_{1}+a_{2}+p^{2}+p+1\right)+O\left(t^{3}\right)
$$
while from the defining formula for $Z(C, s)$ we get
$$
\begin{aligned}
Z(C, s) &=\exp \left(N_{1} t+\frac{N_{2}}{2} t^{2}+O\left(t^{3}\right)\right) \\
&=1+N_{1} t+\frac{1}{2} N_{2} t^{2}+\frac{1}{2} N_{1}^{2} t^{2}+O\left(t^{3}\right)
\end{aligned}
$$
from which we get the formulas
$$
a_{1}=p+1-N_{1}, \quad a_{2}=\frac{1}{2}\left(N_{2}+N_{1}^{2}\right)-(p+1) N_{1}+p
$$
While the formula for $a_{2}$ might not be very enlightening, the formula for $a_{1}$ should be familiar: it's precisely the definition of the so-called trace of [[lombardo_av_DEFINITION 5.4|Frobenius]] (very often denoted by $a_{p}$ ) for elliptic curves!
More generally, we have:

# See Also

# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, EXAMPLE 6.4, Page 49
