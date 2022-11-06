---
cssclass: clean-embeds
aliases: []
tags: [_auto/notations_added, _auto/links_added, _meta/example, _meta/literature_note, _reference/lombardo_av, _meta/TODO/change_title]
---
# Topic[^1]
EXAMPLE 7.3. Let $C$ be the [[foag_11.1.3|curve]] over $\mathbb{Q}$ defined by $y^{2}+\left(x^{2}+x+1\right) y=-x^{6}$ and let $J$ be its [[lombardo_av_THEOREM 9.16|Jacobian]]. We determine the torsion in $J(\mathbb{Q})$.
(1) We check that $C$ has bad reduction only at 83,139
(2) By point-counting we determine that for $p=3$ the characteristic polynomial of [[lombardo_av_DEFINITION 5.4|Frobenius]] is $f_{3}(t)=t^{4}-t^{3}-3 t+9$, while for $p=5$ we have $f_{5}(t)=t^{4}-t^{3}+4 t^{2}-$ $5 t+25$
(3) Assume that $P \in J(\mathbb{Q})$ is a torsion point of order $N$, and let $\ell^{k}$ be a prime power dividing $N .$ Then the representation $\rho_{\ell^{k}}$ has a fixed point, which means that (for all primes $p \neq \ell$ at which $C$ has [[lombardo_av_DEFINITION 4.1|good]] reduction, $p \neq \ell$ ) the characteristic polynomial of the [[lombardo_av_DEFINITION 5.4|Frobenius]] at $p$ must have 1 as a root modulo $\ell^{k}$. This means in particular that $\ell^{k}$ is either a power of 3 or it divides $f_{3}(1)=6$, hence $\ell^{k} \in\left\{2,3^{k}\right\}$ For the same reason, $\ell^{k}$ is either a power of 5 (which we have already ruled out) or it divides $f_{5}(1)=24$. Combining these two pieces of information we obtain $\ell^{k} \in\{2,3\}$
(4) This already shows that $J(\mathbb{Q})_{\text {tors }}$ is killed by $6 .$ By using exercise 1.8, we check that there is no 2 -torsion in $J(\mathbb{Q})$. This implies that $J(\mathbb{Q})$ tors is either trivial or has order $3 .$
(5) Checking more characteristic polynomials of [[lombardo_av_DEFINITION 5.4|Frobenius]], a factor of 3 keeps popping up, so we suspect there might be 3-torsion in the [[lombardo_av_THEOREM 9.16|Jacobian]] after all.
(6) We notice two obvious rational points on $C$, namely $P_{1}=(0,0)$ and $P_{2}=(0,-1)$. From these two points we obtain a point in $J(\mathbb{Q})$, namely $[D]$[^2]               where $D$ is the [[lombardo_av_DEFINITION 9.1|divisor]] $P_{2}-P_{1}$. Notice that $[D] \neq 0$[^2]               for an argument we have already used many times: if $[D]=0$[^2]              , then $D=\operatorname{div}(g)$ with $g: C \rightarrow \mathbb{P}^{1}$ of [[degree_of_an_algebraic_field_extension|degree]] 1, which is not possible since $C$ and $\mathbb{P}^{1}$ are not isomorphic.
(7) We show that $3[D]=0$[^2]               : this will imply $J(\mathbb{Q})$ tors $=\{0,[D],[2 D]\}$[^2]              . We need to find a function which vanishes at $(0,-1)$ of order 3 . Such a function will necessarily be of the form $f=a(x) y+b(x)$ with $a(x), b(x)$ rational functions; replacing in the equation for $C$ we find that the $x$-coordinates of the zeroes of $f$ in the affine52
2. GALOIS REPRESENTATIONS
patch are to be found among the solutions to
$$
\left\{\begin{array}{l}
y=-b(x) / a(x) \\
\left(\frac{-b(x)}{a(x)}\right)^{2}+\left(x^{2}+x+1\right)\left(\frac{-b(x)}{a(x)}\right)=-x^{6}
\end{array}\right.
$$
Since $-x^{6}$ vanishes at $(0,-1)$ with high order, we'd like the left-hand side to do the same. Hence we may try setting it equal to 0, which gives
$$
\frac{b(x)}{a(x)}=\left(x^{2}+x+1\right)
$$
that is, $f=a(x)\left(y+x^{2}+x+1\right)$. Since we have already observed that $f$ vanishes only at points with $x=0$, for these points we have either $a(0)=0$ or $y=-1 .$ Since we want $f$ to only vanish at $P_{2}$, it suffices to choose $a(0) \neq 0$. The simplest choice $a(x)=1$ leads to
$$
\operatorname{div}(f)=6 P_{2}-3\left(\infty_{1}+\infty_{2}\right)
$$
[^3]
where $\infty_{1}, \infty_{2}$ are the two points at infinity on $C ;$ this doesn't quite work yet. Thus we now need to choose $a(x)$ so that $\operatorname{div}(a)=3\left(\infty_{1}+\infty_{2}\right)-3 P_{1}-3 P_{2}$, that is, $a(x)$ needs to have zeroes at infinity and poles precisely where $x$ vanishes. It is then immediate to deduce that we need to take $a(x)=\frac{1}{x^{3}}$, which does indeed have a pole of order 3 at both $P_{1}, P_{2}$ and a triple zero at each point at infinity. Putting everything together, we have that
$$
3 D=\operatorname{div}\left(\frac{y+x^{2}+x+1}{x^{3}}\right)=\operatorname{div}\left(\frac{x^{3}}{y}\right)
$$
and therefore $3[D]=0 \in J(\mathbb{Q})$[^2]              
Having treated this example with a minimal amount of theory, we point out that in fact one has finer tools to compare the torsion in $\operatorname{Jac}(C)(\mathbb{Q})$ with the [[foag_finite_morphism_of_schemes|finite]] groups $\operatorname{Jac}(C)\left(\mathbb{F}_{p}\right):$

# See Also

# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, EXAMPLE 7.3, Page 51
[^2]: ![[lombardo_av_notation_class_of_divisor]]
[^3]: ![[lombardo_av_notation_div_f]]