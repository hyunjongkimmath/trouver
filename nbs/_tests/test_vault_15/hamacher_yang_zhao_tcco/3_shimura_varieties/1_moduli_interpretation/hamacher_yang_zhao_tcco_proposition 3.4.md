---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]
\begin{proposition}
\label{prop: moduli over E}
If $K \subseteq G(\mathbb{A}_f)$ is neat, then the canoncial model $\mathrm{Sh}_K(G,\Omega)$ of $\mathrm{Sh}_K(G, \Omega)$ over $E$ is a solution to the fine moduli problem $S \mapsto \mathcal{M}_K(S)$.   
\end{proposition}
\begin{proof}
When $(G, \Omega)$ is of Hodge type, this is a special case of \cite[Thm~3.31]{Mil94}. 

% Note that Lem.~3.29 in \textit{loc. cit.} says that if (i) is satisfied by some $\tau$, then it is satisfied by every $\tau$. 

Now assume that $(G, \Omega)$ is the adjoint Shimura datum to some $(\widetilde{G}, \widetilde{\Omega})$ of Hodge type which satisfies (SV5). Let $\mathcal{K} \subseteq \widetilde{G}(\mathbb{A}_f)$ be a neat subgroup which lies in the preimage of $K$ under the adjoint morphism $\widetilde{G} \to G$. Then we have a morphism $\varpi : \mathrm{Sh}_\mathcal{K}(\widetilde{G}, \widetilde{\Omega})_\mathbb{C} \to \mathrm{Sh}_K(G, \Omega)_\mathbb{C}$ which surjects to some connected components of the target. Let $\sigma \in \mathrm{Aut}(\mathbb{C}/E)$ be any element and let $f_\sigma : \mathrm{Sh}_K(\widetilde{G}, \widetilde{\Omega})_\mathbb{C}^\sigma \stackrel{\sim}{\to} \mathrm{Sh}_K(\widetilde{G}, \widetilde{\Omega})_\mathbb{C}$ be the isomorphism defined by the canonical model. 

Let us denote by $\mathcal{M}_K^\circ(\mathbb{C})$ the set of tuples
defined just as $\mathcal{M}_K(\mathbb{C})$ but with the $\iota$ in (i) fixed to be the identity. Then Prop.~\ref{prop-Shimura-moduli} says that the $\mathbb{C}$-points of $\mathrm{Sh}_K(G, \Omega)_\mathbb{C}$ are in canonical bijection with $\mathcal{M}_K^\circ(\mathbb{C})$. Let $x \in \mathcal{M}_K^\circ(\mathbb{C})$ be a point given by tuple $(M, (t_\alpha), [\eta])$. 

Since the canonical model of $\mathrm{Sh}_K(G, \Omega)$ is uniquely characterized by the property that $\varpi$ is defined over $E$, it would be enough to show the following: 
\begin{enumerate}
    \item[(a)]$(M^\sigma, (t^\sigma_\alpha), [\eta^\sigma])$ defines a new point $\sigma(x) \in \mathcal{M}^\circ_K(\mathbb{C})$.
    \item[(b)] For any $\widetilde{x} \in \mathrm{Sh}_K(\widetilde{G}, \Omega)_\mathbb{C}$ lifting $x$, $\varpi(f_\sigma(\widetilde{x})) = \sigma(x)$. 
\end{enumerate}
Note that up to changing the level structure on $x$, we may always make sure that $x$ lies in the image of $\mathrm{Sh}_\mathcal{K}(\widetilde{G}, \widetilde{\Omega}) \to \mathrm{Sh}_K(G, \Omega)$. 

Choose a faithful reprensentation $\widetilde{\xi} : \widetilde{G} \hookrightarrow \mathrm{GL}(\widetilde{V})$ which realizes $\widetilde{G}$ as the stabilizer of $\widetilde{s}_\beta$'s. View $V$ as a $\widetilde{G}$-representation via $\widetilde{G} \to G$. Since the category of $\widetilde{G}$-representations is semisimple and $\widetilde{V}$ is faithful, for some finite direct sum $H$ of modules of the form $\widetilde{V}^{m} {\otimes} \widetilde{V}^n, (m, n) \in \mathbb{Z}_{\ge 0}^2$, there exists some embedding $i : V \hookrightarrow H$ of $\widetilde{G}$-representations together with a projection $\pi : H \to V$ such that $\pi \circ i = \mathrm{id}$. One may extend the pair $(i, \pi)$ to $(i_* : V^{\otimes} \hookrightarrow H^{\otimes}, \pi_* : H^{\otimes} \to V^{\otimes})$ such that $\pi_* \circ i_* = \mathrm{id}$, and view $i_* \circ \pi_*$ as an element of $\widetilde{V}^{\otimes}$. 

Now we view $\widetilde{G}$ as the stabilizer of the collection of tensors $\{ \widetilde{s}_\beta \}, \{ i \circ \pi, i_*(s_\alpha), i_* \circ \pi_* \}$ in $\mathrm{GL}(\widetilde{V})$ and endow $\mathrm{Sh}_\mathcal{K}(\widetilde{G}, \widetilde{\Omega})$ with a moduli interpretation using $\widetilde{\xi}$ and this group of tensors. Let $\widetilde{x}$ be a lifting of $x$. Then $\widetilde{x}$ corresponds to a tuple of the form $(\widetilde{M}, \{\{ \widetilde{t}_\beta \}, \{ i \circ \pi, i_*(t_\alpha), i_* \circ \pi_* \} \}, [\widetilde{\eta}])$. Let $H(\widetilde{M})$ be the submodule of $\widetilde{M}^{\otimes}$ formed out of $\widetilde{M}$ in the same way as $H$ out of $\widetilde{V}$. Then there is an isomorphism 
$$ (\omega_\mathrm{Hdg}(M), t_\alpha, [\eta]) \stackrel{\sim}{\to} (\mathrm{im}(i \circ \pi) \subseteq \omega_\mathrm{Hdg}(H(\widetilde{M})), i_*(t_\alpha), \pi(H([\widetilde{\eta}]))), $$
where $H(\widetilde{\eta})$ is defined in the obvious way. The RHS is part of the data of the tuple $(\widetilde{M}, \{\{ \widetilde{t}_\beta \}, \{ i \circ \pi, i_*(t)_\alpha, i_* \circ \pi_* \} \}, [\widetilde{\eta}])$ and the map $\varpi: \widetilde{x} \mapsto x$ is simply given by forgetting extra data. Since the pair $(i, \pi)$ is absolute Hodge, we obtain an isomorphism
$$ (\omega_\mathrm{Hdg}(M^\sigma), t^\sigma_\alpha, [\eta^\sigma]) \stackrel{\sim}{\to} (\mathrm{im}((i \circ \pi)^\sigma) \subseteq \omega_\mathrm{Hdg}(H(\widetilde{M}^\sigma)), i_*(t^\sigma_\alpha), \pi(H([\widetilde{\eta}^\sigma]))). $$
The RHS is a part of the data of the tuple $(\widetilde{M}^\sigma, \{\{ \widetilde{t}^\sigma_\beta \}, \{ (i \circ \pi)^\sigma, i_*(t_\alpha)^\sigma, (i_* \circ \pi_*)^\sigma \} \}, [\widetilde{\eta}^\sigma])$, which defines $f_\sigma(\widetilde{x})$ as the proposition is known in the Hodge type case. This allows one to easily check (a) and (b). 
\end{proof}

# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, proposition 3.4