---
cssclass: clean-embeds
aliases: [lombardo_av_analytic_uniformization_of_complex_abelian_varieties]
tags: [_reference/lombardo_av, _meta/literature_note, _auto/links_added, _meta/concept, _meta/proof, _meta/TODO/change_title]
---
# Analytic uniformization of complex abelian varieties[^1]
Let $A$ be a $g$ dimensional [[lombardo_av_1.3|abelian variety]] over the complex numbers. 

Then there exists a [[18785_Definition 5.9|lattice]] $\Lambda \subseteq \mathbb{C}^{g}$ such that $A(\mathbb{C})$ is isomorphic (as a Lie group) to $\mathbb{C}^{g} / \Lambda$.

# Proof

PROOF. Write $V=T_{0} A$ for the tangent space at identity. From the differential geometry of Lie groups we know that for every $v \in V$ there is a unique analytic group [[lombardo_av_DEFINITION 5.1|homomorphism]]
$$
\varphi_{v}: \mathbb{C} \rightarrow A
$$
with $d \varphi_{v}(0)=v .$ One knows that $\varphi: V \times \mathbb{C} \rightarrow A$ is analytic. The exponential map is
$$
\begin{aligned}
\exp : & \rightarrow A \\
v & \mapsto \varphi_{v}(1)
\end{aligned}
$$
It is clear that $\varphi_{v}(t)=\exp (t v)$ (by uniqueness of $\varphi_{v}$ we have $\varphi_{v}(s t)=\varphi_{t v}(s)$, so the formula follows setting $s=1) .$ Moreover, exp : $V \rightarrow A$ is a group [[lombardo_av_DEFINITION 5.1|homomorphism]]: indeed
$$
t \mapsto \exp (t x) \exp (t y)
$$
is a group [[lombardo_av_DEFINITION 5.1|homomorphism]] (because $A$ is abelian); taking the derivative at 0 and using the uniqueness of $\varphi_{x+y}$ we obtain $\exp (t x) \exp (t y)=\exp (t(x+y))$ as claimed. Finally, exp is surjective because $\exp (V)$ is a subgroup of $A(\mathbb{C})$ that contains a neighbourhood of the12
1. INTRODUCTION TO ABELIAN VARIETIES
identity (and $A$ is [[connected_topological_space|connected]]). Now define $\Lambda$ to be the [[lombardo_av_DEFINITION 5.1|kernel]] of exp: on the one hand it is discrete, because exp is a local homeomorphism, and on the other $\Lambda$ must have full rank since $\mathbb{C}^{g} / \Lambda \cong A$ is compact.


# See Also
- [[lombardo_av_DEFINITION 4.2|lombardo_av_complex_torus]]
- [[lombardo_av_REMARK 4.3|lombardo_av_Not_every_complex_torus_is_an_abelian_variety]]
- [[lombardo_av_THEOREM 2.10|lombardo_av_Tates_conjecture]]
	- [[lombardo_av_REMARK 2.12|lombardo_av_Tates_theorem_is_an_analogue_to_analytic_uniformization]]
# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, THEOREM 4.1, Page 11
