---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]
\begin{theorem}
\label{thm: comparison is dR}
Let $K \subseteq \bar{\mathbb{Q}}_p$ be a finite extension of $\mathbb{Q}_p$ and choose an isomorphism $\iota : \bar{\mathbb{Q}}_p \,{\cong}\, \mathbb{C}$. Let $S$ be a smooth $K$-variety. Let $\mathfrak{h} \in \mathsf{Mot}(S)$ be a family of motives over $S$ such that: 
\begin{itemize}
    \item The $\mathbb{Q}$-VHS $\mathbb{V}(\mathfrak{h}_{\mathbb{C}}/S_\mathbb{C})$ is pure of weight $2$ and has big variation somewhere on every connected component of $S_\mathbb{C}$. 
    \item For every $s \in S_\mathbb{C}$, every $(1, 1)$-class in $\omega_B(\mathfrak{h}_s)$ is algebraic, i.e., comes from a submotive isomorphic to the Lefschetz motive $\mathfrak{l}$. 
\end{itemize}
Let $\mathfrak{h}'$ be another family with the same properties and let $(f_B, f_{\mathrm{dR}, \mathbb{C}}) \colon \mathbb{V}(\mathfrak{h}_{\mathbb{C}}/S_\mathbb{C}) \stackrel{\sim}{\to} \mathbb{V}(\mathfrak{h}'_{\mathbb{C}}/S_\mathbb{C})$ be an isomorphism such that $f_B {\otimes} \mathbb{Q}_p$ descends to an isomorphism $f_p \colon \omega_p(\mathfrak{h}/S) \to \omega_p(\mathfrak{h}'/S)$. Then $(f_B, f_{\mathrm{dR}, \mathbb{C}})$ satisfies Conj.~\ref{conj: de Rham} as a relative Hodge cycle on $\mathrm{Hom}(\mathfrak{h}_\mathbb{C}, \mathfrak{h}_\mathbb{C}')$ over $S_\mathbb{C}$. 
\end{theorem}
\begin{proof}
Let $\alpha \coloneqq f_{\mathrm{dR}, \mathbb{C}}^{-1} \circ \mathbb{D}^\mathrm{alg}_\mathrm{dR}(f_p) {\otimes}_\iota \mathbb{C}$. Then $\alpha$ is an automorphism of $\omega_\mathrm{dR}(\mathfrak{h}_{\mathbb{C}}/ S_\mathbb{C})$ as an object of $\mathrm{FIC}(S_\mathbb{C})$. Since the choice of $\iota$ is arbitrary, it suffices to show that $\alpha = \mathrm{id}$. Let $S_\mathbb{C}^\circ$ be any connected component of $S_\mathbb{C}$ and choose a base point $s \in S_\mathbb{C}^\circ$. To show that $\alpha|_{S_\mathbb{C}^\circ} = \mathrm{id}$ it suffices to show that $\alpha_{s} = \mathrm{id}$. Let $s$ be another point on $S_\mathbb{C}^\circ$ and $\gamma$ be a topological path from $s$ to $s'$. Denote the parallel transport operators induced by $\gamma$ by the same letter. Then $\alpha_{s}$ can be viewed as $\gamma^{-1} \alpha_{s'} \gamma$, which is independent of the choice of $\gamma$. This implies that to check $z \in \omega_\mathrm{dR}(\mathfrak{h}_{s})$ is invariant under $\alpha_s$, it suffices to check that $\gamma(z) \in \omega_\mathrm{dR}(\mathfrak{h}_{s'})$ is invariant under $\alpha_{s'}$. \\\\
\textit{Claim: If $z$ lies in $\omega_B(\mathfrak{h}_{s})^{(1, 1)}$, then $z$ is $\alpha_{s}$-invariant.}
 By assumption, $z = \mathrm{cl}(\xi)$ for some submotive $\xi \,{\cong}\, \mathfrak{l}$ of $\mathfrak{h}$. By Rmk~\ref{rmk: dR ind of K}, we may replace $K$ by a finite extension and assume that $(s, \xi)$ are defined over $K$ and denote the descent by $(\underline{s}, \underline{\xi})$. The we have a commutative diagram:  

\[\begin{tikzcd}
	& \omega_p(\mathfrak{h}_{s}) & {} & \omega_p(\mathfrak{h}'_{s}) & {} \\
	\omega_B(\mathfrak{h}_s) && \omega_B(\mathfrak{h}'_s) \\
	&& \omega_\mathrm{dR}(\mathfrak{h}_{\underline{s}}) && \omega_\mathrm{dR}(\mathfrak{h}'_{\underline{s}}) \\
	& \omega_\mathrm{dR}(\mathfrak{h}_s) && \omega_\mathrm{dR}(\mathfrak{h}'_{s})
	\arrow[from=2-1, to=1-2]
	\arrow[from=2-1, to=4-2]
	\arrow[dashed, from=1-2, to=3-3]
	\arrow[from=3-3, to=4-2]
	\arrow[from=2-1, to=2-3, crossing over]
	\arrow[from=1-2, to=1-4]
	\arrow[dashed, from=1-4, to=3-5]
	\arrow[from=2-3, to=4-4, crossing over]
	\arrow[from=4-2, to=4-4]
	\arrow[from=3-5, to=4-4]
	\arrow[from=3-3, to=3-5]
	\arrow[from=2-3, to=1-4]
\end{tikzcd}\]
In the diagram above, every solid arrow becomes an isomorphism when the source is tensored with the natural coefficient of the target (i.e., $\mathbb{Q}_p, K$ or $\mathbb{C}$), and all the squares with only solid arrows commute except possibly the bottom one, whose commutativity is precisely what we want to show. The main obstacle is that the dashed arrows do not literally exist. Instead, they are only drawn to suggest the de Rham comparison isomorphisms, which only exist when the modules are tensored with $B_\mathrm{dR}$. 

This problem goes away, however, when we restrict to considering the Galois invariant part of $\omega_p(-)$: For any trivial $G_K$-representation $M$, the isomorphism $M {\otimes}_{\mathbb{Q}_p} B_\mathrm{dR} \stackrel{\sim}{\to} \mathbb{D}_\mathrm{dR}(M) {\otimes}_K B_\mathrm{dR}$ comes from the natural $\mathbb{Q}_p$-linear map $M \to M {\otimes}_{\mathbb{Q}_p} K = \mathbb{D}_{\mathrm{dR}}(M)$. Now we set $\omega_B^\circ(-) = \omega_B(\mathfrak{h}_s(1))^{(0, 0)} \cap \omega_p(-(1))^{G_K}$. Then we obtain a diagram

\[\begin{tikzcd}
	& \omega_p(\mathfrak{h}_{s})^{G_K} & {} & \omega_p(\mathfrak{h}'_{s})^{G_K} & {}  \\
	\omega^\circ_B(\mathfrak{h}_s) && \omega^\circ_B(\mathfrak{h}'_s) \\
	&& \omega_\mathrm{dR}(\mathfrak{h}_{\underline{s}}) && \omega_\mathrm{dR}(\mathfrak{h}'_{\underline{s}}) \\
	& \omega_\mathrm{dR}(\mathfrak{h}_s) && \omega_\mathrm{dR}(\mathfrak{h}'_{s})
	\arrow[from=2-1, to=1-2]
	\arrow[from=2-1, to=4-2]
	\arrow[from=1-2, to=3-3]
	\arrow[from=3-3, to=4-2]
	\arrow[from=2-1, to=2-3, crossing over]
	\arrow[from=1-2, to=1-4]
	\arrow[from=1-4, to=3-5]
	\arrow[from=2-3, to=4-4, crossing over]
	\arrow[from=4-2, to=4-4]
	\arrow[from=3-5, to=4-4]
	\arrow[from=3-3, to=3-5]
	\arrow[from=2-3, to=1-4]
\end{tikzcd}\]
Again, every square commutes, except possibly the bottom one. In particular, the squares on the top, left, right and front commute because the classes in $\omega_B^\circ(\mathfrak{h}_s)$ are precisely given by submotives of $\mathfrak{h}_s$ which are defined over $K$. This implies that, if we denote the image of $\omega_B^\circ(\mathfrak{h}_s)$ in $\omega_\mathrm{dR}(\mathfrak{h}_{\underline{s}})$ as $\omega_\mathrm{dR}(\mathfrak{h}_{\underline{s}})^\dagger$, then restriction of the bottom diagram 
\[\begin{tikzcd}
\omega_\mathrm{dR}(\mathfrak{h}_{\underline{s}})^\dagger \arrow{r}{} \arrow{d}{} & \omega_\mathrm{dR}(\mathfrak{h}_{\underline{s}}) \arrow{d}{} \\
\omega_\mathrm{dR}(\mathfrak{h}_s) \arrow{r}{} & \omega_\mathrm{dR}(\mathfrak{h}'_s) 
\end{tikzcd} \]
commutes. In particular, $\alpha_s(z) = z$ as desired. \\\\
Now we return to the proof of the theorem. By the preceeding lemma, there exists a basis $\{ z_i \}_{i \in I}$ of $\omega_B(\mathfrak{h}_s)$ such that for each $z_i$ has the following property: There exists a another point $s'$ and a topological path $\gamma$ from $s$ to $s'$ such that $\gamma(s')$ is of type $(1, 1)$, and hence invariant under $\alpha_{s'}$ by the claim. This implies, by the first paragraph, that $z_i$ is invariant under $\alpha_s$. Since $\{ z_i \}_{i \in I}$ is also a $\mathbb{C}$-basis of $\omega_\mathrm{dR}(\mathfrak{h}_s)$, $\alpha_s$ has to be the identity. 
\end{proof}

# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, theorem 4.6