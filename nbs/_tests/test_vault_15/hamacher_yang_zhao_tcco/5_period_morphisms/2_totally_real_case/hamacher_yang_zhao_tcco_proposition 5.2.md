---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]
\begin{proposition}
If $E$ is totally real, then for the morphism $\rho_\mathrm{Nm} \colon S \to \mathrm{Sh}_\mathsf{K}(H^\bullet)$ constructed above there is an isomorphism of VHS $$(\alpha_B^\circ, \alpha_{\mathrm{dR}, \mathbb{C}}^\circ) \colon (\rho_\mathrm{Nm}|_{S_\mathbb{C}^\circ})^* (\boldsymbol{\mathcal{V}}_B, \boldsymbol{\mathcal{V}}_{\mathrm{dR}, \mathbb{C}}) \stackrel{\sim}{\to} (\mathbf{P}_B, \mathbf{P}_{\mathrm{dR}, \mathbb{C}})_{S^\circ_\mathbb{C}}$$
and an isomorphism of $\mathbb{Q}_\ell$-liss\'e \'etale sheaves $\alpha_\ell \colon \rho_\mathrm{Nm}^* \boldsymbol{\mathcal{V}}_\ell \stackrel{\sim}{\to} \mathbf{P}_\ell$ for each $\ell$ such that $\alpha_B^\circ {\otimes} \mathbb{Q}_\ell = \alpha_\ell|_{S_\mathbb{C}^\circ}$ under the Artin comparison isomorphism.   
\end{proposition}
\begin{proof}
Take $\rho$ to be the morphism $\rho_\mathrm{Nm}$ constructed above. The existence of $(\alpha_B^\circ, \alpha^\circ_{\mathrm{dR}, \mathbb{C}})$ follows from the fact that $\rho|_{S_\mathbb{C}^\circ}$ is given by $\rho_\mathrm{std}^\circ$. Note that in particular $(\alpha_B^\circ, \alpha^\circ_{\mathrm{dR}, \mathbb{C}})$ is an extension of an isomorphism of Hodge structures $(\boldsymbol{\mathcal{V}}_{B, \rho(b)}, \boldsymbol{\mathcal{V}}_{\mathrm{dR}, \rho(b)}) \stackrel{\sim}{\to} (\mathrm{PH}^2(\mathscr{X}_b, \mathbb{Q}), \mathrm{PH}^2_\mathrm{dR}(\mathscr{X}_b/\mathbb{C}))$. We only need to show that $\alpha^\circ_{B, b} {\otimes} \mathbb{Q}_\ell$ is $\pi_1^\mathrm{{\acute{e}}t}(S, b)$-equivariant, so that it extends to the $\alpha_\ell$'s as desired.

We first treat the case when $\dim_E \mathcal{V}$ is odd. By construction of $\rho_\mathrm{Nm}$, we have that $\mathcal{N}(\alpha^\circ_{B, b} {\otimes} \mathbb{Q}_\ell)$ globalizes to an isomorphism $\rho_\mathrm{Nm}^* \boldsymbol{\mathcal{N}}_\ell \stackrel{\sim}{\to} \mathcal{N}(\mathbf{P}_\ell)$, i.e., $\mathcal{N}(\alpha^\circ_{B, b} {\otimes} \mathbb{Q}_\ell)$ is $\pi_1^\mathrm{{\acute{e}}t}(S, b)$-equivariant. As the image of the monodromy representation $\pi_1^\mathrm{{\acute{e}}t}(S, b) \to \mathrm{GL}(\mathbf{P}_{\ell, b})$ lies in $H(\mathbb{Q}_\ell)$ via $\psi$, and $r_\mathrm{Nm}$ is a faithful representation of $H$, the $\pi_1^\mathrm{{\acute{e}}t}(S, b)$-equivariance of $\mathcal{N}(\alpha^\circ_{B, b} {\otimes} \mathbb{Q}_\ell)$ implies that of $\alpha^\circ_{B, b} {\otimes} \mathbb{Q}_\ell$. 

Now we treat the case when $\dim_E \mathcal{V}$ is even. Then we apply the argument in the above paragraph to the family $\mathscr{Y}/S$ to conclude that there is an isomorphism $$(\widetilde{\alpha}_B^\circ, \widetilde{\alpha}_{\mathrm{dR}, \mathbb{C}}^\circ) \colon (\widetilde{\rho}_\mathrm{Nm}|_{S^\circ_\mathbb{C}})^*(\widetilde{\boldsymbol{\mathcal{V}}}_B, \widetilde{\boldsymbol{\mathcal{V}}}_{\mathrm{dR}, \mathbb{C}}) \stackrel{\sim}{\to} (\widetilde{\mathbf{P}}_B, \widetilde{\mathbf{P}}_{\mathrm{dR}, \mathbb{C}})|_{S^\circ_\mathbb{C}} $$
such that $\widetilde{\alpha}_{B, b} {\otimes} \mathbb{Q}_\ell$ is $\pi_1^\mathrm{{\acute{e}}t}(S, b)$-equivariant. But this implies the $\pi_1^\mathrm{{\acute{e}}t}(S, b)$-equivariance of $\alpha_{B, b} {\otimes} \mathbb{Q}_\ell$, because the $\ell$-adic realizations of the exceptional divisors are certainly $\pi_1^\mathrm{{\acute{e}}t}(S, b)$-invariant. 
\end{proof}

# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, proposition 5.2