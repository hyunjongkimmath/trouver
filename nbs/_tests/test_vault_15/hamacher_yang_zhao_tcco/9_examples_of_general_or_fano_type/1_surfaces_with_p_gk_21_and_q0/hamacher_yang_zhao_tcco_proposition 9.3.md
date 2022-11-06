---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]
\begin{proposition}
\label{prop: Lefschetz embedding}
Let $k$ be an algebraically closed field of characteristic $p > 3$. Let $Y \subseteq \mathbb{P}_k$ be a proper smooth hypersurface. Then embedding $\iota \colon Y \hookrightarrow \mathbb{P}' \coloneqq |\mathcal{O}_{\mathbb{P}_k}(6)|$ is a Lefschetz embedding. 
\end{proposition}
\begin{proof}
Since the coordiante $x_0$ has degree $1$, the $x_0 \neq 0$ locus of $\mathbb{P}_k$ is an affine chart isomorphic to $\mathbb{A}^4_k$ with coordinates $y_i \coloneqq x_i / x_0^{\mathrm{deg} \, x_i}$. We view the affine variable $y_i$ as having degree $\mathrm{deg} \, x_i$. Let $P$ be a point on $Y$ and assume that the projection of $\mathbb{A}^k_4$ to the $y_4$-axis is etale at $P$. Up to a translation, we further assume that $y_i = 0$ at $P$ for $i = 1, 2, 3$. By Prop.~3.3 and Cor.~3.5.0 in \textit{loc. cit.}, it suffices to show that for some $H \in |\mathcal{O}_{\mathbb{P}_k}(6)|$, the intersection $H \cap Y$ has an ODP at $P$. To this end, it suffices to present a polynomial in variables $y_1, y_2, y_3$ of weighted degree $\le 6$ such that its vanishing locus has an odp singularity at the origin, for which one may simply take $y_3^2 + y_1 y_2 = 0$. The role of $y_4$ could be replaced by any $y_i$'s, since we have $\mathrm{deg} \, y_i + \mathrm{deg} \, y_j \le 6$ for any $1 \le i, j \le 4$.
\end{proof}

# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, proposition 9.3