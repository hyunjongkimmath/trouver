---
cssclass: clean-embeds
aliases: []
tags: [_auto/notations_added, _auto/links_added, _meta/narrative, _meta/literature_note, _reference/lombardo_av, _meta/TODO/change_title, _meta/remark]
---
# Topic[^1]
REMARK 7.2 (Torsion of the [[lombardo_av_THEOREM 9.16|Jacobian]], global approach). There is a notion of canonical height on Jacobians. If one denotes by $\hat{h}$ this canonical height and by $h$ some naive height on [[lombardo_av_DEFINITION 9.1#Topic 1|divisors]], then $|h-\hat{h}|$ is bounded by an absolute constant $c=c(J)$, and furthermore one knows that $\hat{h}([D])=0$[^2]               if and only if $[D]$[^2]               is a torsion point. Therefore a possible approach to computing $J(\mathbb{Q})_{\text {tors }}$ is as follows: one determines $c$ from the equations of $C$, and then enumerates all points on the [[lombardo_av_THEOREM 9.16|Jacobian]] up to naive height $c$. This [[foag_finite_morphism_of_schemes|finite]] (and computable) set of [[lombardo_av_DEFINITION 9.1|divisor]] classes contains all the torsion points in $J(\mathbb{Q})$. This leaves us with two problems:
(1) enumerating [[lombardo_av_DEFINITION 9.1#Topic 1|divisors]]: this is computationally challenging when the genus increases. As a first approximation, consider that a [[lombardo_av_DEFINITION 9.1|divisor]] class on $J$ of height bounded by $c$ can be represented by a [[lombardo_av_DEFINITION 9.1|divisor]] $D=\left[P_{1}+\ldots+P_{g}-g \infty\right]$, where $\infty$ is a fixed rational point 5 and the naive height of each of the $P_{i}$ is bounded by $c .$
5 of course the situation is even more complicated if there is no rational point at all!7. TORSION IN THE JACOBIAN
51
Since the height in question is typically a logarithmic measure of size, one needs to enumerate all rational points with numerator and denominator up to $e^{c}$, and then take all possible multi-sets of size at most $g$ built from these points. It is not hard to image how this computation might quickly become unfeasible.

We note however that in order to test whether a given [[lombardo_av_DEFINITION 9.1|divisor]] is a torsion point one needs an a priori bound on its torsion order. This is typically obtained by the techniques we shall see in the following example (namely computing in $J\left(\mathbb{F}_{p}\right)$ for some small prime $p$ ).
(2) More importantly, explicit values for the constant $c$ have only been worked out for small values of $g:$ the theory is very well understood for $g=1$ (elliptic curves) and there are satisfactory answers also for $g=2[\mathbf{M S 1 6}]$, but for $g \geq 3$ no [[foag_proper_morphism_of_schemes#Complete k -scheme|complete]] answer is known (see however [Sto17] for recent progress on the $g=3$ case).
However, given a concrete [[foag_11.1.3|curve]] $C$ one may often gain a fairly [[lombardo_av_DEFINITION 4.1|good]] idea of what the torsion subgroup of $\operatorname{Jac}(C)(\mathbb{Q})$ looks like by studying the action of Galois on torsion points:

# See Also

# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, REMARK 7.2, Page 50
[^2]: ![[lombardo_av_notation_class_of_divisor]]