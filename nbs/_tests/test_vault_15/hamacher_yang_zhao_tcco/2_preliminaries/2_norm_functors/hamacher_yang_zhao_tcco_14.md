---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]
 

We recall the basics of norm functors. The reader may refer to \cite[\S3]{Moonen} for more details. Let $k$ be a field in characteristic zero and $E$ be an \'etale $k$-algebra. Let $\mathscr{C}$ be any Tannakian $k$-linear category and $\mathscr{C}_{(E)}$ be the category of $E$-modules in $\mathscr{C}$. Then we may consider a norm functor $\mathrm{Nm}_{E/k} \colon \mathscr{C}_{(E)} \to \mathscr{C}$ (\cite[\S3.6]{Moonen}). For any object $M \in \mathscr{C}_{(E)}$, we write $M_{(k)}$ for the underlying object in $\mathscr{C}$ when we forget the $E$-linear structure. 

We now specialize to the case when $\mathscr{C}$ is the category of $k$-modules $\mathsf{Mod}_k$. For any $M \in \mathsf{Mod}_E$, there is a functorial polynomial map $\nu_M \colon M \to \mathrm{Nm}_{E/k}(M)$ such that $\nu_M(em) = \mathrm{Nm}_{E/k}(e) \nu_M(m)$ for any $e \in E$ and $m \in M$. The norm functor $\mathrm{Nm}_{E/k}$ is a ${\otimes}$-functor and is non-additive (unless $E = k$). However, for any $M_1, M_2 \in \mathsf{Mod}_E$, there is an identification 
$$ \mathrm{Nm}_{E/k}(\mathrm{Hom}_E(M_1, M_2)) = \mathrm{Hom}_k(\mathrm{Nm}_{E/k}(M_1), \mathrm{Nm}_{E/k}(M_2)). $$
Let us write $N(-)$ for $\mathrm{Nm}_{E/k}(-)$ when no ambiguity arises. The above identification gives us a structural map 
$$ \eta \colon \mathrm{Res}\,_{E/k} \mathrm{GL}(V) \to \mathrm{GL}(N(V)) $$
for any $V \in \mathsf{Mod}_E$, which sends an $E$-linear automorphism $f$ to $\mathrm{Nm}_{E/k}(f)$. 

Let $T_E$ denote the torus $\mathrm{Res}\,_{E/k} \mathbb{G}_m$ and $T_E^1$ denote the kernel of the norm map $T_E \to T_k$. If $V$ is a faithful $E$-module, then $\ker(\eta) = T^1_E$. Given an algebraic group $\mathcal{G}$ over $E$ we denote the Weil restriction by $\mathcal{G}_{E/\mathbb{Q}}$. For $V \in \mathsf{Mod}_E$ and $G \subseteq \mathrm{GL}(V_{(k)})$, we denote the intersection of $G$ with the centralizer of $T_E$ in $\mathrm{GL}(V)$ by $C_E(G)$. 


We now further specialize to the situation when $k = \mathbb{Q}$ and $E$ is a totally real field. Recall that $(V,\widetilde\phi) \mapsto (V_{\mathbb{Q}},\phi \coloneqq \mathrm{tr}_{E/\mathbb{Q}} \circ \phi)$ defines an equivalence of categories between quadratic forms over $E$ and quadratic forms over $\mathbb{Q}$ with an self-adjoint $E$-action (\cite[Ch~1, Thm~7.4.1]{Knus}). We call $\phi$ the transfer of $\widetilde\phi$. This equivalence identifies $\mathrm{O}_{E/\mathbb{Q}}(V, \widetilde{\phi})$ with the centralizer $C_E(\mathrm{O}(V_{(\IQ)}, \phi))$. Let $Z = T_E^1 \cap (\mu_{2, E})_{E/\mathbb{Q}}$. Then we have a commutative diagram 

\begin{equation}
    \begin{tikzcd}
     & 1 \arrow{d}{} & 1 \arrow{d}{} & & \\
     & \mathrm{SO}_{E/ \mathbb{Q}}(V) \arrow{d}{} \arrow[equal]{r}{} & \mathrm{SO}_{E/ \mathbb{Q}}(V) \arrow{d}{} & & \\
     1 \arrow{r}{} & C_E(\mathrm{SO}(V_{(\IQ)})) \arrow{d}{} \arrow{r}{} & \mathrm{O}_{E/\mathbb{Q}}(V)  \arrow{d}{(\det_E)_{E/\mathbb{Q}}} \arrow{r}{\det} & \mu_2 \arrow{r}{} \arrow[equal]{d}{} & 1 \\
     1 \arrow{r}{} & Z \arrow{r}{} \arrow{d}{} & (\mu_{2, E})_{E/\mathbb{Q}} \arrow{d}{} \arrow{r}{\mathrm{Nm}} & \mu_2 \arrow{r}{} & 1 \\
     & 1 & 1 & & 
    \end{tikzcd}
\end{equation}
with exact rows and columns. The key observation we will use is that if $\dim_E V$ is odd, then the vertical exact sequences are naturally split by the maps induced by the inclusion $\mu_{2, E} \hookrightarrow \mathrm{O}(V)$, and the composition 
\begin{equation}
    \label{eqn: composite norm map}
    \mathrm{SO}_{E/\mathbb{Q}}(V) \hookrightarrow \mathrm{GL}_{E/\mathbb{Q}}(V) \stackrel{\eta}{\to} \mathrm{GL}(N(V)) 
\end{equation}
is injective. 

Finally, we recall some facts about spin groups from \cite[\S4.2, 4.3]{Moonen}. The transfer of quadratic forms induces a morphism $\mathrm{CSpin}_{E/\mathbb{Q}}(V) \to \mathrm{CSpin}(V_{(\IQ)})$ with coimage $\overline{\mathrm{CS}}\mathrm{pin}_{E/\mathbb{Q}}(V) \coloneqq \mathrm{CSpin}_{E/\mathbb{Q}}(V)/T_E^1$. Moreover, we have an identification
\begin{equation}
\label{eqn: CSpin-bar}
    \overline{\mathrm{CS}}\mathrm{pin}_{E/\mathbb{Q}}(V) = \mathrm{SO}_{E/\mathbb{Q}}(V) \times_{\mathrm{SO}(V_{(\IQ)})} \mathrm{CSpin}(V_{(\IQ)}). 
\end{equation}

% There is a natural morphism $\mathrm{CSpin}_{E/\mathbb{Q}}(V) \to \mathrm{CSpin}(V_{(\IQ)})$ which factors through a subgroup $\overline{\mathrm{CS}}\mathrm{pin}_{E/\mathbb{Q}}(V)$ of $\mathrm{CSpin}(V_{(\IQ)})$. Moreover, there is an identification 
% \begin{equation}
%     \overline{\mathrm{CS}}\mathrm{pin}_{E/\mathbb{Q}}(V) = \mathrm{SO}_{E/\mathbb{Q}}(V) \times_{\mathrm{SO}(V_{(\IQ)})} \mathrm{CSpin}(V_{(\IQ)}). 
% \end{equation}



# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, 14