---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]
\begin{proposition}
For a general $z \in \mathsf{M}_\mathbb{C}$ and $X \coloneqq \mathscr{X}_z$, the Kodaira-Spencer map $$ T_z \mathsf{M}_\mathbb{C} \to \mathrm{Hom}(\mathrm{H}^1(\Omega^1_{X}), \mathrm{H}^2(\mathcal{O}_{X}))$$ has rank at least $3$. 
\end{proposition}
\begin{proof}
This follows from a construction of Ikeda \cite{Ikeda} that we now briefly recall. In \textit{loc. cit.}, Ikeda constructed a subfamily of elliptic surfaces over $\mathbb{C}$ with the given invariants $p_g = q = 1$ using bielliptic curves of genus $3$. Let $\widetilde{C}$ be a bielliptic curve of genus $3$, equipped with an involution $\sigma$ such that $\widetilde{C}/\sigma$ is a smooth genus $1$ curve $C$. On the symmetric square $\widetilde{C}^{(2)}$ of $\widetilde{C}$, $\sigma$ also lifts to an involution $\sigma^{(2)}$. Consider the surface $Y'={\widetilde{C}}^{(2)}/\sigma^{(2)}$, which is shown to be a projective surface of Kodaira dimension $1$ with $6$ ODPs. Its minimal resolution $Y$ is an elliptic surface with $p_g = q = 1$. By Prop.~2.9 in \textit{loc. cit.}, the morphism $\widetilde{C} \to C$ can be recovered from $Y$. Note however the Weierstrass model of $Y$ is singular, so $Y$ is not given by a point on $\mathsf{M}$.

By applying the Artin-Brieskorn resolution of singularieties \cite{Artin-Res} to $\overline{\mathscr{X}}|_{\mathsf{M}_\mathbb{C}}$, we obtain a smooth and proper algebraic space $\mathscr{X}_\mathbb{C}^\# \to \mathsf{P}_\mathbb{C}^\#$, where $\mathsf{P}_\mathbb{C}^\#$ is an algebraic space which admits a morphism to $\mathsf{P}_\mathbb{C}$ which is bijective on geometric points. Moreover, since the fibers of $\overline{\mathscr{X}}$ have at most rational double point singularieties \cite[Thm~1]{Kas}, \cite[Thm~2]{Artin-Res} tells us that for any $\mathbb{C}$-point $z$ of $\mathsf{P}^\#_\mathbb{C}$ which maps to a point $s$ of $\mathsf{P}_\mathbb{C}$, the Henselianization (and hence also the completion) of $\mathsf{P}^\#_\mathbb{C}$ at $z$ maps surjectively to that of $\mathsf{P}_\mathbb{C}$ at $s$. Let $\mathsf{P}^+_\mathbb{C}$ be a resolution of singularieties of $\mathsf{P}^\#_\mathbb{C}$ and pullback the family $\mathscr{X}^\#$ to $\mathsf{P}^+_\mathbb{C}$. 

Now let $\mathsf{B}$ be the moduli space of bielliptic curves of genus $3$ over $\mathbb{C}$. Then there is a family of elliptic surfaces $\mathscr{Y}$ over $\mathsf{B}$. Let $\Omega$ be the period domain parametrizing Hodge structures of K3-type on the integral lattice $\Lambda$ given by the singular cohomology of any complex elliptic surface with $p_g = q = 1$. Let $\widetilde{\mathsf{B}}$ be the universal cover of $\mathsf{B}$. Then there is a period morphism $\widetilde{\mathsf{B}} \to \Omega$ which is well defined up to $\mathrm{O}(\Lambda)$. In \cite[\S 5]{Ikeda}, the author showed that the period image has dimension at least $3$. 

One quickly obtains the conclusion using the observation that the period image of the universal cover of $\mathsf{P}_\mathbb{C}^+$ contains the period image of $\widetilde{\mathsf{B}}$ up to the action of $\mathrm{O}(\Lambda)$ and that $\mathsf{M}_\mathbb{C}$ is connected. Indeed, the pullback of $\mathsf{M}_\mathbb{C}$ to $\mathsf{P}^+_\mathbb{C}$ is open and dense. By a continuity argument, we know that the period image of $\mathsf{M}_\mathbb{C}$ has the same dimension as that of $\mathsf{P}^+_\mathbb{C}$. 
\end{proof}

# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, proposition 8.12