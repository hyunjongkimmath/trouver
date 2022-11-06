---
cssclass: clean-embeds
aliases: [lombardo_av_group_scheme]
tags: [_meta/notation, _meta/TODO/change_title, _meta/literature_note, _meta/definition, _reference/lombardo_av]
---
# Group scheme over a scheme[^1]
Let $S$ be a [[foag_scheme|scheme]]. A **group scheme over $S$** is an $S$[[foag_category_of_schemes_over_a_base_scheme|-scheme]] $\mathcal{G}$ together with three morphisms
$$
m: \mathcal{G} \times_{S} \mathcal{G} \rightarrow \mathcal{G}, \quad i: \mathcal{G} \rightarrow \mathcal{G}, \quad e: S \rightarrow \mathcal{G}
$$
called respectively the multiplication, inverse, and unit maps. They satisfy the obvious axioms to endow the set of points $\mathcal{G}(A)$ (for any $S-$ scheme $A$ ) with the structure of a group; for example, associativity translates into the commutativity of the following diagram

![[Pasted image 20220308154036.png]]

and there are analogous diagrams that encode the fact that $i$ gives the inverse and $e$ the unit for the group law.

# See Also
- [[lombardo_av_EXAMPLE 1.2|lombardo_av_Multiplicative_and_additive_groups]] - Basic examples
- [[lombardo_av_DEFINITION 5.1|lombardo_av_homomorphism_of_group_schemes]]
# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, DEFINITION 1.1, Page 5
