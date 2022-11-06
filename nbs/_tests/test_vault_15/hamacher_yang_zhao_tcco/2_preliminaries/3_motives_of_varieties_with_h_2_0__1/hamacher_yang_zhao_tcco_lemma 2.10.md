---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]
\begin{lemma}
\label{lem: descend n to Q}
Let $E/k$ be a field extension, $R$ be a $E$-algebra and $M, N$ be finite dimensional $E$-vector spaces. Let $H \coloneqq M {\otimes}_E N$ and suppose $h \in H {\otimes}_k R$ is a nonzero element of the form $m {\otimes} n$ under the canonical isomorphism 
$$ H {\otimes}_k R \,{\cong}\, (M {\otimes}_k R) {\otimes}_{E {\otimes}_k R} (N {\otimes}_k R), $$
where $m \in M {\otimes}_k R$ and $n \in N {\otimes}_k R$. If $h \in H$ and $m \in M$, then $n \in N$. 
\end{lemma}
\begin{proof}
  By choosing bases of $M$ and $N$, we may assume $M = E^m$ and $N = E^n$ and identify $H$ with $E^{m\times n}$ and $h$ with $m \cdot n^T$. We denote by $(m_i),(n_j),(h_{i,j})$ the respective coordinates of $m,n$ and $h$ and fix $i$ such that $m_i \not= 0$. Then $h_{i,j} = m_i \cdot n_j$ and hence $n_j = m_i^{-1} h_{i,j}  \in E$.
\end{proof}

# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, lemma 2.10