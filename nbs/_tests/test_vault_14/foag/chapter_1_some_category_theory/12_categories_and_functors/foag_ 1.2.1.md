---
cssclass: clean-embeds
aliases: [foag_Category, foag_Morphism_in_a_category, foag_Isomorphism_in_a_category, foag_object_in_a_category, foag_arrow_in_a_category, foag_map_in_a_category, foag_source_of_a_morphism_in_a_category, foag_target_of_a_morphism_in_a_category, foag_identity_morphism_in_a_category, foag_automorphism_in_a_category]
tags: [_reference/foag, _meta/literature_note, _meta/notation, _meta/definition]
---
# Categories[^1]
1.2.1. Categories.

# Category
26
The Rising Sea: Foundations of Algebraic Geometry
A **category** consists of a collection of **objects**, and for each pair of objects, a set of **morphisms** (or **arrows**) between them. (For experts: technically, this is the definition of a locally small category. In the correct definition, the morphisms need only form a class, not necessarily a set, but see Caution 0.3.1.) Morphisms are often informally called **maps**. The collection of objects of a category $\mathscr{C}$ is often denoted **$\operatorname{obj}(\mathscr{b})$**, but we will usually denote the collection also by **$\mathscr{C} .$** If $A, B \in \mathscr{C}$, then the set of morphisms from $A$ to $B$ is denoted **$\operatorname{Mor}(A, B) .$** A morphism is often written **$f: A \rightarrow B$**, and $A$ is said to be the **source of $f$**, and $B$ the **target of $f$**. (Of course, Mor $(A, B)$ is taken to be disjoint from $\operatorname{Mor}\left(A^{\prime}, B^{\prime}\right)$ unless $A=A^{\prime}$ and $\left.B=B^{\prime} .\right)$

# Morphism in a category
Morphisms compose as expected: there is a composition Mor $(B, C) \times$ Mor $(A, B)-$ Mor $(A, C)$, and if $f \in \operatorname{Mor}(A, B)$ and $g \in \operatorname{Mor}(B, C)$, then their composition is denoted $g \circ$ f. Composition is associative: if $f \in \operatorname{Mor}(A, B), g \in \operatorname{Mor}(B, C)$, and $\mathrm{h} \in \operatorname{Mor}(\mathrm{C}, \mathrm{D})$, then ho $(\mathrm{g} \circ \mathrm{f})=(\mathrm{h} \circ g) \circ \mathrm{f}$. For each object $A \in \mathscr{E}$, there is always an **identity morphism** **$\operatorname{id}_{A}: A \rightarrow A$**, such that when you (left-or right-)compose a morphism with the identity, you get the same morphism. More precisely, for any morphisms $f: A \rightarrow B$ and $g: B \rightarrow C$, id $_{B} \circ f=f$ and $g \circ i d_{B}=g .$ (If you wish, you may check that"identity morphisms are unique": there is only one morphism deserving the name id $_{A}$.) This ends the definition of a category.

## Isomorphism in a category
We have a notion of **isomorphism** between two objects of a category (a morphism $\mathrm{f}: \mathrm{A} \rightarrow \mathrm{B}$ such that there exists some - necessarily unique - morphism $g: B \rightarrow A$, where $f \circ g$ and $g \circ f$ are the identity on $B$ and $A$ respectively), and a notion of **automorphism** of an object (an isomorphism of the object with itself).


# See Also
- [[foag_notation_obj_b]]
- [[foag_notation_C_]]
- [[foag_notation_Mor_A__B_]]
- [[foag_notation_f_A_arrow_B]]
- [[foag_notation_id_A_A_arrow_A]]
- [[foag_ 1.2.2|foag_Category_of_setes]]
- [[foag_ 1.2.3|foag_Category_of_vector_spaces_over_a_field]]
- [[foag_ 1.2.A|foag_Groupoid]]
- [[foag_ 1.2.B|foag_Automorphism_group_of_an_object_in_a_cateo]]
- [[foag_ 1.2.4|foag_Category_of_abelian_groups]]
- [[foag_ 1.2.5|foag_Category_of_modules_over_a_ring]]
- [[foag_ 1.2.6|foag_Category_of_rings]]
- [[foag_page_27|foag_Concrete_category]]
- [[foag_ 1.2.8|foag_Partially_ordered_sets]]
- [[foag_ 1.2.9|foag_Category_of_open_subsets_of_a_topological_space]]
- [[foag_ 1.2.9|foag_Category_of_open_subsets_of_a_topological_space]]
- [[foag_ 1.2.11|foag_Covariant_functor]]
- [[foag_ 1.2.16|foag_Contravariant_functor]]
- [[foag_ 1.2.21|foag_Equivalence_of_categories]]
- [[foag_ 1.6.1|foag_Additive_category]]
	- [[foag_ 1.6.1|foag_homomorphism_in_an_additive_category]]
- [[foag_ 6.3.3|foag_category_of_schemes]]
- [[foag_ 6.6.4|foag_Group_object_in_a_category]]
# Meta
## References
![[_reference_foag]]


## Citations and Footnotes
[^1]: Vakil,  1.2.1, Page 25

