---
cssclass: clean-embeds
aliases: []
tags: [_auto/notations_added, _auto/links_added, _meta/literature_note, _reference/lombardo_av, _meta/TODO/change_title, _meta/definition]
---
# Topic[^1]
EXAMPLE 1.18 (Real multiplication by $\mathbb{Z}\left[\frac{1+\sqrt{5}}{2}\right]$ ). We take this example from $[\mathbf{K M} \mathbf{1} \mathbf{6}]$. Consider the [[foag_11.1.3|curve]]
$$
C: u^{2}=h(t):=t^{5}-t^{4}+t^{3}+t^{2}-2 t+1
$$
with [[lombardo_av_THEOREM 9.16|Jacobian]] $J$. Define $Z$ to be the [[foag_11.1.3|curve]]
$$
Z:\left\{\begin{array}{l}
u^{2}=h(t) \\
t^{2} x^{2}-x-t+1=0
\end{array}\right.
$$
The obvious map $\varphi: Z \rightarrow C$ given by $(t, u, x) \mapsto(t, u)$ is a 2 -to- 1 cover, but there is also a further map $Z \rightarrow C$ given by
$$
\psi:(u, t, x) \mapsto\left(x, \frac{u}{t^{3}}(1-x(t+1))\right)
$$
One may check that $T:=\psi_{*} \varphi^{*}$ is an [[lombardo_av_DEFINITION 5.9|endomorphism]] of $J$ with minimal polynomial $T^{2}-$ $T-1$, hence it generates a subring of End $_{\mathbb{Q}}^{0}(J)$ isomorphic to $\mathbb{Z}\left[\frac{1+\sqrt{5}}{2}\right]$
We now show that $\mathbb{Z}\left[\frac{1+\sqrt{5}}{2}\right]$ is the full ring of endomorphisms of $J_{\mathbb{Q}}$
First we compute $f_{3}(t)=t^{4}+3 t^{3}+7 t^{2}+9 t+9$ and $f_{5}(t)=t^{4}+2 t^{3}+6 t^{2}+10 t+25 ;$ as $f_{3}(t)$ is [[foag_irreducible_topological_space|irreducible]] over $\mathbb{Q}$, this implies that $J_{\mathbb{Q}}$ is [[18785_simple_ring|simple]]. Further manipulations of $f_{3}(t)$ (see exercise 2.15 ) show that $J$ is [[foag_geometric_point#Geometric properties|geometrically]] [[18785_simple_ring|simple]], and that its geometric [[lombardo_av_DEFINITION 5.9|endomorphism]] ring is commutative. It follows from theorem 1.1 that $D:=$ End $\frac{0}{\mathbb{Q}}(J)$ is a field, and we already know that it contains $\mathbb{Q}(\sqrt{5}) .$ Hence there are only two possibilities: either $D=\mathbb{Q}(\sqrt{5})$, or $D$ is a quartic [[lombardo_av_DEFINITION 2.1_page_60|CM field]].

One checks (using proposition 1.12) that $J$ is [[lombardo_av_DEFINITION 1.11|ordinary]] at 3 and 5, which implies (by theorems 1.13 and 2.15 ) that $\operatorname{End}_{\mathrm{F}_{3}}^{0}(J)=\operatorname{End}_{\mathrm{F}_{3}}(J)=\mathbb{Q}[t] /\left(f_{3}(t)\right)=: F_{3}$ and $\operatorname{End}_{\mathrm{F}_{5}}(J)=$ End $_{\left[F_{5}\right.}(J)=\mathbb{Q}[t] /\left(f_{5}(t)\right)=: F_{5} .$ It follows that if $D$ were a quartic [[lombardo_av_DEFINITION 2.1_page_60|CM field]], the three fields $F_{3}, F_{5}$ and $D$ should all coincide. It is easy to see (for example computing discriminants) that this does not happen, so $D$ cannot be a [[lombardo_av_DEFINITION 2.1_page_60|CM field]]. Finally, since $D=\mathbb{Q}(\sqrt{5})$ and $\mathbb{Z}\left[\frac{1+\sqrt{5}}{2}\right]$ is the unique maximal order of $D$, we deduce as desired that End $_{\mathbb{Q}}(J)=\mathbb{Z}\left[\frac{1+\sqrt{5}}{2}\right]$
2. Complex multiplication
In this final paragraph we quickly review the theory of [[lombardo_av_DEFINITION 1.9|complex multiplication]] from the point of view of Galois representations.60
3. ENDOMORPHISM ALGEBRAS, COMPLEX MULTIPLICATION, AND EXAMPLES
In this section $A$ will be a $g$-dimensional [[lombardo_av_1.3|abelian variety]] defined over a [[number_field|number field]] $^{1} K$ of [[lombardo_av_DEFINITION 2.2|CM type]] (see definition 1.9 ). The general principle is that everything about CM [[lombardo_av_1.3|abelian varieties]] is well understood, but of course turning this vague (and optimistic) statement into actual computations can be challenging at times! See for example Exercise 2.14.

The most important results (due variously to Shimura, Taniyama, Weil, Serre and Tate, and nicely explained in [ST68]) are as follows.
(1) $A$ has potential [[lombardo_av_DEFINITION 4.1|good]] reduction at all places of $K .$
(2) from now on, suppose that $A / K$ has [[lombardo_av_DEFINITION 1.9|complex multiplication]] defined over $K-$ that is, $\operatorname{End}_{K}(A)=\operatorname{End}_{K}(A) .$[^2]               Let $E:=\operatorname{End}_{K}^{0}(A)$ be the field of [[lombardo_av_DEFINITION 1.9|complex multiplication]] and let $R=$ End $_{K}(A) .$ Then $V_{\ell}(A)$[^3][^4]               is a free $E_{\ell}:=E \otimes \mathbb{Q}_{\ell}$-vector space of dimension 1 , and $T_{\ell}(A)$[^5]               is a free $R_{\ell}:=R \otimes \mathbb{Z}_{\ell}$-module of rank 1 provided that $\ell$ does not divide the index of $R$ inside the maximal order of $E .$ Moreover, an element of $E_{\ell}$ carries $T_{\ell}(A)$[^5]               to itself if and only if it is contained in $R_{\ell}$.
(3) Using this, we may identify the [[lombardo_av_DEFINITION 1.1_page_37|Galois representation]]
$$
\rho_{\ell} \infty: \operatorname{Gal}(\bar{K} / K) \rightarrow \operatorname{Aut}\left(T_{\ell}(A)\right)
$$
[^5]
with a representation
$$
\rho_{\ell^{\infty}}: \operatorname{Gal}(\bar{K} / K) \rightarrow R_{\ell}^{\times}
$$
[^6][^7]
(4) For each [[place_of_a_global_field#Place of a global field 1|place]] $v$ of $K$ there is a [[lombardo_av_DEFINITION 5.1|homomorphism]]
$$
\varphi_{v}: I(v) \rightarrow \mu(E)
$$
from the [[18785_Definition 7.9#Inertia group 1|inertia group]] at $v$ to the group of roots of unity in $E$. The [[fixed_field_by_group|fixed field]] of its [[lombardo_av_DEFINITION 5.1|kernel]] is the minimal extension of $K$ over which $A$ acquires [[lombardo_av_DEFINITION 4.1|good]] reduction at the places above $v ;$ in particular, $\varphi_{v}$ is trivial if $A$ has [[lombardo_av_DEFINITION 4.1|good]] reduction at $v$.
(5) let $n_{v}$ be the minimal integer such that $\varphi_{v}$ is trivial on the $n_{v}$-th ramification group $I(v)^{\left(n_{v}\right)}$ (in the upper numbering). Then the exponent of the conductor of $A$ at $v$ is equal to $2 \operatorname{dim}(A) n_{v}$
(6) there is a map $\psi_{\ell}$[^8]              , which we describe below, such that for every idèle $a \in I_{K}$ we have
$$
\rho_{\ell^{\infty}}(a)=\varepsilon(a) \psi_{\ell}\left(a_{\ell}^{-1}\right)
$$
[^6][^7][^8]
where $a_{\ell}$ is the component of $\ell$ along the places of characteristic $\ell$.
(7) $\varepsilon$ agrees with $\varphi_{v}$ upon restriction to $U_{v}(K)$, the group of units of the [[18785_Definition 1.25|ring of integers]] of the [[completion_of_a_metric_space#Completion of a metric space that is a ring|completion]] $K_{v}$
In order to describe the map $\psi_{\ell}$[^8]               we need to introduce some further concepts specific to CM [[lombardo_av_1.3|abelian varieties]]:


# See Also

# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, EXAMPLE 1.18, Page 59
[^2]: ![[lombardo_av_notation_End_K_A]]
[^3]: ![[lombardo_av_notation_V_ell_A]]
[^4]: ![[lombardo_av_notation_V_ell_A_rational_tate_module]]
[^5]: ![[lombardo_av_notation_T_ell_A]]
[^6]: ![[lombardo_av_notation_rho_ell_infty]]
[^7]: ![[lombardo_av_notation_rho_ell_infty_ell_adic_representation]]
[^8]: ![[lombardo_av_notation_psi_ell]]