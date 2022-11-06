---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]
\begin{lemma}
\label{lem: very ample on WPS}
Let $Q = (q_0, \cdots, q_r)$ be a tuple of natural numbers such that $\{ q_i \colon 0 \le i \le r \} = \{ 1, 2, 3 \}$. Then $\mathcal{O}(6)$ is a very ample line bundle on the weighted projective space $\mathbb{P}(Q)$.
\end{lemma}
\begin{proof}
By \cite[Thm~4B.7(c)]{WPS}, it suffices to show that for any positive integer $h$, and every tuple of natural numbers $(A, B, C)$ such that $A + 2B + 3C = 6 + 6h$, there exist a tuple of natural numbers $(a, b, c)$ such that $a \le A, b \le B, c \le C$ and $a + 2b + 3c = 6h$. 

We first show this for $h = 1$. If we have $A \ge 6$, $B \ge 3$, or $C \ge 2$, then $(a, b, c)$ certainly exists. Now suppose $A < 6, B < 3$, and $C < 2$. However, in that case $A + 2B + 3C \le 5 + 2\cdot 2 + 3 = 12$, so that we must have $(A, B, C) = (5, 2, 1)$. Then we may take $(a, b, c)$ to be, e.g., $(2, 2, 0)$. Now the lemma follows from a simple inductive argument. 
\end{proof}

# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, lemma 9.2