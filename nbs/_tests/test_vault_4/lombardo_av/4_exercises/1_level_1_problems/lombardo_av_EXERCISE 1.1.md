---
cssclass: clean-embeds
aliases: [lombardo_av_Alternate_proof_that_abelian_varieties_are_commutative]
tags: [_reference/lombardo_av, _meta/literature_note, _meta/exercise, _auto/links_added, _meta/TODO/change_title, _meta/proof]
---
# Alternate proof that abelian varieties are commutative[^1]
(Commutativity of [[lombardo_av_1.3|abelian varieties]], slightly different proof). 

Using the fact[^2] that the map $x \mapsto x^{-1}$ is algebraic, show that an [[lombardo_av_1.3|abelian variety]] is commutative.

[^2]: By definition.

# Proof
Let $A$ be an [[lombardo_av_1.3|abelian variety]]. To show that  it is commutative, it suffices to show that the inverse map $x \mapsto x^{-1}$ is a [[lombardo_av_DEFINITION 5.1|homomorphism]]. Since this map is an [[fulton_it_ B.2.1|algebraic morphism]], it is the composition of a [[lombardo_av_DEFINITION 5.1|homomorphism]] with a translation. Note that it sends $0_A$ to $0_A$[^3], any such translation must be the translation-by-$0_A$ map. Thus, $x \mapsto x^{-1}$ is itself a [[lombardo_av_DEFINITION 5.1|homomorphism]].

[^3]: lombardo_av_notation_0_A_identity_element

# See Also

# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, EXERCISE 1.1, Page 63
