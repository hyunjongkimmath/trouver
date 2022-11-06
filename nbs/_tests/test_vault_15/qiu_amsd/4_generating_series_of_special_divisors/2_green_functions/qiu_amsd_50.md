---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/qiu_amsd]
---
# Topic[^1]
 


Recall that  $\widetilde{\lim\limits _{s\to 0}}$ denotes the constant term at $s=0$.
\begin{rmk}  (1) We      read the residue
$\kappa$ in  \cite[Theorem 7.8.1 (3)]{OT} as follows.
Beside the obvious differences between the choices of % the $s$-variables   %(up to shift and multiplying  2)
%and 
 Green function  %(up to multiplying  $-2$)
 here and in \cite{OT} (more precisely, $s$-variables and signs),       the K\"ahler form and ``volume form" here and in \cite{OT} are different.  
First, the K\"ahler form on the bottom of \cite[514]{OT} is $\pi c_1(\overline\Omega)$ in our notation.
Second,  \cite[Theorem 7.8.1 (3)]{OT} uses volumes to express the residue, 
while  we use degrees of line bundles to express the residue. 
%    factorial factor when defining the volume form on the  top of \cite[515]{OT}.
The volume form for $  {\mathbb {B}}_n$ on the  top of  \cite[515]{OT} is     $\frac{\pi^n}{n!}c_1(\overline\Omega)^n$ 
%and $\frac{\pi^{n-1}}{(n-1)!}c_1(\overline\Omega_
%{\Gamma'})^{n-1}$ 
in our notation.
Third, there is a $\pi$ missing in (the numerator of) the residue $\kappa$ in  \cite[Theorem 7.8.1 (3)]{OT}. It should be easy to spot from \cite[Proposition 3.1.2, Lemma 7.2.2]{OT}.

(2) When $n=1$ and $\Gamma={\mathrm{SL}}_2({\mathbb {Z}})$ via $U({\mathbb {C}}^{1,1})\simeq {\mathrm{SL}}_2({\mathbb {R}})$,  we have $\deg  (\overline\Omega_
\Gamma)=\frac{1}{12}$ (see \cite[4.10]{Kuh}). Thus for $\Gamma_0(N)$ a standard congruence subgroup of $\Gamma$, 
Theorem \ref{OTthm} (1) coincides with the residue $\frac{-12}{[\Gamma:\Gamma_0(N)]}$ in \cite[p 239, (2.13)]{GZ}.
Theorem \ref{OTthm} (1)  is not used in any other place of the paper.

\end{rmk}
By  \cite[Proposition 3.1.2]{OT} and taking care of the differences in the remark, we have 
$$\int_{\Gamma\backslash {\mathbb {B}}_n} g_s  {c_1(\overline \Omega)}^n=\frac{n\deg_{\overline\Omega_\Gamma}(C((0,...,0,1),\Gamma))}{s(s+n)}.$$
Thus
\begin{align}\label{gnm1} \int_{\Gamma\backslash {\mathbb {B}}_n}(\widetilde{\lim\limits _{s\to 0}}g_s ) {c_1(\overline \Omega)}^n=-\frac{\deg_{\overline\Omega_\Gamma}(C((0,...,0,1),\Gamma))}{n}.   \end{align}



For    $t\in F_{>0}$,   we define  the automorphic Green function  for the weighted special divisor $Z_t(\phi)$   on ${\mathrm{Sh}}({\mathbb {V}})_{K}$ as follows.     Let $v\in \infty$.  For   $s \in {\mathbb {C}}$ with ${\mathrm{Re}} s> 0$, consider the  following absolutely convergent (by \Cref{gaodingle}) sum for  $(z,h)\in \left({\mathbb {B}}_n-{\mathbb {B}}_{n-1}\right) \times  U({\mathbb {V}}^\infty)$:
\begin{align}\label{cpluni1} \sum_{x\in   V^t }   \phi\left( x_v \left( h^{-1}x\right)\right) G_{x,s}(z)
\end{align}
where $ x_v \in   {\mathbb {V}}_v $ such that ${q(x_v)}={q(x)}(=t)$ in $F_v$, and $x_v (h^{-1}x)\in {\mathbb {V}}$ has  $v$-component $x_v$
and finite component $h^{-1}x$.
By \eqref{zhx} and Theorem \ref{OTthm},   \eqref{cpluni1}
descends to a Green function for  $Z_t(\phi)_{E_v}$, which we  call $ {\mathcal {G}}_{Z_t(\phi)_{E_v},s}$.
%By \eqref{ppg}, $g_s$ satisfies $$\Delta g_s =s(s+n) g_s .$$
Define the automorphic Green function
\begin{align}\label{GGZ}  {\mathcal {G}}^{{\mathrm {aut}}}_{Z_t(\phi)_{E_v}}=\widetilde{\lim_{s\to 0}}  {\mathcal {G}}_{Z_t(\phi)_{E_v},s},   \end{align}
which 
is    admissible   by Theorem \ref{OTthm}.
Similarly, we have $ {\mathcal {G}}^{{\mathrm {aut}}}_{Z_t(\phi^\infty)_{E_v}}$,
and   \begin{equation*} 
{\mathcal {G}}^{{\mathrm {aut}}}_{Z_t(\omega(g)\phi)_{E_v}}= {\mathcal {G}}^{{\mathrm {aut}}}_{Z_t(\omega(g^\infty)\phi^\infty)_{E_v}} W^{{\mathfrak{w}}}_{\infty, t}(g_\infty).\end{equation*}

Let $ {\mathcal {G}}^{\overline L_{E_v}}_{Z_t(\phi)_{E_v}}$ be the normalized admissible Green function
for $Z_t(\phi)_{E_v}$  with respect to $\overline L_{E_v}$ as in \Cref{admextgreen}.



# See Also

# Meta
## References
![[_reference_qiu_amsd]]


## Citations and Footnotes
[^1]: Citation, 50