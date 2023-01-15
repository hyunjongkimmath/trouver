---
cssclass: clean-embeds
aliases: [poonen_curves_Zeta_function_of_a_variety_over_a_finite_field]
tags: [_meta/TODO/change_title, _meta/literature_note, _reference/poonen_curves, _meta/definition, _meta/notation]
---
# Zeta function of a variety over a finite field[^1]
Let $X$ be a [[poonen_curves_1.0.2 DEFINITION|variety]] over $\mathbb{F}_{q}$. 

Define

**$$\begin{aligned} Z_{X}(T):= & \prod_{\text {closed points } P \in X}\left(1-T^{\operatorname{deg} P}\right)^{-1} \quad \in \mathbb{Z}[[T]] \\ \zeta_{X}(s): &=Z_{X}\left(q^{-s}\right) \end{aligned}$$**

[^2]

[^2]: ![[poonen_curves_notation_deg_P_degree_of_closed_point]]

A priori, these are formal series, but in fact they converge for $|T|<1 / q^{d}$ and $\operatorname{Re} s>d$, respectively, where $d:=\operatorname{dim} X$ : see [[poonen_curves_ 3.6_page_56|Exercise 6]].


# See Also
- [[poonen_curves_notation_Z_X_T]]
- [[poonen_curves_notation_zeta_X_s_zeta_function_of_variety]]
# Meta
## References
![[_reference_poonen_curves]]

## Citations and Footnotes
[^1]: Poonen, 3.4.1 DEFINITION, Page 53