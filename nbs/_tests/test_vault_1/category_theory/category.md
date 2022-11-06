A category $\mathcal{C}$ consists of a class or collection of **objects** and for each pair of objects $A$ and $B$, a class or collection of **maps**, **arrows**, or **morphisms** $\operatorname{Mor}_\mathcal{C}(A,B) = \operatorname{Mor}(A,B)$ satisfying the following:
1. For objects $A,B,C$ and morphisms $f \in \operatorname{Mor}(A,B)$ and $g \in \operatorname{Mor}(B,C)$, there is a **composition** $g \circ f \in \operatorname{Mor}(A,C)$.
	1. Composition is associative, i.e. if 
		- $f \in \operatorname{Mor}(A,B)$
		- $g \in \operatorname{Mor}(B,C)$
		- $h \in \operatorname{Mor}(C,D)$
	then $(h \circ g) \circ f = h \circ (g \circ f)$.
2. For each object $A$, there is a (unique) morphism $\operatorname{id}_A \in \operatorname{Mor}(A,A)$, called the **identity morphism of $A$** such that 
	1. For all objects $B$ and $g \in \operatorname{Mor}(B,A)$, we have $\operatorname{id}_A \circ g = g$.
	2. For all objects $B$ and $g \in \operatorname{Mor}(A,B)$, we have $g \circ \operatorname{id}_A = g$.

The notation $f: A \to B$ is used to denote that $f \in \operatorname{Mor}(A,B)$.

The collection of objects of $\mathcal{C}$ is denoted by $\operatorname{Ob}(\mathcal{C})$