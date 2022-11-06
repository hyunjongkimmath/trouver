---
cssclass: clean-embeds
aliases: [lombardo_av_weil_pairing]
tags: [_auto/notations_added, _meta/literature_note, _reference/lombardo_av, _meta/TODO/change_title, _meta/notation, _meta/definition]
---
# Weil pairing of an abelian variety[^1]

Let $A/K$ be an [[lombardo_av_1.3|abelian variety]].

For every $n$ there is a canonical pairing
$$
e_{n}: A[n] \times A^{\vee}[n] \rightarrow \mathbb{G}_{m}[n]=\mu_{n}
$$
[^2][^3][^4][^5][^6]
defined as follows. 

Let $t \in A[n]$[^2][^3][^4] and $\mathcal{L} \in A^{\vee}[n]$[^4][^5]              . By definition we have $n t=0$ and $\mathcal{L}^{\otimes} n \cong \mathcal{O}$. An application of the theorem of the cube gives $[n]^{*} \mathcal{L} \cong \mathcal{L}^{\otimes n} \cong \mathcal{O}$[^4]              , so we may fix an isomorphism $u: \mathcal{O} \rightarrow[n]^{*} \mathcal{L} .$[^4]               Denote by $\tau_{t}: A \rightarrow A$ the morphism translation-by-t. Pulling back the isomorphism $u: \mathcal{O} \rightarrow[n]^{*} \mathcal{L}$[^4]               via $\tau_{t}$ we obtain
$$
\tau_{t}^{*} u: \tau_{t}^{*} \mathcal{O} \rightarrow \tau_{t}^{*}[n]^{*} \mathcal{L} \cong\left([n] \circ \tau_{t}\right)^{*} \mathcal{L}=[n]^{*} \mathcal{L}
$$
[^4]
Recalling that $\tau_{t}^{*} \mathcal{O}=\mathcal{O}$, it follows in particular that $u \circ\left(\tau_{t}^{*} u\right)^{-1}$ is an isomorphism of $[n]^{*} \mathcal{L}$[^4]              ; an automorphism of a line bundle on the complete variety A can only be multiplication by an element $\zeta$ of $H^{0}\left(A_{K}, \mathcal{O}^{\times}\right)=\bar{K}^{\times}$, and we define e $_{n}(t, \mathcal{L})=\zeta .$ It is clear from the definition that
$$
1=e_{n}(n t, \mathcal{L})=e_{n}(t, \mathcal{L})^{n}=\zeta^{n}
$$
[^6]
so $\zeta$ is in fact an $n$-th root of unity.

# See Also
- [[lombardo_av_notation_e_n_weil_pairing]]
- [[lombardo_av_REMARK 6.16]]
- [[lombardo_av_THEOREM 6.17]]
- [[lombardo_av_REMARK 10.11|lombardo_av_ell_adic_weil_pairing]]
# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, DEFINITION 6.15, Page 21
[^2]: ![[lombardo_av_notation_A_n_complex]]
[^3]: ![[lombardo_av_notation_A_n_general]]
[^4]: ![[lombardo_av_notation_brackets_n]]
[^5]: ![[lombardo_av_notation_A_vee_dual_abelian_variety]]
[^6]: ![[lombardo_av_notation_e_n_weil_pairing]]