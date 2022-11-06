---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]
\begin{proposition}
 The isomorphism class of the pair $(G^{\sigma, s}, \Omega^{\sigma, s})$ does not depend on $s$ and $\xi$, and depends on $\sigma$ only up to $\sigma|_E$.  Moreover, $(G^{\sigma, s}, \Omega^{\sigma, s})$ defines a Shimura datum such that $\mathrm{Sh}_K(G^{\sigma, s}, \Omega^{\sigma, s})$ represents the functor $\mathcal{M}_{\tau, K}$ for $\tau = \sigma^{-1}(\tau_0)$. 
 \end{proposition}
\begin{proof}
 We first explain that the isomorphism class of the pair $(G^{\sigma, s}, \Omega^{\sigma, s})$ does not depend on the choice of $s$ and depends only on $\sigma$ up to the action of $\mathrm{Aut}(\mathbb{C}/E)$. Let $s'$ be another point on $\mathrm{Sh}_K(G, \Omega)_\mathbb{C}$. Up to changing the level structure of the defining tuple of $s'$, we may assume that $s$ and $s'$ lie on the same connected component. By choosing a topological path from $\sigma(s)$ to $\sigma(s')$ on $\mathrm{Sh}_K(G, \Omega)_\mathbb{C}^\sigma$, we obtain by parallel transport an isomorphism $\omega_B((\mathbf{M}^\sigma_s,(\mathbf{t}^\sigma_{\alpha,s}))) \cong \omega_B((\mathbf{M}^\sigma_{s'},(\mathbf{t}^\sigma_{\alpha,s'})))$, through which $h_{s'}^\sigma$ defines the same $G^{\sigma, s}(\mathbb{R})$-conjugacy class as $h_s^\sigma$ by \cite[(1.1.12)]{DelVdShimura}. This shows the independence of $s$. Next, if $\sigma' = \sigma \circ \varsigma$ for $\varsigma \in \mathrm{Aut}(\mathbb{C}/E)$, we have by Prop.~\ref{prop: moduli over E}
  $$
   (\mathbf{M}^\mathrm{univ}_{s},(\mathbf{t}_{\alpha,s}))^{\sigma'} = ((\mathbf{M}_{s},(\mathbf{t}_{\alpha,s}))^{\varsigma})^{\sigma} \,{\cong}\, (\mathbf{M}_{\varsigma(s)},(\mathbf{t}_{\alpha,\varsigma(s)}))^\sigma;
  $$
  thus the isomorphism class of $(G^{\sigma, s},\Omega^{\sigma, s})$ depends only on the restriction $\sigma|_E$ rather than $\sigma$.
  
  When $s$ is a special point, Langlands defined a Shimura datum in \cite[\S6]{Langlands:EinMärchen}, which he denoted by $(G^{\sigma, \mu}, \Omega^{\sigma, \mu})$, where $\mu$ is the cocharacter defined by $h$. The pair $(G^{\sigma, \mu}, \Omega^{\sigma, \mu})$ is isomorphic to our $(G^{\sigma, s}, \Omega^{\sigma, s})$ (\cite[Rmk~4.1(a)]{Milne:CanonicalModels}). This implies that $(G^{\sigma, s},\Omega^{\sigma, s})$ is a Shimura datum and is moreover independent of the choice of the representation $\xi$ as Langlands' construction does not involve choosing $\xi$. If $(G, \Omega)$ is of Hodge type, then clearly so is $(G^{\sigma, s},\Omega^{\sigma, s})$; moreover, as $G^{\sigma, s}$ is an inner form of $G$, they have the same center. Hence our standing assumptions on $(G, \Omega)$ also apply to $(G^{\sigma, s}, \Omega^{\sigma, s})$. 
  % (see e.g., \cite[Rmk~4.3]{Orr})
  Finally, let $\xi^{\sigma, s} : G^{\sigma, s} \to \mathrm{GL}(\omega_B(\mathbf{M}^\sigma_s))$ be the tautological representation through which we view $G^{\sigma, s}$ as the stabilizer of $(\mathbf{t}_{\alpha, s}^\sigma)$'s. Let $\mathcal{M}_K^{\sigma, s}$ be the moduli problem which is represented by $\mathrm{Sh}_K(G^{\sigma, s}, \Omega^{\sigma, s})$, as given by Prop.~\ref{prop: moduli over E}. One easily checks using the first paragraph that the moduli problem $\mathcal{M}_K^{\sigma, s}$ is isomorphic to $\mathcal{M}_{\tau, K}$ for $\tau := \sigma^{-1}(\tau_0)$. 
 \end{proof}

# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, proposition 3.6