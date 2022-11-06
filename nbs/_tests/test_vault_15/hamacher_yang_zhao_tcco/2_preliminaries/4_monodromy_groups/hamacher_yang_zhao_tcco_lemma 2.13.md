---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]
\begin{lemma}
\label{lem: geometric Tate}
Let $S$ be a smooth connected $\mathbb{C}$-variety and $\mathscr{X} \to S$ be a projective family of $h^{2, 0} = 1$ varieties which satisfies $(\heartsuit)$. Let $\eta$ be the generic point of $S$. Then the natural morphism
$$ \mathrm{NS}(\mathscr{X}_{\bar{\eta}}) {\otimes} \mathbb{Q}_\ell \stackrel{\sim}{\to} \varinjlim_{U \subseteq \pi_1^\mathrm{{\acute{e}}t}(S, \bar{\eta})} \mathrm{H}^2_\mathrm{{\acute{e}}t}(\mathscr{X}_{\bar{\eta}}, \mathbb{Q}_\ell)^U, $$
where $U$ runs through compact open subgroups, is an isomorphism. 
\end{lemma}
\begin{proof}
We recall that as $S$ is normal, the natural map $\pi_1^\mathrm{{\acute{e}}t}(\eta, \bar{\eta}) \to \pi_1^\mathrm{{\acute{e}}t}(S, \bar{\eta})$ is surjective and open (\cite[0BQJ]{stacks-project}). The elements of $\mathrm{NS}(\mathscr{X}_{\bar{\eta}})$ are hence stabilized by an open subgroup of $\pi_1^\mathrm{{\acute{e}}t}(S, \bar{\eta})$. This gives rise to the map in the lemma. Moreover, it is clearly injective. 

To see the surjectivity, choose a polarization on $\mathscr{X}/S$ and let $\mathbb{V}$ be the $\mathbb{Q}$-VHS $\mathrm{PH}^2(\mathscr{X}/S, \mathbb{Q})(1)$. It suffices to show that for a very general point $s \in S$, we have 
$$ \mathrm{PH}^2(\mathscr{X}_s, \mathbb{Q})^{(1, 1)} = \varinjlim_{U \subseteq \pi_1(S, s)} \mathrm{PH}^2(\mathscr{X}_s, \mathbb{Q})^U, $$
as $U$ runs through finite index subgroups. The RHS can be identified with the subspace of $\mathrm{PH}^2(\mathscr{X}_s, \mathbb{Q})$ fixed by the identity component $\mathrm{Mon}^\circ(\mathbb{V}, s)$ of $\mathrm{Mon}(\mathbb{V}, s)$. Let $T$ be the transcendental part of $\mathbb{V}_s$. We reduce to showing that $\mathrm{Mon}^\circ(\mathbb{V}, s)$ cannot fix any element in $T$. 

Let $E \coloneqq \mathrm{End}_\mathrm{Hdg} T$. By Thm~\ref{thm: Zarhin} and the above, there are only three possibilities for $\mathrm{Mon}^\circ(\mathbb{V}, s)$ (cf. \cite[Prop.~6.4(iii)]{Moonen} and its proof): 
\begin{enumerate}[label=\upshape{(\alph*)}]
    \item If $E$ is totally real and $\dim_E T \neq 4$, $\mathrm{Mon}^\circ(\mathbb{V}, s) = \mathrm{SO}_{E/\mathbb{Q}}(T)$.
    \item If $E$ is totally real, $\dim_E T = 4$, and $\mathrm{Mon}^\circ(\mathbb{V}, s)$ is a proper subgroup of $\mathrm{SO}_{E/\mathbb{Q}}(T)$, then $\mathrm{Mon}^\circ(\mathbb{V}, s) = H_{E/\mathbb{Q}}$, where $H$ is a nontrivial normal subgroup of the $E$-group $\mathrm{SO}(T)$. 
    \item If $E$ is CM, then $\mathrm{Mon}^\circ(\mathbb{V}, s) = \mathrm{SU}_{E/\mathbb{Q}}(T)$. 
\end{enumerate}
The statements (a) and (c) are straightforward as in those cases $\mathrm{SO}_{E/\mathbb{Q}}(T)$ and $\mathrm{SU}_{E/\mathbb{Q}}(T)$ are simple. (b) was mentioned in \cite[\S8.1]{Moonen} and follows from \cite[Prop.~6.18]{BorelTits}. 

We first prove the lemma in case (a). Since the set of rational points in a connected reductive group is Zariski dense, it suffices to show that the action of $\mathrm{SO}_{E/\mathbb{Q}}(T) {\otimes}_\mathbb{Q} \mathbb{C}$ on $T {\otimes}_\mathbb{Q} \mathbb{C}$ has no fixed elements. But then the statement is clear, as 
$$ \mathrm{SO}_{E/\mathbb{Q}}(T) {\otimes}_\mathbb{Q} \mathbb{C} = \prod_{\sigma \colon E \hookrightarrow \mathbb{C}} \mathrm{SO}(T) {\otimes}_\sigma \mathbb{C}. $$
Case (c) is entirely similar. Now we consider (b). For any embedding $\sigma \colon E \hookrightarrow \mathbb{C}$, $H {\otimes}_\sigma \mathbb{C}$ is one of the two normal subgroups of $\mathrm{SO}(T) {\otimes}_\sigma \mathbb{C}$ isomorphic to $\mathrm{SL}_2$. Recall that over $\mathbb{C}$ we have $(\mathrm{SL}_2 \times \mathrm{SL}_2) / \mu_2 \,{\cong}\, \mathrm{SO}_4$. If we view $\mathrm{SO}_4$ as defined by the determinant form on the space of $2 \times 2$ matrices, then the two copies of $\mathrm{SL}_2$ act via left or right multiplication. It is clear then neither of them fixes any nonzero element. 
\end{proof}

# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, lemma 2.13