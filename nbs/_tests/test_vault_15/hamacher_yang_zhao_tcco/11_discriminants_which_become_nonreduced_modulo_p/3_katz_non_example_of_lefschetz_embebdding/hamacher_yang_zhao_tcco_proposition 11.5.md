---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]
\begin{proposition}
View $X$ and $\mathbb{P}^r$ as being defined over $W := W(k)$ by the same equation. Let $\mathfrak{D} \subseteq \check{\mathbb{P}}^r$ be the discriminant locus of the universal hyperplane section. Then $\mathfrak{D}_{k} \subseteq \check{\mathbb{P}}^r_k$ is defined by the $p^{m(r-1)}$-th power of an irreducible polynomial. In particular, $\mathfrak{D}_k$ is not reduced. 
\end{proposition}
\begin{proof}
Take a line $L \subseteq \check{\mathbb{P}}^r_k$ that intersects transversely with the (scheme-theoretic) image $\check{X}_k$ of $X_k$ under the Gauss map. By Lem.~\ref{lem: open in proj tangent bundle} we may choose the line $L$ such that $\mathcal{X}_L$ has a smooth total space. Choose a $W$-lifting $\widetilde{L}$ of $L$ such that $\widetilde{L}_{\bar{K}}$ is a Lefschetz pencil. 

Let $x \in X$ be a $k$-point and $\check{x} \in \check{X}_k$ be its image under the Gauss map. Note that the association of $x$ to $\check{x}$ is bijective. If $\check{x} \not \in L \cap \check{X}$, then the fiber $\mathcal{X}_{\check{x}}$ is smooth; otherwise, the fiber $\mathcal{X}_{\check{x}}$ has a unique singulariety at $x$. Therefore, $\mathfrak{D}_{k, \mathrm{red}}$ is nothing but $\check{X}_k$. By applying \cite[{\S}XVI~Prop.~2.1]{SGA7II} and a lifting argument as in the proof of Thm~\ref{thm: Saito+}, we reduce to showing that $\mu(\mathcal{X}_L/L, x) = p^m$ whenever $\check{x} \in L \cap \check{X}_k$. By Lem.~\ref{lem: Milnor as multiplicity}, $\mu(\mathcal{X}_L/L, x)$ is computed by $(\mathbb{P}(N), \mathcal{X}_L)_{\mathcal{X}, x}$. Now note that 
$$ \mathbb{P}(N) \cap \mathcal{X}_L = \mathbb{P}(N) \times_{\mathcal{X}} \mathcal{X}_L = \mathbb{P}(N) \times_{\mathcal{X}} \mathcal{X} \times_{\check{\mathbb{P}}} \times L = \mathbb{P}(N) \times_{\check{\mathbb{P}}} L.  $$
Together with the fact that $L$ intersects $\check{X}_k$ transversely, this implies that $(\mathbb{P}(N), \mathcal{X}_L)_{\mathcal{X}, x}$ is the degree of the preimage of $\check{x}$ under the Gauss map $X = \mathbb{P}(N) \to \check{\mathbb{P}}$, and this degree is clearly $p^{m(r-1)}$ as desired.
\end{proof}

# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, proposition 11.5