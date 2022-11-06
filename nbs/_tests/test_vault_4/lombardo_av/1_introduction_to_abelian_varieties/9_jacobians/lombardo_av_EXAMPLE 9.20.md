---
cssclass: clean-embeds
aliases: [lombardo_av_An_elliptic_curve_is_its_own_Jacobian]
tags: [_auto/notations_added, _auto/links_added, _meta/example, _meta/literature_note, _reference/lombardo_av, _meta/TODO/change_title]
---
# An elliptic [[foag_11.1.3|curve]] is its own [[lombardo_av_THEOREM 9.16|Jacobian]][^1]
EXAMPLE 9.20 (An elliptic [[foag_11.1.3|curve]] is its own [[lombardo_av_THEOREM 9.16|Jacobian]]). Let $E / K$ be an elliptic [[foag_11.1.3|curve]]. We shall show that $E$ is isomorphic to its [[lombardo_av_THEOREM 9.16|Jacobian]] variety by using the classical construction of the group law on an elliptic [[foag_11.1.3|curve]].

We claim that any [[lombardo_av_DEFINITION 9.1|divisor]] of [[degree_of_an_algebraic_field_extension|degree]] 0 on $E$ is [[lombardo_av_DEFINITION 9.9|linearly equivalent]] to a [[lombardo_av_DEFINITION 9.1|divisor]] of the form $P-O$, where $O$ is the origin of the group law on $E$ and $P$ is a point on $E .$ To see this, embed $E$ as a plane cubic in $\mathbb{P}^{2}$ (with the origin of the group law being the point $[0: 1: 0]$ ). Now any line different from the line at infinity meets $E$ at three points $P_{1}, P_{2}, P_{3}$ in the affine plane; the [[lombardo_av_DEFINITION 9.1|divisor]] of such a line is therefore $P_{1}+P_{2}+P_{3}-3 O$. Now fix two points $P$, $Q$ lying in the affine part of $E$ (not both on the same vertical line). Then the line through $P$ and $Q$ meets $E$ exactly at a third point $R$ (possibly coincident with $P$ or $Q$ ), so the [[lombardo_av_DEFINITION 9.1|divisor]] of the rational function corresponding to this line is $P+Q+R-3 O$. It follows that $P+Q \sim 3 O-R$[^2][^3]              . On the other hand, if $R$ and $R^{\prime}$ lie in the [[foag_finite_morphism_of_schemes|finite]] plane on the same vertical line, then the line in question is $x-x(R)=0$, which has zeroes at $R, R^{\prime}$ and has a double pole at $[0: 1: 0]$. It follows that $R+R^{\prime} \sim 2 O$[^2][^3]              . Combined with $P+Q \sim 3 O-R$[^2][^3]              , this yields $P+Q \sim 3 O-R \sim 3 O-\left(2 O-R^{\prime}\right)=O+R^{\prime} .$[^2][^3]               On the one hand, this recovers the classical construction of the addition law on elliptic curves; on the other, it gives us an algorithm to transform any [[lombardo_av_DEFINITION 9.1|divisor]] of the form $\sum_{i=1}^{k} P_{i}$ into one of the form $(k-1) O+Q$. Now consider a general [[lombardo_av_DEFINITION 9.1|divisor]] of [[degree_of_an_algebraic_field_extension|degree]] $0, D=\sum_{i=1}^{k} P_{i}-\sum_{j=1}^{k} Q_{j}$. We already know how to construct points $Q_{j}^{\prime}$ such that $Q_{j}+Q_{j}^{\prime} \sim 2 O$[^2][^3]              , so $D$ is [[lombardo_av_DEFINITION 9.9|linearly equivalent]] to $\sum_{i=1}^{k} P_{i}+\sum_{j=1}^{k}\left(Q_{j}^{\prime}-2 O\right) ;$ applying our reduction algorithm to $\sum_{i=1}^{k} P_{i}+\sum_{j=1}^{k} Q_{j}^{\prime}$, we find that it is [[lombardo_av_DEFINITION 9.9|linearly equivalent]] to a [[lombardo_av_DEFINITION 9.1|divisor]] of the form $R+(2 k-1) O$, where $R$ is a single point on $E$. Putting everything together, we obtain as desired
$$
D \sim R+(2 k-1) O-2 k O=R-O
$$
[^2][^3]
It follows in particular that the map $E \rightarrow \operatorname{Pic}^{0}(E)$ given by $P \mapsto[P-O]$ is surjective, and it's not hard to see that it is injective (if $P-O$ were a principal [[lombardo_av_DEFINITION 9.1|divisor]], $P-O=\operatorname{div}(f)$[^4]              , then $f: E \rightarrow \mathbb{P}^{1}$ would be a map of [[degree_of_an_algebraic_field_extension|degree]] 1 , hence an isomorphism, which is impossible since $E$ has genus 1 while $\mathbb{P}^{1}$ has genus 0 ).


# See Also

# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, EXAMPLE 9.20, Page 29
[^2]: ![[lombardo_av_notation_sim]]
[^3]: ![[lombardo_av_notation_sim_linearly_equivalent]]
[^4]: ![[lombardo_av_notation_div_f]]