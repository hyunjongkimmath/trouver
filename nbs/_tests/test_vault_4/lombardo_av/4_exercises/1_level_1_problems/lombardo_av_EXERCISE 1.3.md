---
cssclass: clean-embeds
aliases: [lombardo_av_Homomorphisms_of_abelian_varieties_go_in_both_directions]
tags: [_reference/lombardo_av, _meta/literature_note, _auto/links_added, _meta/TODO/change_title, _meta/example, _meta/exercise, _meta/proof]
---
# Homomorphisms of abelian varieties go in both directions[^1]
Let $A \rightarrow B$ be a surjective [[lombardo_av_DEFINITION 5.1|homomorphism]] of [[lombardo_av_1.3|abelian varieties]]. 

Prove that $B$ is [[lombardo_av_DEFINITION 5.13|isogenous]] to a [[lombardo_av_DEFINITION 5.18#Abelian subvariety 1|subvariety]] of $A$.

Let $A \rightarrow B$ be an injective [[lombardo_av_DEFINITION 5.1|homomorphism]]: prove that there is a surjective [[lombardo_av_DEFINITION 5.1|homomorphism]] $B \rightarrow A$ (hence, up to [[lombardo_av_DEFINITION 5.3|isogeny]], "homomorphisms of [[lombardo_av_1.3|abelian varieties]] go in both directions").

# Proof
Suppose that $f: A \to B$ is a surjective homomorphism of abelian varieties. In particular, $\ker f$[^2] is an abelian subvariety of $A$, in which case [[lombardo_av_THEOREM 7.1|Poincare's theorem]] shows that there is an abelian subvariety $C$ of $A$ such that $\ker f \times C \to A, \quad (a,b) \mapsto a+b$ is an [[lombardo_av_DEFINITION 5.3|isogeny]]. Composing this isogeny with $f$ yields a surjective homomorphism $\ker f \times C \to B$. Note that $\ker f$ maps to $0$ under this homomorphism, so the homomorphism is tantamount to a surjective homomorphism $C \to B$.

To show that this surjective homomorphism is an isogeny, [[lombardo_av_PROPOSITION 5.5|it suffices]] to show that $\dim B = \dim C$. Note that $\dim \ker f + \dim C = \dim A$ since we have an isogeny $\ker f \times C \to A$. Moreover, $\dim \ker f + \dim B = \dim A$ because $f: A \to B$ is a surjective homomorphism. Thus, $\dim C = \dim B$ as desired.

#_meta/TODO show that kernel is abelian subvariety

#_meta/TODO show that some kind of rank-nullity theorem holds for fibers of flat morphisms.

[^2]: ![[lombardo_av_notation_ker_f_kernel_of_group_scheme_homomorphism]]


Now suppose that $f: A \to B$ is an injective homomorphism of abelian varieties. In particular, $A$ is (isomorphic to) an abelian subvariety of $B$. There [[lombardo_av_THEOREM 7.1|is thus]] an abelian subvariety $C$ of $A$ such that $A \times C \to B$ is an isogeny. Since [[lombardo_av_REMARK 5.14|isogenies are equivalence relations]], there is an isogeny $B \to A \times C$ and hence. In particular, such an isogeny [[lombardo_av_PROPOSITION 5.5|is]] surjective, so the induced homomorphism $B \to A$ is also surjective.

# See Also

# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, EXERCISE 1.3, Page 63