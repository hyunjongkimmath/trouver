---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]
\begin{remark}
\label{rmk: no dR realization}
The $\ell$-adic and Betti realization functors $\omega_\ell$ and $\omega_B$ are naturally defined for $\mathsf{Mot}_\eta(S)$. Moreover, $\omega_B$ on $\mathsf{Mot}_\eta(S)$ is compatible with $\omega^\eta_\mathrm{Hdg}$. However, there does not seem to be a de Rham realization functor $\omega_\mathrm{dR}$ from $\mathsf{Mot}_\eta(S)$ to the category of filtered vector bundles with integrable connection over $S$ in literature when $K$ is an arbitrary field of characteristic $0$. Here we make an ad hoc definition which is good enough for our applications when $K = \mathbb{C}$ or has finite transcendence degree over $\mathbb{Q}$: Let $M \in \mathsf{Mot}_\eta(S)$. If $K = \mathbb{C}$, we write $\omega_\mathrm{dR}(M)$ for the underlying filtered vector bundle with integrable connection of $\omega^\eta_\mathrm{Hdg}(M)$. Now suppose that $K$ is of finite transcendence degree over $\mathbb{Q}$. Recall that any two embeddings $K \hookrightarrow \mathbb{C}$ differ by an element of $\mathrm{Aut}(\mathbb{C})$. We choose an embedding $\iota : K \hookrightarrow \mathbb{C}$ and take $U \subseteq S$ to be an open dense subvariety such that $M$ is defined by an object $M_U \in \mathsf{Mot}(U)$. Denote $-{\otimes}_\iota \mathbb{C}$ with a supscript ``$\mathbb{C}$''. Let $\mathcal{V}$ be the filtered vector bundle with integrable connection $\omega_\mathrm{dR}(M_U)$ over $U$. The $K$-model $U$ of $U_\mathbb{C}$ defines a Galois descent datum $\{ g_\sigma : U_\mathbb{C}^\sigma \stackrel{\sim}{\to} U_\mathbb{C} \}_{\sigma \in \mathrm{Aut}(\mathbb{C}/K)}$, and the $K$-model $\mathcal{V}$ of $\mathcal{V}_\mathbb{C}$ defines a Galois descent datum $\{ \psi_\sigma : g_\sigma^*(\mathcal{V}_\mathbb{C}|_{U_\mathbb{C}}) \stackrel{\sim}{\to} \mathcal{V}_{\mathbb{C}}|_{U^\sigma_\mathbb{C}} \}_{\sigma \in \mathrm{Aut}(\mathbb{C}/K)}$. However, $\psi_\sigma$ comes from an isomorphism of polarizable $\mathbb{Q}$-VHS, so it can be extended uniquely to a Galois decent datum for the vector bundle $\omega_\mathrm{dR}(M_\mathbb{C})$ over $S_\mathbb{C}$. We define $\omega_\mathrm{dR}(M)$ to be $\omega_\mathrm{dR}(M_\mathbb{C})$ together with the descent data $\{ \psi_\sigma \}_{\sigma \in \mathrm{Aut}(\mathbb{C}/K)}$. If in addition the descent data $\{ \psi_\sigma \}$ is known to be effective,\footnote{We expect that this is always true, but we have not checked the details.} then we identify $\omega_\mathrm{dR}(M)$ with the descent. 
\end{remark}

# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, remark 2.3