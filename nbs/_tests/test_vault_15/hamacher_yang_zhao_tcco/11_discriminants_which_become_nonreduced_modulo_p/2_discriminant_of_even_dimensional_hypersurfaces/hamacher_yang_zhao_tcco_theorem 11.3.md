---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]
\begin{theorem}
\label{thm: Saito+}
Let $p$ be a prime and let $\bar{\mathbb{F}}_p$ be an algebraic closure of $\mathbb{F}_p$. Then the fiber $\mathfrak{D} {\otimes} \bar{\mathbb{F}}_p$ is irreducible unless $r$ is odd and $p = 2$, in which case the defining equation of $\mathfrak{D} {\otimes} \bar{\mathbb{F}}_2$ in $\mathbb{P}^N_\mathbb{Z} {\otimes} \bar{\mathbb{F}}_2$ is the square of an irreducible polynomial. 
\end{theorem}
\begin{proof}
Let $k$ denote $\bar{\mathbb{F}}_p$ and write $W$ for $W(k)$. Let $\bar{K}$ be an algebraic closure of $K := W[1/p]$. Note that by Lem.~\ref{lem: image of P(N)} $\mathfrak{D}_{k, \mathrm{red}}$ is irreducible, so it suffices to show that 
\begin{enumerate}[label=\upshape{(\alph*)}]
    \item when $p \neq 2$ or $r$ is even, $\mathrm{deg}(\mathfrak{D}_{k, \mathrm{red}}) = \mathrm{deg}(\mathfrak{D}_{\bar{K}})$;
    \item when $p = 2$ and $r$ is odd, $2\mathrm{deg}(\mathfrak{D}_{k, \mathrm{red}}) = \mathrm{deg}(\mathfrak{D}_{\bar{K}})$.
\end{enumerate}
Here by degree we just mean the usual notion of the degree of the hypersurface $\mathfrak{D}_{k, \mathrm{red}}$ (resp. $\mathfrak{D}_{\bar{K}}$) in the projective space $\mathbb{P}^{N_d}_k$ (resp. $\mathbb{P}^{N_d}_{\bar{K}}$). 

By Katz' criterion, the embedding $i_k : \mathbb{P}^r_k \hookrightarrow \mathbb{P}^{N_d}_k$ is a Lefshetz embedding, so we may choose a Lefschetz pencil $L \subseteq \check{\mathbb{P}}^{N_d}_k$. We may choose a $W$-lifting $\widetilde{L} \subseteq \check{\mathbb{P}}^{N_d}_W$ such that the geometric generic fiber $\widetilde{L}_{\bar{K}}$ is a Lefschetz pencil over $\bar{K}$. We may assume that $L$ and $\widetilde{L}_{\bar{K}}$ intersects $\mathfrak{D}_{k, \mathrm{red}}$ and $\mathfrak{D}_{\bar{K}}$ transversely. For $\kappa = k$ or $\bar{K}$, let $x'$ denote the unique singulariety on the fiber of $\mathcal{X}$ over a point $x \in (\widetilde{L} \cap \mathfrak{D})_\kappa(\kappa)$. Then we have a formula (\cite[{\S}XVI~Prop.~2.1]{SGA7II})
\begin{equation}
    \label{eqn: global Milnor formula}
    \chi(\mathcal{X}_{\widetilde{L}_{\kappa}}) = \chi(\mathbb{P}^1_\kappa) \chi(\mathcal{X}_{\bar{\eta}(\widetilde{L}_\kappa)}) - (-1)^{r - 1} \sum_{x \in (\widetilde{L} \cap \mathfrak{D})_\kappa(\kappa)} \mu(\mathcal{X}_L/L, x').
\end{equation}
One may easily check by the smooth and proper base change theorem that the numbers $\chi(\mathcal{X}_{\widetilde{L}_{\kappa}})$ and $\chi(\mathcal{X}_{\bar{\eta}(\widetilde{L}_\kappa)})$ do not depend on whether $\kappa$ is $k$ or $\bar{K}$. As $x'$ in the above equation is always an ordinary quadratic singulariety, the same is true for $\mu(\mathcal{X}_L/L, x')$ as well for every $x'$ when $p \neq 2$ or $r$ is even (\cite[{\S}XVI~Cas 1, 2]{SGA7II}). In fact, these Milnor numbers are all equal to $1$. Therefore, we have $\#(\widetilde{L} \cap \mathfrak{D})_k(k) = \#(\widetilde{L} \cap \mathfrak{D})_{\bar{K}}(\bar{K})$. This implies (a). 

For (b) we apply a theorem of Beilinson \cite[Thm~1.7]{Beilinson} with $\mathcal{F} := \mathbb{F}_\ell$ being the constant sheaf on $\mathbb{P}^r$. Let $N$ denote the conormal bundle of $X_k$ in $\mathbb{P}^N_k$. Below we follow the notations of \textit{loc. cit.}, except that his $\mathbb{P}$ is our $X_k$ and his $\widetilde{\mathbb{P}}$ is our $\mathbb{P}^{N_d}_k$. Let $\widetilde{Q} \subseteq \mathbb{P}^{N_d}_k \times \check{\mathbb{P}}^{N_d}_k$ be the universal hyperplane section and let $D_\mathcal{F} \subseteq \check{\mathbb{P}}^{N_d}$ be the smallest closed subvariety such that on the complement $\check{\mathbb{P}}^{N_d} - D_\mathcal{F}$ the Radon transform $\widetilde{R}(i_* \mathcal{F})$ is locally constant. Since $\mathcal{X}_k = X_k \times_{\mathbb{P}^{N_d}_k} \widetilde{Q}$, the proper base change theorem tells that $\widetilde{R}(i_* \mathbb{F}_\ell) \,{\cong}\, (f_* \mathbb{F}_\ell)[N_d - 1]$ as objects in the bounded derived category of constructible sheaves on $\check{\mathbb{P}}_k$ with $\mathbb{F}_\ell$-coefficients, where $f$ is the composition $\mathcal{X} \to Q \to \check{\mathbb{P}}^N$. Now the smooth and proper base change theorem implies that $D_\mathcal{F} \subseteq \mathfrak{D}_{k, \mathrm{red}}$. However, by Beilinson's theorem, $D_\mathcal{F}$ is a divisor. As $\mathfrak{D}_{k, \mathrm{red}}$ is irreducible, we must in fact have $D_\mathcal{F} = \mathfrak{D}_{k, \mathrm{red}}$. Then Beilinson's theorem further tells us that the morphism $\mathbb{P}(N) \to \mathfrak{D}_{k, \mathrm{red}}$ is generically radicial and has generic degree at most $2$. Indeed, it is not hard to see that $D_\mathcal{F} = \mathbb{P}(i_\circ C)$ for $C$ being the $0$-section of $T^* X_k$ (the notation $i_\circ$ is explained in the last paragraph of \cite[\S1.2]{Beilinson}). 

Therefore, we may take an open dense subset $U \subseteq \mathfrak{D}_{k, \mathrm{red}}$ such that $\mathbb{P}(N)|_{U} \to U$ is finite flat of degree $\le 2$. We may assume that the our Lefschetz pencil $L$ intersects $U$ transversely, which is a generic property. By Lem.~\ref{lem: Milnor as multiplicity}, we have that for every $x \in (L \cap \mathfrak{D})_k(k)$, 
$$ \mu(\mathcal{X}_L/L, x') = (\mathbb{P}(N), \mathcal{X}_L)_{\mathcal{X}, x'} \le 2. $$
By \cite[Prop.~3.24]{Daichi}, $\mu(\mathcal{X}_L/L, x')$ is always an even number. Since it has to be positive, it is equal to $2$. Together with (\ref{eqn: global Milnor formula}), this implies (b). 
\end{proof}

# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, theorem 11.3