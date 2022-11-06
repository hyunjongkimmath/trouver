---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]
\begin{proposition}
\label{prop: (4, 6) curve strongly dominates}
When $\mathcal{O}_S = k$ for some algebraically closed field $k$, the family $\mathbb{A}^1_T / T$ strongly dominates $\mathbb{A}(\mathcal{V}_4 \oplus \mathcal{V}_6)^*$ via $\varphi$. Moreover, for a general point $t \in T$, $\overline{\varphi}_t(\infty) \not\in \overline{\mathfrak{D}}$. 
\end{proposition}
\begin{proof}
Let us denote $\mathbb{A}(\mathcal{W}_4^{d_1} \oplus \mathcal{W}_6^{d_2})$ temporarily by $T^+$ and $\mathbb{A}(\mathcal{V}_4 \oplus \mathcal{V}_6)$ by $\mathscr{A}$. Note that $T^+ \,{\cong}\, \mathbb{A}^{5 d_1 + 7 d_2}$, as it simply parametrizes the coefficients of $f_i$ and $g_j$'s. We also view $T^+$ as a $k$-vector space of dimension $5 d_1 + 7 d_2$. 

There is a natural morphism $\varphi^+ \colon \mathbb{A}^1_{T^+} \to \mathbb{A}$ which extends $\varphi$. With the chosen coordinates, we may naturally identify $\mathcal{T} \mathscr{A}$ with $\mathscr{A} \times \mathscr{A}$. Consider the natural morphism $\Gamma \colon \mathbb{A}^1 \times_k T^+ \to \mathcal{T} \mathscr{A}$ defined by 
$$ \Gamma(u, (f_i, g_j)) = \left( (f_i(u), g_j(u)), (f'(u), g'(u)) \right). $$
For any $u_0 \in \mathbb{A}^1(k)$, the fiber $\Gamma_{u_0}$ is simply a morphism of vector spaces $T^+ \to k^2$. Moreover, it is clearly surjective, which readily implies that the morphism $\Gamma$ has equi-dimensional fibers. Then one readily checks that $\mathbb{A}^1_{T^+}$ strongly dominates $\mathscr{A}$ via $\varphi^+$. 

To see that $\mathbb{A}^1_T$ strongly dominates $\mathscr{A}^*$ it suffices to show that for each point $(x, v) \in \mathcal{T}_x \mathscr{A}$, a general point $(f_i, g_j)$ in $\Gamma^*(x, v)$ satisfies the property that the common vanishing locus of (re-homogenized) $f_i$ and $g_j$'s on $\mathbb{P}^1$ is empty. One easily checks this by dimension counting. 

For the second statement, consider the $\infty$-section $\sigma_\infty \colon T \to \mathbb{P}^1_T$ which sends every $t \in T$ to $\infty$. It suffices to show that the closed subscheme $\overline{\varphi}^*(\overline{\mathfrak{D}})$ is not the entire $T$, for which we only need to construct a point on $T$ not in $\overline{\varphi}^*(\overline{\mathfrak{D}})$. Let $t \in T$ be any point such that for some point $w \in \mathbb{A}^1$, $\varphi_t(w) \not\in \mathfrak{D}$. Then we can always apply a linear change of variables (i.e., an automorphism of $\mathbb{P}^1$) to switch $w$ and $\infty$. This gives us another point $t' \in T$ and by construction $\varphi_{t'}(\infty) \not\in \overline{\mathfrak{D}}$. 
\end{proof}

# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, proposition 8.8