---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]
\begin{proposition}
\label{prop: strongly dominates smooth total family}
Let $\mathscr{X}$ and $S$ be as in Lem.~\ref{lem: open in proj tangent bundle}. Suppose that 
\begin{itemize}
    \item the generalized discriminant variety $D \coloneqq \mathrm{Disc}(f) \subseteq S$ is mild; 
    \item there is a family of smooth curves $\mathscr{C} / T$ which homogeneously dominates $S$ through a morphism $\varphi$.
\end{itemize}
Then for a general $k$-point $t \in T$, the total space of the pullback family $\mathscr{X}|_{\mathscr{C}_t}$ is smooth. 
\end{proposition}
\begin{proof}
By assumption we have a diagram 
\[\begin{tikzcd}
	& \mathscr{C} && \mathscr{X} \\
	T && S
	\arrow["g", from=1-2, to=2-1]
	\arrow["\varphi"', from=1-2, to=2-3]
	\arrow["f"', from=1-4, to=2-3]
\end{tikzcd}\]

Let $\mathcal{Z} \subseteq S \times T$ be the subset of points $(s, t)$ such that $\mathscr{C}_t$ passes through $t$ and the total space of $\mathscr{X}|_{\mathscr{C}_t}$ has a singulariety lying above $\varphi^{-1}_t(s)$. It is easy to see that $\mathcal{Z}$ is constructible: Let $\mathscr{X}|_\mathscr{C}$ be the pullback of $\mathscr{X}$ along $\varphi$. Then we have a natural morphism $\mathscr{X}|_\mathscr{C} \to T \times_k S$ and $\mathcal{Z}$ is the set-theoretic image of $\mathrm{Sing}(\mathscr{X}|_\mathscr{C} \to T)$. Endow $\mathcal{Z}$ with the structure of a reduced scheme. 

It suffices to show that $\dim \mathcal{Z} < \dim T$. Let $V$ be as in Def.~\ref{def: generalized disc}(c) and for $s \in V(k)$, let $U_s \subseteq \varphi^{-1}(s)$ be as in Def.~\ref{def: homogeneously dominates}(b). Let $t = g(s)$. By Lem.~\ref{lem: open in proj tangent bundle}, there exists a proper closed subvariety $U_{s, \mathrm{bad}} \subseteq U$ such that the total space of $\mathscr{X}|_{\mathscr{C}_t}$ is not smooth near the fiber $\mathscr{X}_u$ only if $u \in U_{s, \mathrm{bad}}$. Let $\widetilde{\mathcal{Z}}_s \subseteq \varphi^{-1}(s)$ be the union of the complement of $U_s$ and the Zariski closure of $U_{s, \mathrm{bad}}$. Then $\widetilde{\mathcal{Z}}_s$ is a proper closed subvariety of $\varphi^{-1}(s)$. Since the morphism $\varphi^{-1}(s) \to T$ is quasi-finite and the fiber $\mathcal{Z}_s \subseteq T$ is contained in the image of $\widetilde{\mathcal{Z}}_s$, we have $$ \dim \mathcal{Z}_s <  \dim \varphi^{-1}(s) = \dim \mathscr{C} - \dim S. $$
Since the image of $\mathcal{Z}$ in $S$ is contained in $D$, and $s$ was taken as a general point of $D$, we have that $\dim \mathcal{Z} \le \dim \mathscr{C} - 2 = \dim T - 1$ as desired. 
\end{proof}

# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, proposition 7.4