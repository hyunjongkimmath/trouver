---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]

\label{sec: totally real case}
Let $\mathcal{V}(E)$ be a quadratic form over $E$ which is isomorphic to $\mathrm{PH}^2(\mathscr{X}_b, \mathbb{Q})$ equipped with the $E$-action. Fix an $E$-isometry $\psi \colon \mathcal{V} \stackrel{\sim}{\to} \mathrm{PH}^2(\mathscr{X}_b, \mathbb{Q})$ such that $V = \mathcal{V}_{(\IQ)}$. Write $H$ for $\mathrm{SO}_{E/\mathbb{Q}}(\mathcal{V})$. Let $\mathsf{K} \subseteq \mathrm{SO}_{E/\mathbb{Q}}(\mathcal{V})(\mathbb{A}_f)$ be a neat compact open subgroup. Assume that $\mathsf{K} \subseteq K$ and $\mathrm{Mon}(\mathrm{H}^2_\mathrm{{\acute{e}}t}(\mathscr{X}/S, \mathbb{Q}_\ell), b) \subseteq \psi^{-1}(\mathsf{K})$, which can always be achieved by replacing $S$ by a further connected \'etale cover. Then the isomorphism $\psi$ globalizes to a $\mathsf{K}$-level structure $\widetilde{\psi}$ on $\mathrm{PH}^2_\mathrm{{\acute{e}}t}(\mathscr{X}/S, \mathbb{A}_f)$. 

\paragraph{The odd case} Assume for now that $\dim_E \mathcal{V}$ is odd. When $[E : \mathbb{Q}] \neq 4$, we define $\mathcal{N} = \mathcal{N}(V)$ to be $\mathrm{Nm}(\mathcal{V}) {\otimes} \det(V)$ and when $[E : \mathbb{Q}] = 4$, we define $\mathcal{N}$ to be $\mathrm{Nm}(\mathcal{V})$. We consider two faithful representations of $H$. One is the standard representation $r_\mathrm{std} \colon H \hookrightarrow \mathrm{O}(V)$ and the other is the composition 
$$ r_\mathrm{Nm} \colon H \hookrightarrow \mathrm{GL}_{E/\mathbb{Q}}(\mathcal{V}) \to \mathrm{GL}(\mathcal{N}). $$
Let $\lambda \in V^{\otimes}$ be a tensor such that $H$ is the stabilizer of the $\mathbb{Q}$-pairing, $E$-action and $\lambda$, and let $\{ s_\alpha \} \subseteq \mathrm{Nm}(\mathcal{V})^{\otimes}$ be tensors such that $\mathrm{SO}_{E/\mathbb{Q}}(\mathcal{V})$ is the stabilizer of $s_\alpha$'s via $r_\mathrm{Nm}$. 

Let $\boldsymbol{\mathcal{V}}_*$ denote the automorphic sheaves on $\mathrm{Sh}_\mathsf{K}(H)$ given by $r_\mathrm{std}$ ($*= B, \mathrm{dR}, \ell$ on appropriate fibers). Then $\boldsymbol{\mathcal{N}}_* \coloneqq \mathcal{N}(\boldsymbol{\mathcal{V}}_*)$ are the automorphic sheaves given by $r_\mathrm{Nm}$. Moreover, the tautological $\mathsf{K}$-level structure $\eta_\mathrm{Nm}$ on $\boldsymbol{\mathcal{N}}_{\mathbb{A}_f}$ is also just obtained by applying $\mathcal{N}(-)$ to the $\mathsf{K}$-level structure $\eta_\mathrm{std}$ on $\boldsymbol{\mathcal{V}}_{\mathbb{A}_f}$. Let $\widetilde{\lambda}_*$ and the $\widetilde{s}_{\alpha, *}$'s be the global sections of $\boldsymbol{\mathcal{V}}_*^{\otimes}$ and $\mathcal{N}(\boldsymbol{\mathcal{V}}_*)^{\otimes}$ given by $\lambda$ and $s_\alpha$'s respectively.

Define $\lambda_b \coloneqq \psi(\lambda)$. As $\mathrm{Mon}^2(\mathscr{X}|_{S_\mathbb{C}^\circ}, \mathbb{Q})$ is a subgroup of $\mathrm{SO}_{E/\mathbb{Q}}(\mathrm{PH}^2(\mathscr{X}_b, \mathbb{Q}))$, $\lambda_b$ spreads to a global section $\boldsymbol{\lambda}$ of $(\mathbf{P}_{B}|_{S_\mathbb{C}^\circ})^{\otimes}$. The moduli interpretation of $\mathrm{Sh}_\mathsf{K}(H)$ given by $r_\mathrm{std}$ then gives us a period morphism 
$$ \rho^\circ_\mathrm{std} \colon S_\mathbb{C}^\circ \to \mathrm{Sh}_\mathsf{K}(H)_\mathbb{C}, $$
characterized by the property that there is a (necessarily unique) isomorphism $\rho^*(\mathbf{V}_B, \mathbf{V}_\mathrm{dR}) \stackrel{\sim}{\to} (\mathbf{P}_B, \mathbf{P}_\mathrm{dR})|_{S_\mathbb{C}^\circ}$ which preserves the $E$-actions, $\mathbb{Q}$-pairing, sends $\widetilde{\lambda}$ to $\boldsymbol{\lambda}$, and respects the $\mathsf{K}$-level structures $\widetilde{\psi}$ and $\eta_\mathrm{std}$. 

Similarly, consider $s_{\alpha, b} \coloneqq \psi(s_\alpha)$. Note that as $\mathcal{N}(\mathfrak{p}^2(\mathscr{X}/S))$ is an object of $\mathsf{Mot}^\mathsf{Ab}(S)$ (Thm~\ref{thm: Moonen}), $s_{\alpha, b}$ is given by a absolute Hodge cycle. Moreover, as its $\ell$-adic realizations are $\pi_1^\mathrm{{\acute{e}}t}(S, b)$-invariant, $s_{\alpha, b}$ extends to a relative cycle $\mathbf{s}_\alpha$ on $\mathcal{N}(\mathfrak{p}^2(\mathscr{X}/S))^{\otimes}$. The moduli interpretation of $\mathrm{Sh}_\mathsf{K}(H)$ given by $r_\mathrm{Nm}$ then gives another period morphism 
$$ \rho_\mathrm{Nm} \colon S \to \mathrm{Sh}_\mathsf{K}(H^\bullet) $$
characterized by the property that there is (necessarily unique) isomorphism $\rho^*(\mathcal{N}(\mathfrak{V})) \stackrel{\sim}{\to} \mathcal{N}(\mathfrak{p}^2(\mathscr{X}/S))$ which sends $\widetilde{s}_\alpha$ to $\mathfrak{s}_\alpha$ and $\eta_\mathrm{Nm}$ to $\mathcal{N}(\widetilde{\psi})$. It is easy to check that by construction $\rho_\mathrm{Nm}|_{S_\mathbb{C}^\circ} = \rho^\circ_\mathrm{std}$. If we know that $\mathfrak{p}^2(\mathscr{X}/S)$ is a family of abelian motives, then in fact $\rho_\mathrm{std}^\circ$ can also be extended to $\rho_\mathrm{std}: S \to \mathrm{Sh}_\mathsf{K}(H^\bullet)$ and $\rho_\mathrm{Nm} = \rho_\mathrm{std}$ on the entire $S$. 

\paragraph{The even case} When $\dim_E \mathcal{V}$ is even, one can still construct $\rho^\circ_\mathrm{std}$ verbatim. However, $r_\mathrm{Nm}$ is no longer faithful. We overcome this difficulty by the following trick: Let $d \coloneqq [E : \mathbb{Q}]$. Define $\mathscr{Y}_0 \coloneqq \mathscr{X}$ and iteratively define $\mathscr{Y}_{i + 1}$ to be the relative Hilbert scheme of $2$ points on $\mathscr{Y}_i$. Then the morphism $\mathscr{Y}_{i+1} \to \mathscr{Y}_i$ is smooth since it satisfies the formal lifting criterion by \cite[top of p.~34]{Kollar}; note that we can apply Kollar's construction since any length-$2$ subscheme is lci and can be embedded into an affine open subscheme. %it is flat (see e.g \cite[Thm.~I.2.15.4]{Kollar}) with smooth fibres (\cite[Thm.~2.9]{Fogarty}). 
Set $\mathscr{Y}$ to be $\mathscr{Y}_d$. Then we have an isomorphism of motives $\mathfrak{h}^2(\mathscr{X}/S) \oplus \underline{\mathbb{Q}(-1)}_S^{\oplus d} \,{\cong}\, \mathfrak{h}^2(\mathscr{Y}/S)$. We denote by $\mathfrak{p}^2(\mathscr{Y}/S)$ the image of $\mathfrak{p}^2(\mathscr{X}/S) \oplus \underline{\mathbb{Q}(-1)}_S^{\oplus}$. By choosing an isomorphism $\mathbb{Q}^{\oplus d} \,{\cong}\, E$, we equip $\underline{\mathbb{Q}(-1)}_S^{\oplus d}$ with an $E$-action and the trace pairing. This way we have equipped $\mathfrak{p}^2(\mathscr{Y}/S)$ with an $E$-action and an $E$-symmetric pairing 
$$ \mathfrak{p}^2(\mathscr{Y}/S)(1) \times \mathfrak{p}^2(\mathscr{Y}/S)(1) \to \underline{\mathbb{Q}}_S. $$
Moreover, the $E$-action and the pairing are both given by motivated cycles. 

Set $\widetilde{\mathcal{V}} \coloneqq \mathcal{V} \oplus E$, $\widetilde{V} = V \oplus \mathbb{Q}^{\oplus d}$, and $\widetilde{H} \coloneqq \mathrm{SO}_{E/\mathbb{Q}}(\widetilde{\mathcal{V}})$. Note that $\dim_E \widetilde{\mathcal{V}}$ now becomes odd. Suppose now we are given a neat compact open subgroup $\widetilde{\mathsf{K}} \subseteq \widetilde{H}(\mathbb{A}_f)$ such that $\mathsf{K} \subseteq \widetilde{\mathsf{K}} \cap H(\mathbb{A}_f)$, and the inclusion $V \hookrightarrow \widetilde{V}$ induces an embedding $\iota \colon \mathrm{Sh}_K(H) \hookrightarrow \mathrm{Sh}_{\widetilde{K}}(\widetilde{H})$. By applying the constructions in the odd case to the family $\mathfrak{p}^2(\mathscr{Y}/S)$, we obtain morphisms $\widetilde{\rho}_\mathrm{std}$ and $\widetilde{\rho}_\mathrm{Nm}$ which fit into a commutative diagram 

\[\begin{tikzcd}
	S_\mathbb{C}^\circ & \mathrm{Sh}_\mathsf{K}(H)_\mathbb{C} & \mathrm{Sh}_{\widetilde{K}}(\widetilde{H})_\mathbb{C} \\
	S & \mathrm{Sh}_\mathsf{K}(H^\bullet) & \mathrm{Sh}_{\widetilde{K}}(\widetilde{H}^\bullet)
	\arrow["{\rho^\circ_\mathrm{std}}", from=1-1, to=1-2]
	\arrow["\iota_\mathbb{C}", from=1-2, to=1-3]
	\arrow[from=1-1, to=2-1]
	\arrow["\rho_\mathrm{Nm}", dashed, from=2-1, to=2-2]
	\arrow["\iota^\bullet",from=2-2, to=2-3]
	\arrow[from=1-3, to=2-3]
	\arrow[from=1-2, to=2-2]
	\arrow["{\widetilde{\rho}_\mathrm{std}}", curve={height=-30pt}, from=1-1, to=1-3]
	\arrow["{\widetilde{\rho}_\mathrm{Nm}}", curve={height=30pt}, from=2-1, to=2-3]
	\arrow["\lrcorner"{anchor=center, pos=0.125}, draw=none, from=1-2, to=2-3]
	\arrow["\lrcorner"{anchor=center, pos=0.125}, draw=none, from=1-1, to=2-2]
\end{tikzcd}\]
Since $\widetilde{\rho}_\mathrm{Nm}$ is defined over $\mathbb{Q}$ and $\mathrm{Aut}(\mathbb{C})$ acts transitively on the set of connected components of $S_\mathbb{C}$, $\widetilde{\rho}_\mathrm{Nm}$ factors through $\iota^\bullet$, so that we can fill in the dashed arrow and denote it suggestively as $\rho_\mathrm{Nm}$. 

We denote the automorphic sheaves associated to $\widetilde{\mathcal{V}}$ by $\widetilde{\boldsymbol{\mathcal{V}}}_*$ and the cohomology sheaves associated to $\mathfrak{p}^2(\mathscr{Y}/S)(1)$ by $\widetilde{\mathbf{P}}_*$. 



# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, 37