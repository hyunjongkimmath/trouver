$Z_{X}(T)$ [[poonen_curves_3.4.1 DEFINITION|denotes]] the Zeta function of the variety $X/\mathbb{F}_q$.

It is defined as 

$$Z_{X}(T):= \prod_{\text {closed points } P \in X}\left(1-T^{\operatorname{deg} P}\right)^{-1} .$$

A priori, this is a formal series, but in fact [[poonen_curves_3.4.1 DEFINITION|it converges]] for $|T| < 1/q^{\dim X}$.

It satisfies
![[poonen_curves_3.4.3 Proposition#^bf087b]]

or equivalently
![[poonen_curves_3.4.3 Proposition#^9b3b16]]

The [[poonen_curves_3.2.1 THEOREM|Weil conjectures]] [[poonen_curves_3.5.1 THEOREM|can be stated]] in terms of $Z_X(T)$: 
- $Z_X(T)$ is (the Taylor series of) a rational function.
- If $X$ is smooth and projective of dimension $d$, then it satisfies the functional equation

![[poonen_curves_3.5.1 THEOREM#^75bd16]]

where $\chi$ is the Euler characteristic of $X$.