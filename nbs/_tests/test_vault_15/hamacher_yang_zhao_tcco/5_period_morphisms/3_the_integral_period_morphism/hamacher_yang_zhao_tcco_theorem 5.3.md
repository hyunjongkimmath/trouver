---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]
\begin{theorem}
\label{thm: integral period}
The morphism $\rho$ given by Thm~\ref{thm: period} extends to a $\mathbb{Z}_{(p)}$-morphism $S \to \mathscr{S}_K(G)$. Moreover, 
\begin{enumerate}[label=\upshape{(\alph*)}]
    \item $\alpha_\ell$ extends to an isomorphism of $\mathbb{Z}_\ell$-liss\'e \'etale sheaves $\rho^* \mathbf{L}_\ell \stackrel{\sim}{\to} \mathbf{P}_\ell$ over $S$ for every $\ell \neq p$, where we use the natural $\mathbb{Z}_\ell$-integral structure of $\mathbf{P}_\ell$;
    \item there is an isomorphism of filtered vector bundles $\alpha_{\mathrm{dR}, \mathbb{Q}_p} \colon \rho_{\mathbb{Q}_p}^* \mathbf{L}_\mathrm{dR} \stackrel{\sim}{\to} \mathbf{P}_\mathrm{dR}|_{S {\otimes} \mathbb{Q}_p}$ over $S {\otimes} \mathbb{Q}_p$ such that for any chosen isomorphism $\bar{\mathbb{Q}}_p \,{\cong}\, \mathbb{C}$, $\alpha_\mathrm{dR} |_{S_\mathbb{C}^\circ} = \alpha_{\mathrm{dR}, \mathbb{C}}^\circ$ and $(\alpha_{\mathrm{dR}, \mathbb{Q}_p}) = \mathbb{D}_\mathrm{dR}(\alpha_p)$.
\end{enumerate}
Assume in addition that $p \ge 5$, $\mathbf{P}_\mathrm{dR} := \mathrm{PH}^2_\mathrm{dR}(\mathscr{X}/S)(1)$ is locally free, and for every $S$-scheme $T$, the natural morphism $\mathrm{H}^2_\mathrm{dR}(\mathscr{X}/S) {\otimes} \mathcal{O}_T \to \mathrm{H}^2_\mathrm{dR}(\mathscr{X}_T/T)$ is an isomorphism. Moreover, assume that for every closed point $s \in \mathsf{M}$, $\mathrm{H}^2_\mathrm{cris}(\mathscr{X}_s/W(k(s)))$ and $\mathrm{H}^3_\mathrm{cris}(\mathscr{X}_s/W(k(s)))$ are torsion free. Then 
\begin{itemize}
    \item[\upshape{(c)}] $\alpha_{\mathrm{dR}, \mathbb{Q}_p}$ extends to an isomorphism $\alpha_\mathrm{dR} : \rho^* \mathbf{L}_\mathrm{dR} \stackrel{\sim}{\to} \mathbf{P}_\mathrm{dR}$ over $S$;
    \item[\upshape{(d)}] there is an isomorphism $\alpha_\mathrm{cris} \colon \rho_{\mathbb{F}_p}^* \mathbf{L}_\mathrm{cris}(-1) \stackrel{\sim}{\to} \mathbf{P}_\mathrm{cris}(-1)$ of F-crystals whose evaluation on $S_{\mathbb{Z}_p}$ agrees with $\alpha_\mathrm{dR}$ via the crystalline-de Rham comparison isomorphism. 
\end{itemize}
\end{theorem}
\begin{proof} That $\rho$ can be extended over $\mathbb{Z}_{(p)}$ follows from the extension property of canonical integral models. (a) follows simply from the fact that the natural map $\pi_1^\mathrm{{\acute{e}}t}(\eta, b) \to \pi_1^\mathrm{{\acute{e}}t}(S, b)$ is surjective (\cite[0BQJ]{stacks-project}). (b) follows from Thm~\ref{thm: comparison is dR}. Technically, we do not know if $\mathbf{L}_\mathrm{dR}$ comes from an object of $\mathsf{Mot}(\mathrm{Sh}_K(G))$. However, we can check this by passing to $S \times_\rho \mathrm{Sh}_\mathcal{K}(\widetilde{G})$ and then use Prop.~\ref{prop: come from actural motive}. 

For (c), we only need to show that $\mathbb{D}_\mathrm{dR}(\alpha_p) \colon \rho^*_{\mathbb{Q}_p} \mathbf{L}_\mathrm{dR} {\otimes} \mathbb{Q}_p \stackrel{\sim}{\to} \mathbf{P}_\mathrm{dR} {\otimes} \mathbb{Q}_p$ respects the integral structure. By \cite[Lem.~6.15]{Maulik}, it suffices to show that for every closed point $s \in S$ and $W\coloneqq W(k(s))$-lifting $\widetilde{s}$, $\mathbb{D}_\mathrm{dR}(\alpha_p)$ restricts to an isomorphism $\mathbf{L}_{\mathrm{dR}, \rho(\widetilde{s})} \stackrel{\sim}{\to} \mathbf{P}_{\mathrm{dR}, \widetilde{s}}$. Let $K_0 \coloneqq W[1/p]$ and choose an algebraic closure $\bar{K}_0$. Let $\bar{s}$ be the $\bar{K}_0$-point over $\widetilde{s}$. By \cite[Thm~1.3]{BMS}, the $W$-module $\mathbf{P}_{\mathrm{dR}, \widetilde{s}}$ is recovered from $\mathbf{P}_{p, \bar{s}}=\mathrm{PH}^2_\mathrm{{\acute{e}}t}(\mathscr{X}_{\bar{s}}, \mathbb{Z}_p)$ as $\mathfrak{M}(\mathbf{P}_{p, \bar{s}}) {\otimes}_{\mathfrak{S}} W$, which is naturally a $W$-submodule of $\mathbb{D}_\mathrm{dR}(\mathbf{P}_{p, \bar{s}} {\otimes} \mathbb{Q}_p)$. Here $\mathfrak{M}(-)$ denote the Breuil-Kisin functor, which takes a crystalline $\mathbb{Z}_p$-representation of $\mathrm{Gal}_{K_0}$ to a $\mathfrak{S} \coloneqq W[\![u]\!]$-module with extra structures. The $W$-module $\mathbf{L}_{\mathrm{dR}, \rho(\widetilde{s})}$ is recovered from $\mathbf{L}_{p, \rho(\bar{s})}$ is the same way. As $\alpha_{p, \bar{s}}$ maps the $\mathbb{Z}_p$-lattice $\mathbf{P}_{p, \bar{s}}$ isomorphically onto $\mathbf{L}_{p, \bar{s}}$, $\mathbb{D}_\mathrm{dR}(\alpha_{p, \bar{s}})$ maps the $W$-module $\mathbf{L}_{\mathrm{dR}, \rho(\widetilde{s})}$ isomorphically onto $\mathbf{P}_{\mathrm{dR}, \widetilde{s}}$. 

(d) is a direct consequence of (c). The crystalline-de Rham comparison isomorphism always gives us an isomorphism of crystals $\alpha_\mathrm{cris}$. We only need to check that it is F-equivariant. We may transport the Frobenius action to $\mathbf{L}_\mathrm{dR}$ and $\mathbf{P}_\mathrm{dR}$ and check that $\alpha_\mathrm{dR}$ is F-equivariant. It suffices to show this over the generic fiber, i.e., $\alpha_\mathrm{dR} {\otimes} \mathbb{Q}_p$ is F-equivariant. By the preceeding paragraph, this is true for a Zariski dense set of points on $S_{\mathbb{Q}_p}$. Then we are done because F-equivariance is clearly a Zariski closed condition. 
\end{proof}

# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, theorem 5.3