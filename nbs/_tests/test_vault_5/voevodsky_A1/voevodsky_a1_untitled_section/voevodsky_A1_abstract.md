---
cssclass: clean-embeds
aliases: []
tags: [_reference/voevodsky_A1, _meta/literature_note]
---
# Topic[^1]
\begin{abstract}
A}^{1}$-homotopy theory is the homotopy theory for algebraic varieties and schemes which uses the affine line as a replacement for the unit interval. In the paper I present in detail the basic constructions of the theory following the sequence familiar from standard texbooks on algebraic topology. At the end I define motivic cohomology and algebraic cobordisms and describe algebraic K-theory in terms of this theory.
\end{abstract}
Contents
1 Introduction ..... 579
2 Spaces ..... 581
3 Unstable homotopy category ..... 584
4 Spanier-Whitehead category . ..... 587
5 Spectra and the stable homotopy category ..... 591
6 Three cohomology theories ..... 595
6.1 Motivic cohomology ..... 595
6.2 Algebraic K-theory ..... 598
6.3 Algebraic cobordism ..... 601
7 Concluding remarks ..... 601


\section*{1 INTRODUCTION}

In my talk I will outline the foundations of the $\mathbf{A}^{1}$-homotopy theory. This theory is based on the idea that one can define homotopies in the algebro-geometrical context using the affine line $\mathbf{A}^{1}$ instead of the unit interval. My exposition will follow the sequence familiar from the standard textbooks on topological homotopy theory which roughly looks as follows.

Let $\mathcal{C}$ be a category which we want to study by means of homotopy theory. Usually $\mathcal{C}$ itself is not "good enough" and first one has to choose a convenient category of "spaces" $S p c$ which contains $\mathcal{C}$ and has good categorical properties (in particular has internal Hom-objects and all small limits and colimits). In topology $\mathcal{C}$ may be the category of $\mathrm{CW}$-complexes and $S p c$ the category of compactly generated spaces $([8, \S 6.1])$. Then one defines the class of weak equivalences on Spc. The localization of the category of spaces with respect to this class is then the (unstable) homotopy category $H$. To make the localization procedure effective one usually chooses in addition classes of cofibrations and fibrations such as to get
a closed model structure in the sense of Quillen (see [8, Def. 3.2.3] for the modern formulation of Quillen's axioms).

Next one considers suspension functors. Stabilizing with respect to these functors in the naive way one obtains a new category $S W$ called the SpanierWhitehead category. If the suspensions satisfy some natural conditions this new category is additive and triangulated. As a result it is more accessible to study than the original unstable category. One of the necessary conditions for this to work is that the category $H$ should be pointed i.e. its initial and final object should coincide. Thus one always applies the stabilization construction to the homotopy category of pointed spaces.

The Spanier-Whitehead categories lack an important property - they do not have infinite coproducts ( $=$ infinite direct sums). This is a result of the naive procedure used to invert the suspension functors. To obtain a category where suspensions are inverted and which still has infinite direct sums one uses the idea of spectra. This approach produces another triangulated category which is called the stable homotopy category $S H$. The reason infinite direct sums are so important lies in the fact that once we have them we can apply to $S H$ the representability theory of in [16], [17] and [18].

Thus the standard sequence of constructions in homotopy theory leads to a sequence of categories and functors of the form

$$
\mathcal{C} \rightarrow S p c \rightarrow H \rightarrow S W \rightarrow S H
$$

In what follows I will construct such a sequence starting with the category $\mathrm{Sm} / \mathrm{S}$ of smooth schemes over a Noetherian base scheme $S$. A reader who is more comfortable with the language of algebraic varieties may always assume that $S=$ $\operatorname{Spec}(k)$ for a field $k$ in which case $\mathcal{C}$ is the category of smooth algebraic varieties over $k$. At the end I will define three cohomology theories on $\operatorname{Spc}(S)$ for any $S$ - algebraic K-theory, motivic cohomology and algebraic cobordism. In each case one defines the theory by giving an explicit description on the spectrum which represents it. Algebraic K-theory defined this way coincides on $S m / S$ with homotopy algebraic K-theory of Chuck Weibel [27], motivic cohomology coincide for smooth varieties over a field of characteristic zero with higher Chow groups of S. Bloch [2] and algebraic cobordism is a new theory originally introduced in [26].

Modulo the general nonsense of the abstract homotopy theory all the statements of this paper except for Theorem 6.2 have simple proofs. The hard part of the work which was needed to develop the theory presented here consisted in choosing among many different plausible variants of the main definitions. I believe that in its present form the $\mathbf{A}^{1}$-homotopy theory gives a solid foundation for the study of cohomology theories on the category of Noetherian schemes.

Individual constructions which remind of $\mathbf{A}^{1}$-homotopy theory go back to the work of Karoubi-Villamayor on K-theory and more recently to the work of Rick Jardine [9],[10] and Chuck Weibel [27]. For me the starting point is [21] where the first nontrivial theorem showing that this theory works was proven. The first definition of the unstable $\mathbf{A}^{1}$-homotopy category equivalent to the one presented here was given by Fabien Morel. $\mathbf{A}^{1}$-homotopy theory for varieties over a field of characteristic zero was the main tool in the proof of the Milnor conjecture given
in [26]. The current work on the Bloch-Kato conjecture which is a generalization of Milnor conjecture to odd primes uses even more of it.

This text was written during my stay at FIM which is a part of ETH in Zurich. I am very glad to be able to use this opportunity to say that this was a very nice place to work. My special thanks go to Ruth Ebel for her help with all kinds of everyday problems.

\section*{2 SPACES}

The main problem which prevents one from applying the constructions of abstract homotopy theory directly to the category $S m / S$ of smooth schemes over a base $S$ is nonexistence of colimits. In classical algebraic geometry this is known as nonexistence of "contractions". One can solve this problem for particular types of contractions by extending the category to include nonsmooth varieties, algebraic spaces etc. For our purposes it is important to have all colimits which is not possible in any of these extended categories.

There is a standard way to formally add colimits of all small diagrams to a category $\mathcal{C}$. Consider the category of contravariant functors from $\mathcal{C}$ to the category of sets. Following Grothendieck one calls such functors presheaves on $\mathcal{C}$. We denote the category of all presheaves by $\operatorname{PreShv}(\mathcal{C})$. Any object $X$ of $\mathcal{C}$ defines a presheaf $R_{X}: Y \mapsto \operatorname{Hom}_{\mathcal{C}}(Y, X)$ which is called the presheaf representable by $X$. By Yoneda Lemma the correspondence $X \mapsto R_{X}$ identifies $\mathcal{C}$ with the subcategory of representable presheaves on $\mathcal{C}$. The category $\operatorname{PreShv}(\mathcal{C})$ has all small colimits (and limits). Moreover any presheaf is the colimit of a canonical diagram of representable presheaves. Thus $\operatorname{PreShv}(\mathcal{C})$ is in a sense the category obtained from $\mathcal{C}$ by formal addition of all small colimits.

It is quite possible to develop homotopy theory for algebraic varieties taking the category $\operatorname{Pre} S h v(S m / S)$ as the category $S p c$ of spaces. However this approach has a disadvantage which can be illustrated by the following example. For two subspaces $A, B$ of a space $X$ denote by $A \cup B$ the colimit of the diagram

![](https://cdn.mathpix.com/cropped/2024_04_03_0faf43a22498ae844030g-03.jpg?height=133&width=247&top_left_y=1825&top_left_x=901)

where $A \cap B=A \times{ }_{X} B$ is the fiber product of $A$ and $B$ over $X$. This is the categorical definition of union which makes sense in any category with limits and colimits. Consider now a covering $X=U \cup V$ of a scheme $X$ by two Zariski open subsets $U$ and $V$. The square

![](https://cdn.mathpix.com/cropped/2024_04_03_0faf43a22498ae844030g-03.jpg?height=130&width=241&top_left_y=2209&top_left_x=904)

is a pushforward square in $S m / S$ and thus $X$ is the categorical union of $U$ and $V$
in $S m / S$. However the corresponding square of representable presheaves

$$
\begin{array}{cccc}
R_{U \cap V} & \rightarrow & R_{U} \\
\downarrow & & \downarrow  \tag{3}\\
R_{V} & & \rightarrow & R_{Y}
\end{array}
$$

is not a pushforward square in $\operatorname{PreShv}(\operatorname{Sm} / S)$ unless $U=X$ or $V=X$. Thus if we define spaces as presheaves the union $U \cup_{\text {PreShv }} V$ of $U$ and $V$ as spaces is not the same as $X$. There is a morphism $j_{U, V}: U \cup_{\text {PreShv }} V \rightarrow X$ but it is not an isomorphism.

Definition 2.1 An elementary distinguished square in $S m / S$ is a square of the form

$$
\begin{array}{ccc}
p^{-1}(U) & \rightarrow & V  \tag{4}\\
\downarrow & & \downarrow p \\
U & & \rightarrow \\
& X
\end{array}
$$

such that $p$ is an etale morphism, $j$ is an open embedding and $p^{-1}(X-U) \rightarrow X-U$ is an isomorphism (here $X-U$ is the maximal reduced subscheme with support in the closed subset $X-U)$.

An important class of elementary distinguished squares is provided by coverings $X=U \cup V$ by two Zariski open subsets. In this case $p=j_{V}$ is an open embedding and the condition that $p^{-1}(X-U) \rightarrow X-U$ is an isomorphism is equivalent to the condition that $U \cup V=X$. One can easily see that an elementary distinguished square is a pushforward square in $S m / S$ i.e. $X$ is the colimit of the diagram

$$
\begin{align*}
& p^{-1}(U) \rightarrow V  \tag{5}\\
& \downarrow \\
& U
\end{align*}
$$

We want to define our category of spaces in such a way that elementary distinguished squares remain pushforward squares when considered in this category of spaces. The technique which allows one to add new colimits taking into account already existing ones is the theory of sheaves on Grothendieck topologies.

Definition 2.2 A contravariant functor $F: S m / S \rightarrow$ Sets (= a presheaf on $\mathrm{Sm} / \mathrm{S})$ is called a sheaf in Nisnevich topology if the following two conditions hold
1. $F(\emptyset)=p t$

2. for any elementary distinguished square as in Definition 2.1 the square of sets

$$
\begin{array}{ccc}
F(X) & \rightarrow & F(V)  \tag{6}\\
\downarrow & & \downarrow \\
F(U) & \rightarrow & F\left(p^{-1}(U)\right)
\end{array}
$$

is Cartesian i.e. $F(X)=F(U) \times{ }_{F\left(p^{-1}(U)\right)} F(V)$.

Denote the full subcategory of $\operatorname{PreShv}(\mathrm{Sm} / \mathrm{S})$ which consists of sheaves in Nisnevich topology by $\operatorname{Shv}_{N i s}(S m / S)$. This is our category of spaces. Because elementary distinguished squares are pushforward squares in $S m / S$ any representable presheaf belongs to $S h v_{N i s}(S m / S)$. Thus the functor $X \mapsto R_{X}$ factors through an embedding $S m / S \rightarrow S h v_{N i s}(S m / S)$. We will use this embedding to identify smooth schemes with the corresponding spaces (= representable sheaves). By Yoneda Lemma and our definition the square of representable sheaves corresponding to an elementary distinguished square is a pushforward square in $S h v_{N i s}(S m / S)$. The following result is a corollary of the general theory of sheaves on Grothendieck topologies.

THEOREm 2.3 The category $\operatorname{Shv}_{N i s}(S m / S)$ has all small limits and colimits. The inclusion functor $\operatorname{Shv}_{N i s}(\mathrm{Sm} / \mathrm{S}) \rightarrow \operatorname{PreShv}(\mathrm{Sm} / \mathrm{S})$ has a left adjoint $a_{N i s}$ : $\operatorname{PreShv}(S m / S) \rightarrow \operatorname{Shv}_{N i s}(S m / S)$ which commutes with both limits and colimits.

The functor $a_{N i s}$ is called the functor of associated sheaf. To compute a colimit in $S h v_{N i s}(S m / S)$ one first computes it in $\operatorname{PreShv}(S m / S)$ and then applies functor $a_{N i s}$. Starting from this point we denote the category $S h v_{N i s}(S m / S)$ by $S p c$ or $\operatorname{Spc}(S)$ and its final object i.e. the space corresponding to the base scheme $S$ by $p t$.

We will need a definition of a subcategory $S p c^{f t}$ of spaces of finite type in $S p c$ whose objects play the role of compact spaces in topology. We define $S p c^{f t}$ as the smallest subcategory in $S p c$ which satisfies the following two conditions

1. spaces corresponding to smooth schemes over $S$ belong to $S p c^{f t}$

2. if in a pushforward square $\begin{array}{llll}A & i & X \\ & \downarrow & & \downarrow\end{array}$ spaces $A, X$ and $B$ belong to $S p c^{f t}$ and $i$ is a monomorphism then $Y$ belongs to $S p c^{f t}$.

The following proposition shows that spaces of finite type are compact objects of $S p c$ in the sense of the categorical definition of compactness.

Proposition 2.4 For any space of finite type $X$ and any filtered system of spaces $X_{\alpha}$ the canonical map colim ${ }_{\alpha} \operatorname{Hom}\left(X, X_{\alpha}\right) \rightarrow \operatorname{Hom}\left(X, \operatorname{colim}_{\alpha} X_{\alpha}\right)$ is a bijection.

A pointed space $(X, x)$ is a space togther with a morphism $x: p t \rightarrow X$. We will also denote by $x$ the subspace $x(p t)=\operatorname{Im} x$ of $X$. For a space $X$ and a subspace $A \subset X$ denote by $X / A$ the "quotient space" i.e. the colimit of the diagram

$$
\begin{gather*}
A \\
\downarrow  \tag{7}\\
p t
\end{gather*}
$$

We always consider $X / A$ as a pointed space with the distinguished point given by the canonical morphism $p t \rightarrow X / A$. For two pointed spaces $(X, x),(Y, y)$ define their smash product as $(X, x) \wedge(Y, y)=X \times Y /(X \times y) \cup(x \times Y)$.

As an example of how all these definitions work consider Thom spaces of vector bundles. For a vector bundle $E \rightarrow U$ over a smooth scheme $U$ over $S$ set $T h(E)=E /(E-s(U))$ where $s: U \rightarrow E$ is the zero section. For two vector bundles $E \rightarrow X$ and $F \rightarrow Y$ we have

$$
T h(E \times F)=E \times F /(E \times F-s(X \times Y))=T h(E) \wedge T h(F)
$$

Note that in order to have this equality we need to know that

$$
E \times F-s(X \times Y)=((E-s(X)) \times F) \cup(E \times(F-s(Y)))
$$

i.e. that the square

$$
\begin{array}{ccc}
(E-s(X)) \times(F-s(Y)) & \rightarrow & (E-s(X)) \times F  \tag{8}\\
\downarrow & & \downarrow \\
E \times(F-s(Y)) & \rightarrow & E \times F-s(X \times Y)
\end{array}
$$

is a pushforward square. It is true in our case because this is the elementary distinguished square associated to a Zariski open covering.

\section*{3 UNSTABLE HOMOTOPY CATEGORY}

To do homotopy theory in $S p c$ we have to define classes of weak equivalences, fibrations and cofibrations. We start with the class of weak equivalences. We shall proceed in the same way as one does in homotopy theory of simplicial sets. We first define an analog of Kan simplicial sets and Kan completion functor. Then the analog of homotopy groups and then define weak equivalences as morphisms inducing isomorphisms on homotopy groups. Theorem 3.6 below shows that this definition is equivalent to another, more technical one, given in [14].

Denote by $\Delta_{S}^{n}$ the closed subscheme in $\mathbf{A}_{S}^{n+1}$ given by the equation $\sum_{i=0}^{n} x_{i}=$ 1. Clearly $\Delta_{S}^{n}$ is a smooth scheme over $S$ which is noncanonically isomorphic to $\mathbf{A}_{S}^{n}$. For any map of sets $\phi:\{0, \ldots, n\} \rightarrow\{0, \ldots, m\}$ define a morphism $\phi_{S}: \Delta_{S}^{n} \rightarrow \Delta_{S}^{m}$ setting $\phi_{S}^{*}\left(x_{i}\right)=\sum_{j \in \phi^{-1}(i)} x_{j}$. This gives us a functor from the standard simplicial category $\Delta$ to $S m / S$ and thus to $S p c$. Since $S p c$ has all colimits this functor has the right Kan extension $|-|_{S}: \Delta^{o p} S e t s \rightarrow S p c$ which is characterized by the properties that it commutes with colimits and $\left|\Delta^{n}\right|_{S}=\Delta_{S}^{n}$.

Example 3.1 Let $\partial \Delta^{2}$ be the boundary of the standard 2-simplex i.e. the simplicial set whose geometrical realization looks like the boundary of an equilateral triangle. Then $\left|\partial \Delta^{2}\right|_{S}$ is the space which is a union of three affine lines in the form of a triangle with sides extended to infinity. Similarly $\left|\partial \Delta^{3}\right|_{S}$ is the union of four affine planes in the form of a tetrahedra.

For a space $X$ and a smooth scheme $U$ consider the sets $\operatorname{Sing}_{n}(X)(U)=$ $\operatorname{Hom}\left(U \times \Delta_{S}^{n}, X\right)$. Since $\Delta_{S}^{\bullet}$ is a cosimplicial space these sets form a simplicial set $\operatorname{Sing}_{*}(X)(U)$ which is a direct analog of the singular simplicial set of a topological space in the $\mathbf{A}^{1}$-theory.

Definition $3.2 A$ space $X$ is called almost fibrant if for any open embedding $j: V \rightarrow U$ of smooth schemes over $S$ the associated morphism of simplicial sets $\operatorname{Sing}_{*}(X)(U) \rightarrow \operatorname{Sing}_{*}(X)(V)$ is a Kan fibration.

Note in particular that for any almost fibrant space $X$ and any smooth scheme $U$ the simplicial set $\operatorname{Sing}_{*}(X)(U)$ is a Kan simplicial set.

Let $i_{k}^{n}: \Lambda_{k}^{n} \rightarrow \Delta^{n}$ be the inclusion of the "hat" simplicial set to the standard simplex and let $j: V \rightarrow U$ be an open embedding of smooth schemes over $S$. Consider the following embedding of spaces

$$
i_{n, k, j}: U \times\left|\Lambda_{k}^{n}\right|_{S} \cup_{V \times\left|\Lambda_{k}^{n}\right|_{S}} V \times\left|\Delta^{n}\right|_{S} \rightarrow U \times\left|\Delta^{n}\right|_{S}
$$

These embeddings for all $n, k$ and $j: V \rightarrow U$ form the set of elementary "anodyne" morphisms which we can use to define our analog of Kan completion functor. For a space $X$ let $A_{X}$ be the set of all triples of the form $\left(\Lambda_{k}^{n} \rightarrow \Delta^{n}, j: V \rightarrow U, f\right.$ : $\left.U \times\left|\Lambda_{k}^{n}\right|_{S} \cup_{V \times\left|\Lambda_{k}^{n}\right|_{S}} V \times\left|\Delta^{n}\right|_{S} \rightarrow X\right)$. We have a canonical diagram

$$
\begin{gather*}
\coprod_{A_{X}} U \times\left|\Lambda_{k}^{n}\right|_{S} \cup_{V \times\left|\Lambda_{k}^{n}\right|_{S}} V \times\left|\Delta^{n}\right|_{S} \rightarrow X  \tag{9}\\
\downarrow \\
\coprod_{A_{X}} U \times \Delta_{S}^{n}
\end{gather*}
$$

and we define $E x^{1}(X)$ as the colimit of this diagram. Clearly $E x^{1}(X)$ is functorial in $X$ and there is a canonical morphism $X \rightarrow E x^{1}(X)$. Set $E x^{n}(X)=$ $E x^{1}\left(E x^{n-1}(X)\right)$ and $E x^{\infty}(X)=\operatorname{colim}_{n} E x^{n}(X)$. Proposition 2.4 immediately implies the following fact.

Lemma 3.3 The space $\operatorname{Ex}^{\infty}(X)$ is almost fibrant for any space $X$.

Let $X$ be a space, $U$ a smooth scheme and $x$ an element in $\operatorname{Sing}_{0}(X)(U)=$ $\operatorname{Hom}(U, X)$. Define homotopy "groups" $\pi_{i, U}^{\mathbf{A}^{1}}(X, x)$ as homotopy groups of the Kan simplicial set $C_{*}\left(E x^{\infty}(X)\right)(U)$ with respect to the base point $x$.

Definition 3.4 A morphism of spaces $f: X \rightarrow Y$ is called an $\mathbf{A}^{1}$-weak equivalence (or just weak equivalence) if for any smooth scheme $U$, any $x \in \operatorname{Hom}(U, X)$ and any $i \geq 0$ the corresponding map of homotopy groups

$$
\pi_{i, U}^{\mathbf{A}^{1}}(X, x) \rightarrow \pi_{i, U}^{\mathbf{A}^{1}}(Y, f(x))
$$

is a bijection.

Definition 3.5 The $\mathbf{A}^{1}$-homotopy category $H^{\mathbf{A}^{1}}(S)$ of smooth schemes over $S$ is the localization of the category of spaces over $S$ with respect to the class of weak equivalences.

The following is the list of basic properties of weak equivalences. They can either be deduced from [14] using Theorem 3.6 or proven directly.

1. the canonical morphism $\Delta_{S}^{1} \rightarrow p t$ is a weak equivalence

2. if $f: X \rightarrow Y$ and $f^{\prime}: X^{\prime} \rightarrow Y^{\prime}$ are weak equivalences then $f \times f^{\prime}: X \times X^{\prime} \rightarrow$ $Y \times Y^{\prime}$ is a weak equivalence

![](https://cdn.mathpix.com/cropped/2024_04_03_0faf43a22498ae844030g-08.jpg?height=155&width=1201&top_left_y=611&top_left_x=446)
either $f$ or $g$ is a monomorphism then $f^{\prime}$ is a weak equivalence

4. let $\left(X_{\alpha}, f_{\alpha \beta}: X_{\alpha} \rightarrow X_{\beta}\right.$ ) be a filtered system of spaces such that the morphisms $f_{\alpha \beta}$ are weak equivalences. Then the morphisms $X_{\gamma} \rightarrow \operatorname{colim} X_{\alpha}$ are weak equivalences.

Another approach to homotopy theory of spaces over $S$ based on the use of homotopy theory of simplicial sheaves is developed in [14]. The following result shows that these two approaches are equivalent and therefore we can use the techical results of [14] in the context of definitions given above.

THEOREm 3.6 A morphism of spaces is a weak equivalence in the sense of definition 3.4 if and only if its is an $\mathbf{A}^{1}$-weak equivalence in the sense of [14]. The category $H^{\mathbf{A}^{1}}(S)$ defined above is equivalent to the category $\mathcal{H}^{\mathbf{A}^{1}}(S)$ defined in $[14]$.

Let $\mathbf{W}$ be the class of weak equivalences. Define the class of cofibrations $\mathbf{C}$ in $S p c$ as the class of all monomorphisms and the class of fibrations $\mathbf{F}$ as the class of morphisms having the rigtht lifting property with respect to morphisms from $\mathbf{C} \cap \mathbf{W}$ (see [8, p.26]). As a corollary of Theorem 3.6 we have.

ThEOREM 3.7 The classes $(\mathbf{W}, \mathbf{F}, \mathbf{C})$ form a proper closed model structure on Spc.

Once we know the notions of weak equivalences, fibrations and cofibrations for spaces we can define them for pointed spaces. A morphism of pointed spaces is called a weak equivalence, fibration or cofibration if it is a weak equivalence, fibration or cofibration as a morphism of spaces with forgotten distinguished points. Standard reasoning shows that so defined classes form a proper closed model structure on the category $S p c_{\bullet}$ of pointed spaces. We denote the pointed homotopy category by $H_{\bullet}^{\mathbf{A}^{1}}(S)$. Properties 2 and 3 of weak equivalences from the list given above imply that the smash product gives a symmetric monoidal structure ([11, p.180]) on $H_{\bullet}^{\mathbf{A}^{1}}(S)$. The unit object of this monoidal structure is the space $\left(S \amalg S, i_{S}\right)$ which one denotes $S^{0}$ and calles 0 -sphere.

The functor $|-|_{S}$ from simplicial sets to spaces takes weak equivalences of simplicial sets to weak equivalences of spaces and thus defines a functor from the ordinary homotopy category $H^{t o p}$ to $H^{\mathbf{A}^{1}}$ (and from $H_{\bullet}^{t o p}$ to $H_{\bullet}^{\mathbf{A}^{1}}$ ). For any two simplicial sets $X, Y$ one has a canonical morphism $|X \times Y|_{S} \rightarrow|X|_{S} \times|Y|_{S}$ which is not an isomorphism but always a weak equivalence. Therefore the functor from $H^{t o p}$ to $H^{\mathbf{A}^{1}}$ commutes with products and the functor from $H_{\bullet}^{t o p}$ to $H_{\bullet} \mathbf{A}^{1}$ commutes with smash products.

Define the simplicial circle $S_{s}^{1}$ as $\left|\Delta^{1} / \partial \Delta^{1}\right|_{S}$. Geometrically $S_{s}^{1}$ is the space obtained from the affine line $\mathbf{A}^{1}$ by identification of points 0 and 1 . The smash product with $S_{s}^{1}$ is the simplicial suspension functor. We denote $\left(S_{s}^{1}\right)^{\wedge n}$ by $S_{s}^{n}$. This is the space obtained from $\mathbf{A}_{S}^{n}$ by contraction of the union of hyperplanes $x_{i}=1, x_{i}=0, i=1, \ldots, n$ to the point. One can use the simplicial suspension to describe homotopy groups $\pi_{i, U}^{\mathbf{A}^{1}}(X, x)$ in terms of morphisms in the pointed homotopy category as follows.

Lemma 3.8 For any pointed space $(X, x)$, smooth scheme $U$ and $i \geq 0$ one has

$$
\pi_{i, U}^{\mathbf{A}^{1}}(X, x)=\operatorname{Hom}_{H_{\bullet}^{\mathbf{A}^{1}}}\left(S_{s}^{i} \wedge U_{+},(X, x)\right)
$$

where $U_{+}$is the pointed space $\left(U \amalg S, i_{S}\right)$.

The notion of almost fibrant space turns out to be too restrictive in concrete applications. For example the Eilenberg-MacLane spaces used in Section 6.1 to build the Eilenberg-MacLane spectrum representing motivic cohomology are not almost fibrant. A wider class of quasi-fibrant spaces defined below turns out to be more useful.

DEFinition 3.9 A space $X$ is called quasi-fibrant if for any smooth scheme $U$ over $S$ which is quasi-projective over an affine open subset in $S$ the map of simplicial sets $\operatorname{Sing}_{*}(X)(U) \rightarrow \operatorname{Sing}_{*}\left(\operatorname{Ex}^{\infty}(X)\right)(U)$ is a weak equivalence.

The role of quasi-fibrant spaces in the theory is partly explained by the following corollary of Lemma 3.8.

Proposition 3.10 Let $(X, x)$ be a pointed quasi-fibrant space and $U$ be a smooth scheme over $S$ which is quasi-projective over an affine open subset in $S$. Then for any $i \geq 0$ one has $\operatorname{Hom}_{H^{\mathbf{A}^{1}}}\left(S_{s}^{i} \wedge U_{+},(X, x)\right)=\pi_{i}\left(\operatorname{Sing}_{*}(X)(U), x\right)$.

\section*{4 Spanier-Whitehead CATEgory}

One of the fundamental differences between $H=H^{\mathbf{A}^{1}}$ and the ordinary homotopy category $H^{t o p}$ lies in the fact that besides the simplicial circle $S_{s}^{1}$ there is another circle $S_{t}^{1}$ which we call Tate circle and which is defined as the space $\mathbf{A}^{1}-\{0\}$ pointed by 1 . The following lemma shows how different types of "spheres" can be expressed in $H_{\bullet}$ in terms of $S_{t}^{n}$ and $S_{s}^{n}$.

LEmma 4.1 There are canonical isomorphisms in $H_{\bullet}$ of the form

$$
\left(\mathbf{A}^{n}-\{0\}, \mathbf{1}\right) \cong S_{t}^{n} \wedge S_{s}^{n-1} ; \quad \mathbf{P}^{n} / \mathbf{P}^{n-1} \cong \mathbf{A}^{n} / \mathbf{A}^{n}-\{0\} \cong S_{t}^{n} \wedge S_{s}^{n}
$$

The Spanier-Whitehead category $S W=S W^{\mathbf{A}^{1}}(S)$ is the category obtained from $H_{\bullet}$ by stabilization with respect to the suspensions associated to the circles $S_{s}^{1}$ and

$S_{t}^{1}$. For technical reasons it is more convenient to talk about stabilization with respect to one suspension associated with $S_{s}^{1} \wedge S_{t}^{1}$ which leads to an equivalent category. Note that by Lemma $4.1 S_{t}^{1} \wedge S_{s}^{1}$ is canonically weakly equivalent to $\mathbf{A}^{1} / \mathbf{A}^{1}-\{0\}$ and to $\left(\mathbf{P}^{1}, \infty\right)$.

The construction of $S W$ from $H_{\bullet}$ is an example of a very simple general construction which allows one to "invert" an object in a symmetric monoidal category. Let $(\mathcal{C}, \wedge, \mathbf{1})$ be a symmetric monoidal category (here $\wedge$ denotes the monoidal structure and $\mathbf{1}$ is the unit object) and $T$ an object in $\mathcal{C}([11$, p.157,180]). Denote by $\mathcal{C}\left[T^{-1}\right]$ the category whose objects are pairs of the form $(X, n), X \in$ $o b(\mathcal{C}), n \in \mathbf{Z}$ and morphisms are given by

$$
\operatorname{Hom}\left((X, n),\left(X^{\prime}, n^{\prime}\right)\right)=\operatorname{colim}_{m \geq-n,-n^{\prime}} \operatorname{Hom}_{\mathcal{C}}\left(T^{\wedge(m+n)} \wedge X, T^{\wedge\left(m+n^{\prime}\right)} \wedge X^{\prime}\right)
$$

One can easily define composition of morphisms and check that $\mathcal{C}\left[T^{-1}\right]$ is indeed a category. The assigment $X \mapsto(X, 0)$ gives us a functor from $\mathcal{C}$ to $\mathcal{C}\left[T^{-1}\right]$.

Definition 4.2 $S W=H_{\bullet}\left[\left(S_{s}^{1} \wedge S_{t}^{1}\right)^{-1}\right]$.

The next step is to define a symmetric monoidal structure on $\mathcal{C}\left[T^{-1}\right]$ such that the canonical functor from $\mathcal{C}$ is a symmetric monoidal functor and the object $(T, 0)$ is invertible in $\mathcal{C}\left[T^{-1}\right]$. It turns out that there is an obvious obstruction to the existence of such a structure. Indeed, the group of automorphisms of an invertible object in a symmetric monoidal category is necessarily abelian. Thus the cyclic permutation on $T \wedge T \wedge T$ being in the commutatnt of $\Sigma_{3}$ must become identity in $\operatorname{Aut}_{\mathcal{C}\left[T^{-1}\right]}((T, 0))$. If one tries to extend directly the monoidal structure from $\mathcal{C}$ to $\mathcal{C}\left[T^{-1}\right]$ one discovers that this condition is indeed necessary and sufficient for the obvious constructions to be well defined. Thus one gets the following general result.

THEOREm 4.3 Let $(\mathcal{C}, \wedge, \mathbf{1})$ be a symmetric monoidal category and $T$ an object such that the cyclic permutation on $T \wedge T \wedge T$ equals identity in $\mathcal{C}\left[T^{-1}\right]$. Then there exists a symmetric monoidal structure $\wedge$ on $\mathcal{C}\left[T^{-1}\right]$ such that $(X, n) \wedge(Y, m)=$ $(X \wedge Y, n+m)$.

The canonical functor $\mathcal{C} \rightarrow \mathcal{C}\left[T^{-1}\right]$ is then a symmetric monoidal functor and the object $T=(T, 0)$ is invertible with the canonical inverse given by $T^{-1}=$ $(1,-1)$.

Lemma 4.4 The cyclic permutation on $\left(S_{s}^{1} \wedge S_{t}^{1}\right)^{\wedge 3}$ equals identity in $H_{\bullet}$.

Combining Theorem 4.3 and Lemma 4.4 we get:

Proposition 4.5 The category $S W$ has a structure of a symmetric monoidal category $\left(\wedge, S^{0}\right)$ such that the canonical functor $\left(H_{\bullet}, \wedge, S^{0}\right) \rightarrow\left(S W, \wedge, S^{0}\right)$ is symmetric monoidal and $((X, x), n) \wedge((Y, y), m)=((X, x) \wedge(Y, y), n+m)$.

Denote the object $\left(S^{0}, n\right)$ of $S W$ by $T^{n}$ and objects of the form $((X, x), 0)$ simply by $(X, x)$. Then for any $n \in \mathbf{Z}$ one has a canonical isomorphism $((X, x), n)=$ $T^{n} \wedge(X, x)$ which we will use to avoid notations of the form $((X, x), n)$ below.

Proposition 4.6 The category $S W$ is an additive category.

To get the abelian group structures on the Hom-sets in $S W$ one observes that the image of $S_{s}^{2}$ in $S W$ is an abelian cogroup object which is invertible with respect to the monoidal structure.

The last structure on $S W$ which we want to describe is a structure of a triangulated category ( $[6$, ch.IV $])$. To specify a triangulated structure on an additive category $\mathcal{D}$ one has to describe two things. One is an additive autoequivalence $S: \mathcal{D} \rightarrow \mathcal{D}$ which is called the shift functor and denoted by $X \mapsto X[1]$. Another one is a class of diagrams of the form $X \rightarrow Y \rightarrow Z \rightarrow X[1]$ called distinguished triangles (all such diagrams are called triangles). These data should satisfy some conditions listed for example in [6, p.239]. These conditions have the following fundamental corollary which makes triangulated structure into a surprisingly effective tool to produce long exact sequences and, more generally, spectral sequences.

Lemma 4.7 Let $X \rightarrow Y \rightarrow Z \rightarrow X[1]$ be a distinguished triangle in a triangulated category and $U$ be any object of this category. Then the sequences of abelian groups

$$
\begin{aligned}
& \rightarrow \operatorname{Hom}(U, X[n]) \rightarrow \operatorname{Hom}(U, Y[n]) \rightarrow \operatorname{Hom}(U, Z[n]) \rightarrow \operatorname{Hom}(U, X[n+1]) \rightarrow \\
& \rightarrow \operatorname{Hom}(Z[n], U) \rightarrow \operatorname{Hom}(Y[n], U) \rightarrow \operatorname{Hom}(X[n], U) \rightarrow \operatorname{Hom}(Z[n-1], U) \rightarrow
\end{aligned}
$$

are exact.

All known long exact sequences can be traced back to this lemma applied to distinguished triangles in different triangulated categories. In our case we will construct the Mayer-Vietoris, Gysin and blow-up long exact sequences in homology and cohomology as the long exact sequences associated with distinguished triangles in the Spanier-Whitehead category $S W$ (see Propositions 4.11-4.13).

Let us describe now the triangulated structure on $S W$. We define the shift functor by $X[1]=X \wedge S_{s}^{1}$. To define distinguished triangles we have to recall the notion of cofibration sequences in our context. Let $f:(X, x) \rightarrow(Y, y)$ be a morphism of pointed spaces. Define cone $(f)$ as the colimit of the diagram

![](https://cdn.mathpix.com/cropped/2024_04_03_0faf43a22498ae844030g-11.jpg?height=154&width=422&top_left_y=1666&top_left_x=816)

where the vertical arrow is $f$ and $\Delta_{S}^{1} \cong \mathbf{A}_{S}^{1}$ is considered as a pointed space with the distinguished point 0 . We have a canonical morphism $(Y, y) \rightarrow \operatorname{cone}(f)$ which we denote $\eta_{f}$. For any commutative square

![](https://cdn.mathpix.com/cropped/2024_04_03_0faf43a22498ae844030g-11.jpg?height=171&width=338&top_left_y=2007&top_left_x=861)

we have a canonical morphism cone $(f) \rightarrow \operatorname{cone}\left(f^{\prime}\right)$ which makes the diagram

![](https://cdn.mathpix.com/cropped/2024_04_03_0faf43a22498ae844030g-11.jpg?height=156&width=362&top_left_y=2283&top_left_x=841)
commutative. In particular for any $f$ we have a canonical morphism cone $(f) \rightarrow$ $\operatorname{cone}((X, x) \rightarrow p t)$. The space on the right hand side is canonically isomorphic to $(X, x) \wedge S_{s}^{1}$ and therefore to any $f$ we assigned in a canonical way a sequence

$$
(X, x) \xrightarrow{f}(Y, y) \xrightarrow{\eta_{f}} \operatorname{cone}(f) \xrightarrow{\epsilon_{f}}(X, x) \wedge S_{s}^{1}
$$

which is called the cofibration sequence of $f$. The idea of the following definition is that the distinguished triangles in $S W$ are exactly the triangles isomorphic to suspensions of images of cofibration sequences from $S p c_{\bullet}$.

Definition 4.8 A sequence of morphisms of the form $A \rightarrow B \rightarrow C \rightarrow A[1]$ in $S W$ is called a distinguished triangle if there exist a morphism $f: X \rightarrow Y$ in $S p c_{\bullet}$, an integer $n$ and isomorphisms

$$
\phi_{1}: T^{n} \wedge X \rightarrow A ; \quad \phi_{2}: T^{n} \wedge Y \rightarrow B ; \quad \phi_{3}: T^{n} \wedge \operatorname{cone}(f) \rightarrow C
$$

in $S W$ such that the following diagram commutes

$$
\begin{array}{ccccccc}
T^{n} \wedge X & \stackrel{I d \wedge f}{\rightarrow} & T^{n} \wedge Y & \xrightarrow{I d \wedge \eta_{f}} & T^{n} \wedge \text { cone }(f) & { }^{\alpha \circ\left(T^{n} \wedge \epsilon_{f}\right)} & \left(T^{n} \wedge X\right)[1] \\
\phi_{1} \downarrow & & \phi_{2} \downarrow & & \phi_{3} \downarrow & & \phi_{1}[1] \downarrow  \tag{13}\\
A & \rightarrow & B & \rightarrow & C & \rightarrow & A[1]
\end{array}
$$

(here $\alpha=\alpha_{T^{n}, X}$ is the canonical isomorphism $T^{n} \wedge X[1] \rightarrow\left(T^{n} \wedge X\right)[1]$ ).

THEOREm 4.9 The category $S W$ with the shift functor and the class of distinguished triangles defined above is a triangulated category.

The main application of Theorem 4.9 is that in combination with Lemma 4.7 it implies that any distinguished triangle in $S W$ generates two long exact sequences of Hom-groups. To take advantage of this fact one has to have a way to produce interesting distinguished triangles. At the moment we know of three main types of such triangles which generate correspondingly Mayer-Vietoris, Gysin and blow-up long exact sequences. They are described in Propositions 4.11-4.13 below. In all three cases the proof is based on an unstable result from [14] combined with the following general lemma.

Lemma 4.10 Consider a commutative square in $S p c_{\bullet}$

$$
\begin{array}{cccc} 
& (A, a) & \rightarrow & (X, x)  \tag{14}\\
& \downarrow & & \downarrow \\
& (Y, y) & \xrightarrow{i^{\prime}} & (Z, z)
\end{array}
$$

such that $i$ is a monomorphism (= cofibration) and the canonical morphism $(X, x) \cup_{(A, a)}(Y, y) \rightarrow(Z, z)$ is a weak equivalence. Then there is a canonical morphism $(Z, z) \rightarrow(A, a) \wedge S_{s}^{1}$ in $H_{\bullet}$ such that the sequence

$$
(A, a) \xrightarrow{p \oplus i}(Y, y) \oplus(X, x) \xrightarrow{i^{\prime} \oplus p^{\prime}}(Z, z) \rightarrow(A, a)[1]
$$

is a distinguished triangle in $S W$.

In the propositions below we denote by $X_{+}$the pointed space ( $X \amalg p t, i_{p t}$ ) associated with a space $X$.

Proposition 4.11 For any elementary distinguished square as in Definition 2.1 there is a canonical distinguished triangle in $S W$ of the form

$$
p^{-1}(U)_{+} \rightarrow U_{+} \oplus V_{+} \rightarrow X_{+} \rightarrow p^{-1}(U)_{+}[1]
$$

In particular for the distinguished square associated to a Zariski open covering $X=U \cup V$ we get the Mayer-Vietoris distinguished triangle

$$
(U \cap V)_{+} \rightarrow U_{+} \oplus V_{+} \rightarrow X_{+} \rightarrow(U \cap V)_{+}[1]
$$

Proposition 4.12 Let $i: Z \rightarrow X$ be a closed embedding of smooth schemes over $S$ and $N$ the normal bundle to $Z$ in $X$. Then there is a canonical Gysin distinguished triangle of the form $(X-Z)_{+} \rightarrow X_{+} \rightarrow \operatorname{Th}(N) \rightarrow(X-Z)_{+}[1]$.

Proposition 4.13 Let $i: Z \rightarrow X$ be a closed embedding of smooth schemes over $S$ and $p: X_{Z} \rightarrow X$ the blow-up of $Z$ in $X$. Then there is a canonical blow-up distinguished triangle of the form

$$
p^{-1}(Z)_{+} \rightarrow Z_{+} \oplus\left(X_{Z}\right)_{+} \rightarrow X_{+} \rightarrow p^{-1}(Z)_{+}[1]
$$

The following Connectivity Theorem is the basis for the proof of convergence results for spectral sequences in the homotopy theory of algebraic varieties.

THEOREM 4.14 Let $(X, x)$ be a pointed smooth scheme over $S,(Y, y)$ a pointed space and $m \in \mathbf{Z}$ an integer. Then one has

$$
\operatorname{Hom}_{S W}\left((X, x), S_{s}^{n} \wedge S_{t}^{m} \wedge(Y, y)\right)=0
$$

for any $n>\operatorname{dim}(X)$ where $\operatorname{dim}(X)$ is the absolute dimension of $X$

Denote by $S W^{f t}$ the full subcategory in $S W$ which consists of objects isomorphic to objects of the form $T^{n} \wedge(X, x)$ for $(X, x) \in S p c^{f t}$. By definition of cofibration sequences and spaces of finite type this is a triangulated subcategory of $S W$. Lemma 4.10 implies that it coincides with the triangulated subcategory generated by objects of the form $T^{n} \wedge(X, x)$ for smooth schemes $X$ over $S$. This category actually plays more important role in the theory than the category $S W$ itself which is a wrong category to work with if we are interested in spaces not of finite type. The correct replacement for $S W$ is the stable homotopy category $S H=S H^{\mathbf{A}^{1}}(S)$ discussed in the following section.

\section*{5 Spectra and the Stable homotopy CATEgory}

The stabilization construction used to define the Spanier-Whitehead category in the previous section has a serious drawback. One of the good properties of the homotopy category $H=H_{\bullet}^{\mathbf{A}^{1}}(S)$ is the existence of infinite coproducts. For
any collection of pointed spaces $\left(X_{\alpha}, x_{\alpha}\right)$ the space $\vee_{\alpha}\left(X_{\alpha}, x_{\alpha}\right)$ represents the coproduct of $\left(X_{\alpha}, x_{\alpha}\right)$ 's in $H$ i.e. for any $(Y, y)$ one has

$$
\operatorname{Hom}_{H}\left(\vee_{\alpha}\left(X_{\alpha}, x_{\alpha}\right),(Y, y)\right)=\prod_{\alpha} \operatorname{Hom}_{H}\left(\left(X_{\alpha}, x_{\alpha}\right),(Y, y)\right)
$$

When we invert $S_{s}^{1} \wedge S_{t}^{1}$ to get the Spanier-Whitehead category we lose this property. For a family of objects like $\left\{T^{-i}\right\}_{i \geq 0}$ there is clearly no coproduct (= direct sum) in $S W$. Moreover for an infinite family of pointed spaces $\left(X_{\alpha}, x_{\alpha}\right)$ the space $\vee_{\alpha}\left(X_{\alpha}, x_{\alpha}\right)$ considered as an object of $S W$ is not the coproduct of $\left(X_{\alpha}, x_{\alpha}\right)$ 's in this category because infinite colimits do not commute with infinite products.

There is another way to stabilize $H$ with respect to the suspension functor $(X, x) \mapsto T \wedge(X, x)$ associated to any pointed space $T$. The resulting category which we denote by $H\left[\left[T^{-1}\right]\right]$ is called the stable homotopy category of $T$-spectra or just the $T$-stable homotopy category. It has all coproducts and the canonical functor $\Sigma_{T}^{\infty}: H \rightarrow H\left[\left[T^{-1}\right]\right]$ takes $\vee_{\alpha}\left(X_{\alpha}, x_{\alpha}\right)$ to the direct sum of $\left(X_{\alpha}, x_{\alpha}\right)$ 's in $H\left[\left[T^{-1}\right]\right]$. Unfortunately no one knows how to construct a category $H\left[\left[T^{-1}\right]\right]$ with properties described above from $H$. Instead we will have to build it directly from spaces.

Let $T$ be a pointed space of finite type. A T-spectrum $\mathbf{E}$ is a sequence of pointed spaces $E_{i}, i \geq 0$ which are called terms of $\mathbf{E}$ and morphisms $e_{i}: T \wedge E_{i} \rightarrow$ $E_{i+1}$ which are called the assembly morphisms of $\mathbf{E}$. A morphism of T-spectra $\mathbf{E} \rightarrow \mathbf{F}$ is a collection of morphisms of pointed spaces $E_{i} \rightarrow F_{i}$ which commute with the assembly morphisms. Denote the category of T-spectra by $S p\left(S p c_{\bullet}, T\right)$. For a T-spectrum $\mathbf{E}$ define a family of functor $E^{n}: S p c_{\bullet}^{f t} \rightarrow$ Sets, $n \in \mathbf{Z}$ setting

$$
E^{n}(X, x)=\operatorname{colim}_{i \geq \max \{0,-n\}} \operatorname{Hom}_{H}\left(T^{\wedge i} \wedge(X, x), T^{\wedge(i+n)} \wedge E_{i}\right)
$$

where the maps in the inductive system are defined by the assembly morphisms of E. A morphism of T-spectra $\mathbf{E} \rightarrow \mathbf{F}$ is called a stable weak equivalence if the corresponding natural transformations of functors $E^{n}(-) \rightarrow F^{n}(-)$ are isomorphisms for all $n \in \mathbf{Z}$.

Definition 5.1 The category $H\left[\left[T^{-1}\right]\right]$ is the localization of $S p\left(S p c_{\bullet}, T\right)$ with respect to the class of weak equivalences.

The category of T-spectra has all small limits and colimits which are defined termwise. In particular for a collection of spectra $\mathbf{E}_{\alpha}=\left(E_{i, \alpha}, e_{i, \alpha}\right)$ their coproduct in $S p\left(S p c_{\bullet}, T\right)$ is given by $\oplus_{\alpha} \mathbf{E}_{\alpha}=\left(\vee_{\alpha} E_{i, \alpha},\left(\delta_{i} \circ\left(\vee e_{i, \alpha}\right)\right)\right)$ where $\delta_{i}$ is the canonical isomorphism $T \wedge\left(\vee_{\alpha} E_{i, \alpha}\right) \rightarrow \vee_{\alpha}\left(T \wedge E_{i, \alpha}\right)$. One can verify easily that it is also the direct sum in $H\left[\left[T^{-1}\right]\right]$ i.e. that for any spectrum $\mathbf{F}$ one has

$$
\operatorname{Hom}_{H\left[\left[T^{-1}\right]\right]}\left(\oplus_{\alpha} \mathbf{E}_{\alpha}, \mathbf{F}\right)=\prod_{\alpha} \operatorname{Hom}_{H\left[\left[T^{-1}\right]\right]}\left(\mathbf{E}_{\alpha}, \mathbf{F}\right)
$$

For a pointed space $(X, x)$ denote by $\Sigma_{T}^{\infty}(X, x)$ the T-spectrum $\left(T^{\wedge n} \wedge\right.$ $(X, x), I d)$. The functor $\Sigma_{T}^{\infty}$ takes weak equivalences to stable weak equivalences and for any collection of spaces we have a canonical isomorphism
$\Sigma_{T}^{\infty}\left(\vee_{\alpha}\left(X_{\alpha}, x_{\alpha}\right)\right) \rightarrow \oplus_{\alpha} \Sigma_{T}^{\infty}\left(X_{\alpha}, x_{\alpha}\right)$. One can also verify easily that the functor $H \rightarrow H\left[\left[T^{-1}\right]\right]$ admits a canonical decomposition of the form $H \rightarrow H\left[T^{-1}\right] \rightarrow$ $H\left[\left[T^{-1}\right]\right]$ where the second functor takes $((X, x), n)$ to the spectrum

$$
\Sigma^{\infty}((X, x), n)_{i}= \begin{cases}p t & \text { for } \quad i<-n  \tag{15}\\ T^{\wedge(i+n)} & \text { for } \quad i \geq-n\end{cases}
$$

The following result is the main technical thing one needs to know to be able to use the construction described above.

Theorem 5.2 For any space of finite type $(X, x)$ and any T-spectrum $\mathbf{E}$ one has

$$
\operatorname{Hom}_{H\left[\left[T^{-1}\right]\right]}\left(\Sigma_{T}^{\infty}(X, x), \mathbf{E}\right)=\operatorname{colim}_{n} \operatorname{Hom}_{H}\left(T^{\wedge n} \wedge(X, x), E_{n}\right)
$$

where the maps in the inductive system are defined by the assembly morphisms of E.

Corollary 5.3 Let $(X, x),(Y, y)$ be spaces of finite type. Then one has

$$
\operatorname{Hom}_{H\left[\left[T^{-1}\right]\right]}\left(\Sigma_{T}^{\infty}(X, x), \Sigma_{T}^{\infty}(Y, y)\right)=\operatorname{colim}_{n} \operatorname{Hom}_{H}\left(T^{\wedge n} \wedge(X, x), T^{\wedge n} \wedge(Y, y)\right)
$$

For a T-spectrum $\mathbf{E}$ define $\mathbf{E}[1]$ to be the spectrum $\left(E_{i} \wedge S_{s}^{1}, e_{i} \wedge I d_{S_{s}^{1}}\right)$. For a morphism of T-spectra $f: \mathbf{E} \rightarrow \mathbf{F}$ define the associated cofibration sequence

$$
\mathbf{E} \rightarrow \mathbf{F} \rightarrow \operatorname{cone}(f) \rightarrow \mathbf{E}[1]
$$

in exactly the same way as we did for morphisms of pointed spaces in the previous section setting $\mathbf{E} \wedge \Delta_{S}^{1}$ to be the spectrum of the form $\left(E_{i} \wedge \Delta_{S}^{1}, e_{i} \wedge I d_{\Delta_{S}^{1}}\right)$. A sequence of morphisms in $H\left[\left[T^{-1}\right]\right]$ is called a distinguished triangle if it is isomorphic to the image of the cofibration sequence for a morphism in $S p\left(S p c_{\bullet}, T\right)$.

Proposition 5.4 For any pointed space $T$ of finite type the category $H\left[\left[\left(S_{s}^{1} \wedge\right.\right.\right.$ $\left.\left.T^{\prime}\right)^{-1}\right]$ is additive and the shift functor and the class of distinguished triangles defined above satisfy the axioms of a triangulated structure.

The following technical result allows one to apply the general representablility theorems proven in [16], [17], [18] to the stable homotopy category of algebraic varieties.

Proposition 5.5 For any space of finite type $T$ and any Noetherian base scheme $S$ the category $H\left[\left[T^{-1}\right]\right]$ is compactly generated and suspension spectra of spaces of finite type are compact. If in addition $S$ can be covered by affine open subsets $U_{i}=\operatorname{Spec}\left(R_{i}\right)$ such that $R_{i}$ are countable rings then the subcategory of compact objects in $H\left[\left[T^{-1}\right]\right]$ is equivalent to a countable category.

THEOREm 5.6 Let $T$ be a space of finite type such that the cyclic permutation on $T^{\wedge 3}$ equals identity in $H\left[T^{-1}\right]$. Then the category $H\left[\left[T^{-1}\right]\right]$ has a symmetric monoidal structure $(\wedge, \mathbf{1})$ such that:

1. for a spectrum $\mathbf{E}$ and a pointed space $(X, x)$ the spectrum $\mathbf{E} \wedge \Sigma_{T}^{\infty}(X, x)$ is canonically isomorphic to $\left(E_{i} \wedge(X, x), e_{i} \wedge I d_{(X, x)}\right)$

2. for a collection of spectra $\mathbf{E}_{\alpha}$ and a spectrum $\mathbf{F}$ there is a canonicall isomorphism

$$
\left(\oplus_{\alpha} \mathbf{E}_{\alpha}\right) \wedge \mathbf{F} \rightarrow \oplus_{\alpha}\left(\mathbf{E}_{\alpha} \wedge \mathbf{F}\right)
$$

3. for a cofibration sequence $\mathbf{E} \rightarrow \mathbf{F} \rightarrow$ cone $(f) \xrightarrow{\epsilon} \mathbf{E}[1]$ and a spectrum $\mathbf{G}$ the sequence $\mathbf{E} \wedge \mathbf{G} \rightarrow \mathbf{F} \wedge \mathbf{G} \rightarrow$ cone $(f) \wedge \mathbf{G} \rightarrow \mathbf{E} \wedge \mathbf{G}[1]$ where the last morphism is the composition of $\epsilon \wedge I d_{G}$ with the canonical isomorphism $\mathbf{E}[1] \wedge \mathbf{G} \rightarrow$ $(\mathbf{E} \wedge \mathbf{G})[1]$ is isomorphic to a cofibration sequence.

All the results of this section except for Theorem 5.6 have simple proofs. I know of two ways to prove Theorem 5.6. One is to explicitly construct the symmetric monoidal structure on $H\left[\left[T^{-1}\right]\right]$ starting with the obvious badly defined smash product in $S p\left(S p c_{\bullet}, T\right)$ and checking that all the ambiguities disappear when one passes to the homotopy category. In the case of the ordinary topological stable category a detailed exposition of this approach is given for example in $[1$, pp. 158-190]. It takes Adams thirty pages to verify that nothing goes wrong and it is terrible. Also it is hard to see that the cyclic permutation condition is indeed the key. Another way to prove Theorem 5.6 is to use the idea of symmetric spectra introduced recently by Jeff Smith (see [8] for an exposition in the context of simplicial sets and topological spaces). In this approach one defines first the category $S p^{\Sigma}\left(S p c_{\bullet}, T\right)$ of so called symmetric T-spectra and the associated stable homotopy category which I denote $H\left[\left[T^{-1}, \Sigma\right]\right]$. These categories have symmetric monoidal structures for any $T$ and one can construct a functor $H\left[\left[T^{-1}\right]\right] \rightarrow H\left[\left[T^{-1}, \Sigma\right]\right]$ which commutes in the obvious sense with the suspension spectrum functors. The cyclic permutation condition is then necessary and sufficient for this functor to be an equivalence [19].

This ends our discussion of the general stabilization construction $H \mapsto$ $H\left[\left[T^{-1}\right]\right]$. Now we specialize to the only case which we are really interested in namely $T=S_{s}^{1} \wedge S_{t}^{1}$. For the reasons which will become clear in the next section when we consider concrete examples of spectra we choose $\left(\mathbf{P}^{1}, \infty\right)$ as the model for $S_{s}^{1} \wedge S_{t}^{1}$ used in the definition of $S H$.

Definition 5.7 The stable $\mathbf{A}^{1}$-homotopy category over $S$ is the category

$$
S H(S)=H_{\bullet}^{\mathbf{A}^{1}}(S)\left[\left[\left(\mathbf{P}^{1}, \infty\right)^{-1}\right]\right]
$$

We denote $S H(S)$ simply by $S H$ and the suspension spectrum functor $\Sigma_{\left(\mathbf{P}^{1}, \infty\right)}^{\infty}$ by $\Sigma^{\infty}$. The canonical functor $S W \rightarrow S H$ described on objects by (15) respects both the symmetric monoidal and the triangulated structures. In particular Propositions 4.11-4.13 have straightforward analogs in $S H$ and in view of Theorem 5.2 the same is true for the Connectivity Theorem 4.14.

According to Theorem 5.6(1) and Lemma 4.1 for any $n \geq 0$ we have canonical isomorphisms

$$
\Sigma^{\infty}\left(S_{s}^{n}\right) \wedge \Sigma^{\infty}\left(S_{t}^{n},-n\right) \cong \mathbf{1} ; \quad \Sigma^{\infty}\left(S_{t}^{n}\right) \wedge \Sigma^{\infty}\left(S_{s}^{n},-n\right) \cong \mathbf{1}
$$
and therefore we can define objects $S_{s}^{n}$ and $S_{t}^{n}$ of $S H$ for all $n \in \mathbf{Z}$ as follows

$$
S_{s}^{n}=\left\{\begin{array}{lll}
\Sigma^{\infty}\left(S_{s}^{n}\right) & \text { for } & n \geq 0  \tag{16}\\
\Sigma^{\infty}\left(S_{t}^{n},-n\right) & \text { for } & n \leq 0
\end{array} \quad S_{t}^{n}=\left\{\begin{array}{lll}
\Sigma^{\infty}\left(S_{t}^{n}\right) & \text { for } & n \geq 0 \\
\Sigma^{\infty}\left(S_{s}^{n},-n\right) & \text { for } & n \leq 0
\end{array}\right.\right.
$$

\section*{6 Three cohomology theories}

To any object $\mathbf{E}$ of $S H$ we assign a cohomology theory $E^{p, q}(-)$ and a homology theory $E_{p, q}(-)$ on $S p c_{\bullet}$ given by

$$
\begin{aligned}
& E^{p, q}(X, x)=\operatorname{Hom}_{S H}\left(\Sigma^{\infty}(X, x), S_{s}^{p-q} \wedge S_{t}^{q} \wedge \mathbf{E}\right) \\
& E_{p, q}(X, x)=\operatorname{Hom}_{S H}\left(S_{s}^{p-q} \wedge S_{t}^{q}, \mathbf{E} \wedge \Sigma^{\infty}(X, x)\right)
\end{aligned}
$$

The reason for this somewhat strange indexing is hidden in connections with the theory of motives. Propositions 4.11-4.13 together with Lemma 4.7 imply that any cohomology or homology theory constructed in this way has three types of long exact sequences called respectively Mayer-Vietoris, Gysin and blow-up exact sequences.

One can give a formal definition of a cohomology theory as a collection of functors $S p c_{\bullet} \rightarrow A b$ satisfying some simple axioms and use Theorem 5.5 together with [16, Th. 3.1] to prove that any such theory is of the form $E^{p, q}$ for an object $\mathbf{E}$ of $S H$. Usefulness of this construction is restricted by the fact that in any formulation I know one has to start with a family of functors defined on the category of all spaces or, at least, on the subcategory of spaces of finite type and not just on the category of smooth schemes over $S$. On the other hand as the example of algebraic cobordism considered below shows the direct correspondence $\mathbf{E} \mapsto\left(E^{p, q}(-)\right)_{p, q \in \mathbf{Z}}$ allows one to give simple definition for theories which would otherwise be hard to construct. The possibility to use the stable homotopy category to produce theories with desired properties is one of the key ingredients in the proof of the Milnor conjecture given in [26].

\subsection*{6.1 Motivic cohomology}

Let us first define the Eilenberg-MacLane spectrum $\mathbf{H}_{\mathbf{Z}}$ which represents a theory $H_{\mathbf{Z}}^{p, q}(-)=H^{p, q}(-, \mathbf{Z})$ called motivic cohomology (with integral coefficients). It is an analog of ordinary cohomology in the $\mathbf{A}^{1}$-homotopy theory. The theory of motivic cohomology described here was developed in [5] and [25] before the $\mathbf{A}^{1}$-homotopy theory was introduced. The first definition in terms of the stable homotopy category was given in [26]. The only technical result about motivic cohomology which we can not obtain as a specialization of general results in $\mathbf{A}^{1}$ homotopy theory is Theorem 6.2. If we knew how to prove this theorem without going through all the moves of [24] and [5] a major part of these papers would become obsolete at least as far as the theory of motivic cohomology is concerned. But we do not.

The tricky part in getting the $\mathbf{A}^{1}$-analog of the topological Eilenberg-MacLane spectrum is to guess what the Eilenberg-MacLane spaces in $S p c_{\bullet}$ are. The obvious
idea to take a space $K(\mathbf{Z}, n)$ which has the property that for any connected $U$

$$
\pi_{i, U}(K(\mathbf{Z}, n))=\left\{\begin{array}{lll}
0 & \text { for } & i \neq n  \tag{17}\\
\mathbf{Z} & \text { for } \quad i=n
\end{array}\right.
$$

does not work. To build a spectrum out of $K(\mathbf{Z}, n)$ 's we would have to specify assembly morphisms $\left(\mathbf{P}^{1}, \infty\right) \wedge K(\mathbf{Z}, n) \rightarrow K(\mathbf{Z}, n+1)$ but a simple computation shows that any morphism of the form $\left(\mathbf{P}^{1}, \infty\right) \wedge(X, x) \rightarrow K(\mathbf{Z}, n+1)$ is trivial in the $\mathbf{A}^{1}$-homotopy category. The correct approach was discovered by A. Suslin around 1987. The idea is to define the $\mathbf{A}^{1}$-analogs of the EilenbergMacLane spaces through the Dold-Thom Theorem. For a pointed topological space $(T, *)$ let $\operatorname{Symm}^{\infty}(T, *)$ be its infinite symmetric product $\operatorname{Symm}^{\infty}(T, *)=$ $\operatorname{colim}_{n} \operatorname{Symm}^{n}(T, *)$ where $\operatorname{Symm}^{n}(T, *)=(T, *)^{\times n} / \Sigma_{n}$ and the maps Symm $\rightarrow$ Symm $^{n+1}$ send $\left(x_{1}, \ldots, x_{n}\right)$ to $\left(x_{1}, \ldots, x_{n}, *\right)$. The Dold-Thom Theorem [4] says that for a connected pointed CW-complex $(T, *)$ the space $\operatorname{Symm}^{\infty}(T, *)$ is weakly equivalent to the product $\prod_{i>0} K\left(H_{i}(T), i\right)$ where $H_{i}(T)$ are the integral homology of $T$. To formulate Dold-Thom Theorem for spaces which are not necessarily connected one considers $\operatorname{Symm}^{\infty}(T, *)$ as a topological monoid with respect to the obvious addition and takes its group completion $\left(\operatorname{Symm}^{\infty}(T, *)\right)^{+}$. The general Dold-Thom theorem then says that

$$
\left(\operatorname{Symm}^{\infty}(T, *)\right)^{+} \cong \prod_{i \geq 0} K\left(H_{i}(T), i\right)
$$

for any $T$ and that in the case of a connected $T$ the group completion does not change the homotopy type of $\operatorname{Symm}^{\infty}(T, *)$. In particular one way to define $K(\mathbf{Z}, n)$ for all $n \geq 0$ is to set

$$
K(\mathbf{Z}, n)=\left(\operatorname{Symm}^{\infty}\left(S^{n}\right)\right)^{+}
$$

Once we understand the correct analog of the symmetric product construction in the $\mathbf{A}^{1}$-context this definition works perfectly well and gives us EilenbergMacLane spaces which fit together into the Eilenberg-MacLane spectrum representing motivic cohomology.

Assume for a moment that the base scheme $S$ is regular. For a smooth scheme $X$ over $S$ and a smooth connected scheme $U$ define $c(U, X)$ as the free abelian group generated by closed irreducible subsets $Z$ of $U \times X$ which are finite and surjective over $U$. For any morphism $U_{1} \rightarrow U_{2}$ over $S$ one can define the base change homomorphism $c\left(U_{2}, X\right) \rightarrow c\left(U_{1}, X\right)$ which makes $c(-, X)$ into a contravariant functor from $S m / S$ to abelian groups. One can verify easily that this functor takes elementary distinguished squares to Cartesian squares i.e. that it is a space in the sense of our definition. We consider it as a pointed space with the distinguished point given by zero and denote by $L(X)$. If $S$ is not regular the correct definition of $c(U, X)$ and $L(X)$ becomes more technical and requires the theory of realtive equidimensional cycles developed in [22]. In the notations of that paper $c(U, X)=c\left(U \times_{S} X / U, 0\right)([22$, p.30]). The graph of any morphism $U \rightarrow X$ is an element of $c(U, X)$ which gives us canonical maps $\operatorname{Hom}(U, X) \rightarrow c(U, X)$ i.e. a morphism of spaces $X \rightarrow L(X)$.

It turns out that the space $L(X)$ plays the role of $\left(\operatorname{Symm}^{\infty}\left(X_{+}\right)\right)^{+}$in our context. Intuitively one can see this as follows. Assume $S=\operatorname{Spec}(k)$ and $X$ is a smooth variety over $k$. Consider first the subspace $L^{\text {eff }}(X)$ in $L(X)$ which consists of formal linear combinations of closed subsets with nonnegative coefficients. A point in $L^{\text {eff }}(X)$ i.e. an element in $\operatorname{Hom}_{S p c}\left(p t, L^{\text {eff }}(X)\right)=c^{\text {eff }}(\operatorname{Spec}(k), X)$ is, by definition, a formal linear combination of closed points of $X$ with nonnegative coefficients which is exatly what one would expect from points of the infinite symmetric product. The whole space $L(X)$ is clearly obtained from $L^{\text {eff }}(X)$ by the naive group completion with respect to the obvious abelian monoid structure on $L^{\text {eff }}(X)$. A detailed discussion of how $L(X)$ relates to usual symmetric products for quasi-projective varieties over a field $k$ can be found in $[21, \S 6]$ and especially in $[21$, Th. 6.8$]$ where

$$
z_{0}^{e f f}(Z)=\left\{\begin{array}{lll}
L(Z) & \text { if } & \operatorname{char}(k)=0  \tag{18}\\
L(Z)[1 / \operatorname{char}(k)] & \text { if } & \operatorname{char}(k)>0
\end{array}\right.
$$

To define Eilenberg-MacLane spaces we should apply this construction to our spheres $S_{s}^{n} \wedge S_{t}^{m}$. To do it we have to say what $L(X)$ is for a space which is not a smooth scheme. Instead of giving a general definition we only consider spaces of the form $X /\left(\cup_{i=1}^{n} Z_{i}\right)$ where $X$ is a smooth scheme and $Z_{i}$ 's are smooth subschemes in $X$ such that all the intersections of $Z_{i}$ 's are also smooth over $S$. We call such spaces scheme-like. This class includes in particular the spaces $S_{s}^{n} \wedge S_{t}^{m}$ for all $n, m \geq 0$ and it is closed under smash products. We set

$$
L\left(X /\left(\cup_{i=1}^{n} Z_{i}\right)\right)=\left(L(X) /\left(\sum_{i=1}^{n} L\left(Z_{i}\right)\right)\right)_{a b}
$$

where the subscript $a b$ indicates that we take the quotient in the category of abelian group spaces and then forget the abelian group structure. It can be shown that any morphism of scheme-like spaces $f: X \rightarrow Y$ induces homomorphism $L(f): L(X) \rightarrow L(Y)$ and that for an $\mathbf{A}^{1}$-weak equivalence $f$ the morphism $L(f)$ is also an $\mathbf{A}^{1}$-weak equivalence.

DEFINITION $6.1 K(\mathbf{Z}(n), 2 n)=L\left(\left(\mathbf{P}^{1}, \infty\right)^{\wedge n}\right)$

The notation $K(\mathbf{Z}(n), 2 n)$ has the same origin as the indexing in the definition of $E^{p, q}$ 's and as Theorem 6.3 below shows is consistent with this indexing. In view of Lemma 4.1 and previous discussion this definition reads

$$
K(\mathbf{Z}(n), 2 n) \cong\left(\operatorname{Symm}^{\infty}\left(\left(S_{s}^{1} \wedge S_{t}^{1}\right)^{\wedge n}\right)\right)^{+}
$$

One can show that the "wrong" Eilenberg-MacLane space $K(\mathbf{Z}, n)$ specified by (17) is weakly equivalent to $L\left(S_{s}^{n}\right)$.

For any smooth schemes $X, Y$ over $S$ there is a billinear morphism $L(X) \times$ $L(Y) \rightarrow L(X \times Y)$ defined by external product of relative cycles (see [22, p. 54]) which is natural in $X$ and $Y$. This implies that for scheme-like spaces $X, Y$ we have a canonical morphism $L(X) \wedge L(Y) \rightarrow L(X \wedge Y)$. In particular we have canonical morphisms

$$
m_{m, n}: K(\mathbf{Z}(m), 2 m) \wedge K(\mathbf{Z}(n), 2 n) \rightarrow K(\mathbf{Z}(n+m), 2 n+2 m)
$$

Composing $m_{1, n}$ with the morphism $i \wedge I d$ where $i$ is the canonical morphism $\left(\mathbf{P}^{1}, \infty\right) \rightarrow L\left(\mathbf{P}^{1}, \infty\right)$ we get the assembly morphisms of the Eilenberg-MacLane spectrum $\mathbf{H}_{\mathbf{Z}}$

$$
e_{n}:\left(\mathbf{P}^{1}, \infty\right) \wedge K(\mathbf{Z}(n), 2 n) \rightarrow K(\mathbf{Z}(n+1), 2 n+2)
$$

The main thechnical result about the motivic cohomology spectrum is the following theorem. This is the only theorem in the paper for which we do not know a good proof.

THEOREM 6.2 Let $S$ be a smooth variety over a field $k$ of characteristic zero. Then the spaces $K(\mathbf{Z}(n), 2 n)$ are quasi-fibrant (Definition 3.9) and the morphisms

$$
\tilde{e}_{n}: K(\mathbf{Z}(n), 2 n) \rightarrow \Omega_{\left(\mathbf{P}^{1}, \infty\right)}^{1} K(\mathbf{Z}(n+1), 2 n+2)
$$

adjoint to the assembly morphisms are $\mathbf{A}^{1}$-weak equivalences.

Conjecturally the statement of Theorem 6.2 should be true for any regular base scheme $S$. There is an example of a normal surface over $\mathbf{C}$ with an isolated nonrational singularity for which the second half of the theorem does not hold. The only reason the condition on the characteristic of the base field appears in the theorem is because the proof is based on techniques developed in [5] and in particular requires [5, Lemma 5.4] which in turn uses Hironaka's resolution of singularities. Theorem 6.3 has the following corollary.

THEOREM 6.3 Let $U$ be a smooth quasi-projective variety over a field of characteristic zero. Then for any $n, i \geq 0$ there is a canonical isomorphism

$$
H_{\mathbf{Z}}^{2 n-i, n}\left(U_{+}\right)=\pi_{i}\left(\operatorname{Sing}_{*}(K(\mathbf{Z}(n), 2 n)(U), *)\right)
$$

The groups on the right hand side can be easily identified with the motivic cohomology groups defined in [5, Definition 9.2] where the notation $H^{p}(-, \mathbf{Z}(q))$ is used instead of $H_{\mathbf{Z}}^{p, q}(-)$. Together with [5, Th. 8.2, Th. 8.3(1)] and [25, Prop. 4.2.9] this gives the following comparison between our motivic cohomology and higher Chow groups introduced by S. Bloch in [2].

THEOREM 6.4 Let $U$ be a smooth quasi-projective variety over a field of characteristic zero. Then there are canonical isomorphisms

$$
H_{\mathbf{Z}}^{p, q}\left(U_{+}\right)=C H^{q}(U, 2 q-p)
$$

\subsection*{6.2 Algebraic K-theory}

The next cohomology theory which we are going to discuss is algebraic K-theory. This theory is the best known one of the three theories considered here and it is also the least convenient one to define in terms of the stable homotopy category. The first definition of higher K-groups which works properly for all Noetherian schemes was given by $\mathrm{B}$. Thomason in [23]. An $\mathbf{A}^{1}$-homotopy invariant version of algebraic K-theory which agrees with Thomason K-theory for regular schemes
was defined by C. Weibel in [27]. What follows gives a description of a spectrum BGL which represents a theory which after reindexing coincides on $S m / S$ with Weibel's homotopy K-theory. The construction given here is very ugly and I am sure that there exists a better way to do it.

Denote by $B G L(d)$ the infinite Grassmannian $B G L(d)=\operatorname{colim}_{N \geq d} G(d, N)$ where $G(d, N)$ is the Grassmannian of linear subspaces of dimension $d$ in the standard linear space of dimension $N$ which we denote by $\mathcal{O}^{N}$. The maps $G(d, N) \rightarrow G(d, N+1)$ take $L \subset \mathcal{O}^{N}$ to $L \oplus\{0\} \subset \mathcal{O}^{N} \oplus \mathcal{O}$. We have canonical monomorphisms $B G L(d) \rightarrow B G L(1+d)$ which take $L \subset \mathcal{O}^{N}$ to $\mathcal{O} \oplus L \subset \mathcal{O} \oplus \mathcal{O}^{N}$ and we denote by $B G L$ the colimit $\operatorname{colim}_{d \geq 0} B G L(d)$. The spectrum representing algebraic K-theory is defined as follows

$$
\mathbf{B G L}=\left(E x^{\mathbf{A}^{1}}(B G L \times \mathbf{Z}), e:\left(\mathbf{P}^{1}, \infty\right) \wedge E x^{\mathbf{A}^{1}}(B G L \times \mathbf{Z}) \rightarrow E x^{\mathbf{A}^{1}}(B G L \times \mathbf{Z})\right)
$$

where $B G L \times \mathbf{Z}=\coprod_{i \in \mathbf{Z}} B G L$ and $E x^{\mathbf{A}^{1}}(B G L \times \mathbf{Z})$ is a fibrant replacement of $B G L \times \mathbf{Z}$ in the sense of the closed model structure of Theorem 3.7. The reason we have to take $\operatorname{Ex}^{\mathbf{A}^{1}}(B G L \times \mathbf{Z})$ instead of $B G L \times \mathbf{Z}$ itself is that the only way I know to define the assembly morphism is to define first a morphism $\bar{e}:\left(\mathbf{P}^{1}, \infty\right) \wedge(B G L \times \mathbf{Z}) \rightarrow B G L \times \mathbf{Z}$ in the homotopy category and then say that any morphism in the homotopy category with values in a fibrant object can be lifted to the category of spaces. It is a little ugly but it works. To specify $e$ we will use the following result proven in [14].

THEOREm 6.5 For any smooth scheme $X$ over $S$ and any $i \geq 0$ there is a canonical map

$$
K_{i}(X) \rightarrow \operatorname{Hom}_{H_{\bullet}}\left(S_{s}^{i} \wedge X_{+}, B G L \times \mathbf{Z}\right)
$$

which is a bijection if $S$ is regular (the K-groups on the left are Thomason K-groups [23]).

For a pointed scheme $(X, x)$ denote by $K_{n}(X, x)$ the subgroup of $K_{n}(X)$ which consists of elements vanishing on $x$. For a pair of pointed smooth schemes $(X, x)$, $(Y, y)$ denote by $K_{i}((X, x) \wedge(Y, y))$ the subgroup in $K_{i}(X \times Y)$ which consists of elements vanishing on $X \times\{y\} \subset X \times Y$ and on $\{x\} \times Y \subset X \times Y$. Note that this is always a direct summand in $K_{i}(X \times Y)$. Theorem 6.5 has the following corollary.

Corollary 6.6 Let $(X, x),(Y, y)$ be pointed smooth schemes over $S$. Then for any $i \geq 0$ there is a canonical map

$$
K_{i}((X, x) \wedge(Y, y)) \rightarrow \operatorname{Hom}_{H \bullet}\left(S_{s}^{i} \wedge(X, x) \wedge(Y, y), B G L \times \mathbf{Z}\right)
$$

which is a bijection if $S$ is regular.

To define the assembly morphism of the spectrum BGL we want to use Corollary 6.6 to compute the set of morphisms $\left(\mathbf{P}^{1}, \infty\right) \wedge(B G L \times \mathbf{Z}) \rightarrow B G L \times \mathbf{Z}$ in the $\mathbf{A}^{1}$-homotopy category. Unfortunately $B G L$ is not a smooth scheme but a colimit of filtered system of such schemes which makes us to use the following lemma.

Lemma 6.7 Let $\left(X_{n}, i_{n}:\left(X_{n}, x_{n}\right) \rightarrow\left(X_{n+1}, x_{n+1}\right)\right)$ be an inductive system of pointed spaces such that all the morphisms $i_{n}$ are monomorphisms and $(Y, y)$ be a pointed space such that all the maps

$$
\operatorname{Hom}_{H}\left(S_{s}^{1} \wedge\left(X_{n+1}, x_{n+1}\right),(Y, y)\right) \rightarrow \operatorname{Hom}_{H}\left(S_{s}^{1} \wedge\left(X_{n}, x_{n}\right),(Y, y)\right)
$$

induced by $I d \wedge i_{n}$ are surjective. Then the canonical map

$$
\operatorname{Hom}_{H}\left(\operatorname{colim}_{n}\left(X_{n}, x_{n}\right),(Y, y)\right) \rightarrow \lim _{n} \operatorname{Hom}_{H}\left(\left(X_{n}, x_{n}\right),(Y, y)\right)
$$

is bijective.

Projective bundle theorem for algebraic K-theory together with standard geometrical constructions imply that the embeddings of Grassmannians $G(d, N) \rightarrow G(1+$ $d, 1+N+1)$ induce surjections of K-groups $K_{n}(G(1+d, 1+N+1)) \rightarrow K_{n}(G(d, N))$ for all $n \in \mathbf{Z}$. The same projective bundle theorem applied to the trivial bundle of dimension one implies that $K_{n}\left(\left(\mathbf{P}^{1}, \infty\right) \wedge(X, x)\right)=K_{n}(X, x)$ for any pointed smooth scheme $(X, x)$ over $S$. Thus Lemma 6.7 implies that for a regular scheme $S$ one has

$$
\begin{gathered}
\operatorname{Hom}_{H}\left(\left(\mathbf{P}^{1}, \infty\right) \wedge(B G L \times \mathbf{Z}), B G L \times \mathbf{Z}\right)= \\
=\lim _{d} \operatorname{Hom}_{H}\left(\left(\mathbf{P}^{1}, \infty\right) \wedge\left(\coprod_{i=-d}^{d} G(d, 2 d)\right), B G L \times \mathbf{Z}\right)= \\
\lim _{d} K_{0}\left(\left(\mathbf{P}^{1}, \infty\right) \wedge\left(\coprod_{i=-d}^{d} G(d, 2 d)\right)\right)=\lim _{d} K_{0}\left(\coprod_{i=-d}^{d} G(d, 2 d)\right)= \\
\lim _{d} \operatorname{Hom}_{H}\left(\coprod_{i=-d}^{d} G(d, 2 d), B G L \times \mathbf{Z}\right)=\operatorname{Hom}_{H}(B G L \times \mathbf{Z}, B G L \times \mathbf{Z})
\end{gathered}
$$

Denote by $e$ the morphism $\left(\mathbf{P}^{1}, \infty\right) \wedge(B G L \times \mathbf{Z}) \rightarrow B G L \times \mathbf{Z}$ corresponding under these identifications to the identity morphism of $B G L \times \mathbf{Z}$ and define the assembly morphism of the spectrum BGL as a morphism of spaces which projects to $e$ in the homotopy category. This defines BGL for regular base schemes $S$. To get BGL for any $S$ one uses the inverse image functor on the homotopy categories associated with the canonical morphism $S \rightarrow \operatorname{Spec}(\mathbf{Z})$. As an easy corollary of this construction of $\mathbf{B G L}$ we get the following periodicity theorem.

ThEOREm 6.8 There is a canonical isomorphism BGL $=S_{s}^{1} \wedge S_{t}^{1} \wedge \mathbf{B G L}$.

Thus from the point of view of the $\mathbf{A}^{1}$-theory algebraic $\mathrm{K}$-theory is periodic with period $(2,1)$ which is why it is usually written with only one index instead of two. While the construction of BGL presented here is not very nice it is actually easy to prove comparison theorems with it.

Theorem 6.9 For any Noetherian base scheme $S$ and any smooth scheme $X$ over $S$ one has canonical isomorphisms

$$
B G L^{p, q}\left(X_{+}\right)=K H_{2 q-p}(X)
$$
where $K H$ is the homotopy K-theory of [27]. In particular for a regular base $S$ one has

$$
B G L^{p, q}\left(X_{+}\right)=K_{2 q-p}(X)
$$

where $K$ is the $K$-theory of [23].

\subsection*{6.3 Algebraic CObordism}

Algebraic cobordism was introduced in [26] as one of the tools necessary for the proof of the Milnor conjecture. According to our current understanding it is the universal cohomology theory which has direct image homomorphisms for all smooth proper morphisms. It is represented by a spectrum MGL $=\left(M G L(n), e_{n}\right)$ completely analogous to the Thom spectrum representing complex cobordism in the topological homotopy theory.

Recall that for a vector bundle $E$ over $X$ we defined its Thom space as $T h(E)=E /(E-s(X))$ where $s: X \rightarrow E$ is the zero section. For any morphism $f: X \rightarrow Y$ and a vector bundle $E$ over $Y$ we have a canonical morphism of spaces $T h\left(f^{*} E\right) \rightarrow T h(E)$. Let $E_{n, N}$ be the universal bundle over the Grassmannian $G(n, N)$. The embeddings $G(n, N) \rightarrow G(n, N+1)$ induce morphisms $T h\left(E_{n, N}\right) \rightarrow T h\left(E_{n, N+1}\right)$ and we define $M G L(n)$ as $\operatorname{colim}_{N} T h\left(E_{n, N}\right)$. To define assembly morphisms note that if $\mathcal{O}$ is the trivial bundle of dimension one then $T h(\mathcal{O} \oplus E)=\left(\mathbf{A}^{1} / \mathbf{A}^{1}-\{0\}\right) \wedge T h(E)$. For the embeddings $f: G(n, N) \rightarrow G(1+$ $n, 1+N)$ we have canonical isomorphisms $f^{*}\left(E_{1+n, 1+N}\right)=\mathcal{O} \oplus E_{n, N}$ which implies that we have canonical morphisms $e_{n}^{\prime}:\left(\mathbf{A}^{1} / \mathbf{A}^{1}-\{0\}\right) \wedge M G L(n) \rightarrow M G L(n+1)$. Since the elementary distinguished square corresponding to the standard covering $\mathbf{P}^{1}=\mathbf{A}^{1} \cup \mathbf{A}^{1}$ is a pushforward square the morphism of quotient spaces $\mathbf{A}^{1} /\left(\mathbf{A}^{1}-\{0\}\right) \rightarrow \mathbf{P}^{1} /\left(\mathbf{P}^{1}-\{0\}\right)$ is an isomorphism. The inverse gives us a morphism $\phi:\left(\mathbf{P}^{1}, \infty\right) \rightarrow \mathbf{A}^{1} /\left(\mathbf{A}^{1}-\{0\}\right)$. We define the assembly morphisms of the Thom spectrum MGL as compositions $e_{n}=e_{n}^{\prime} \circ(\phi \wedge I d)$.

Since algebraic cobordism is a new theory we can not formulate here a comparison theorem as we have done with motivic cohomology and algebraic K-theory. Instead I will end this section with a conjecture which describes a part of algebraic cobordisms in terms of the usual complex cobordism ring $M U^{*}$.

CONJECtURe 1 For any $S$ there is a natural homomorphism $\oplus_{i=-\infty}^{\infty} M U^{2 i} \rightarrow$ $\oplus_{i=-\infty}^{\infty} M G L^{2 i, i}(S)$ which is an isomorphism if $S$ is local and regular.

\section*{7 Concluding Remarks}

This paper outlines the very basics of the $\mathbf{A}^{1}$-homotopy theory. One reason I did not say more about concrete computations such as the description of the motivic Steenrod algebra is that at the moment these computations can only be done in the case when $S$ is a variety over a field of characteristic zero. This is partly due to the conditions of Theorem 6.2 and partly to technical difficulties in the proof of Spanier-Whitehead duality.

One of the two major directions of current work on the theory is to eliminate this restriction. There are two sources of new techniques which I believe will allow us to do it. One is related to the study of functoriality of the stable homotopy
categories with respect to $S$. There is a theory here which is largely parallel to the functoriality for the constructible sheaves in the etale topology [13, Ch.VI]. It allows in particular to prove the Spanier-Whitehead duality for smooth proper schemes over any base. However, just as in the etale theory there are certain statements which apparently require some kind of resolution of singularities (in the etale case this is for example the theorem saying that $\mathbf{R} p_{*}(\mathbf{Z} / n)$ is constructible for any morphism $p$ of finite type [13, VI.5.7]). Surprisingly the same kind of problems comes up when one tries to generalize Theorem 6.2. I am rather optimistic about these problems at the moment. My optimism is mostly based on the amazing proof which Spencer Bloch gave for his localization theorem for higher Chow groups in [3]. It seems that he found a way to use Spivakovsky's solution of Hironaka's polyhedra game ([20]) instead of resolution of singularities to deal with problems essentially similar to the ones mentioned above.

The second main direction of current work can be described as an attempt to find an algebro-combinatorial description of $\mathbf{A}^{1}$-homotopy types. We do have a very hypothetical theory of rational homotopy type. The rational homotopy type of a scheme $S$ is a differential graded Hopf algebra (commutative, not cocommutative) $\mathcal{H}_{\mathbf{Q}}(S)$ over $\mathbf{Q}$ such that the derived category of modules over $\mathcal{H}_{\mathbf{Q}}(S)$ is equivalent to the triangulated subcategory $D M^{l c}(S, \mathbf{Q})$ of local systems in the derived category $\operatorname{DM}(S, \mathbf{Q})$ of modules over the Eilenberg-MacLane spectrum $\mathbf{H}_{\mathbf{Q}}$ over $S$.

In topological context $\mathcal{H}_{\mathbf{Q}}(T)$ is the differential graded Hopf algebra associated with the cosimplicial Hopf algebra $C^{*}\left(\Omega^{1} T\right)$ of singular cochains on the first loop space of $T$ and $D M^{l c}(T, \mathbf{Q})$ is the full subcategory of complexes with locally constant cohomology sheaves in the derived category of consructible sheaves of Q-vector spaces on $T$.

In the particular case $S=\operatorname{Spec}(k)$ the (weak) $K(\pi, 1)$-conjecture says that $\mathcal{H}_{\mathbf{Q}}(S)$ is the Hopf algebra of functions on a proalgebraic group $\operatorname{Gal}_{\mathcal{M}, \mathbf{Q}}(k)$ (in particular it sits entirely in grading zero). This group is called the motivic Galois group of $k$. The category $D M^{l c}(S, \mathbf{Q})$ is in this case equivalent to the whole category $D M(S, \mathbf{Q})$ and the equivalence of the derived categories mentioned above becomes the known hypothetical correspondence between motives and representations of the motivic Galois group [15]. This wonderful picture whose origins go back to Grothendieck's idea of motives ([7], [12], [15]) must have an analog for integral homotopy types. All my attempts to find such an analog even in the case when $S$ is the spectrum of an algebraically closed field of characteristic zero so far failed. We have a lot of knowledge about torison effects in the motivic category and this knowledge does not want to fit into any nice scheme.

\section*{REFERENCES}

[1] J. F. Adams. Stable homotopy and generalized homology. University of Chicago Press, 1974.

[2] S. Bloch. Algebraic cycles and higher K-theory. Adv. in Math., 61:267-304, 1986 .

Documenta Mathematica $\cdot$ Extra Volume ICM $1998 \cdot$ I $\cdot$ 579-604

[3] S. Bloch. The moving lemma for higher Chow groups. J. Algebr. Geom., 3(3):537-568, Feb. 1994.

[4] A. Dold and R. Thom. Quasifaserungen und unendliche symmtrische Produkte. Ann. of Math., 67:230-281, 1956.

[5] E. M. Friedlander and V. Voevodsky. Bivariant cycle cohomology. http://www.uiuc.edu/K-theory, (75), 1995.

[6] S. I. Gelfand and Yu. I. Manin. Methods of homological algebra. SpringerVerlag, Berlin, 1996.

[7] A. Grothendieck. Standard conjectures on algebraic cycles. In Algebraic geometry. International Colloq., Tata Inst., Bombay 1968, pages 193-199. Oxford Univ. Press, London, 1969.

[8] M. Hovey, B. Shipley, and J. Smith. Symmetric spectra. http://hopf.math.purdue.edu/pub/Hovey-Shipley-Smith/, 1998.

[9] J.F. Jardine. Algebraic homotopy theory. Canadian J. Math., 33(2):302-319, 1981.

[10] J.F. Jardine. Algebraic homotopy theory and some homotopy groups of algebraic groups. C. R. Math. Rep. Acad. Sci. Canada, 3(4):191-196, 1981.

[11] S. MacLane. Categories for working mathematician, volume 5 of Graduate texts in Mathematics. Springer-Verlag, 1971.

[12] Yu. Manin. Motifs and monoidal transformations. Math. of the USSR Sbornik, 6(4):439-470, 1968.

[13] J.S. Milne. Etale Cohomology. Princeton Univ. Press, Princeton, NJ, 1980.

[14] F. Morel and V. Voevodsky. A ${ }^{1}$-homotopy theory of schemes. Preprint, 1998.

[15] Motives, volume 54-55 of Proc. of Symp. in Pure Math. AMS, 1994.

[16] A. Neeman. The Grothendieck duality theorem via Bousfield's techniques and Brown representabilty. J. Amer. Math. Soc., 9(1):205-236, 1996.

[17] A. Neeman. On a theorem of Brown and Adams. Topology, 36(3):619-645, 1997.

[18] A. Neeman. Brown representability for the dual. Inv. Math., 133(1):97-105, 1998.

[19] J. Smith. Private communication. 1998.

[20] M. Spivakovsky. A solution to Hironaka's polyheda game. In Arithmetic and Geometry, volume 2, pages 419-432. Birkhauser, Boston, 1983.

[21] A. Suslin and V. Voevodsky. Singular homology of abstract algebraic varieties. Inv. Math., 123(1):61-94, 1992.

[22] A. Suslin and V. Voevodsky. Relative cycles and Chow sheaves. http://www.math.uiuc.edu/K-theory, (35), 1994.

[23] R. Thomason and T. Trobaugh. Higher algebraic K-theory of schemes and of derived categories. In The Grothendieck festchrift, volume 3, pages 247-436. Birkhauser, Boston, 1990.

[24] V. Voevodsky. Homology of schemes II. http://www.math.uiuc.edu/K-theory, (34), 1994.

[25] V. Voevodsky. Triangulated categories of motives over a field. http://www.math.uiuc.edu/K-theory, (74), 1995.

[26] V. Voevodsky. The Milnor Conjecture. Max-Planck Inst. preprint series or http://www.math.uiuc.edu/K-theory (170), 1996.

[27] C. Weibel. Homotopy K-theory. In Algebraic K-theory and algebraic number theory, volume 83 of Contemp. Math., pages 461-488. AMS, Providence, 1989.

Vladimir Voevodsky

Department of Mathematics

Northwestern University

Evanston IL USA

vladimir@math.nwu.edu



\end{document}

# See Also

# Meta
## References
![[_reference_voevodsky_A1]]


## Citations and Footnotes
[^1]: Voevodsky, abstract