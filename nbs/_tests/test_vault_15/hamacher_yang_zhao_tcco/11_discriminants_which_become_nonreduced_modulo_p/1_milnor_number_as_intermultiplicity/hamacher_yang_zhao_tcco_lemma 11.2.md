---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]
\begin{lemma}
\label{lem: Milnor as multiplicity}
Let $x \in \mathcal{X}_L^\circ$ be a $k$-point which is an isolated singulariety on the fiber $\mathcal{X}_{p_L(x)}$. Then the Milnor number $\mu(p_L, x)$ is computed by the intersection multiplicity $(\mathbb{P}(N), \mathcal{X}_L)_{\mathcal{X}, x}$. 
\end{lemma}
\begin{proof}
This follows from \cite[Lem.~5.4(1)]{Saito2}, with $C$ being the $0$-section of $T^* X$ and $\mathbb{P}(\widetilde{C})$ being $\mathbb{P}(N)$. Unless otherwise noted, all references below come from \textit{loc. cit.} 

First, we explain that $x$ is an isolated characteristic point of $p_L^\circ : X_L^\circ \to L$, as defined in Def.~5.3(1), for which we need to check that 

\begin{enumerate}[label=\upshape{(\alph*)}]
    \item the pair $X \leftarrow X_L^\circ - \{ x \} \to L$ is $C$-transversal at a punctured neighborhood of $x$; 
    \item $X \leftarrow X_L^\circ \to L$ is not $C$-transversal at $x$.
\end{enumerate}

We refer the reader to Def.~3.3 and 3.5 for the definition of $C$-transversality in different contexts. Since $X^\circ_L \to X$ is an isomorphism locally at $x$ and $C$ is the $0$-section, this morphism is $C$-transversal at an open neighborhood of $x$ by Lem.~3.4(2). Let $dp_L^{-1}(C)$ denote the pullback of $C$ along the natural morphism $dp_L : T^* L|_{\mathcal{X}_L} \to T^* \mathcal{X}_L$. We need to show that for a small open neighborhood $U$ of $x$ in $\mathcal{X}^\circ_L$, $dp_L^{-1}(C)|_{U - \{ x \}}$ is contained in the $0$-section, but the fiber $dp_L^{-1}(C)|_{x}$ is not. This follows from the assumption that $p_L$ is a submersion on the punctured neighborhood $U - \{ x \}$ but not at $x$. 

Now Lem.~5.4(1) tells us that $(\mathbb{P}(N), \mathcal{X}_L)_{\mathcal{X}, x} = (C, dp_L^\circ)_{T^* X, x}$. The number $(C, dp_L^\circ)_{T^* X, x}$ is defined as follows (cf. Def.~5.3(2)): Let $V \subseteq L$ be an open neighborhood of $p_L(x)$ and $\omega \in \Gamma(V, \Omega^1_V)$ be a nowhere vanishing section. Then $p_L^*(\omega)$ defines an embedding $p_L^{-1}(V) \hookrightarrow T^* \mathcal{X}_L$. The number $(C, dp_L^\circ)_{T^* X, x}$ is defined to be $(C, p_L^{-1}(V))_{T^* \mathcal{X}, x}$, which is independent of the choice of $(V, \omega)$. It follows from \cite[{\S}XVI~Ex.~1.3]{SGA7II} that $(C, p_L^{-1}(V))_{T^* \mathcal{X}, x}$ is precisely the Milnor number $\mu(p_L, x)$.
\end{proof}

# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, lemma 11.2