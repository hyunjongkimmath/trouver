---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]



The degree of the discriminant $\mathrm{disc}(x^3 + Ax + B)$ is $12n = e(X)$. Recall that the genus $g(C)$ is equal to the irregularity $q(X)$ and we have $p_g(X) = n - 1 + g(C)$. Therefore, elliptic surfaces with $p_g = 1$ fall into two types: 

\begin{itemize}
    \item $n = 2$ and $g(C) = 0$. These are elliptic K3 surfaces. 
    \item $n = g(C) = 1$. These surfaces have Kodaira dimension $1$. 
\end{itemize}

We are interested in the latter class. Note that although these surfaces are elliptic fibrations over genus $1$ curves, one should not confuse them with \textit{bielliptic surfaces}, which are of Kodaira dimension $0$. 


For future reference we introduce some notation. Let $S$ be a base scheme and $V$ be a vector bundle over $S$. We denote by $\mathbb{A}(V)$ the relative affine space over $S$ defined by $V$ and $\mathbb{A}(V)^*$ the open part of $\mathbb{A}(V)$ minus the zero section. Given a sequence of numbers $q= (q_0, \cdots, q_m)$ and vector bundles $V_0, \cdots, V_m$ such that $V = \oplus_{i = 0}^m V_i$, we denote by $\mathcal{P}_{q}(V)$ the resulting \textit{weighted projective stack}, i.e., the quotient stack of $\mathbb{G}_m$-action on $V$ given by 
$$ \lambda \colon (v_0, \cdots, v_m) \mapsto (\lambda^{q_0} v_0, \cdots, \lambda^{q_m} v_m) \text{ for } \lambda \in \mathbb{G}_m, $$
and by $\mathbb{P}_{q}(V)$ the coarse moduli space of $\mathcal{P}_q(V)$. It is well known that this coarse moduli space can be constructed explicitly by applying the relative Proj functor to a sheaf of graded algebras over $S$. We omit the details. If $q$ is not specified, then it is assumed to be $(1, \cdots, 1)$.


\begin{construction}
\label{constr: family of ES over S}
Let $S$ be a $\mathbb{Z}[1/6]$-scheme, $\varpi \colon \mathcal{C} \to S$ be a family of smooth projective curves over $S$ of genus $g$ and $\mathcal{L}$ be a relative line bundle on $\mathcal{C}$ of degree $h$. Assume that $4h \ge 2g - 1$ and $h \ge 1$. Let $\mathcal{V}_r$ denote the vector bundle $\varpi_* \mathcal{L}^r$ for $r \ge 4$. Let $\widetilde{\mathcal{X}}$ be the subscheme of $\mathbb{A}(\mathcal{V}_4 \oplus \mathcal{V}_6)^* \times \mathbb{P}(\mathcal{L}^2 \oplus \mathcal{L}^3 \oplus \mathcal{O}_\mathcal{C})$ defined by the Weierstrass equation (\ref{eqn: Weierstrass for elliptic surfaces}) in the obvious way. Let $\mu$ be the $\mathbb{G}_m$-action on $\mathbb{A}(\mathcal{V}_4 \oplus \mathcal{V}_6)^* \times \mathbb{P}(\mathcal{L}^2 \oplus \mathcal{L}^3 \oplus \mathcal{O}_\mathcal{C})$ defined by 
\begin{equation}
\label{eqn: mu action stack}
    \lambda \cdot ((a_4, a_6), [x : y : z]) = ((\lambda^4 a_4, \lambda^6 a_6), [\lambda^2 x : \lambda^3 y : z]), \text{ for } \lambda \in \mathbb{G}_m.
\end{equation}
Let $\mathcal{Q}(\mu)$ denote the quotient stack of the $\mathbb{G}_m$-action $\mu$. Then $\widetilde{\mathcal{X}}$ descends to an algebraic substack $\mathcal{X}$ of $\mathcal{Q}(\mu)$. Note that $\mathcal{Q}(\mu)$, and hence $\mathcal{X}$, admit natural morphisms to $\mathcal{P}_{(4, 6)}(\mathcal{V}_4 \oplus \mathcal{V}_6)$.
\end{construction}  


 We remark that these stacks are only ``stacky'' because of the base. 



# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, 53