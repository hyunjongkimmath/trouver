---
cssclass: clean-embeds
aliases: []
tags: [_reference/lombardo_av, _meta/literature_note, _meta/TODO/change_title, _auto/links_added, _meta/remark, _meta/TODO/split, _meta/narrative]
---
# Topic[^1]
REMARK 6.6 (Number of $\mathbb{F}_{q}$-rational points of the [[lombardo_av_THEOREM 9.16|Jacobian]]). If we are interested in the arithmetic of the [[lombardo_av_THEOREM 9.16|Jacobian]] itself (rather than the arithmetic of $C$ ), another formula which often comes in handy is the equality
$$
\# \operatorname{Jac}(C)\left(\mathbb{F}_{q}\right)=P_{C}(1)
$$
The quickest proof of this equality I know goes through the Lefschetz trace formula: the number of fixed points of [[lombardo_av_DEFINITION 5.4|Frobenius]] is equal to the alternating sum of traces of Frob on $H_{e t}^{i}\left(J, Q_{\ell}\right)$, that is,
$$
\begin{aligned}
\# J\left(\mathbb{F}_{q}\right) &=\# J\left(\overline{\mathbb{F}_{q}}\right)^{\text {Frob }} \\
&=\sum_{i=0}^{2 g}(-1)^{i} \operatorname{tr}\left(\operatorname{Frob} \mid H_{e ́ t}^{i}\left(J, \mathbb{Q}_{\ell}\right)\right) \\
&=\sum_{i=0}^{2 g}(-1)^{i} \operatorname{tr}\left(\text { Frob } \mid \Lambda^{i} H_{e t}^{1}\left(J, \mathbb{Q}_{\ell}\right)\right) \\
&=\sum_{i=0}^{2 g}(-1)^{i} \sum_{H \subseteq\{1, \ldots, 2 g\} \atop|H|=i} \prod_{h \in H} \alpha_{h} \\
&=P_{C}(1) .
\end{aligned}
$$
7. Torsion in the [[lombardo_av_THEOREM 9.16|Jacobian]]
We may now ask a very concrete computational question:
QUESTION 7.1. Let $C / \mathbb{Q}$ be a [[lombardo_av_1.1|nice curve]] of genus $g$ with [[lombardo_av_THEOREM 9.16|Jacobian]] J. How does one compute the torsion of $J(\mathbb{Q})$ ?

To my knowledge, the answer is fully known only for $g \leq 2$, and work is being done on the $g=3$ case. The reason for these restrictions is described in the following remark:


# See Also

# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, REMARK 6.6, Page 50
