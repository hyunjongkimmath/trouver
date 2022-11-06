---
cssclass: clean-embeds
aliases: [foag_Covariant_functor, foag_identity_functor, foag_functors]
tags: [_meta/definition, _reference/foag, _meta/literature_note, _meta/notation]
---
# Covariant functor[^1]
1.2.11. Functors.
A **covariant functor** $F$ from a category $\mathscr{A}$ to a category $\mathscr{B}$, denoted $\mathrm{F}: \mathscr{A} \rightarrow \mathscr{B}$, is the following data. It is a map of objects $\mathrm{F}: \operatorname{obj}(\mathscr{A}) \rightarrow \operatorname{obj}(\mathscr{B})$, and for each $\mathrm{A}_{1}$, $\mathrm{A}_{2} \in \mathscr{A}$, and morphism $\mathrm{m}: \mathrm{A}_{1} \rightarrow \mathrm{A}_{2}$, a morphism $\mathrm{F}(\mathrm{m}): \mathrm{F}\left(\mathrm{A}_{1}\right) \rightarrow \mathrm{F}\left(\mathrm{A}_{2}\right)$ in $\mathscr{B} .$ We require that F preserves identity morphisms (for $\left.A \in \mathscr{A}, \mathrm{F}\left(\mathrm{id}_{\mathrm{A}}\right)=\operatorname{id}_{\mathrm{F}(\mathrm{A})}\right)$, and that F preserves composition $\left(\mathrm{F}\left(\mathrm{m}_{2} \circ \mathrm{m}_{1}\right)=\mathrm{F}\left(\mathrm{m}_{2}\right) \circ \mathrm{F}\left(\mathrm{m}_{1}\right)\right) .$ (You may wish to verify that covariant functors send isomorphisms to isomorphisms.) A trivial example is the **identity functor** **$\operatorname{id}: \mathscr{A} \rightarrow \mathscr{A}$**, whose definition you can guess. Here are some less trivial examples.


# See Also
- [[foag_notation_id_A_arrow_A]]
- [[foag_ 1.2.12|foag_Forgetful_functor]]
- [[foag_ 1.2.13|foag_Topological_functor_examples]]
- [[foag_ 1.2.14|foag_Representable_functor_example]]
- [[foag_ 1.2.15|foag_Composition_of_functors]]
- [[foag_ 1.2.15|foag_Full_and_faithful_functors]]
- [[foag_ 1.2.16|foag_Contravariant_functor]]
- [[foag_ 1.2.21|foag_Natural_transformations_of_functors]]
- [[foag_ 1.2.C|foag_Double_dual_functor_on_the_category_of_finite_dimensional_vector_spaces_is_naturally_isomorphic_to_the_identity_functor]]
- [[foag_ 1.2.22|foag_A_covariant_functor_is_an_equivalence_of_categories_if_it_is_fully_faithful_and_essentially_surjective]]
- [[foag_ 1.2.22|foag_essentially_surjective_functor]]
- [[foag_ 1.3.K|foag_Tensor_product_is_a_functor]]
 - [[foag_ 1.6.1|foag_additive_functor]]
 - [[foag_ 1.6.7|foag_Exact_functors]] - For additive functors of abelian categories
 - [[foag_ 6.2.D|foag_spectrum_of_rings_is_functorial]]
 - [[foag_ 16.3.D|foag_Pullback_on_schemes_gives_a_covariant_functor_on_the_quasicoherent_sheaves]] - An example
 - [[foag_ 16.3.7|foag_pullbacks_of_quasicoherent_sheaves_is_functorial]]
# Meta
## References
![[_reference_foag]]


## Citations and Footnotes
[^1]: Vakil,  1.2.11, Page 28