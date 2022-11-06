---
cssclass: clean-embeds
aliases: [foag_Natural_transformations_of_functors, foag_Equivalence_of_categories, foag_natural_isomorphism_of_functors]
tags: [_reference/foag, _meta/literature_note, _meta/definition]
---
# Natural transformations of functors[^1]
1.2.21. $\star$ Natural transformations (and natural isomorphisms) of covariant functors, and equivalences of categories.
(This notion won't come up in an essential way until at least Chapter 6, so you shouldn't read this section until then.) Suppose Fand $G$ are two covariant functors

30
The Rising Sea: Foundations of Algebraic Geometry
from $\mathscr{A}$ to $\mathscr{B}$. A **natural transformation of covariant functors** $\mathrm{F} \rightarrow \mathrm{G}$ is the data of a morphism $m_{A}: F(A) \rightarrow G(A)$ for each $A \in \mathscr{A}$ such that for each $f: A \rightarrow A^{\prime}$ in A, the diagram
commutes. A **natural isomorphism of functors** is a natural transformation such that each $m_{A}$ is an isomorphism. (We make analogous definitions when $F$ and $G$ are both contravariant.)

# Equivalence of categories
The data of functors $F: \mathscr{A} \rightarrow \mathscr{B}$ and $\mathrm{F}^{\prime}: \mathscr{B} \rightarrow \mathscr{A}$ such that $\mathrm{F} \circ \mathrm{F}^{\prime}$ is naturally isomorphic to the identity functor $i d_{s}$ on $\mathscr{B}$ and $\mathrm{F}^{\prime} \circ \mathrm{F}$ is naturally isomorphic to id $_{L f}$ is said to be an **equivalence of categories**. "Equivalence of categories" is an equivalence relation on categories. The right notion of when two categories are "essentially the same" is not isomorphism (a functor giving bijections of objects and morphisms) but equioalence. Exercises 1.2.C and 1.2.D might give you some vague sense of this. Later exercises (for example, that "rings" and "affine schemes" are essentially the same, once arrows are reversed, Exercise 6.3.D) may help too.

Two examples might make this strange concept more comprehensible. The double dual of a finite-dimensional vector space $V$ is not $\mathrm{V}$, but we learn early to say that it is canonically isomorphic to $\mathrm{V}$. We can make that precise as follows. Let f.d. $V e c_{k}$ be the category of finite-dimensional vector spaces over $k$. Note that this category contains oodles of vector spaces of each dimension.


# See Also
- [[foag_ 1.2.C|foag_Double_dual_functor_on_the_category_of_finite_dimensional_vector_spaces_is_naturally_isomorphic_to_the_identity_functor]]
- [[foag_ 1.2.22|foag_A_covariant_functor_is_an_equivalence_of_categories_if_it_is_fully_faithful_and_essentially_surjective]]
- [[foag_ 2.3.3|foag_Morphism_of_presheaves_is_a_natural_transformation]]
- [[foag_ 2.5.2|foag_There_is_an_equivalence_of_categories_between_sheaves_and_sheaves_on_a_base]] - Example of an equivalence of categories
- [[foag_ 6.3.D|foag_Category_of_rings_and_the_opposite_category_of_affine_schemes_are_equivalent]] - An example of equivalence of categories
# Meta
## References
![[_reference_foag]]


## Citations and Footnotes
[^1]: Vakil,  1.2.21, Page 29