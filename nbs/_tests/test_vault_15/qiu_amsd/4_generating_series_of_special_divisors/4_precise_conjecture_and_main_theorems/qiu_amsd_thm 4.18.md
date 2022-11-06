---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/qiu_amsd]
---
# Topic[^1]
\begin{thm} \label{hypothm} 
Assume Assumption \ref{asmp1}.

(1) For $K\in {{\widetilde K_\Lambda}}$, there is a regular integral model  ${\mathcal {X}}_K$ of  ${\mathrm{Sh}}({\mathbb {V}})_{K}$ over ${\mathrm{Spec}} {\mathcal {O}}_{E}$ such that ${\mathcal {X}}_{K, {\mathcal {O}}_{E,(v)}}\simeq \mathscr{S}_v$  as integral models (see   \ref{integral modeldef}). Moreover, Assumption \ref{A11asmp11} holds for  ${\mathcal {X}}_K$.

(2) There is   a   finite flat morphism  $\pi _{K,K' }:{\mathcal {X}}_{K }\to {\mathcal {X}}_{K' }$  extending
the natural morphism ${\mathrm{Sh}}({\mathbb {V}})_{K }\to {\mathrm{Sh}}({\mathbb {V}})_{K' }$.

(3) Regard ${\mathcal {X}}_{K }$ as an $ {\mathcal {X}}_{K_{\Lambda} }$-scheme and ${\mathrm{Sh}}({\mathbb {V}})_{K }$ as an $ {\mathrm{Sh}}({\mathbb {V}})_{K_{\Lambda} }$-scheme  via    
$\pi _{K,K' }$. 
There is   an action of $K_\Lambda/K$ (note that 
$K$ is normal in $K_{\Lambda}$) on  the $ {\mathcal {X}}_{K_{\Lambda} }$-scheme ${\mathcal {X}}_{K }$    extending  the standard action of $K_\Lambda/K$ on the $ {\mathrm{Sh}}({\mathbb {V}})_{K_{\Lambda} }$-scheme  ${\mathrm{Sh}}({\mathbb {V}})_{K }$  by ``right translation".

(4) There is an ample ${\mathbb {Q}}$-bundle ${\mathcal {L}}_{K_{\Lambda}}$ on  ${\mathcal {X}}_{K_{\Lambda}}$ extending  $L_{K_{\Lambda}}$.  

 

\end{thm}
\begin{proof} The construction  of ${\mathcal {X}}_K$  is as follow. Continue to use the notation $M$ in the proof of Lemma \ref{regmod}.   
First,  consider the analog of the morphism  \eqref{map-mathcalM-Gtilde-to-mathcal-M0} over ${\mathcal {O}}_M[R^{-1}]$ where $R$ is a finite set of finite places of $ {\mathbb {Q}}$ such that
$K_v=K_{\Lambda,v}$ for $v$ not over $R$ (in particular, we do not need the Drinfeld level structure and  matching condition in \ref{defn-mathscrS-G2} and other parahoric level structures in \ref{AT-parahoric-level-section}).  See for example \cite[5.1]{RSZ-arithmetic-diagonal-cycles} with extra level structures over $R$ (similar to %\eqref{leveloutp0} and
\eqref{leveloutp}). Denote this morphism by ${\mathcal {M}}\to {\mathcal {M}}_0$.
We use Galois descent to construct a model of ${\mathrm{Sh}}({\mathbb {V}})_K$  outside finitely many finite places.  
 Let $N/M$ be a finite   extension, Galois over $E$, such that the base change of  
${\mathcal {M}}_0$ to  ${\mathrm{Spec}} {\mathcal {O}}_{N}[R^{-1}]$ is a finite disjoint   union of  ${\mathrm{Spec}} {\mathcal {O}}_{N}[R^{-1}]$.  Let $S\supset R$ be a finite set of finite places of ${\mathbb {Q}}$ such that ${\mathrm{Spec}} {\mathcal {O}}_{N}[S^{-1}]\to {\mathrm{Spec}} {\mathcal {O}}_{E}[S^{-1}] $ is unramified.
Then the fiber of  ${\mathcal {M}}_{{\mathcal {O}}_{N}[S^{-1}]}\to {\mathcal {M}}_{0,{\mathcal {O}}_{N}[S^{-1}]}$ over  a chosen  ${\mathrm{Spec}} {\mathcal {O}}_{N}[S^{-1}]$ 
is a  regular Deligne-Mumford stack ${\mathcal {M}}^S$  proper over $ {\mathrm{Spec}} {\mathcal {O}}_{N}[S^{-1}]$  with generic fiber  ${\mathrm{Sh}}({\mathbb {V}})_{K,N}$. 
By Zariski's main theorem (for stacks which easily follows from the scheme version),  after possibly enlarging $S$, we may assume that   the action of the finite group ${\mathrm{Gal}}(N/E)$ on  ${\mathrm{Sh}}({\mathbb {V}})_{K,N}$ extends to an action on ${\mathcal {M}}^S$. 
By  \cite[Section 6, Example]{BLR} (see \cite{Vis1} for the stack case), after  possibly enlarging $S$,  
${\mathcal {M}}^S$  descends to ${\mathrm{Spec}} {\mathcal {O}}_{E}[S^{-1}]$.
 Let ${\mathcal {Y}} ^S$ be the resulted  Deligne-Mumford stack.  By construction and  \ref{Corollary 2.30}, we have ${\mathcal {Y}} ^S_{{\mathcal {O}}_{E,(v)}}\simeq \mathscr{S}_v$ for $v\not\in S$. 
  Now, let ${\mathcal {X}}_K$ be the glueing of ${\mathcal {Y}}^S$ and  $\mathscr{S}_v$ with $v\in S$.   Then ${\mathcal {X}}_{K, {\mathcal {O}}_{E,(v)}}\simeq \mathscr{S}_v$ for every finite place $v$.
  
We check Assumption \ref{A11asmp11}. For $K'\subset K$ small enough with $K'^S=K^S$,   the resulted  Deligne-Mumford stack ${\mathcal {Y}}'^S$   is representable \cite[5.2]{RSZ-arithmetic-diagonal-cycles}. Note that ${\mathrm{Spec}} {\mathcal {O}}_{N}[S^{-1}]\to {\mathrm{Spec}} {\mathcal {O}}_{E}[S^{-1}] $ is unramified (so finite \'etale).
Then  Assumption \ref{A11asmp11} (1) holds (with the current $S$) by construction. Similarly, assumption \ref{A11asmp11} (2) holds.

(2) and (3) 
follow easily from the construction and corresponding properties of the PEL type integral models in \cite[Theorem 5.4]{RSZ-arithmetic-diagonal-cycles}. We omit the details.


(4)   Let ${\mathcal {L}}'$ be an arbitrary extension of $L_{K_\Lambda}$. Since $L_{K_\Lambda}$ is ample, by \cite[9.6.4]{EGA-IV}, for a finite set $S$ of  finite places of $E$, ${\mathcal {L}}'[S^{-1}]$ on ${\mathcal {X}}_{K_\Lambda}[S^{-1}]$ is  ample. 
Glueing ${\mathcal {L}}'[S^{-1}]$ with $\mathscr{P}_v$'s in Lemma \ref{regmod} (2) for $v\in S$,  we get the desired 
ample ${\mathbb {Q}}$-line bundle.
%The construction in (1)   for $K=K_\Lambda$ carries over and gives a  line bundle  $\mathscr{P}^S$ over  ${\mathcal {Y}}^S  $ extending  $L_{K_\Lambda}$ (after possibly enlarging $S$). We use \qcl{qcl: Appendix \ref{SectionB} 2.11} 
\end{proof}

# See Also

# Meta
## References
![[_reference_qiu_amsd]]


## Citations and Footnotes
[^1]: Citation, thm 4.18