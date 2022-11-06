---
cssclass: clean-embeds
aliases: [foag_Functor_of_points_is_an_example_of_a_contravariant_functor]
tags: [_meta/example, _reference/foag, _meta/literature_note, _meta/definition, _meta/notation]
---
# Functor of points is an example of a contravariant functor[^1]
1.2.20. Example (the functor of points, of. Example 1.2.14). Suppose $A$ is an object of a category $\mathscr{C}$. Then there is a contravariant functor **$\mathrm{h}_{\mathrm{A}}: \mathscr{C} \rightarrow$** Sets sending $\mathrm{B} \in \mathscr{C}$ to Mor $(\mathrm{B}, \mathrm{A})$, and sending the morphism $\mathrm{f}: \mathrm{B}_{1} \rightarrow \mathrm{B}_{2}$ to the morphism $\operatorname{Mor}\left(\mathrm{B}_{2}, \mathrm{~A}\right) \rightarrow \operatorname{Mor}\left(\mathrm{B}_{1}, \mathrm{~A}\right)$ via
$$
\left[g: B_{2} \rightarrow A\right] \mapsto\left[g \circ f: B_{1} \rightarrow B_{2} \rightarrow A\right]
$$
This example initially looks weird and different, but Examples 1.2.17 and 1.2.19 may be interpreted as special cases; do you see how? What is $A$ in each case? This functor might reasonably be called the functor of maps (to $\mathrm{A}$ ), but is actually known as the **functor of points**. We will meet this functor again in $\1.3.10 and (in the category of schemes) in Definition 6.3.9


# See Also
- [[foag_notation_h_A_C_arrow]]
- [[foag_ 1.3.10]]
- [[foag_ 1.3.Y|foag_Yonedas_lemma]]
- [[foag_ 6.3.10|foag_Functor_of_scheme_valued_points]]
# Meta
## References
![[_reference_foag]]


## Citations and Footnotes
[^1]: Vakil,  1.2.20, Page 29