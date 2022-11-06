---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]
\begin{proposition}
\label{prop: smoothness of total space elliptic}
The morphism $\widetilde{\mathcal{X}} \to S$ is smooth. 
\end{proposition}
\begin{proof}
We may assume that $S = \mathrm{Spec}(k)$, where $k$ is an algebraically closed field of characteristic $\neq 2, 3$. Let us simply write $\mathbb{A}^*$ for $\mathbb{A}(\mathcal{V}_4 \oplus \mathcal{V}_6)^*$. Choose a point $u \in \mathbb{A}^*(k)$ and $c \in \mathcal{C}(k)$. Choose a uniformizer $t$ of $C$ at $c$ and bases $\{ \sigma_i \}, \{ \theta_j \}$ for $\mathcal{V}_4, \mathcal{V}_6$ respectively. Then the formal complection of $\mathbb{A}^* \times C$ at $(u, c)$ can be identified with $\mathrm{Spf}(R)$, where $R = k[\![t, \alpha_0, \cdots, \alpha_{4h - g}, \beta_0, \cdots, \beta_{6h - g}]\!]$.

By choosing a local $\mathcal{O}_C$-generator of $L$ at $c$, we turn $\sigma_i$'s and $\theta_j$'s into elements in $k[\![t]\!]$. Let $(\{a_i\}, \{b_j\}) \in k^{10h - 2g}$ be the affine coordinates of $u$ in $\mathbb{A}(\mathcal{V}_4 \oplus \mathcal{V}_6)$. Then the restriction of $\widetilde{\mathcal{X}}$ to $\mathrm{Spf}(R)$ can be identified with the subscheme of $\mathrm{Proj\,} R[x, y, z]$ defined by the equation 
\begin{equation}
    \label{eqn: local Weierstrass}
    W \coloneqq y^2z - x^3 + (\sum_{i = 0}^{4h - g} (a_i + \alpha_i) \sigma_i(t)) xz^2 + (\sum_{j = 0}^{6h - g} (b_j + \beta_j) \theta_j(t)) z^3 
\end{equation}
Let $r$ be the special point of $\mathrm{Spf}(R)$. The singularity of the (generalized) elliptic curve $\mathcal{X}_t$ defined by the above equation when $t$, $\alpha_i$'s and $\beta_j$'s all vanish cannot appear on the $z = 0$ chart. So we may set $z = 1$ in the above equation and consider the resulting scheme in $\mathrm{Spec} R[x, y]$. Since $\theta_0(0) \neq 0$, we deduce that the partial derivative $\partial W / \partial \beta_0$ remains nonzero on the special fiber. This implies that the total space of the restriction of $\widetilde{\mathcal{X}}$ to $\mathrm{Spf}(R)$ is smooth. But the choice of $(u, c)$ is arbitrary, so $\widetilde{\mathcal{X}}$ is smooth. 
\end{proof}

# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, proposition 8.3