---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/qiu_amsd]
---
# Topic[^1]
\begin{lem}\label{regmod}(1) The  integral model $\mathscr{S}_v$ is regular.
 
(2) If  $K= {K_{\Lambda}}$, there is an ample ${\mathbb {Q}}$-line bundle $\mathscr{P}_v$ on  $\mathscr{S}_v$ extending  $L_{K_\Lambda}$.  
\end{lem}
\begin{proof} (1) We apply  \ref{Corollary 2.30}. 
We use $M$ to denote the  reflex field  in \ref{Corollary 2.30}, which is defined in \eqref{reflex-field-E} (and denoted by $E$ there), to avoid confusion. We use $N$ to denote the
field extension of the  reflex field in \ref{Corollary 2.30} (denoted by $L$ there).
By the finite \'etaleness of  the moduli space of 
relative dimenison 0 as in  \ref{mathcal-M0-defn}, we may choose  $N/M$  
to be unramified at $\nu$ \cite[Tag 04GL]{stacks-project}. Then 
by  \cite{RSZ-arithmetic-diagonal-cycles} and  \ref{Corollary 2.30},  $\mathscr{S}_{v,{\mathcal {O}}_{N,(\nu)}}$ is regular for a place $\nu$ of $N$ over $v$. By the
descent of regularity under faithfully flat morphism \cite[Tag 033D]{stacks-project}, the lemma follows. 

(2)  
Let $N/E$  be a  finite Galois extension and $\nu$ a place  of $N$   unramified at $v$ 
such that every   connected component  of $\mathscr{S}_{v,{\mathcal {O}}_{N,(\nu)}}$ is  geometrically connected.   By its construction (see \eqref{defn-mathscrS-G}), every connected   component  is a quotient of 
a   connected component of an integral model of Hodge type over  ${\mathcal {O}}_{N,(\nu)}$  by a finite group action.
The  integral model of Hodge type is a closed subscheme of  the integral Siegel moduli space (see \cite{xu-normalization,PEL-embedding}), on which we have  a well-known ample  Hodge line bundle.  
The restriction is an ample  line bundle on  each  geometrically connected component of the 
  integral model of Hodge type. 
  Taking  norm along the quotient map by the finite group action, we get an
  an ample  line bundle  on every    component  of $\mathscr{S}_{v,{\mathcal {O}}_{N,(\nu)}}$  (see \cite[Section 6, Theorem 4,7 or Example B]{BLR}  and \cite{Vis1} for the stack case).
  Then taking norm map along the  quotient map by the ${\mathrm{Gal}}(N/E)$, we have an ample   line bundle $\mathscr{P}'$ on $\mathscr{S}_{v}$. 
  %The tensor product of the ${\mathrm{Gal}}(N/E)$-conjugates of $\mathscr{P}'$ descends to an ample line bundle 
%on  $\mathscr{S}_v$ by \cite[Section 6, Theorem 4]{BLR} (note that the tensor product is not just 
%${\mathrm{Gal}}(N/E)$-invariant, but also satisfies the cocycle condition automatically),
%see \cite{Vis1} for the stack case.  
 Dividing $\mathscr{P}'$ by the product of the order of the finite group and $[N:E]$, we get the desired   ample  ${\mathbb {Q}}$-line bundle  on $\mathscr{S}_{v}$. 
  \end{proof}

# See Also

# Meta
## References
![[_reference_qiu_amsd]]


## Citations and Footnotes
[^1]: Citation, lem 4.17