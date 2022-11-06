---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]
\begin{lemma}
\label{lem: key lemma}
Let $\mathbb{V}_\ell$ be a rank $n$ free $\mathbb{Z}_\ell$-local system over $S$. Consider the monodromy representations 
$$ \rho_{\bar{K}} \colon \pi_1^\mathrm{{\acute{e}}t}(S_{\bar{K}}, b) \to \mathrm{GL}(\mathbb{V}_\ell|_b) \text{ and } \rho_k \colon \pi_1^\mathrm{{\acute{e}}t}(S_k, a) \to \mathrm{GL}(\mathbb{V}_\ell|_{a}). $$
If $p \nmid |\mathrm{GL}_n(\mathbb{F}_\ell)|$, or $\mathbb{V}_\ell$ is tamely ramified over $\overline{S}$, then the identity component of the Zariski closure of the image of $\rho_{\bar{K}}$ is equal to that of $\rho_k$ under the identification $\mathbb{V}_\ell|_{a} = \mathbb{V}_\ell|_b$ along the chosen \'etale path. 
\end{lemma}
\begin{proof}
Note that $\rho_{\bar{K}}$ and $\rho_k$ are both obtained by the restricting the monodromy representation $\rho \colon \pi_1^\mathrm{{\acute{e}}t}(S, a) \to \mathrm{GL}(\mathbb{V}_\ell|_{a})$ of the entire $S$. If $\mathbb{V}_\ell$ is tamely ramified along $\overline{S}$, then $\rho$ factors through the tame fundamental group $\pi_1^t(S, a)$, and the lemma follows simply from the fact that the natural map $\pi^t_1(S_k, a) \to \pi_1^t(S, a)$ is an isomorphism (\cite[{\S}XIII~2.10]{EGAIV4}).

Now we prove the lemma under the assumption $p \nmid |\mathrm{GL}_n(\mathbb{F}_\ell)|$. We pick a basis and identify $\mathbb{V}_\ell|_a$ with $\mathbb{Z}_\ell^{n}$. For a subgroup $G$ of $\mathrm{GL}_n(\mathbb{Q}_\ell)$, let use denote by $\overline{G}$ the Zariski closure in $\mathrm{GL}_{n, \mathbb{Q}_\ell}$ and $\overline{G}^\circ$ the identity component. We will repeatedly apply the following observation: $\overline{G}^\circ$ remains unchanged if we replace $G$ by a finite index subgroup. 

Let $U_\ell \coloneqq \ker(\mathrm{GL}_n(\mathbb{Z}_\ell) \to \mathrm{GL}_n(\mathbb{F}_\ell))$. Then $U_\ell$ is a pro-$\ell$ open normal subgroup of $\mathrm{GL}_n(\mathbb{Z}_\ell)$ of index $|\mathrm{GL}_n(\mathbb{F}_\ell)|$. We use supscript $\ell$ to denote the pullback of $U_\ell$ under (various restrictions of) $\rho$, i.e., for $(* = \emptyset, k, {\bar{K}})$ we have a fiber diagram 

\begin{center}
    \begin{tikzcd}
     \pi_1^\mathrm{{\acute{e}}t}(S_*)_\ell \arrow{r}{} \arrow{d}{\rho_{*, \ell}} & \pi_1^\mathrm{{\acute{e}}t}(S) \arrow{d}{\rho} \\
     U_\ell \arrow{r}{} & \mathrm{GL}_n(\mathbb{Z}_\ell). 
    \end{tikzcd}
\end{center}
Moreover, we have $\pi_1^\mathrm{{\acute{e}}t}(S_k)_\ell \to \pi_1^\mathrm{{\acute{e}}t}(S)_\ell \leftarrow \pi_1^\mathrm{{\acute{e}}t}(S_{\bar{K}})_\ell$ which is compatible with $\pi_1^\mathrm{{\acute{e}}t}(S_k) \to \pi_1^\mathrm{{\acute{e}}t}(S) \leftarrow \pi_1^\mathrm{{\acute{e}}t}(S_{\bar{K}})$ via the above diagrams. This implies that we have two sequences of inclusions which are compatible in the obvious way: 
$$ \overline{\mathrm{im}(\rho_{{\bar{K}}, \ell})}^\circ \subseteq \overline{\mathrm{im}(\rho_\ell)}^\circ \supseteq \overline{\mathrm{im}(\rho_{k, \ell})}^\circ, \text{ and } \overline{\mathrm{im}(\rho_{{\bar{K}}})}^\circ \subseteq \overline{\mathrm{im}(\rho)}^\circ \supseteq \overline{\mathrm{im}(\rho_{k})}^\circ.  $$

In particular, as $\pi_1^\mathrm{{\acute{e}}t}(S_*)_\ell$ is of finite index in $\pi_1^\mathrm{{\acute{e}}t}(S_*)$, we have $\overline{\mathrm{im}(\rho_*)}^\circ = \overline{\mathrm{im}(\rho_{*, \ell})}^\circ$. Then it suffices to show that the inclusion $\overline{\mathrm{im}(\rho_\ell)}^\circ \supseteq \overline{\mathrm{im}(\rho_{k, \ell})}^\circ$ is an equality. Note that since $U_\ell$ is pro-$\ell$, any morphism $G \to U_\ell$ from a profinite group $G$ factors through $G \to G^{(p)}$. In particular, the morphisms $\rho_{*, \ell}$ factors through $\rho^{(p)}_{*, \ell} \colon [\pi_1^\mathrm{{\acute{e}}t}(S_*)_\ell]^{(p)} \to U_\ell$. For simplicity, write $\beta_*$ for $\rho^{(p)}_{*, \ell}$. The question now reduces to showing that $\overline{\mathrm{im}(\beta_k)}^\circ \subseteq \overline{\mathrm{im}(\beta)}^\circ$ is an equality. 

We have a commutative diagram: 

\begin{center}
    \begin{tikzcd}
     {[\pi_1^\mathrm{{\acute{e}}t}(S_k)_\ell]}^{(p)} \arrow{r}{} \arrow{d}{} & {[\pi_1^\mathrm{{\acute{e}}t}(S_k)]}^{(p)} \arrow{d}{}  \\
     {[\pi_1^\mathrm{{\acute{e}}t}(S)_\ell]}^{(p)} \arrow{r}{} & {[\pi_1^\mathrm{{\acute{e}}t}(S)]}^{(p)} 
    \end{tikzcd}
\end{center}
In the above diagram, the horizontal arrows have finite cokernels by construction and are injective by Prop.~\ref{prop: max prime-to-p quotient}. Grothendieck's theorem \cite[{\S}XIII~2.10]{EGAIV4} tells us that the right vertical arrow is an isomorphism, so the left vertical arrow has finite cokernel. By the diagram 
\[\begin{tikzcd}
{[\pi_1^\mathrm{{\acute{e}}t}(S_k)_\ell]}^{(p)} \arrow{d}{} \arrow{dr}{\beta_{k, \ell}} & \\
{[\pi_1^\mathrm{{\acute{e}}t}(S)_\ell]}^{(p)} \arrow{r}{\beta} & U_\ell 
\end{tikzcd}
\]
$\overline{\mathrm{im}(\beta_\ell)}^\circ = \overline{\mathrm{im}(\beta)}^\circ$ as desired. 
\end{proof}

# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, lemma 6.3