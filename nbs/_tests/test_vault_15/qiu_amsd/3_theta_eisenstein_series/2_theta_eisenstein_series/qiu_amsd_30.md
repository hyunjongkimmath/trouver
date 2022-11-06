---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/qiu_amsd]
---
# Topic[^1]

From now on,   ${\mathbb {W}}$ is  always assumed to be of dimension 1. %Moreover, except in \ref{Theta-Eisenstein seriesdef}, ${\mathbb {W}}$ is always assumed to be incoherent.
\subsubsection{Definition}\label{Theta-Eisenstein seriesdef}


Let $V^\sharp/E$ be  a    hermitian space of dimension $n>0$. Let $\chi_{V^\sharp}$ be a character of $E^\times\backslash {\mathbb {A}}_E^\times$ such that $\chi_{V^\sharp}|_{{\mathbb {A}}_F^\times}=\eta^{n}$.
Let ${\mathbb {V}}=    {\mathbb {W}}\oplus V^\sharp({\mathbb {A}}_E)$ be the orthogonal direct sum and $\chi _{\mathbb {V}}=\chi_{{\mathbb {W}}}\chi_{V^\sharp}$.  We have the  corresponding Weil representations.
Below we shall use $\omega$ to denote a Weil representation if the hermitian space is indicated in the context, e.g by the function that it acts on.

For $ \phi\in {\mathcal {S}}\left( {\mathbb {V}}\right)$, we  define a  theta-Eisenstein series   $ {E\theta}(s,g,\phi)$ on $G$ associated the to the  orthogonal
decomposition ${\mathbb {V}}=    {\mathbb {W}}\oplus V^\sharp({\mathbb {A}}_E)$:
\begin{equation} {E\theta} (s,g,\phi)= \sum_{\gamma\in P(F)\backslash G(F)}\delta (\gamma  g)^{s }  \sum_{x\in V^\sharp{{}}%\newcommand{\qclE}{{(E)}}}  \omega (\gamma g)\phi ((0,x)).\label{thetae}
\end{equation}
If $\phi=\phi_1\otimes \phi_2$ with $\phi_1\in  {\mathcal {S}}\left( {\mathbb {W}}\right)$  and  $\phi_2\in  {\mathcal {S}}\left( V^\sharp({\mathbb {A}}_E)\right)$,
then  \begin{equation} {E\theta}(s,g,\phi)= E(s,g,\phi_1) \theta(g, \phi_2)  \label{thetae1}.
\end{equation}
%In particular,  %from the absolute  convergence of Eisenstein series  (see \ref{Siegel-Eisenstein series}),
%  \eqref{thetae}
% is absolutely convergent if ${\mathrm{Re}} s>1/2$, and has a meromorphic continuation to the entire  complex plane, holomorphic at $s=0$.
For    $t\in F$, let  ${E\theta} _t (s,g,\phi)$ be the $\psi_t$-Whittaker function  of ${E\theta}  (s,g,\phi)$.

\subsubsection{Coherent case}
Assume that ${\mathbb {W}}=W({\mathbb {A}}_E)$  is coherent.   The regularized Siegel-Weil formula \eqref{Ichthm}    immediately  implies the following  ``mixed   Siegel-Weil formula":
  \begin{equation}\label{Ichthm1}  {E\theta}(0,g,\phi)=\frac{2}{{\mathrm{Vol}}([U(W)])}  \int _{[U(W)]} \theta(g,h,\phi) dh.\end{equation}
(We will prove an arithmetic analog of \eqref{Ichthm1} for ${\mathbb {W}}$ being incoherent in \ref{Arithmetic mixed Siegel-Weil formula}.) Then
for $t\in F$, 
\begin{equation}\label{Evdec1100} {E\theta}_{t} (0,g,\phi) = \frac{2}{ {\mathrm{Vol}}([U(W)]) }  \int_{  [U(W)]}\sum_{x\in   V  ^t   }  \omega(g)\phi(h^{-1} x)dh.
\end{equation}   
For $\phi$   invariant by $U(W(E_v), v\in \infty$,   the integration in \eqref{Evdec1100}  is  a finite sum.
\subsubsection{Incoherent case}
In the rest of this  section, assume that ${\mathbb {W}}$ is incoherent.

For a place $v$ of $F$ nonsplit in $E$, let $W$ be the $v$-nearby hermitian space of ${\mathbb {W}}$.
For  $\phi=\phi_{1}\otimes \phi_{2}$ with $\phi_{1}\in  {\mathcal {S}}\left(  {\mathbb {W}}_v \right)$,  $\phi_2\in  {\mathcal {S}}\left( V^\sharp(E_v)\right)$ and  
$x=(x_1,x_2)\in V:= W(E_v)\oplus V^\sharp(E_v)$ with $ x_1\neq 0,$  let 
\begin{equation}   {W\theta}_{v,x}(s,g,\phi)=  \frac{L(1,\eta_v)}{  {\mathrm{Vol}}(U(W(E_v))}  
W^\circ_{v,q(x_1)}(s,g,\phi_1)  \omega (g)\phi_2(x_2)   \label{thetaw1}\end{equation}
This is a local analog  of  \eqref{thetae1}.
%Extend this definition to general Schwartz functions by linearity.
Extend this definition to $ {\mathcal {S}}\left(  {\mathbb {W}}_v \right)\otimes {\mathcal {S}}\left( V^\sharp(E_v)\right)\subset  {\mathcal {S}}\left(  {\mathbb {V}}_v  \right)$ by linearity.
The inclusion is an equality unless $v\in \infty$. However, this subspace is enough for our purpose.
(Besides, there is another definition of ${W\theta}_{v,x}$ for  the whole  $  {\mathcal {S}}\left(  {\mathbb {V}}_v  \right)$.
We will not   need it.)
%Besides, later we will only use such decomposable functions.
   For $v$ nonsplit in $E$ and $t\neq 0$,   define 
 \begin{equation}\label{Evdec11} {E\theta}'_{t} (0,g,\phi) (v) = \frac{2}{ {\mathrm{Vol}}([U(W)]) }  \int_{  [U(W)]}\sum_{x\in   V  ^t -V^\sharp }  {W\theta}_{v,h_v^{-1}x} '(0, g_v, \phi_v)   \omega(g^v)\phi^v(h^{v,-1} x)dh.
\end{equation} 
Note that the  analog of  \eqref{2.9} does not hold.
%where $W$ is the $v$-nearby hermitian space of ${\mathbb {W}}$ and $V=W\oplus V^\sharp$.


%By    \eqref{ET'dec} and that $ {\mathrm{Vol}}([U(W)])=2L(1,\eta)$, we have   the following lemma.
%\begin{lem} \label{E'dec11} Assume that $\phi=\phi_1\otimes \phi_2$ with $\phi_1\in  {\mathcal {S}}\left( {\mathbb {W}}\right)$  and  $\phi_2\in  {\mathcal {S}}\left( V^\sharp({\mathbb {A}}_E)\right)$. Then
%$$ {E\theta} '_t (0,g,\phi) =-\sum_{v \ \text{nonsplit} }{E\theta}'_{t}(0,g,\phi)(v)+E_0'(0,g,\phi_1)
%\sum_{x\in \left( V^\sharp\right)^t}  \omega (  g)\phi _2(x).$$\end{lem} 





   \subsubsection{Properties of ${W\theta}_{v,x} '(0,g,\phi)$}\label{PPPsg}

We study ${W\theta}_{v,x} '(0,g,\phi)$   following  \cite{YZZ}. Indeed,   the computation is only on the Eisenstein (i.e. Whittaker)  part. 
We remind the reader of the difference  between the modulus characters mentioned in \ref{modulus character}.


By \eqref{translaw1}, \eqref{translaw}  and Lemma \ref{lSWlem}, we have the following lemma, which says that under the action of $P(F_v)$,  ${W\theta}_{v,x} '(s_0,   g , \phi )$ behaves in the same was as the Weil representation.


# See Also

# Meta
## References
![[_reference_qiu_amsd]]


## Citations and Footnotes
[^1]: Citation, 30