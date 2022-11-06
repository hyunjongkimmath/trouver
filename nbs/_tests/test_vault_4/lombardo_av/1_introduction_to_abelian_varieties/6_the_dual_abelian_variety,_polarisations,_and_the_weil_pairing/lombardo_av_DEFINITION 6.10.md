---
cssclass: clean-embeds
aliases: [lombardo_av_dual_homomorphism_of_abelian_varieties]
tags: [_reference/lombardo_av, _meta/TODO/change_title, _meta/definition, _meta/literature_note, _meta/notation]
---
# Dual homomorphism of abelian varieties[^1]
Let $A / K, B / K$ be [[lombardo_av_1.3|abelian varieties]]. Given any $K$[[lombardo_av_DEFINITION 5.1|-homomorphism]] $\varphi: A \rightarrow B$, there is a **dual homomorphism** $\varphi^{\vee}: B^{\vee} \rightarrow A^{\vee}$[^2] constructed by applying the [[lombardo_av_DEFINITION 6.1|universal property]] of $A^{\vee}$ with $T=B^{\vee}$ and $\mathcal{L}=(\varphi \times 1)^{*} \mathcal{P}_{B \times B^{\vee}}$ (notice that this is a line bundle on $A \times B^{\vee}$ ) to obtain a map $B^{\vee}=T \rightarrow A^{\vee}$. Concretely, at the level of points, $\varphi^{\vee}$ is simply the pullback of line bundles from $B$ to A:
$$
\begin{aligned}
\varphi^{\vee}: \quad B^{\vee}(K)=& \operatorname{Pic}^{0}(B) & \rightarrow & A^{\vee}(K) &=\operatorname{Pic}^{0}(A) \\
\mathcal{L} & & & \mapsto & \varphi^{*} \mathcal{L}
\end{aligned}
$$
That $f^{\vee}$ is itself an isogeny is not obvious; for a proof, see for example [EMvG, Theorem 7.5] or [Mum70, p. 143].

[^2]: ![[lombardo_av_notation_A_vee_dual_abelian_variety]]


# See Also
- [[lombardo_av_notation_varphi_vee_dual_homomorphism]]
- [[lombardo_av_THEOREM 6.11]]
# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, DEFINITION 6.10, Page 20