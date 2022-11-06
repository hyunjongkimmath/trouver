---
cssclass: clean-embeds
aliases: [foag_Composition_of_functors, foag_Full_and_faithful_functors, foag_full_functor, foag_faithful_functor, foag_fully_faithful_functor, foag_full_subcategory_of_a_category]
tags: [_meta/definition, _reference/foag, _meta/literature_note, _meta/notation]
---
# Composition of functors[^1]
1.2.15. Definitions. If $\mathrm{F}: \mathscr{A} \rightarrow \mathscr{B}$ and $\mathrm{G}: \mathscr{B} \rightarrow \mathscr{C}$ are covariant functors, then we define a functor **$G \circ F: \mathscr{A} \rightarrow \mathscr{E}$** (the **composition of $\mathrm{G}$ and $\mathrm{F}$** ) in the obvious way. Composition of functors is associative in an evident sense.

# Full and faithful functors
November 18, 2017 draft
29
A covariant functor $F: \mathscr{A} \rightarrow \mathscr{B}$ is **faithful** if for all $A, A^{\prime} \in \mathscr{A}$, the map $\operatorname{Mor}_{\mathscr{A}}\left(\mathrm{A}, \mathrm{A}^{\prime}\right) \rightarrow \operatorname{Mor}_{\mathscr{B}}\left(\mathrm{F}(\mathrm{A}), \mathrm{F}\left(\mathrm{A}^{\prime}\right)\right)$ is injective, and **full** if it is surjective. A functor that is full and faithful is **fully faithful**. A subcategory $i: \mathscr{A} \rightarrow \mathscr{B}$ is a **full subcategory** if $i$ is full. (Inclusions are always faithful, so there is no need for the phrase "faithful subcategory".) Thus a subcategory $\mathscr{A}^{\prime}$ of $\mathscr{A}$ is full if and only if for all $A, B \in \operatorname{obj}\left(\mathscr{A}^{\prime}\right), \operatorname{Mor}_{A^{\prime}}(A, B)=$ Mor $_{\Delta}(A, B) .$ For example, the forgetful functor $V e c_{k} \rightarrow$ Sets is faithful, but not full; and if $A$ is a ring, the category of finitely generated A-modules is a full subcategory of the category Mod $_{\mathrm{A}}$ of A-modules.


# See Also
- [[foag_notation_G_circ_F_A_arrow_E]]
- [[foag_ 1.3.Z|foag_yoneda_embedding]] - Is a fully faithful functor
# Meta
## References
![[_reference_foag]]


## Citations and Footnotes
[^1]: Vakil,  1.2.15, Page 28