---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]
\begin{proposition}
\label{prop: GM big monodromy}
Let $k$ be an algebraically closed field of characteristic $p \ge 3$. There does not exist a connected \'etale cover over $\mathsf{M}_{k}$ such that the pullback of $\mathbb{V}_\ell$ has a nonzero global section. 
\end{proposition}
\begin{proof}
Let $b \in B_k$ be a $k$-point such that the corresponding rank $n + 4$ subspace $\mathbb{P}(\mathcal{H}_k)$ of $\mathbb{P}(\mathcal{F}_k)$ has smooth intersection with $\mathrm{CGr}(2, \mathcal{V}_k)$. Denote this intersection by $Y$.

Fix an embedding $W := W(k) \hookrightarrow \mathbb{C}$. Choose a $W$-point $\widetilde{b}$ on $B_W$ such that the restriction of the $\mathbb{Q}$-VHS $\mathbb{V}$ on $\mathsf{M}_{\widetilde{b}}(\mathbb{C})$ is non-isotrivial, and $\mathsf{M}_{\widetilde{b}, \mathbb{C}}$ does not lie in the Noether-Lefschetz loci. Let $\mathcal{Y} \subseteq \mathbb{P}(\mathcal{F}_W)$ be the lifting of $Y$ over $W$ induced by $\widetilde{b}$. Let the restriction of $\mathcal{O}_{\mathcal{F}_W}(2)$ to $\mathcal{Y}$ (resp. $Y$) be denoted by $\mathcal{O}_\mathcal{Y}(2)$ (resp. $\mathcal{O}_Y(2)$). Let $\mathfrak{D} \subseteq |\mathcal{O}_\mathcal{Y}(2)|$ be the discriminant variety defined by the universal hypersurface. Then the open subscheme $\mathsf{M}_{\widetilde{b}} \subseteq \mathscr{P}_{\widetilde{b}}$ is the complement of $\mathfrak{D}$. 

Let $T$ be the relative Grassmannian of lines in $|\mathcal{O}_\mathcal{Y}(2)|$ and let $\mathscr{C}$ be the universal family over $T$. Then we have a natural morphism $\varphi : \mathscr{C} \to |\mathcal{O}_\mathcal{Y}(2)|$. By \cite[{\S}XVII~Thm~2.5.1]{SGA7II}, the embedding $\mathcal{Y} \hookrightarrow |\mathcal{O}_\mathcal{Y}(2)|$ is a Lefschetz embedding. Therefore, for a general $k$-point $t \in T_k$, the fiber $\varphi_t: \mathscr{C}_t \,{\cong}\, \mathbb{P}^1_k \to |\mathcal{O}_Y(2)|$ defines a Lefschetz pencil. Choose a $W$-lifting $\widetilde{t}$ of $t$ such that the $\mathbb{C}$-fiber of $\varphi_{\widetilde{t}} : \mathbb{P}^1_W \to |\mathcal{O}_\mathcal{Y}(2)|$ is also a Lefschetz pencil, is not contracted by the period morphism, and does not lie in the Noether-Lefschetz loci. By the same argument as in Lem.~\ref{lem: thread the needle}, the intersection $\mathbb{P}^1_W \cap \mathfrak{D}$ is \'etale over $W$, and the restriction of $\mathbb{V}_\ell$ to $\mathbb{P}^1_W - (\mathbb{P}^1_W \cap \mathfrak{D})$ is tamely ramified. We may now conclude by Lem.~\ref{lem: pencil no gl sec}. 
\end{proof}

# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, proposition 9.7