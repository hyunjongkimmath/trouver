---
cssclass: clean-embeds
aliases: [lombardo_av_isogeny_is_an_equivalence_relation]
tags: [_auto/notations_added, _auto/links_added, _meta/literature_note, _reference/lombardo_av, _meta/TODO/change_title, _meta/remark]
---
# Isogeny is an equivalence relation[^1]
REMARK 5.14 (Isogeny is an equivalence relation). $\sim$[^2][^3]               induces an equivalence relation. Indeed, it is clear that $\sim$[^2][^3]               is reflexive and transitive[^5] , and it suffices to check that it is symmetric. Suppose that $\varphi: A \rightarrow B$ is an [[lombardo_av_DEFINITION 5.3|isogeny]]: we want to construct an [[lombardo_av_DEFINITION 5.3|isogeny]] $B \rightarrow A$ in the opposite direction. Since ker $\varphi$ is a [[foag_finite_morphism_of_schemes|finite]] group ([[foag_scheme_over_a_ring#Scheme over a ring 1|scheme]]), it is in particular of [[foag_finite_morphism_of_schemes|finite]] exponent $N$, so ker $\varphi \subseteq \operatorname{ker}[N]$ (also as [[lombardo_av_DEFINITION 1.1|group schemes]]). Consider the following commutative diagram:

![[Pasted image 20220308173307.png]]

We notice that $\psi$ exists and is an isomorphism because of the [[lombardo_av_DEFINITION 6.1|universal property]] of the quotient $A \rightarrow A /$ ker $\varphi ;$ moreover, since ker $\varphi$ is contained in ker $[N]$, one sees that there is a [[lombardo_av_DEFINITION 5.1|homomorphism]] $\pi$ as in the diagram (in fact, it is nothing but the canonical projection from $A / \operatorname{ker} \varphi$ to $\left.\frac{A / \operatorname{ker} \varphi}{A[N] / \operatorname{ker} \varphi}\right) .$ In particular we may define $\chi:=\pi \circ \psi^{-1}$. Finally, using again the [[lombardo_av_DEFINITION 6.1|universal property]] of the quotient one also sees that $\omega$ is an isomorphism. Putting everything together we may define a [[lombardo_av_DEFINITION 5.1|homomorphism]] $B \rightarrow A$ as the composition $\omega \circ \chi=$ $\omega \circ \pi \circ \psi^{-1}$; this [[lombardo_av_DEFINITION 5.1|homomorphism]] is in fact an [[lombardo_av_DEFINITION 5.3|isogeny]] because $\omega$ and $\psi^{-1}$ are isomorphisms and $\pi$ is an [[lombardo_av_DEFINITION 5.3|isogeny]].
The argument in the previous remark implies in particular:

[^5]: if $A \sim B$[^2][^3]               and $B \sim C$[^2][^3]              , then we have isogenies $\varphi_{1}: A \rightarrow B$ and $\varphi_{2}: B \rightarrow C$, so $\varphi_{2} \circ \varphi_{1}$ is an [[lombardo_av_DEFINITION 5.3|isogeny]] $A \rightarrow C$


# See Also

# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, REMARK 5.14, Page 17
[^2]: ![[lombardo_av_notation_sim]]
[^3]: ![[lombardo_av_notation_sim_linearly_equivalent]]