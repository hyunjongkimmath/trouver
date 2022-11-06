---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]
\begin{lemma}
\label{lem: thread the needle}
Suppose that $\mathcal{O}_S = W$ in Construction~\ref{constr: curves dominating moduli of ES}. For a general $k$-point $t \in T_k$, $\overline{\varphi}_t$ has the following properties: 
\begin{enumerate}[label=\upshape{(\alph*)}]
    \item $\overline{\varphi}_t(\infty) \not\in \overline{\mathfrak{D}}_k$, the total space of the family $\overline{\varphi}^*_t(\mathcal{X}) \to \mathbb{P}^1_k$ is smooth and every fiber has at most a single ODP singulariety. 
    \item $\overline{\varphi}^*_t(\overline{\mathfrak{D}}_k)$ is reduced. Moreover, there exists a dense analytically open subset $Q$ of the disk of all $W$-liftings of $t$ on $T$ such that for any $\widetilde{t} \in Q$, $\overline{\varphi}^*_{\widetilde{t}}(\overline{\mathfrak{D}})$ is finite \'etale over $S$. 
\end{enumerate}
\end{lemma}
\begin{proof}
If $\mathrm{codim\,} \mathfrak{D}_k \le 2$, then for a general $t \in T(k)$, we in fact have $\varphi^*_t(\mathfrak{D}_k) = \emptyset$ and the family $\overline{\varphi}^*_t(\mathcal{X}) \to \mathbb{P}^1_k$ is smooth. So we only need to treat the case when $\mathrm{codim\,} \mathfrak{D}_k = 1$. For a general $k$-point $t \in T_k$, (a) follows from Prop.~\ref{prop: strongly dominates smooth total family} and Prop.~\ref{prop: (4, 6) curve strongly dominates}, so we only need to prove (b). 


Let $\mathfrak{D}_{K}^\circ$ and $\mathfrak{D}_k^\circ$ be the irreducible components of maximal dimension of $\mathfrak{D}_{K}$ and $(\mathfrak{D}_k)_{\mathrm{red}}$ respectively. Let $\mathfrak{D}_0, \cdots, \mathfrak{D}_r$ be the irreducible components of $\mathfrak{D}$ such that $\mathfrak{D}_0$ is the component which contains $\mathfrak{D}_{K}^\circ$. We claim that $\mathfrak{D}_0$ contains $\mathfrak{D}^\circ_k$ as well. Let us write $\mathbb{A}(\mathcal{V}_4 \oplus \mathcal{V}_6)$ as $\mathscr{A}$. Then $\mathfrak{D}_{0, K} \subseteq \mathscr{A}_K^*$ is cut out by a single polynomial $F$ in the coordinates of the affine space $\mathscr{A}_K$. By minimally clearing denominators, we may assume that the coefficients of $F$ are defined in $W$ and generate $W$. Using the fact that $\mathscr{A}$ is affine and $\mathcal{O}_{\mathscr{A}}$ is a UFD, one checks that the Zariski closure of $\mathfrak{D}_{0, K}$ in $\mathscr{A}$ contains the vanishing locus $V(F)$ of $F \in \mathcal{O}_{\mathscr{A}}$. Note that $F$ is weighted-homogeneous, so $V(F)_k \subseteq \mathscr{A}_k$ at least contains the origin. In paricular, $V(F) \to S$ is surjective. By \cite[Tag~0B2J]{stacks-project}, $\dim V(F)_k = \dim V(F)_K$. This implies that $\dim \mathfrak{D}_{0, k} = \dim \mathfrak{D}_{0, K}$. By the uniqueness of $\mathfrak{D}_k^\circ$ as an irreducible component of maximal dimension, we conclude that $\mathfrak{D}_k^\circ \subseteq \mathfrak{D}_0$. By applying \cite[Tag~0B2J]{stacks-project} again, we also conclude that for any $i > 0$, $\mathfrak{D}_{i, k}$ has codimension $\ge 2$ in $\mathscr{A}^*_k$. 


Set $U \subseteq \mathfrak{D}_0$ be the complement of the closed subscheme $\cup_{i > 1} (\mathfrak{D}_0 \cap \mathfrak{D}_i)$. Then $(U_k)_{\mathrm{red}}$ is dense in $\mathfrak{D}_{k}^\circ$. As $t$ is general, we may assume that the intersection $\mathrm{im}(\varphi_t) \cap (\mathfrak{D}_k)_{\mathrm{red}}$ is transverse and lies in $U_k$. For any $\widetilde{t} \in T(W)$ lifting $t$, we claim that $\varphi^*_{\widetilde{t}}(\mathfrak{D})$ is flat over $W$. Indeed, note that $\mathfrak{D}_0$ is a Weil divisor, and hence also a Cartier divisor of $\mathscr{A}^*$, as $\mathscr{A}^*$ is regular. This implies that $Z \coloneqq \varphi^*_{\widetilde{t}}(\mathfrak{D}) = \varphi^*_{\widetilde{t}}(U) = \varphi^*_{\widetilde{t}}(\mathfrak{D}_0)$ is everywhere locally cut out in $\mathbb{P}^1_W$ by a single equation. Since $Z_k \subseteq \mathbb{P}^1_k$ is of codimension $1$, $Z$ is flat over $W$ by \cite[Tag~00MF]{stacks-project}.

The flatness of $Z/W$ implies that $Z_k$ is reduced if and only if we have an equality of number of points $\# Z_k(k) = \# Z_{\bar{K}}(\bar{K})$. Note that it suffices to check this for any $\widetilde{t}$ lifting $t$. By Lem.~\ref{lem: FAP for curves}, we may choose $\widetilde{t}$ such that properties (a) and (b) are true for $\widetilde{t} {\otimes} \bar{K}$ as well. By combining the Leray spectral sequence and the Grothendieck-Ogg-Shafarevich formula, we have 
\begin{equation}
    \chi(\overline{\varphi}_t^*(\mathcal{X})) = \chi(\mathcal{X}_{\overline{\eta}(\mathbb{P}^1_k)}) \chi(\mathbb{P}^1_k) + \sum_{z \in Z_k(k)} \left( \chi(\mathcal{X}_{z}) - \chi(\mathcal{X}_{\overline{\eta}(\mathbb{P}^1_k)}) - \mathrm{sw}_z(\mathrm{H}_\mathrm{{\acute{e}}t}^*(\mathcal{X}_{\overline{\eta}(\mathbb{P}^1_k)}, \mathbb{Q}_\ell)) \right)
\end{equation}
where $\mathrm{sw}_z(\mathrm{H}_\mathrm{{\acute{e}}t}^*(\mathcal{X}_{\overline{\eta}(\mathbb{P}^1_k)}, \mathbb{Q}_\ell))$ denotes the alternating sum of Swan conductors 
$$ \mathrm{sw}_z(\mathrm{H}_\mathrm{{\acute{e}}t}^*(\mathcal{X}_{\overline{\eta}(\mathbb{P}^1_k)}, \mathbb{Q}_\ell)) \coloneqq \sum_{i = 0}^4 (-1)^i  \mathrm{sw}_z(\mathrm{H}_\mathrm{{\acute{e}}t}^i(\mathcal{X}_{\overline{\eta}(\mathbb{P}^1_k)}, \mathbb{Q}_\ell)).  $$
Since for every $z \in Z_k(k)$, $\mathcal{X}_z$ is smooth away from an ODP, \cite[\S4.2]{WeilI} tells us that the local monodromy action on $\mathrm{H}_\mathrm{{\acute{e}}t}^*(\mathcal{X}_{\overline{\eta}(\mathbb{P}^1_k)}, \mathbb{Q}_\ell)$ factors through $\mathbb{Z} / 2 \mathbb{Z}$ and hence is tamely ramified as $p \neq 2$. This implies that the Swan conductors all vanish. Moreover, by \textit{loc. cit.} we also know that $\chi(\mathcal{X}_{z}) - \chi(\mathcal{X}_{\overline{\eta}(\mathbb{P}^1_k)}) = -1$, so
\begin{equation}
    \label{eqn: number of singular fibers}
    \# Z_k(k) = \chi(\mathcal{X}_{\overline{\eta}(\mathbb{P}^1_k)}) \chi(\mathbb{P}^1_k) - \chi(\overline{\varphi}_t^*(\mathcal{X})).
\end{equation}
The above is true verbatim when $t$ (resp. $k$) is replaced by $\widetilde{t} {\otimes} \bar{K}$ (resp. $\bar{K}$), and the RHS of the above equation remains unchanged by the smooth and proper base change theorem for \'etale cohomology. We may then conclude that $\# Z_k(k) = \# Z_{\bar{K}}(\bar{K})$ as desired. 
\end{proof}

# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, lemma 8.9