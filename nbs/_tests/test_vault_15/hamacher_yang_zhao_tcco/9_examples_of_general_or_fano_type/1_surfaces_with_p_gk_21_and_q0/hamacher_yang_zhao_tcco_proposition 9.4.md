---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]
\begin{proposition}
\label{prop: general type no gl sec}
Let $k$ be an algebraically closed field of characteristic $p > 3$. Let $s$ be any $k$-point on $B_k$ which corresponds to a smooth degree $6$ hypersurface $H_0$ in $\mathbb{P}_k$. 
\begin{enumerate}[label=\upshape{(\alph*)}]
    \item For a general $k$-point $t$ on $\mathfrak{D}_s$, the fiber $\overline{\mathscr{X}}_t$ is smooth away from an ODP. Moreover, the fiber $\mathfrak{D}_s$ is generically reduced. 
    \item There does not exist a finite connected \'etale cover over $\mathsf{M}_{s}$ such that the pullback of $\mathbb{V}_\ell$ has a nonzero global section. 
\end{enumerate}

\end{proposition}
\begin{proof}
(a) The first statement is a straightforward consequence of Prop.~\ref{prop: Lefschetz embedding}. For the second statement, it suffices to show that the degree of the hypersurface $(\mathfrak{D}_s)_{\mathrm{red}}$ in the projective space $|\mathcal{O}_{\mathbb{P}_{s}}(6)|$ is independent of $s$. Let $H_0$ be the degree $6$ hypersurface of $\mathbb{P}_{s}$ given by $s$. Let $\gamma \colon \mathbb{P}^1_{k} \hookrightarrow |\mathcal{O}_{\mathbb{P}_{s}}(6)|$ be a general pencil, which by Prop.~\ref{prop: Lefschetz embedding} is necessarily a Lefschetz pencil for $H_0$ in the sense of \cite[\S XVII, 2.2]{SGA7II}. Then $d_s \coloneqq \mathrm{deg} (\mathfrak{D}_s)_{\mathrm{red}}$ is simply the number of singular fibers on $\overline{\mathscr{X}}|_{\gamma}$. Note that the total space of $\overline{\mathscr{X}}|_{\gamma}$ is smooth and every singular fiber is smooth away from an ODP. Let $\bar{\eta}$ be the geometric generic point of $\mathbb{P}^1_{k(s)}$. We apply the key argument for Lem.~\ref{lem: thread the needle} again: By the Leray spectral sequence and the Grothendieck-Ogg-Shafarevich formula, we have 
\begin{equation}
    d_s = \chi(\overline{\mathscr{X}}|_{\gamma}) - \chi(\mathbb{P}^1) \chi(\mathscr{X}_{\bar{\eta}}) 
\end{equation}
as the total dimension of vanishing cycles of each singular fiber is $1$. By a simple deformation argument, one sees that the RHS of the above equation is independent of $s$, and hence so is the LHS. 


(b) First, we argue that for a general $\mathbb{C}$-point $b \in B_\mathbb{C}$, the period morphism does not contract the fiber $\mathsf{M}_s$. This follows from a dimension count. By \cite[Thm~3.3]{Catanese}, the period morphism is dominant to the 18-dimensional period domain. As $B_\mathbb{C}$ is 13 dimensional, we conclude that the period morphism does not contract the generic fiber.

Next, we take $s$ to be a $k$-point on $\mathsf{M}$. Let $W := W(k)$ and choose an embedding $W \hookrightarrow \mathbb{C}$. By Lem.~\ref{lem: countability trick}, we can find a $W$-lifting $\widetilde{s}$ of such that the fiber $\mathsf{M}_{\widetilde{s} {\otimes} \mathbb{C}}$ is not contracted by the period morphism and does not lie in the Noether-Lefshetz loci. Let $T$ be the Grassmanian of lines in $|\mathcal{O}_{\mathbb{P}_W}(6)|$ and $\mathscr{C}$ be the universal family of $T$. Then we have a natural morphism $\varphi : \mathscr{C} \to |\mathcal{O}_{\mathbb{P}_W}(6)|$. Let $t \in T_k$ be a general $k$-point and again let $\gamma_t : \mathbb{P}^1_k \hookrightarrow |\mathcal{O}_{\mathbb{P}_k}(6)|$ be the resulting pencil. By Lem.~\ref{lem: FAP for curves}, we may choose a $W$-lifting $\widetilde{t}$ of $t$ such that the $\mathbb{C}$-fiber of the resulting $\widetilde{\gamma}_t : \mathbb{P}^1_{W} \hookrightarrow |\mathcal{O}_{\mathbb{P}_W}(6)|$ is not contracted by the period morphism and is not contained in the Noether-Lefschetz loci. Now we conclude by Lem.~\ref{lem: pencil no gl sec}. 
\end{proof}

# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, proposition 9.4