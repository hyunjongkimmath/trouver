---
cssclass: clean-embeds
aliases: [lombardo_av_Rigidity_lemma]
tags: [_reference/lombardo_av, _meta/literature_note, _auto/links_added, _meta/concept, _meta/proof, _meta/TODO/change_title]
---
# Rigidity lemma[^1]
Let $f: A \times B \rightarrow C$ be a morphism of [[lombardo_av_1.1|varieties]] over $k$. If $A$ is [[foag_proper_morphism_of_schemes|proper]] and $f\left(A \times\left\{b_{0}\right\}\right)=f\left(\left\{a_{0}\right\} \times B\right)=\left\{c_{0}\right\}$ for some $a_{0} \in A(k), b_{0} \in B(k), c_{0} \in$ $C(k)$, then $f(A \times B)=\left\{c_{0}\right\}$

# Proof
PROOF. Choose an open affine neighbourhood $C_{0}$ of $c_{0} .$ By properness, $\pi: A \times B \rightarrow B$ is a closed map, hence $Z=\pi\left(f^{-1}\left(C \backslash C_{0}\right)\right)$ is closed in $B$. A closed point $b$ of $B$ lies outside $Z$ if and only if $f(A \times\{b\}) \subseteq C_{0}$; by assumption $b_{0}$ lies in $B \backslash Z$, which is therefore open and nonempty, hence dense (recall that our [[lombardo_av_1.1|varieties]] are [[foag_geometric_point#Geometric properties|geometrically]] [[foag_irreducible_topological_space|irreducible]] by definition). Now pick any point $b \in B \backslash Z$ and consider $f(A \times\{b\}):$ on the one hand, the image of this map is contained in $C_{0}$ by what we just said, and on the other, since $A \times\{b\} \cong A$ is [[foag_proper_morphism_of_schemes|proper]] and $C_{0}$ is affine, $f(A \times\{b\})$ is a point. We also know which point it is: by assumption,
$$
f(A \times\{b\}) \Rightarrow f\left(\left\{a_{0}\right\} \times\{b\}\right) \in f\left(\left\{a_{0}\right\} \times B\right)=\left\{c_{0}\right\}
$$
hence $f(A \times\{b\})=\left\{c_{0}\right\}$ for all $b$ in the dense set $B \backslash Z .$ In particular $f$ is constantly equal to $\left\{c_{0}\right\}$ on the dense open set $A \times(B \backslash Z)$, hence it is constant as claimed.


# See Also

# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, LEMMA 1.8, Page 9
