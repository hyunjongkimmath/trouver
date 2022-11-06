---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]
\begin{proposition}
\label{prop: N is abs Hdg}
Let $E$ be a number field and let $\mathfrak{m}, \mathfrak{n}$ be objects of $\mathsf{Mot}(\mathbb{C})$ with $E$-action. Let $\mathfrak{h} \coloneqq \mathfrak{m} {\otimes}_E \mathfrak{n}$. Let $m \in \omega_B(\mathfrak{m}), n \in \omega_B(\mathfrak{n})$ be nonzero Hodge cycles and define $h \in \omega_B(\mathfrak{h})$ to be $m {\otimes}_E n$. If $h$ and $m$ are both absolute Hodge, then so is $n$. 
\end{proposition}
\begin{proof}
 We need to show that for every $\sigma \in \mathrm{Aut}(\mathbb{C})$, the image $n^\sigma$  of $n$ under the canonical isomorphism 
$$ \omega_B(\mathfrak{n}) \otimes (\mathbb{C} \otimes \mathbb{A}_f) \cong \omega_\mathrm{dR}(\mathfrak{n}) \times \omega_{\mathbb{A}_f}(\mathfrak{n}) \,{\cong}\, \omega_\mathrm{dR}(\mathfrak{n}^\sigma) \times \omega_{\mathbb{A}_f}(\mathfrak{n}^\sigma) \cong \omega_B(\mathfrak{n}^\sigma) \otimes (\mathbb{C} \otimes \mathbb{A}_f). $$
is contained in $\omega_B(\mathfrak{n}^\sigma)$. Since $m$ and $h$ are absolute Hodge, we know that $m^\sigma \in \omega_B(\mathfrak{m}^\sigma)$ and $h^\sigma = m^\sigma \otimes n^\sigma \in \omega_B(\mathfrak{h}^\sigma)$. We conclude by Lemma~\ref{lem: descend n to Q} below.
\end{proof}

# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, proposition 2.9