---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]
\begin{theorem}
\label{thm: TateStrong}
Let $\mathsf{M}$ be a connected smooth variety over $\mathbb{Z}_p$, and let $f \colon \mathscr{X} \to \mathsf{M}$ be a smooth projective family of varieties whose characteristic $0$ fibers have Hodge number $h^{2, 0} = 1$. Let $\eta$ be the generic point of $\mathsf{M}$ and assume that $\mathrm{NS}(\mathscr{X}_{\eta})_\mathbb{Q} = \mathrm{NS}(\mathscr{X}_{\bar{\eta}})_\mathbb{Q}$. Let $\ell$ be any prime $\neq p$ and let $\mathbb{V}_\ell := \mathrm{PH}^2_\mathrm{{\acute{e}}t}(\mathscr{X}/ \mathsf{M}, \mathbb{Q}_\ell)$. Assume the following conditions:
\begin{enumerate}[label=\upshape{(\alph*)}]
    \item The $\mathbb{Q}$-family $\mathscr{X}|_{\mathsf{M}_\mathbb{Q}}$ satisfies property $(\heartsuit)$;
    \item For some (and hence every) point $b \in \mathsf{M}(\mathbb{C})$, the quadratic $\mathbb{Z}_{(p)}$-lattice $\mathrm{PH}^2(\mathscr{X}_b(\mathbb{C}), \mathbb{Z}_{(p)})$ is self-dual;
    \item Let $S$ be any irreducible component of $\mathsf{M}_{\bar{\mathbb{F}}_p}$ and let $\bar{\eta}_S$ be a geometric generic point. Then the $\mathrm{Mon}^\circ(\mathbb{V}_\ell|_{S}, \bar{\eta}_S)$-invariant part of $\mathbb{V}_\ell|_{\bar{\eta}_S}$ is spanned by the image of the specialization map $\mathrm{NS}(\mathscr{X}_{\eta})_\mathbb{Q} \to \mathrm{NS}(\mathscr{X}_{\bar{\eta}_S})_\mathbb{Q}$.
\end{enumerate}
Then for every finite field $k$ over $\mathbb{F}_p$ and $s \in \mathsf{M}(k)$, the fiber $\mathscr{X}_s$ satisfies the Tate conjecture. 
\end{theorem}
\begin{proof}
 Fix the point $b \in \mathsf{M}(\mathbb{C})$ lying above $k(\bar{\eta})$ as a base point and let $L$ be the quadratic $\mathbb{Z}_{(p)}$-lattice $\mathrm{PH}^2(\mathscr{X}_b(\mathbb{C}), \mathbb{Z}_{(p)})$. Let $G \coloneqq \mathrm{SO}(L_{(p)})$ and $\widetilde{G} := \mathrm{CSpin}(L_{(p)})$. Let $K \subseteq G(\mathbb{A}_f)$ be a neat compact open subgroup of the form $K_p K^p$ where $K_p = G(\mathbb{Z}_p)$ and $K^p \subseteq G(\mathbb{A}^p_f)$ and let $\mathcal{K} \subseteq \widetilde{G}(\mathbb{A}_f)$ be the preimage of $K$. Up to replacing $\mathsf{M}$ by a connected \'etale cover, Thm~\ref{thm: integral period} gives us a morphism $\rho : \mathsf{M} \to \mathscr{S}_K(G)$. Since the natural morphism $\mathscr{S}_\mathcal{K}(\widetilde{G}) \to \mathscr{S}_K(G)$ is \'etale, up to replacing $\mathsf{M}$ by a further connected \'etale cover, we may assume that $\rho$ lifts to a morphism $\widetilde{\rho} : \mathsf{M} \to \mathscr{S}_\mathcal{K}(\widetilde{G})$. Let the abelian scheme $\mathscr{A} \to \mathscr{S}_\mathcal{K}(\widetilde{G})$ and sheaves $\mathbf{H}_*, \mathbf{L}_*$ on $\mathscr{S}_\mathcal{K}(\widetilde{G})$ be as in \S\ref{sec: integral period}. Let $\kappa$ be a field and let $s, t$ be $\kappa$-points of $\mathscr{S}_{\mathcal{K}}(\widetilde{G})_\kappa$ and $\mathsf{M}_\kappa$ respectively such that $\widetilde{\rho}(t) = s$. 

We first observe that if $\mathrm{char\,} \kappa = 0$, then there is an isomorphism $\theta : \mathrm{LEnd}(\mathscr{A}_s)_\mathbb{Q} \to \mathrm{PNS}(\mathscr{X}_t)_\mathbb{Q}$ such that for every $\zeta \in \mathrm{LEnd}(\mathscr{A}_s)$, $\zeta$ and $\theta(\zeta)$ have the same cohomological realization in $\mathbf{P}_{\ell, \bar{t}} = \mathbf{L}_{\ell, \bar{s}}$. Indeed, by the Galois descent properties of $\mathrm{NS}(\mathscr{X}_t)_\mathbb{Q}$ and $\mathrm{End}(\mathscr{A}_s)$ we may reduce to considering the case when $\kappa = \mathbb{C}$. Then the statement follows from the fact that both $\mathrm{PNS}(\mathscr{X}_t)$ and $\mathrm{LEnd}(\mathscr{A}_s)$ can be identified with the $(0, 0)$-classes in $\mathbf{L}_{B, s}$. Indeed, although Thm~\ref{thm: integral period} a priori guarantees this only when $t$ lies in the same connected component of $\mathsf{M}_\mathbb{C}$ as $b$, we may still conclude using that $\mathrm{Aut}(\mathbb{C})$ acts transtively on the set of $\mathbb{C}$-connected components of $\mathsf{M}_\mathbb{C}$ and that $(0, 0)$-classes are algebraic. 

Now consider the case when $\kappa$ is a perfect field of characteristic $p$. Let $\widehat{U}_s$ be the formal completion of $\mathscr{S}_\mathcal{K}(\widetilde{G})_{W(\kappa)}$ at $s$. For a special endomorphism $\zeta \in \mathrm{LEnd}(\mathscr{A}_s)$ consider the following functor: 
\begin{equation}
    \label{eqn: local def space of LEnd}
     \mathrm{Def}(\zeta, s) : R \mapsto \{ \widetilde{s} \in \widehat{U}_s(R) \mid \zeta \textit{ deforms to } \mathrm{LEnd}(\mathscr{A}_{\widetilde{s}}) \}
\end{equation}
where $R$ runs through all Artin $W(\kappa)$-algebras. By \cite[\S5.14]{CSpin}, $\mathrm{Def}(\zeta, s)$ is represented by a closed formal subscheme of $\widehat{U}_s$ cut out by a single formal power series $\widehat{f}_\zeta \in \mathcal{O}_{\widehat{U}_s}$. Now suppose that $t \in \mathsf{M}_\kappa$ is a point such that $\widetilde{\rho}(t) = s$. Let $\widehat{\mathsf{M}}_t$ be the formal completion of $\mathsf{M}_{W(\kappa)}$ at $t$. Then $\widetilde{\rho}$ restricts to a morphism $\widehat{\mathsf{M}}_t \to \widehat{U}_s$. Let $\mathrm{Def}(\zeta, t)$ be the functor defined by (\ref{eqn: local def space of LEnd}) with $\widehat{U}_s$ replaced by $\widehat{\mathsf{M}}_t$. Then we have a fiber diagram:
\[\begin{tikzcd}
	\mathrm{Def}(\zeta, t) & \mathrm{Def}(\zeta, s) \\
	\widehat{\mathsf{M}}_t & \widehat{U}_s
	\arrow[from=1-1, to=1-2]
	\arrow[from=1-2, to=2-2]
	\arrow[from=1-1, to=2-1]
	\arrow[from=2-1, to=2-2]
	\arrow["\lrcorner"{anchor=center, pos=0.125}, draw=none, from=1-1, to=2-2]
\end{tikzcd}\]
In particular, $\mathrm{Def}(\zeta, t)$ is a closed formal subscheme of $\widehat{\mathsf{M}}_t$ cut out by the pullback $\widetilde{\rho}^*(\widehat{f}_\zeta)$. 

We prove the following claim: 
\begin{equation}
    \label{eqn: flatness}
    \textit{$\mathrm{Def}(\zeta, t)$ is flat over $\mathbb{Z}_p$.}
\end{equation}

It suffices to show that $\widetilde{\rho}^*(\widehat{f}_\zeta)$ is identically $0$ if and only if it is divisible by $p$. For the proof of the claim we may assume that $\kappa$ is algebraically closed. Suppose that it is indeed divisible by $p$. This implies that $\widehat{\mathsf{M}}_t {\otimes} \mathbb{F}_p \subseteq \mathrm{Def}(\zeta, t)$, i.e., $\zeta \in \mathscr{A}_t$ deforms to the entire disk $\mathbb{D} := \widehat{\mathsf{M}}_t {\otimes} \mathbb{F}_p$. Let $S$ be the irreducible component of $\mathsf{M}_\kappa$ which contains $s$. Note that the geometric point $\bar{\eta}(\mathbb{D}) \to \mathsf{M}_\kappa$ factors through $\bar{\eta}_S$, so we obtain an element $\boldsymbol{\zeta} \in \mathrm{LEnd}(\mathscr{A}_{\bar{\eta}_S})$ which specializes to $\zeta$. By assumption (c), $\boldsymbol{\zeta}$ comes from the specialization of an element of $\mathrm{LEnd}(\mathscr{A}_{\eta})_\mathbb{Q} = \mathrm{PNS}(\mathscr{X}_{\eta})_\mathbb{Q}$. But then $\widehat{f}_\zeta$ has to vanish identically on $\widehat{\mathsf{M}}_t$.

%This implies that there is an element of $\mathrm{LEnd}(\mathscr{A}_{\eta(\mathsf{M}_t)})$ which specializes to $\zeta$.

Now assume that $\kappa$ is an algebraic extension of $\mathbb{F}_p$. We construct a morphism $\theta : \mathrm{LEnd}(\mathscr{A}_s)_\mathbb{Q} \to \mathrm{PNS}(\mathscr{X}_t)_\mathbb{Q}$ which respects the cohomological realizations just as in the second paragraph. Again by Galois descent it suffices to construct the morphism when $\kappa = \bar{\mathbb{F}}_p$. Take any $\zeta \in \mathrm{LEnd}(\mathscr{A}_s)$. By (\ref{eqn: flatness}) there exists a characteristic
$0$ point $\widetilde{t}$ which specializes to $t$ such that $\zeta$ comes from the specialization of an element $\widetilde{\zeta} \in \mathscr{A}_{\widetilde{s}}$, where $\widetilde{s} := \widetilde{\rho}(\widetilde{t})$. By the second paragraph we obtain an element of $\widetilde{\xi} \in \mathrm{PNS}(\mathscr{X}_{\widetilde{t}})_\mathbb{Q}$ with the same cohomological realization as $\widetilde{\zeta}$. Then we specialize $\widetilde{\xi}$ to an element $\xi \in \mathrm{PNS}(\mathscr{X}_t)$, which we define to be $\theta(\zeta)$. It is clear that the definition does not depend on the choice of $\widetilde{t}$. 

Finally assume that $\kappa = k$. By the above paragraph we have a commutative diagram 
\[
\begin{tikzcd}
\mathrm{LEnd}(\mathscr{A}_s) {\otimes} \mathbb{Q}_\ell \arrow{d}{\theta} \arrow{r}{} & \mathbf{L}_{\ell, \bar{s}}^{\mathrm{Gal}_k} \arrow[equal]{d}{} \\
\mathrm{PNS}(\mathscr{X}_t) {\otimes} \mathbb{Q}_\ell \arrow{r}{} & \mathrm{PH}^2_\mathrm{{\acute{e}}t}(\mathscr{X}_t, \mathbb{Q}_\ell(1))
\end{tikzcd}
\]
By the Tate conjecture for special endomorphisms \cite[Thm~6.4]{MPTate}, the top arrow is an isomorphism, and hence so is the bottom arrow. This affirms the Tate conjecture for $\mathscr{X}_t$. 
\end{proof}

# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, theorem 6.7