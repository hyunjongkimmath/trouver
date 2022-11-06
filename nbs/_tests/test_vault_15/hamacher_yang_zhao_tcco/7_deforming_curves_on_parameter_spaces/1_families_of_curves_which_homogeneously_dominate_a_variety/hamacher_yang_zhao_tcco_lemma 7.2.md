---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]
\begin{lemma}
\label{lem: open in proj tangent bundle}
Let $S$ be a smooth $k$-variety and $\mathscr{P} \to S$ be a smooth family of varieties over $S$. Let $\mathscr{X} \subseteq \mathscr{P}$ be a relative effective Cartier divisor whose total space is smooth. If $s \in S(k)$ is a point such that $\mathscr{X}_s$ has isolated singularieties, then there exists an open dense subvariety $U \subseteq \mathbb{P}(\mathcal{T}_s S)$ with the following property: 

For every unramified morphism $\varphi \colon C \to S$ from a smooth curve $C$ which sends a point $c \in C$ to $s$, the total space of the pullback family $\mathscr{X}|_C$ has no singularity on $\mathscr{X}_t$ if $d \varphi(\mathcal{T}_c C) \in U$. 
\end{lemma}
\begin{proof}
Since the question is \'etale-local in nature, we may assume that $S = \mathbb{A}^m_k$ for $m = \dim S$, $s = 0$, $\mathscr{X}_s$ has a single isolated singulariety at a $k$-point $P \in \mathscr{X}_s \subseteq \mathscr{P}_s$, and $\mathscr{P}$ is isomorphic to $\mathbb{A}^n$ near $P$. Suppose that $\mathscr{X}$ is locally cut out by an equation $F(x_1, \cdots, x_n, s_1, \cdots, s_m)$ near $P$. That $P$ is a singularity of the fiber $\mathscr{X}_s$ but not of the total space $\mathscr{X}$ implies that $\partial F / \partial s_j \neq 0$ at $P$ for some $j$. One may simply take $U$ to be the open subscheme of $\mathcal{T}_s S \,{\cong}\, \mathbb{P}^{m - 1}$ where the coordinate of the basis vector $\partial_{s_j}$ is nonzero. 
\end{proof}

# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, lemma 7.2