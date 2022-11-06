---
cssclass: clean-embeds
aliases: [lombardo_av_dual_abelian_variety]
tags: [_meta/notation, _meta/TODO/change_title, _meta/literature_note, _meta/definition, _reference/lombardo_av]
---
# Dual abelian variety[^1]

Let $A/K$ be an abelian variety.

A pair $\left(A^{\vee}, \mathcal{P}\right)$, where $A^{\vee}$ is an [[lombardo_av_1.3|abelian variety]] and $\mathcal{P}$ is a [[foag_locally_free_sheaf_on_a_scheme#invertible sheaf 2|line bundle]] on $A \times A^{\vee}$, is a (the) **dual abelian variety** of $A$ if the following holds:
1. $\left.\mathcal{P}\right|_{A \times\{b\}}$ is in $\operatorname{Pic}^{0}\left(A_{b}\right)$[^2]
2. $\left.\mathcal{P}\right|_{\{0\} \times A^{\vee}}$ is trivial
3. $\left(A^{\vee}, \mathcal{P}\right)$ is universal among such pairs, that is, the following universal property holds: for all pairs $(T, \mathcal{L})$ consisting of a variety and an invertible sheaf $\mathcal{L}$ on $A \times T$ that satisfies

	1. $\left.\mathcal{L}\right|_{A \times\{t\}}$ is in $\operatorname{Pic}^{0}\left(A_{t}\right)$
	2. $\mathcal{L} \mid\{0\} \times T$ is trivial	

	there is a unique regular map $\alpha: T \rightarrow A^{\vee}$ such that $\mathcal{L} \cong(1 \times \alpha)^{*} \mathcal{P}$.

[^2]: ![[lombardo_av_notation_Pic_0_A]]

# See Also
- [[lombardo_av_notation_A_vee_dual_abelian_variety]]
- [[lombardo_av_REMARK 6.2|lombardo_av_Dual_varieties_exist]]
- [[lombardo_av_REMARK 6.3]]
- [[lombardo_av_DEFINITION 6.4]]
# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, DEFINITION 6.1, Page 19