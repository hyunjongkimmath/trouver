---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/qiu_amsd]
---
# Topic[^1]
\label{Green functions}

\subsubsection{Complex uniformization}\label{Complex uniformization}
For nonnegative integers $p,q$,  let ${\mathbb {C}}^{p,q}$ be the $p+q$ dimensional hermitian space associated to the hermitian matrix 
${\mathrm{diag}}(-1_p,1_q)$. %We will consider ${\mathbb {C}}^{1,n}$, i.e. the hermitian  matrix is ${\mathrm{diag}}(-1,1,1,...,1).$  
Let $U\left({\mathbb {C}}^{1,n}\right)$ be the unitary group of  ${\mathbb {C}}^{1,n}$ (so of signature $(n,1)$ in the usual convention). 
Let ${\mathbb {B}}_n$ be the complex open unit ball of dimension $n$. 
Embed  ${\mathbb {B}}_n$  in ${\mathbb {P}}({\mathbb {C}}^{1,n})$ as the set of negative lines as follows:
the  point  $[z_1,...,z_n]\in {\mathbb {B}}_{n}$ under the usual coordinate, where $\sum_{i=1}^{n}|z_i|^2<1$,   is   the line containing  the vector $(1,z_1...,z_n) $.  
Then $U\left({\mathbb {C}}^{1,n}\right)$   acts on ${\mathbb {B}}_n$  naturally  and transitively. 
Let $\Omega$ be the tautological bundle  of negative lines, and $\overline \Omega$ the hermitian line bundle with the metric induced from the negative of the hermitian form.
The Chern form of $\overline \Omega$ is a 
$U\left({\mathbb {C}}^{1,n}\right)$-invariant 
K\"ahler form
\begin{equation}c_1(\overline\Omega)= \frac{1}{2\pi i } \partial \bar\partial \log (1-\sum_{i=0}^{n-1}|z_i|^2).\label{mun}\end{equation}  
%Let the volume form on ${\mathbb {B}}_n$ be $\Omega^n$ (instead of $\frac{1}{n!}\Omega^n$). 
For an arithmetic subgroup $\Gamma\subset U({\mathbb {C}}^{1,n})$, on (the orbifold) $\Gamma\backslash{\mathbb {B}}_n $, we have the descent $\overline\Omega_\Gamma$ of $\overline\Omega$ whose (orbifold) Chern curvature  form  is the descent of $c_1(\overline\Omega)$. 
Define the degree $$\deg(\overline\Omega_\Gamma)=\int_{\Gamma\backslash{\mathbb {B}}_n} c_1(\overline\Omega_
\Gamma)^n.$$
If $\Gamma\backslash {\mathbb {B}}_n$ is compact,  this degree   is the usual degree via intersection theory.

Let $v$ be an infinite place of $F$. 
Let $V$ be the unique hermitian space over $E$ such that $V({\mathbb {A}}_F^v)\simeq {\mathbb {V}}^v$ and $V_v\simeq {\mathbb {C}}^{1,n}$. 
We have the complex uniformization of    the base change   to $E_v\simeq {\mathbb {C}}$: %(see \cite[Remark 3.2]{RSZ-arithmetic-diagonal-cycles})
\begin{equation}\label{compl}{\mathrm{Sh}}({\mathbb {V}})_{K,E_v} \simeq   U(V)\backslash(   {\mathbb {B}}_n \times  U({\mathbb {V}}^\infty)/K). \end{equation}
Then the Hodge bundle $L_{E_v}$ is the descent of $\Omega\times 1_{U({\mathbb {V}}^\infty)/K}$ and let $\overline{L}_{E_v}$ be the descent of $\overline \Omega\times 1_{U({\mathbb {V}}^\infty)/K}$. % Define $\deg(\overline{L}_{E_v})$ as above.

% Equip ${\mathrm{Sh}}({\mathbb {V}})_{K,E_v}$ with this K\"ahler form and volume form. 




Now we consider special divisors.
For $x\in {\mathbb {C}}^{1,n}-\{0\}$,
let ${\mathbb {B}}_x\subset {\mathbb {B}}_n$ be the subset of  negative lines  perpendicular to $x$.
If ${q(x)}\leq 0$, then ${\mathbb {B}}_x$ is empty.
If ${q(x)}>0$, then ${\mathbb {B}}_x$ is a complex unit ball of  dimension $n-1$.  
The following function  on ${\mathbb {B}}_n$ will be important for us later:
$$R_x(z)=-\frac{|\pair{x,\widetilde z}|^2}{\pair{\widetilde z,\widetilde z}}$$
where $\widetilde z $ is a nonzero vector contained in the  line  $z$.   
If    $x\in V-\{0\}$, then  $\Gamma\cap U (x^\perp)$ is   an arithmetic subgroup
of $U (x^\perp)$. 
Let   $C(x,\Gamma)$ be    the pushforward of the fundamental cycle by 
$$\left( \Gamma \cap U(x^\perp)\right) \backslash {\mathbb {B}}_x \to \Gamma \backslash {\mathbb {B}}_n.$$
Define $$\deg_{\overline\Omega_\Gamma}(C(x,\Gamma))=\int_{C(x,\Gamma)} c_1(\overline\Omega_
\Gamma)^{n-1}.$$
%This is also $\deg({\overline\Omega_{\Gamma\cap U(x^\perp)}})$ by definition.


For $x\in V$, regard $x$ as an element in ${\mathbb {V}}^\infty$.
For $h\in U({\mathbb {V}}^\infty)$,  we  have $h^{-1}x\in {\mathbb {V}}^\infty$.  Assume that $q(x)\neq 0$
Then the special divisor $Z(h^{-1}x)_{E_v}$ on    ${\mathrm{Sh}}({\mathbb {V}})_{K,E_v}$ is  represented  by 
\begin{equation}
\{(z,h_1h): z\in {\mathbb {B}}_x, \ h_1\in U(x^\perp) \}\label{zhx0}\end{equation}
via \eqref{compl}.   
%(Recall that we have defined $Z(h^{-1}x)_{E_v}=\emptyset$ is $q(x)\not\in F_{>0}$.)
Let $h_1,. . .,h_m$ be a set of representatives of  $U(V)\backslash U({\mathbb {V}}^\infty)/K$. 
Let $\Gamma_{h_j}=U(V)\cap h_jKh_j^{-1}$.  
Then we have
(see \cite[p 56]{Kud97})
\begin{equation}
Z(h^{-1}x)_{E_v}=\sum_{j=1}^m\sum_{y\in \Gamma_{h_j}\backslash U(V)x\cap h_jK h^{-1}x} C(y,\Gamma_{h_j}).\label{zhx}\end{equation}
By \cite[Lemma 3.1]{Liu}, every element of $  {\mathbb {V}}^\infty_{>0} $    is of the form $h^{-1}x$ for some $x$ with $q(x)\in F_{>0}$ as above. Thus we have  decomposed    special cycles into geometrically connected components.


\subsubsection{Admissible Green functions}\label{Admissible Green functions}

Admissible Green functions are Green functions with harmonic curvatures (see Appendix \ref{until}). 
Admissible Green functions  for special divisors are constructed  by  Bruinier \cite{Bru}, Oda and Tsuzuki \cite{OT}.  For $F={\mathbb {Q}}$ and $n=1$, it  appeared in the work of   Gross and Zagier \cite{GZ} for $n=1$.
We learned the following explicit computation from S. Zhang.

The following special case is important: embed  ${\mathbb {B}}_{n-1}$ in ${\mathbb {B}}_n$ via    $${\mathbb {C}}^{1,n-1}\hookrightarrow {\mathbb {C}}^{1,n},\   (z_1,...,z_{n-1})  \mapsto  (z_1,...,z_{n-1},0)  .$$
Then ${\mathbb {B}}_{n-1}$ is  ${\mathbb {B}}_{(0,...,0,1) }$.   
The same embedding  ${\mathbb {C}}^{1,n-1}\hookrightarrow {\mathbb {C}}^{1,n}$ also fixes an embedding  $U\left({\mathbb {C}}^{1,n-1}\right)\hookrightarrow U\left({\mathbb {C}}^{1,n}\right)$.
The action of $U\left({\mathbb {C}}^{1,n-1}\right)$ on ${\mathbb {B}}_{n-1}$ is compatible with the embeddings. 


We look for a $U\left({\mathbb {C}}^{1,n-1}\right)$-invariant smooth function $G$ on ${\mathbb {B}}_n-{\mathbb {B}}_{n-1}$ 
such that $G(z_1,...,z_n)+\log|z_n|^2 $ is a smooth function on ${\mathbb {B}}_n,$
%(so $G$ is a Green current of ${\mathbb {B}}_{n-1}$ by the Poincar\'e-Lelong formula \cite[1.3.1.1]{GS},)  
$\lim_{|z|\to 1}G(z) =0,$ 
and   
%\begin{equation}\label{ppg} \frac{i}{2\pi } G\wedge \omega^{n-1}=\epsilon G\omega^n.\end{equation}
\begin{equation*} \frac{i}{2\pi } \partial \bar\partial G =\frac{s(s+n) }{2}G \cdot {c_1(\Omega)},\ s\in {\mathbb {C}}  .\end{equation*}
A solution of this equation will be a solution of the Laplacian equation 
\begin{equation}\left(\frac{i }{2\pi } \partial \bar\partial G \right) {c_1(\Omega)}^{n-1}=\frac{s(s+n) }{2}G \cdot {c_1(\Omega)}^{n}  .\label{ppg}\end{equation}

The quotient of  
${\mathbb {B}}_n-{\mathbb {B}}_{n-1}$ by  $U\left({\mathbb {C}}^{1,n-1}\right)$ is isomorphic to $(1,\infty)$ via 
$$z=[z_1,...,z_n]\mapsto t(z):= 1+ R_{ (0,...,0,1) }\left( z\right)=\frac{1-\sum_{i=1}^{n-1}|z_i|^2}{1-\sum_{i=1}^{n}|z_i|^2} .$$
Thus we look for  $G=Q(t(z))$ where $Q$ is a smooth function on $(1,\infty)$ such that $ Q(t)+ \log( t-1) $   extends to a smooth function on ${\mathbb {R}}$. 
By \eqref{mun} and the $U\left({\mathbb {C}}^{1,n-1}\right)$-invariance, 
\eqref{ppg} is reduced to the
following   hypergeometric differential equation
\begin{equation*} \left( t-t^2\right) \frac{d^2Q}{dt^2}  +\left( n-(n+1)t\right)\frac{dQ}{dt} +s(s+n) Q=0,\ t\in (1,\infty).\label{ODE1} \end{equation*} 
For ${\mathrm{Re}} s>-1$, there is a unique solution $Q_s$ such that $Q_s(t)+\log (t-1)$  extends to a smooth function on ${\mathbb {R}}$  and $\lim_ {t\to\infty}Q_s(t)=0$:
\begin{equation} \label{Qs} Q_s(t)=\frac{\Gamma(s+n)\Gamma(s+1)}{\Gamma(2s+n+1)t^{s+n}}  F\left( s+n,s+1,2s+n+1;\frac{1}{t},\right), \ t>1\end{equation} 
where $F$ is the hypergeometric function. (See also \cite[2.5.3]{OT}. 
When 
$n=1$, our $Q_s$ is   the Legendre function of the second kind in \cite[238]{GZ}   up to  shifting $s$ by 1).

Finally, for $x\in {\mathbb {C}}^{1,n}$, we define  $$G_{x,s}(z)=Q_s\left( 1+R_x(z)\right).$$ 
Explicitly,  if  $ x=(x_1,x_2)\in {\mathbb {C}}^{1,n}= {\mathbb {C}}^{1,0}\oplus {\mathbb {C}}^{0,n} $, then 
\begin{equation}G_{x,s}([0,...,0]) =Q_s\left( 1-{q(x_1)}\right).\label{GQs}\end{equation}


Now, we define admissible Green functions of special divisors on Shimura varieties.
Let $\Gamma$ be an arithmetic lattice in $U\left({\mathbb {C}}^{1,n}\right)$.
 Let $$g_s=\sum_{\gamma\in \Gamma}\gamma^*G_{(0,...,0,1) ,s}.$$


# See Also

# Meta
## References
![[_reference_qiu_amsd]]


## Citations and Footnotes
[^1]: Citation, 49