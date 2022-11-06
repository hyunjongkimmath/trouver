---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]


\paragraph{Organization of the Paper} For technical reasons, the paper is written in the order (Step II $\Rightarrow$ Step I $\Rightarrow$ Step I+), which is different from the sketch of proofs. In \S2 we recall results on the motives and monodromy of $h^{2, 0} = 1$ varieties and extract the geometric input we need from Moonen's paper. In \S3, we recall the moduli interpretation of conjugate Shimura varieties, so that we may set up period morphisms axiomatically. In \S4, we define relative de Rham cycles in terms of Riemann-Hilbert correspondences, and give a criterion for an isomorphism between weight $2$ Hodge structures coming from motives to be de Rham. In \S5, we set up the integral period morphisms and compare the cohomology sheaves with automorphic sheaves. The genericity theorem is proved in \S6. In \S7, we prove some lemmas about families of curves that homogeneously dominate a variety, and in \S8 and \S9, we prove Thm~\ref{thm: BSD}-\ref{thm: Gushel-Mukai}. 

\paragraph{Notations} Let $f : X \to S$ be a morphism between schemes. If $T \to S$ is another morphism, denote by $X_T$ the base change $X \times_S T$.  We say that $X$ is an $S$-variety if it is separated and of finite type. We use $\mathrm{H}^i_\mathrm{{\acute{e}}t}(X/S, A)$ (resp. $\mathrm{H}^i_\mathrm{dR}(X/S)$) to denote $\mathbb{R}^i f_{\mathrm{{\acute{e}}t}*} A$, whenever $A = \mathbb{Z}_\ell$ or $\mathbb{Q}_\ell$ for $\ell \in \mathcal{O}_S^\times$ (resp. $\mathbb{R}^i f_* \Omega^\bullet_{X/S}$). Given $T \to S$, we may simply write $\mathrm{H}^i_\mathrm{{\acute{e}}t}(X|_T, A)$ (resp. $\mathrm{H}^i_\mathrm{dR}(X|_T)$) for $\mathrm{H}^i_\mathrm{{\acute{e}}t}(X_T/T, A)$ (resp. $\mathrm{H}^i_\mathrm{dR}(X_T/T)$). If $S$ is a $\mathbb{C}$-variety, apply the same conventions to the relative Betti cohomology.  

For an irreducible scheme $X$, we write $k(X)$ for its fraction field and $\eta(X)$ or $\eta_X$ for its generic point. In particular, if $x$ is a point, we write $k(x)$ for its residue field. If $k$ is an algebraically closed field, and $X$ is a (not necessarily irreducible) $k$-variety, by ``a general $k$-point has property $P$'' we mean ``there exists an open dense subscheme $U \subseteq X$ such that every $k$-point on $U$ has property $P$''.

Unless otherwise noted, letters $p$ and $\ell$ will always denote some prime numbers and $\ell \neq p$. We write $\widehat{\mathbb{Z}}$ for the profinite completion of $\mathbb{Z}$ and $\widehat{\mathbb{Z}}^p$ for its prime-to-$p$ part. Define $\mathbb{A}_f := \widehat{\mathbb{Z}} {\otimes} \mathbb{Q}$ and $\mathbb{A}^p_f := \widehat{\mathbb{Z}}^p {\otimes} \mathbb{Q}$. If $k$ is a perfect field of characteristic $p$, we write $W(k)$ for its ring of integers and or simply $W$ when $k$ is understood. For any field $k$, denote by $\bar{k}$ a chosen algebraic closure when such a choice does not need to be specified. For any object $M$ over $\mathbb{C}$ and $\sigma \in \mathrm{Aut}(\mathbb{C})$, denote $M {\otimes}_\sigma \mathbb{C}$ by $M^\sigma$ whenever applicable. 

We use the following abbreviations: VHS for ``variations of Hodge structures'', LHS (resp. RHS) for ``left (resp. right) hand side'', and ODP for ``ordinary double point''. 

\noindent \textbf{Acknowledgements.}
We wish to thank Jordan Ellenberg, Philip Engel, Shizhang Li, Yuchen Fu, Davesh Maulik, Martin Orr, Alex Petrov, Ananth Shankar, Mark Shusterman, Yunqing Tang, Lenny Taelman, Daichi Takeuchi, Kai Xu, Ruijie Yang for helpful conversations or email correspondences. A special thank goes to Dori Bejleri for generously helping us with lots of technical questions about elliptic surfaces. P.H.\ is partially supported by ERC Consolidator Grant 770936: NewtonStrat. X.Z.\ is partially supported by the Simons Collaborative Grant 636187, NSF grant DMS-2101789, and NSF FRG grant DMS-2052665.

Finally, Z.Y. wishes to thank his PhD advisor Mark Kisin, who keeps encouraging him to think about the Tate conjecture. 



# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, 9