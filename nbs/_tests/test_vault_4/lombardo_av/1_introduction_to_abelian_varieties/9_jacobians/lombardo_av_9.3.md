---
cssclass: clean-embeds
aliases: []
tags: [_reference/lombardo_av, _meta/literature_note, _meta/exercise, _auto/links_added, _meta/TODO/change_title, _meta/example]
---
# Topic[^1]
9.3. Example: adding points on a [[lombardo_av_THEOREM 9.16|Jacobian]]. We take the [[foag_11.1.3|curve]] of this example from [CF96]. Consider the [[foag_11.1.3|curve]]
$$
C: y^{2}=x(x-1)(x-2)(x-5)(x-6)
$$
$C$ has a single point at infinity, which we denote by $\infty$; we embed $C$ into $\operatorname{Jac}(C)$ by sending $\infty$ to $[0] \in \operatorname{Jac}(C)(\mathbb{Q})$
We now define [[lombardo_av_DEFINITION 9.1|divisor]] classes (of [[degree_of_an_algebraic_field_extension|degree]] 0 )
$$
A=[(0,0)+(1,0)-2 \infty] \text { and } B=[(2,0)+(3,6)-2 \infty]
$$
on the [[lombardo_av_THEOREM 9.16|Jacobian]] of $C$. We show some manipulations involving the points $A$ and $B$ on the [[lombardo_av_THEOREM 9.16|Jacobian]]; in particular, we want to determine a [[lombardo_av_DEFINITION 9.1|divisor]] $D_{1}+D_{2}-2 \infty$ on $C$ that represents the same [[lombardo_av_DEFINITION 9.1|divisor]] class as $A+B$.

We first find a function vanishing at all the points in the support of $A$ and $B$ : for example, $f: y-x(x-1)(x-2)$ works. Substituting this into the equation for $C$ we find $x(x-1)(x-2)(x-3)\left(x^{2}-x+10\right)=0$. Thus the [[lombardo_av_DEFINITION 9.1|divisor]] of the function $f$ is
$$
(0,0)+(1,0)+(2,0)+(3,6)+C_{1}+C_{2}-6 \infty=A+B+C_{1}+C_{2}-2 \infty,
$$
where
$$
C_{1}=\left(\frac{1}{2}+\frac{1}{2} \sqrt{-39}, 15-5 \sqrt{-39}\right), \quad C_{2}=\left(\frac{1}{2}-\frac{1}{2} \sqrt{-39}, 15+5 \sqrt{-39}\right)
$$
Since $[\operatorname{div} f]=[0]$ in $\operatorname{Jac}(C)$, we have thus proven
$$
[A+B]=[A+B-\operatorname{div} f]=\left[2 \infty-C_{1}-C_{2}\right]
$$
Suppose we want to find a representative of the form $\left[D_{1}+D_{2}-2 \infty\right]$ : then we need to find a function with [[lombardo_av_DEFINITION 9.1|divisor]] $C_{1}+C_{2}+D_{1}+D_{2}-4 \infty$. But we already know such a function! Indeed, $C_{1}, C_{2}$ are zeroes of $x^{2}-x+10$ which, being of [[degree_of_an_algebraic_field_extension|degree]] 4 and regular on the affine chart of our [[foag_11.1.3|curve]], satisfies exactly
$$
\operatorname{div}\left(x^{2}-x+10\right)=C_{1}+C_{2}+D_{1}+D_{2}-4 \infty
$$
with
$$
D_{1}=\left(\frac{1}{2}+\frac{1}{2} \sqrt{-39},-15+5 \sqrt{-39}\right), \quad D_{2}=\left(\frac{1}{2}-\frac{1}{2} \sqrt{-39},-15-5 \sqrt{-39}\right)
$$
Hence $A+B=\left[D_{1}+D_{2}-2 \infty\right]$ on $\operatorname{Jac}(C) ;$ notice that once we find $A+B=\left[2 \infty-C_{1}-C_{2}\right]$ we also obtain the same conclusion by observing that the [[foag_hyperelliptic_curve|hyperelliptic]] involution induces10. TORSION POINTS, THE TATE MODULE
33
-id on the [[lombardo_av_THEOREM 9.16|Jacobian]] (exercise 1.9 ), which means that (denoting by $\bar{P}$ the point $(x,-y)$ when $P=(x, y))$ we have
$$
\iota(\bar{P})=-\iota(P) \Leftrightarrow[\bar{P}-\infty]=[\infty-P]
$$
Applying this in our particular example we obtain
$$
A+B=\left[2 \infty-C_{1}-C_{2}\right]=\left[-2 \infty+\overline{C_{1}}+\overline{C_{2}}\right]=\left[D_{1}+D_{2}-2 \infty\right]
$$
10. Torsion points, the Tate module
In this course we are mainly interested in the torsion points of [[lombardo_av_1.3|abelian varieties]]. Recall the definition of the group of $n$-torsion points of an [[lombardo_av_1.3|abelian variety]]:


# See Also

# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, 9.3, Page 32
