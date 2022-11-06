---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]


\paragraph{Families of Motives} Let $S$ be a smooth connected $K$-variety with generic point $\eta_S$. Currently there does not seem to be a unanimous definition for a family of motives over $S$. We recall two of them: According to \cite[Def.~2.37]{Mil94}, a motive $\mathfrak{M}$ over $S$ is a motive $M$ in $\mathsf{Mot}_\mathrm{AH}(\eta_S)$ such that the action of $\pi_1^\mathrm{{\acute{e}}t}(\eta_S, \bar{\eta}_S)$ on the $\mathbb{A}_f$-realization $\omega_{\mathbb{A}_f}(M_{\eta_S})$ factors through $\pi_1^\mathrm{{\acute{e}}t}(S, \bar{\eta}_S)$. We may view such objects as constituting a subcategory $\mathsf{Mot}_\eta(S)$ of $\mathsf{Mot}(\eta_S)$, with morphisms defined in the obvious way. We define $\mathsf{Mot}_{\eta}(S)$, $\mathsf{Mot}^\mathsf{Ab}_{\eta}(S)$ and $\mathsf{Mot}^\mathsf{Ab}_{\eta, \mathrm{AH}}(S)$ when $\mathsf{Mot}_\mathrm{AH}(\eta_S)$ is replaced by $\mathsf{Mot}(S), \mathsf{Mot}^\mathsf{Ab}(S)$ and $\mathsf{Mot}^\mathsf{Ab}_\mathrm{AH}(S)$ respectively.  

We may also define a motive over $S$ by a tuple $(X, e, n)$ where $f : X \to S$ is a smooth projective morphism with connected fibers, $e$ is a global section of $\mathbb{R}^{2d}(f \times_S f)_* \mathbb{Q}_\ell(d)$ ($d = \dim(X/S)$), and $n$ is an integer such that for every $s \in S$, the fiber of the object $(X, e, n)$ over $s$ defines an object of $\mathsf{Mot}(k(s))$. This is Moonen's definition \cite[Def.~4.3.3]{Moonen-Fom}, except that we do not require $S$ to be geometrically connected. Denote the category of such objects by $\mathsf{Mot}(S)$. Define the $\ell$-adic realization functor $\omega_\ell$ of $M = (X, e, n) \in \mathsf{Mot}(S)$ as: 
$$ \omega_\ell(M) = e \cdot (\bigoplus_{i \ge 0} \mathbb{R}^i f_* \mathbb{Q}_\ell)(n) $$
and define the de Rham, Betti and Hodge realization functors $\omega_\mathrm{dR}, \omega_B, \omega_\mathrm{Hdg}$ by adapting the above definition in the obvious way (of course, $\omega_B$ and $\omega_\mathrm{Hdg}$ are only applicable when $K = \mathbb{C}$). Set $\omega_{\mathbb{A}_f}$ to be the restricted product of all $\omega_\ell$'s. If $S = \mathrm{Spec}(K)$ is a single point, we customarily view $\omega_\ell(M)$ as a $\mathrm{Gal}_K$-module over $\mathbb{Q}_\ell$. 

There is certainly a functor $\xi_\eta : \mathsf{Mot}(S) \to \mathsf{Mot}_\eta(S)$ given by taking the generic fibers. As a ``good reduction theory'' for motives is currently unclear, we do not know whether this functor is essentially surjective. However, there are some useful partial results in this direction. Suppose now that $K = \mathbb{C}$. Let $\mathrm{Hdg}_\mathbb{Q}(S)$ denote the category of polarizable $\mathbb{Q}$-VHS on $S$. Then the extension properties of polarizable $\mathbb{Q}$-VHS (\cite[Thm~2.40]{Mil94}) allows us to define a functor $\omega_{\mathrm{Hdg}}^\eta : \mathsf{Mot}_\eta(S) \to \mathrm{Hdg}_\mathbb{Q}(S)$. This gives us a diagram 
\[\begin{tikzcd}
	{\mathsf{Mot}(S)} & {\mathsf{Mot}_\eta(S)} \\
	& {\mathrm{Hdg}_\mathbb{Q}(S)}
	\arrow["{\xi_\eta}", from=1-1, to=1-2]
	\arrow["{\omega^\eta_\mathrm{Hdg}}", from=1-2, to=2-2]
	\arrow["{\omega_\mathrm{Hdg}}"', from=1-1, to=2-2]
\end{tikzcd}\]
such that for every $M \in \mathsf{Mot}(S)$, $\omega_\mathrm{Hdg}(M)$ is canonically isomorphic to $\omega^\eta_\mathrm{Hdg}(\xi_\eta(M))$. The functor $\omega^\eta_\mathrm{Hdg}$ is fully faithful when restricted to $\mathsf{Mot}^\mathsf{Ab}_{\eta, \mathrm{AH}}(S)$ and we say that an object in the essential image, which we denote by $\mathrm{Hdg}^\mathsf{Ab}_\mathbb{Q}(S)$, is \textit{abelian-motivic} (cf. Def.~2.30 and Prop.~2.42 in \textit{loc. cit.}). For an object $M \in \mathsf{Mot}^\mathsf{Ab}_{\eta, \mathrm{AH}}(S)$ and $s \in S(\mathbb{C})$, we define the fiber $M_s$ to be an object in $\mathsf{Mot}^\mathsf{Ab}_\mathrm{AH}(\mathbb{C})$ such that $\omega_\mathrm{Hdg}(M_s)$ is isomorphic to the fiber of $\omega^\eta_\mathrm{Hdg}(M)$ over $s$. The object $M_s$ is well defined up to isomorphism. 



# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, 11