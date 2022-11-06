---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]
\begin{remark}
\label{rmk: dR ind of K}
The above definition is a relative version of \cite[Def.~2.7]{MPTate} (cf. \cite[(0.2)]{Blasius}) up to a slight twist: Since we are making a definition about Hodge cycles (as opposed to absolute Hodge cycles), we need to start with a system over $\mathbb{C}$. The choice of $K$ in part (a) is not important provided that it exists: If $K' \subseteq \bar{\mathbb{Q}}_p$ is a finite extension of $K$, then there is a commutative diagram:
%by the commutativity of $\mathsf{c}_\mathrm{dR}$ with pullback:
\[\begin{tikzcd}
	\mathbb{D}^\mathrm{alg}_\mathrm{dR}(\omega_p(\underline{\mathfrak{M}} / \underline{S})) & \omega_\mathrm{dR}(\underline{\mathfrak{M}} / \underline{S}) \\
	\mathbb{D}^\mathrm{alg}_\mathrm{dR}(\omega_p(\underline{\mathfrak{M}}_{K'} / \underline{S}_{K'})) & \omega_\mathrm{dR}(\underline{\mathfrak{M}}_{K'} / \underline{S}_{K'}) & \omega_\mathrm{dR}(\mathfrak{M}/ S)
	\arrow["\sim", from=1-1, to=1-2]
	\arrow[from=1-1, to=2-1]
	\arrow["\sim", from=2-1, to=2-2]
	\arrow[from=1-2, to=2-2]
	\arrow[from=1-2, to=2-3]
	\arrow[from=2-2, to=2-3]
\end{tikzcd}\]
Similarly, one checks that the choice of $\iota$ is only important up to precomposing with an element of $G_{\mathbb{Q}_p}$.
\end{remark}

# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, remark 4.2