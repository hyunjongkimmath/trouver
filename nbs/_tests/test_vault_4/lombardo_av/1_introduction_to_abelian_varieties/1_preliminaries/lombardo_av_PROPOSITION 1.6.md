---
cssclass: clean-embeds
aliases: [lombardo_av_Abelian_varieties_are_commutative]
tags: [_reference/lombardo_av, _meta/literature_note, _meta/proof, _meta/concept, _meta/TODO/change_title]
---
# Abelian varieties are commutative[^1]
Any [[lombardo_av_1.3|abelian variety]] is commutative, that is, the two maps

$$\begin{array}{ccc}
A \times A & \rightarrow A \\
(x, y) & \mapsto x \cdot y
\end{array}$$

and

$$\begin{aligned}
A \times A & \rightarrow A \\
(x, y) & \mapsto y \cdot x
\end{aligned}$$

coincide, where we (temporarily) denote by $\cdot$ the multiplication map on $A$.

# Proof
Since we are considering [[lombardo_av_1.3|abelian varieties]] over a field, it suffices to work at the level of $\bar{K}$-points (notice that $A$ is [[foag_separated_morphism#Separated morphism 1 2|separated]], so two morphisms are equal iff they are equal at all closed points). It's enough to show that the image of the map
$$
\begin{aligned}
A(\bar{K}) \times A(\bar{K}) & \rightarrow A(\bar{K}) \\
(x, y) & \mapsto y \cdot x \cdot y^{-1} \cdot x^{-1}
\end{aligned}
$$
is the identity element $e_{A}$ of $A(\bar{K}) .$ Now notice that the restriction of this map to $\left\{e_{A}\right\} \times$ $A(\bar{K})$ and to $A(\bar{K}) \times\left\{e_{A}\right\}$ is constantly equal to $e_{A}$, and apply the Rigidity lemma ([[lombardo_av_LEMMA 1.8|Lemma 1.8]]) below


# See Also
- [[lombardo_av_EXERCISE 1.1|lombardo_av_Alternate_proof_that_abelian_varieties_are_commutative]]
# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, PROPOSITION 1.6, Page 8
