---
cssclass: clean-embeds
aliases: [lombardo_av_Algebraic_morphism_of_abelian_varieties_is_the_composition_of_a_homomorphism_with_a_translation]
tags: [_reference/lombardo_av, _meta/literature_note, _auto/links_added, _meta/concept, _meta/proof, _meta/TODO/change_title]
---
# Algebraic morphism of [[lombardo_av_1.3|abelian varieties]] is the composition of a [[lombardo_av_DEFINITION 5.1|homomorphism]] with a translation [^1]
Let $f: A \rightarrow B$ be an [[fulton_it_ B.2.1|algebraic morphism]] of [[lombardo_av_1.3|abelian varieties]]. 

Then $f$ is the composition of a [[lombardo_av_DEFINITION 5.1|homomorphism]] with a translation.

# Proof
Replacing $f$ with $g(x)=f(x)-f(0)$, we are [[foag_reduced_scheme|reduced]] to showing that an [[fulton_it_ B.2.1|algebraic morphism]] $g: A \rightarrow B$ such that $f\left(0_{A}\right)=0_{B}$ is a [[lombardo_av_DEFINITION 5.1|homomorphism]] of [[lombardo_av_1.3|abelian varieties]]. Consider the map
$$
\varphi: \begin{array}{lll}
A \times A & \rightarrow & B \\
\left(a_{1}, a_{2}\right) & \mapsto & g\left(a_{1}\right)+g\left(a_{2}\right)-g\left(a_{1}+a_{2}\right):
\end{array}
$$
by the [[lombardo_av_LEMMA 1.8|rigidity lemma]], noticing that $\varphi\left(\left\{0_{A}\right\} \times A\right)=\varphi\left(A \times\left\{0_{A}\right\}\right)=\left\{0_{B}\right\}$, we obtain that $\varphi(A \times A)=\left\{0_{B}\right\}$, that is, $g\left(a_{1}\right)+g\left(a_{2}\right)=g\left(a_{1}+a_{2}\right)$ as desired.

# See Also
- [[lombardo_av_EXERCISE 1.1|lombardo_av_Alternate_proof_that_abelian_varieties_are_commutative]] - Application
# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, PROPOSITION 1.9, Page 9
