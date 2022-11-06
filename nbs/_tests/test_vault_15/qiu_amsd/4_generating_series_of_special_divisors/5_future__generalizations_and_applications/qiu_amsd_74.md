---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/qiu_amsd]
---
# Topic[^1]





\subsubsection{Higher codimensions}

Based on their modularity result for generating series of special divisors, Yuan, S. Zhang and W. Zhang \cite{YZZ1} proved the modularity  for higher-codimensional  special cycles inductively, assuming the convergence.  
One would like to mimic their proof in the arithmetic situation. 
%Ignore  the technicality in arithmetic  intersection theory and formally check their inductive scheme. 
Then  one  needs    a modularity theorem for divisors 
with
general level structures and test functions, even if the given test function is very good.  
Thus the generality of our  results is necessary toward   arithmetic modularity  in higher codimensions.

In the codimension $n$ case (i.e. for arithmetic 1-cycles),
S. Zhang's theory of admissible cycles is unconditional modulo  vertical 1-cycles that are numerically trivial \cite{Zha20}. % (in arithmetic intersection theory). 
Then
  the method in
the current paper is still applicable to approach the arithmetic modularity. 
   



\subsubsection{Almost-self dual lattice} 
In  the proof of Theorem \ref{main}, we use  the exotic smoothness of our integral models (see Lemma \ref{expectlem}). 
There is another level structure at a finite place considered in \cite{RSZ-arithmetic-diagonal-cycles}, defined by an almost-self dual lattice. 
The integral model is not smooth, but is explicitly described in \cite{Let}.  We hope to include this level structure in a future work.
In fact, if we also use admissible 1-cycles, 
 our approach combined with a recent result of Z. Zhang \cite[Theorem 14.6]{ZZY}
 is already  applicable to prove 
the analog of 
Theorem \ref{main}, after replacing normalized admissible extensions of special divisors by the ``admissible projections" of   the  Kudla-Rapoport divisors at these new places (provided that they can also be suitably defined on  our models).
However, the  difference  between two extensions is not clear so far. 


\subsubsection{Faltings heights of Shimura varieties and Arithmetic Siegel-Weil formula}
\label{Faltings heights of Shimura varieties and Arithmetic Siegel-Weil formula}
Following  Kudla  \cite{Kud02}\cite{Kud03}, we propose  the   arithmetic 
analog  of  the geometric Siegel Weil formula   \eqref{Proposition 4.1.5}.
\begin{problem}\label{theqSW}
 Match   $c_1(\overline {\mathcal {L}})^n\cdot  z(g, \phi)_{ {\mathfrak{a}}}^{{\mathcal {L}},\mathrm{Kud}}$ with a linear combination of 
$E(0,g, \phi)$ and $  E'(0,g, \phi)$ (possibly up to some error terms).  
\end{problem}
The  modularity of $z(g, \phi)_{ {\mathfrak{a}}}^{{\mathcal {L}},\mathrm{Kud}}$ helps to  attack this problem as follows.
The constant term of  $c_1(\overline {\mathcal {L}})^n\cdot  z(g, \phi)_{ {\mathfrak{a}}}^{{\mathcal {L}},\mathrm{Kud}}$  is indeed the Faltings height of ${\mathcal {X}}_{K}$ itself, while the non-constant terms are given by Faltings heights of Shimura subvarieties with the numbers in   Definition  \ref{GK0}. (Here, by the 
Faltings height of     ${\mathcal {X}}$, we mean   $   \deg c_1(\overline {\mathcal {L}})^{n+1}$.)
There is clearly an inductive scheme to compute the Faltings heights/attack arithmetic Siegel-Weil formula, by applying the modularity of the generating series. Moreover, 
we  only need to compute enough terms.  This might enable us to avoid   dealing with Shimura subvarieties of  general level structures from the inductive steps. 
We can also use   
$ z(g, \phi)_{{\mathfrak{k}},{\mathfrak{a}} }^{{\overline\cL}}$  to attack \Cref{theqSW}, since  by a direct computation,
\begin{equation}\label{samefal} 
c_1(\overline {\mathcal {L}})^n\cdot z(g, \phi)_{ {\mathfrak{a}}}^{{\mathcal {L}},\mathrm{Kud}} =c_1(\overline {\mathcal {L}})^n \cdot z(g, \phi)_{{\mathfrak{k}},{\mathfrak{a}} }^{{\overline\cL}}.
\end{equation}
 





For quaternionic Shimura curves, Faltings heights are computed in \cite{KRY2} \cite{Yuan}.
For unitary Shimura varieties, in the case $F={\mathbb {Q}}$, the Faltings height of ${\mathcal {X}}_{K_\Lambda}$ (for a different lattice $\Lambda$)  was computed in \cite{BH} using   Borcherds'    theory.   See  \cite{BH} for other related results. 
 
 
\subsubsection{Arithmetic theta lifting and Gross-Zagier type formula}
   Consider the inner product of   the modular generating series    of special divisors   on the generic fiber,
with a cusp form of $G$ \cite{Kud02}\cite{Kud03}. When $n=1$,  it is  cohomological trivial and its  Beilinson-Bloch
height  pairing was studied in \cite{Liu}\cite{Liu0}. However,  when $n>1$, the Picard group of ${\mathrm{Sh}}({\mathbb {V}})_K$ is CM (see \cite{KRa}), so that the inner product is 0 in most cases after cohomological trivializaion. 
Thus it is necessary to consider   arithmetic   intersection pairing  on an integral model (without  cohomological trivializaion). 
A Gross-Zagier  type formula was obtained in
 \cite{BHY}\cite{Bet2}  in the case  $\phi^\infty=1_{\Lambda}$.  
For   general test functions as in our case, a   corresponding  theory of Shimura type integrals  is to be developed. 



%We also hope that  this idea  can be used to compute the Faltings heights of Shimura varieties. For certain unitary Shimura varieties over ${\mathbb {Q}}$,  Bruinier and  Howard computed  the Faltings heights  using Borcherds' theory. 

%\subsubsection{Arithmetic fundamental lemma and trasnfer} A striking application of the modularity results of Bruinier et al. \cite{Bet}  is W. Zhang's proof of the arithmetic fundamental lemma over ${\mathbb {Q}}_p$ for the unramified  Rapoport-Zink space.  Presumably, our modularity result could be used to prove the arithmetic fundamental lemma over a general $p$-adic field following W. Zhang's strateg, as well as the arithmetic transfer   conjecture for the exotic  smooth Rapoport-Zink space. However, the arithmetic fundamental lemma over a general $p$-adic field is already a theorem of Mihatsch and W. Zhang \cite{MZ}, proved by modifying W. Zhang's original approach and using cycles  of generic degree 0 as mentioned above. Moreover, their strategy  seems also applicable to the arithmetic transfer   conjecture for the exotic  smooth Rapoport-Zink space. 

%In the sequel     \bibitem{Bet2}  of \bibitem{Bet}, several applications of 





# See Also

# Meta
## References
![[_reference_qiu_amsd]]


## Citations and Footnotes
[^1]: Citation, 74