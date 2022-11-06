---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/qiu_amsd]
---
# Topic[^1]
  

\begin{rmk} The automorphic form in \Cref{gnm11} (2) can be made explicit:
\begin{equation}    \label{Proposition 4.1.5}
c_1(L)^{n-1}\cdot z\left(\omega(g)\phi\right) =-c_1(L)^{n}  E(0,g, \phi).  
\end{equation} 
This is  
a geometric version of the Siegel-Weil formula \eqref {Ichthm}. 
It is  stated  in \cite[COROLLARY 10.5]{Kud97} for the orthogonal case, the proof carries  over to the unitary case.



\end{rmk}

\subsubsection{Kudla's Green function}\label{Kudla's Green function}
We recall Kudla's Green functions for special divisors   \cite{Kud1}, following \cite[8.3]{Zha19} in the unitary case.
We consider simple special divisors $Z(x)$'s, instead of weight special divisors $Z_t(\phi)$'s.
%  We extend the definition of special divisors as follows.
For $x\in   {\mathbb {V}}^{\infty} $ such that ${q(x)}\in F ^\times -F_{>0}$,    let $Z(x)_K= 0$. 

First, we  work on  ${\mathbb {B}}_n$.
For    $v\in \infty$, let $V$ is the unique hermitian space over $E$ such that $V({\mathbb {A}}_E^v)\simeq {\mathbb {V}}^v$ and $V(E_v)\simeq {\mathbb {C}}^{1,n}$.   %Abuse notation   and still use  $v$ to denote the restriction of $v$ to $F$.
For
$g\in G(F_v)$ and $x\in V-\{0\}$, define  
$$G^{\mathrm{Kud}}(x,g)(z)=-{\mathrm{Ei}}(-2\pi \delta_v(g) R_x(z))
$$ 
where ${\mathrm{Ei}}$ is  the exponential integral. %   \eqref{Ei}. 
Then $G^{\mathrm{Kud}}(x,g)$ is a (non-admissible) Green function for ${\mathbb {B}}_x$. If ${\mathbb {B}}_x$  is empty, then $G^{\mathrm{Kud}}$ is smooth.


Now we work on  ${\mathrm{Sh}}({\mathbb {V}})_K$. 
Let $x\in  {\mathbb {V}}^\infty  $  with $q(x)\in F^\times$. 
For  $v\in \infty$, if $u(q(x))>0$  for every $u\in \infty-\{v\}$,  
by the Hasse-Minkowski theorem and Witt's theorem,
there exists  $h\in U({\mathbb {V}}^\infty)$
and $x^{(v)}\in V-\{0\}$, where $V$ is as in the last paragraph, such that $ x=h^{-1}x^{(v)}$.
Define 
\begin{equation}{\mathcal {G}}^{\mathrm{Kud}}_{Z( x)_{E_v}}(g)=\sum_{j=1}^m\sum_{y\in U(V)x^{(v)}\cap h_jK h^{-1}x^{(v)}} G^{\mathrm{Kud}}(x,g) .\label{Gzhx}\end{equation}
By   \eqref{zhx}, this is a Green function for $Z(x)_{E_v}$. 
If $u(q(x))<0$  for some $u\in \infty-\{v\}$,    ${\mathcal {G}}^{\mathrm{Kud}}_{Z(x)_{E_v}}(g)=0$.
% In particular, if $q(x)$ is negative at more than 1 infinite places,  then  ${\mathcal {G}}^{\mathrm{Kud}}_{Z(x)_{E_v}}(g)=0$ for every $v\in \infty$. 



%For $x=0$, let 
% \begin{equation}G^{\mathrm{Kud}}(0,g)(z)=-\log |\delta(g)|_{E_v}\label{GK0} .\end{equation} %(this term is one of the terms to be added to the metric of Hodge bundle).  




% Taking linear combination, we get  a Green function $ {\mathcal {G}}^{\mathrm{Kud}}_{Z_t(\phi)_{E_v}}$ of $Z_t(\phi)_{E_v}$ .

Besides Kudla's Green functions, 
we will need their projections to the constant function $1$ to modify  the  normalized  Green function  (see \ref{Conjecture}).





# See Also

# Meta
## References
![[_reference_qiu_amsd]]


## Citations and Footnotes
[^1]: Citation, 51