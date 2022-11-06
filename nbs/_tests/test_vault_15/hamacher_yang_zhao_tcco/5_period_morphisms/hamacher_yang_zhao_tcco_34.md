---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]
















Let $\mathscr{X} / S$ be a polarized family of $h^{2, 0} = 1$ varieties over a smooth connected $\mathbb{Q}$-variety $S$ which satisfies condition $(\heartsuit)$. Let $\eta$ be the generic point of $S$ and choose an embedding $k(\bar{\eta}) \hookrightarrow \mathbb{C}$. %Let the resulting $\mathbb{C}$-point on $S$ be $b$. Let $S^\circ_\mathbb{C}$ be the connected component of $S_\mathbb{C}$ which contains the base point $b$.
We denote by $b \in S(\mathbb{C})$ the resulting point and denote by $S_\mathbb{C}^\circ$ the connected component of $S_\mathbb{C}$ containing $b$. We call it the distinguished component. Let $\mathrm{T}(\mathscr{X}_b, \mathbb{Q})$ be the transcendental part of $\mathrm{H}^2(\mathscr{X}_b, \mathbb{Q}(1))$ and define $\mathrm{T}(\mathscr{X}_b, \mathbb{Q}_\ell) := \mathrm{T}(\mathscr{X}_b, \mathbb{Q}) {\otimes} \mathbb{Q}_\ell$ for every prime $\ell$. Up to replacing $S$ by a connected \'etale cover, we assume that $\mathrm{NS}(\mathscr{X}_\eta)_\mathbb{Q} = \mathrm{NS}(\mathscr{X}_{\bar{\eta}})_\mathbb{Q} = \mathrm{NS}(\mathscr{X}_b)_\mathbb{Q}$ and the monodromy group $\mathrm{Mon}(\mathrm{H}^2_\mathrm{{\acute{e}}t}(\mathscr{X}/S, \mathbb{Q}_2), b)$ is a connected subgroup of $\mathrm{O}(\mathrm{T}(\mathscr{X}_b, \mathbb{Q}_2))$. Note that $\mathrm{O}(\mathrm{T}(\mathscr{X}_b, \mathbb{Q}_2))$ can be naturally viewed as the subgroup of $\mathrm{O}(\mathrm{H}^2_\mathrm{{\acute{e}}t}(\mathscr{X}_b, \mathbb{Q}_2))$ which stabilizes $\mathrm{NS}(\mathscr{X}_b)$. By \cite[Prop.~6.14]{Larsen-Pink}, $\mathrm{Mon}(\mathrm{H}^2_\mathrm{{\acute{e}}t}(\mathscr{X}/S, \mathbb{Q}_2), b)$ is connected for every other $\ell$. Recall that by Lem.~\ref{lem: extend LB on generic} representatives of elements of $\mathrm{NS}(\mathscr{X}_\eta)$ extend uniquely to relative line bundles of $\mathscr{X}/S$. 


Let $E$ be the endomorphism algebra $\mathrm{End}_\mathrm{Hdg}(\mathrm{T}(\mathscr{X}_b, \mathbb{Q}))$. Recall that $E$ come from motivated cycles (Thm~\ref{thm: Moonen}). These cycles are defined over $k(\bar{\eta})$ (\cite[Scolie 2.5]{AndreMot}); moreover, as their $\ell$-adic realizations are $\pi_1^\mathrm{{\acute{e}}t}(S, b)$-invariant, they are defined over $S$. We hence obtain an $E$-action on the entire family $\mathfrak{p}^2(\mathscr{X}/S)$. Note that for every prime $\ell$, the connectedness of $\mathrm{Mon}(\mathrm{H}^2_\mathrm{{\acute{e}}t}(\mathscr{X}/S, \mathbb{Q}_2), b)$ implies that it is a subgroup of $\mathrm{SO}_{E/\mathbb{Q}}(\mathrm{T}(\mathscr{X}_b, \mathbb{Q})))_{\mathbb{Q}_\ell}$, which is the identity component of $C_E(\mathrm{O}(\mathrm{T}(\mathscr{X}_b, \mathbb{Q})))_{\mathbb{Q}_\ell}$.

%\todo{Write down relation between $T(\mathscr{X}_b,\mathbb{Q})$ and $PH^2(\mathscr{X}_b,\mathbb{Q}_\ell)$}
%the identity component of the centralizer $C_E(\mathrm{O}(T(\mathscr{X}_b, \mathbb{Q}))) {\otimes} \mathbb{Q}_\ell$. In particular, when $E$ is totally real, it is a subgroup of $\mathrm{SO}_{E/\mathbb{Q}}(\mathrm{T}(\mathscr{X}_b, \mathbb{Q})) {\otimes} \mathbb{Q}_\ell$. 

Let $V$ be a quadratic form over $\mathbb{Q}$ which is isomorphic to $\mathrm{PH}^2(\mathscr{X}_b, \mathbb{Q})$ and choose an isomorphism $\psi\colon V \stackrel{\sim}{\to} \mathrm{PH}^2(\mathscr{X}_b, \mathbb{Q})$. Set $n \coloneqq \dim V$. Let $G \coloneqq \mathrm{SO}(V)$ and consider the Shimura variety $\mathrm{Sh}(G)$ defined by $V$. All the Shimura varieties used here are the orthogonal ones recalled in \S\ref{sec: orthogonal SV}, so we omit the Hermitian symmetric domains from the notation. Recall that the reflex field of $\mathrm{Sh}(G)$ is $\mathbb{Q}$. The standard representation of $G$ on $V$ endows $\mathrm{Sh}(G)$ with a family of abelian motives $\mathfrak{V} \in \mathsf{Mot}^{\mathsf{Ab}}_{\eta, \mathrm{AH}}(\mathrm{Sh}(G))$. Set $\mathbf{V}_B \coloneqq \omega_B(\mathfrak{V}|_{\mathrm{Sh}(G)_\mathbb{C}})$, $\mathbf{V}_\ell \coloneqq \omega_\ell(\mathfrak{V})$ and $\mathbf{V}_\mathrm{dR} := \omega_\mathrm{dR}(\mathfrak{V})$. Note that $\mathbf{V}_\mathrm{dR}$ is the automorphic vector bundle defined by the standard representation, so the descent data of $\omega_\mathrm{dR}(\mathfrak{V})$ is effective (Rmk~\ref{rmk: no dR realization}). Similarly, let us simply write $\mathbf{P}_B, \mathbf{P}_\ell, \mathbf{P}_\mathrm{dR}$ for $\mathrm{PH}^2(\mathscr{X}|_{S_\mathbb{C}}, \mathbb{Q}(1))$, $\mathrm{PH}^2_\mathrm{{\acute{e}}t}(\mathscr{X}/S, \mathbb{Q}_\ell(1))$ and $\mathrm{PH}^2_\mathrm{dR}(\mathscr{X}/S)(1)$ respectively. The key fact we want to prove is the following.

%We first prove the following theorem: 


# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, 34