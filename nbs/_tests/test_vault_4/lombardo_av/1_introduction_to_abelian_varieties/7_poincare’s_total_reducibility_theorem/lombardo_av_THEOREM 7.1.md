---
cssclass: clean-embeds
aliases: [lombardo_av_Poincares_total_reducibility_theorem, lombardo_av_complement_to_a_subvariety_in_an_abelian_variety]
tags: [_auto/links_added, _meta/literature_note, _meta/permanent_note, _auto/notations_added, _meta/concept, _reference/lombardo_av, _meta/TODO/change_title, _meta/proof, _meta/definition]
---
# Poincare's total reducibility theorem[^1]
The following hold:
1. Let $A / K$ be an [[lombardo_av_1.3|abelian variety]] and let $B / K$ be an [[lombardo_av_DEFINITION 5.18#Abelian subvariety 1|abelian subvariety]] of $A / K$. There exists an [[lombardo_av_DEFINITION 5.18#Abelian subvariety 1|abelian subvariety]] $C$ of $A$, also defined over $K$, such that
$$
\begin{aligned}
B \times C & \rightarrow A \\
(b, c) & \mapsto b+c
\end{aligned}
$$
is an [[lombardo_av_DEFINITION 5.3|isogeny]]. The [[lombardo_av_DEFINITION 5.18#Abelian subvariety 1|subvariety]] $C$ is often called a **complement** to $B$ in $A$.

2. Let A/K be an [[lombardo_av_1.3|abelian variety]]. There exist $K$-[[18785_simple_ring|simple]] abelian $K$-subvarieties $A_{1}, \ldots, A_{n}$ of $A$ such that
$$
\begin{aligned}
A_{1} \times \cdots \times A_{n} & \rightarrow A \\
\left(a_{1}, \ldots, a_{n}\right) & \mapsto a_{1}+\cdots+a_{n}
\end{aligned}
$$
is an [[lombardo_av_DEFINITION 5.3|isogeny]].

# Proof sketch
SKETCH OF PROOF (FIELDS OF CHARACTERISTIC 0). 

The second statement follows from (1) by induction (and the fact that a [[foag_proper_morphism_of_schemes|proper]] [[lombardo_av_DEFINITION 5.18#Abelian subvariety 1|abelian subvariety]] of $A$ has strictly smaller dimension than $A)$. For $(1)$, fix an [[ample_line_bundle|ample line bundle]] $\mathcal{L}$ on $A$ and consider the [[lombardo_av_DEFINITION 5.1|homomorphism]] of [[lombardo_av_1.3|abelian varieties]]
$$
\varphi: A \stackrel{\lambda_{\mathcal{L}}}{\rightarrow} A^{\vee} \stackrel{i^{\vee}}{\rightarrow} B^{\vee}
$$
[^2][^3]
The [[connected_topological_space|connected]] component of the [[lombardo_av_DEFINITION 5.1|kernel]] of $\varphi$ passing through $0_{A}$ is a [[connected_topological_space|connected]], [[foag_proper_morphism_of_schemes|proper]] [[lombardo_av_REMARK 1.3|algebraic group]], hence an [[lombardo_av_1.3|abelian variety]] . Call it $C$. One has
$$
\operatorname{dim} C \geq \operatorname{dim} \operatorname{ker}\left(i^{\vee}\right) \geq \operatorname{dim}\left(A^{\vee}\right)-\operatorname{dim}\left(B^{\vee}\right)=\operatorname{dim}(A)-\operatorname{dim}(B)
$$
[^2]
We now show that $B$ and $C$ intersect in finitely many points: indeed $\left.\left(i^{\vee} \circ \lambda_{\mathcal{L}}\right)\right|_{B}=\lambda_{\left.\mathcal{L}\right|_{B}}$[^3]              , which is an [[lombardo_av_DEFINITION 5.3|isogeny]] $B \rightarrow B^{\vee}$ (hence has [[foag_finite_morphism_of_schemes|finite]] [[lombardo_av_DEFINITION 5.1|kernel]]) since $\left.\mathcal{L}\right|_{B}$ is ample. This implies that $B \times C \rightarrow A$ is a [[lombardo_av_DEFINITION 5.1|homomorphism]] of [[lombardo_av_1.3|abelian varieties]] with [[foag_finite_morphism_of_schemes|finite]] [[lombardo_av_DEFINITION 5.1|kernel]], hence dim $(B)+$ $\operatorname{dim}(C) \leq \operatorname{dim}(A) .$ Combined with our previous inequality, this yields $\operatorname{dim}(B)+\operatorname{dim}(C)=$ $\operatorname{dim}(A)$, and since $B \times C \stackrel{\pm}{\rightarrow} A$ has [[foag_finite_morphism_of_schemes|finite]] [[lombardo_av_DEFINITION 5.1|kernel]] it is an [[lombardo_av_DEFINITION 5.3|isogeny]].
6 since char $(K)=0$9. JACOBIANS
23

# See Also
- [[lombardo_av_REMARK 5.16|lombardo_av_category_of_abelian_varieties_up_to_isogeny_is_a_semisimple_category]]
- [[lombardo_av_EXERCISE 1.2|lombardo_av_Uniqueness_in_Poincares_theorem]]
- [[lombardo_av_EXERCISE 1.3|lombardo_av_Homomorphisms_of_abelian_varieties_go_in_both_directions]] - Exercise/application

# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, THEOREM 7.1, Page 22
[^2]: ![[lombardo_av_notation_A_vee_dual_abelian_variety]]
[^3]: ![[lombardo_av_notation_lambda_L]]