---
cssclass: clean-embeds
aliases: [lombardo_av_Automorphisms_of_a_curve_induce_automorphisms_of_its_Jacobian]
tags: [_auto/notations_added, _meta/concept, _meta/literature_note, _reference/lombardo_av, _meta/TODO/change_title, _meta/proof]
---
# Automorphisms of a curve induce automorphisms of its Jacobian[^1]
Let $\alpha: C \rightarrow C$ be an automorphism of a [[lombardo_av_1.1|nice curve]] of genus at least $2$. 

Then $\alpha$ induces a nontrivial automorphism $\alpha: \operatorname{Jac}(C) \rightarrow \operatorname{Jac}(C) ;$ in other words, $\operatorname{Aut}(C)$ embeds into $\operatorname{Aut}(\operatorname{Jac}(C))$

# Proof
PROOF. The map induced by $\alpha$ on $\operatorname{Jac}(C)$ is not hard to construct using the universal property; here is a concrete description: the divisor class $[D]=\left[\sum P_{i}-\sum Q_{j}\right]$[^2]              , of degree 0, is sent to $[\alpha(D)]:=\left[\sum \alpha\left(P_{i}\right)-\sum \alpha\left(Q_{j}\right)\right] .$ This definition is well posed, because if $D=\operatorname{div}(f)$[^3]               is principal then $\alpha(D)=\operatorname{div}(f \circ \alpha)$ is again principal.

Now we show that nontrivial automorphisms of $C$ induce nontrivial automorphisms of $\operatorname{Jac}(C) .$ Let $Q$ be a point such that $\alpha(Q) \neq Q, P$ and suppose that $\alpha(i(Q))=i(Q)$, that is, $[\alpha(Q)-\alpha(P)]=[Q-P] .$ Then $D:=\alpha(Q)-\alpha(P)+P-Q$ is principal, so it is the divisor of a function $f: C \rightarrow \mathbb{P}^{1}$ of degree $2 ;$ by definition, this is only possible if $C$ is hyperelliptic. So if $C$ is not hyperelliptic we are done; if instead $C$ is hyperelliptic we distinguish three cases:
(1) $C$ is hyperelliptic and $\alpha(P)=P .$ Then $[\alpha(Q)-\alpha(P)]=[Q-P]$ implies $[\alpha(Q)-$ $Q]=0$, which means that $\alpha(Q)-Q$ is the divisor of a function $f_{Q}: C \rightarrow \mathbb{P}^{1}$ of degree 1 , contradiction.
(2) $C$ is hyperelliptic, $\alpha(P) \neq P$, and there is a 2 -to- 1 function $x: C \rightarrow \mathbb{P}^{1}$ such that $x(P)=0$ and $x(\alpha(P))=\infty$. If $\alpha$ induces the identity on the Jacobian, then for every $Q$ (with at most finitely many exceptions) we have that $\alpha(Q)-\alpha(P)+P-Q$ is the divisor of a function $f_{Q}$ of degree 2 to $\mathbb{P}^{1}$. We recall that every hyperelliptic curve of genus at least 2 is hyperelliptic in a unique way; hence $f_{Q}$ is a rational function of $x: C \rightarrow \mathbb{P}^{1}$, and we may write $f_{Q}=\frac{a_{Q} x+b_{Q}}{c_{Q} x+d_{Q}}$ for some constants $a_{Q}$, $b_{Q}, c_{Q}, d_{Q} .$ Since $f_{Q}(P)=0=\frac{b_{Q}}{d_{Q}}$ we obtain $b_{Q}=0$, and since $f_{Q}(\alpha(P))=\infty$ we obtain $c_{Q}=0 .$ It follows that $\operatorname{div}\left(f_{Q}\right)$ is independent of $Q$, but this contradicts the fact that $\operatorname{div}\left(f_{Q}\right)=\alpha(Q)-Q+P-\alpha(P)$
(3) $C$ is hyperelliptic, $\alpha(P) \neq P$, and for all 2 -to-1 functions $x: C \rightarrow \mathbb{P}^{1}$ we have $x(P)=x(\alpha(P)) .$ This immediately leads to a contradiction, because the functions $f_{Q}$ (defined as above) are 2 -to- 1 and take different values at $P, \alpha(P)$.

# See Also

# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, PROPOSITION 9.22, Page 30
[^2]: ![[lombardo_av_notation_class_of_divisor]]
[^3]: ![[lombardo_av_notation_div_f]]