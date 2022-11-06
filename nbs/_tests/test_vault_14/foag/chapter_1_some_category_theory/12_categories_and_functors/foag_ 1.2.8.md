---
cssclass: clean-embeds
aliases: [foag_Partially_ordered_sets, foag_poset]
tags: [_reference/foag, _meta/literature_note, _meta/definition, _meta/example]
---
# Partially ordered sets[^1]
1.2.8. Example: partially ordered sets. A **partially ordered set**, (or **poset**), is a set $S$ along with a binary relation $\geq$ on S satisfying:
(i) $x \geq x$ (reflexivity),
(ii) $x \geq y$ and $y \geq z$ imply $x \geq z$ (transitivity), and
(iii) if $x \geq y$ and $y \geq x$ then $x=y$ (antisymmetry).
A partially ordered set $(S, \geq)$ can be interpreted as a category whose objects are the elements of $S$, and with a single morphism from $x$ to $y$ if and only if $x \geq y$ (and no morphism otherwise).

A trivial example is $(S, \geq)$ whene $x \geq y$ if and only if $x=y .$ Another example is
$(1.2 .8 .1)$
Here there are three objects. The identity morphisms are omitted for convenience, and the two non-identity morphisms are depicted. A third example is
$(1.2 .8 .2)$
Here the "obvious" morphisms are again omitted: the identity morphisms, and the morphism from the upper left to the lower right. Similarly,
depicts a partially ordered set, where again, only the "generating morphisms" are depicted.

28
The Rising Sea: Foundations of Algebraic Geometry


# See Also
- [[foag_ 1.4.A|foag_Limits_of_diagrams_indexed_by_a_partially_ordered_set_with_initial_object_exist]]
- [[foag_ 1.4.7|foag_Filtered_set]]
# Meta
## References
![[_reference_foag]]


## Citations and Footnotes
[^1]: Vakil,  1.2.8, Page 27