---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/qiu_amsd]
---
# Topic[^1]




 

 

\label{ramplace}
Let $v  $  be a finite place of $F$ ramified in $E$. Then $\Lambda_v$  is $\pi_v$-modular or almost $\pi_v$-modular lattice.
This case is more complicated.


For a non-negative integer $m$, let
${\mathcal {N}}_m$    be   the  exotic smooth  relative unitary Rapoport-Zink space  
of signature $(m,1)$ \cite[Section 6,7]{RSZ16} \cite[3.5]{RSZ17}\cite[2.1]{LL2} over ${\mathrm{Spf}} {\mathcal {O}}_{E_v^{\mathrm{ur}}}$.  It   will also be specified below. It
is formally smooth over ${\mathrm{Spf}} {\mathcal {O}}_{E_v^{\mathrm{ur}}}$ of  relative dimension $m$.  
Let   ${\mathcal {N}}={\mathcal {N}}_n$.
\begin{rmk} Note that the case $m=0$ is not covered in \cite{RSZ17}\cite{LL2}, but is specifically indicated in \cite[Example 7.2]{RSZ16}. However, it is connected to \cite[Section 6,7]{RSZ17} by the discussion in \cite[Example 12.2]{RSZ16}. We will use this connection is our ``Fifth" step below.
\end{rmk}

Similar to the last section, we will use  ${\mathcal {N}} $ for the formal uniformization of  ${\mathcal {X}}_K$.    The analog of the formal uniformization \eqref{ascycle} of ${\mathcal {P}}$ using 
${\mathcal {N}}_0$ is more subtle: 
we will   use 
${\mathcal {N}}_1$ to define  morphisms ${\mathcal {N}}_0\to{\mathcal {N}}_1\to {\mathcal {N}}$ which will lead us to the   formal uniformization \eqref{ascycle1} of ${\mathcal {P}}$. 
\begin{rmk}  The reason for this subtly might be explained as follows.   
  Recall that  the construction of ${\mathcal {P}}$  requires an additional rank 2  sub-lattice   $\Lambda_{v,1}$ as in \ref{The case n is odd*} at each finite place, which is a direct summand of $\Lambda_v$. And $E_v\Lambda_{v,1}$ contains a distinguished vector $e_v^{(0)}$ of unit norm. One might consider ${\mathcal {O}}_{E_v}e_v^{(0)}\subset E_v\Lambda_{v,1}$ and $
\Lambda_{v,1}\subset \Lambda_v$  as being parallel to the morphisms ${\mathcal {N}}_0\to{\mathcal {N}}_1$ and ${\mathcal {N}}_1\to {\mathcal {N}}$. 
Note that ${\mathcal {O}}_{E_v}e_v^{(0)}$ is not contained in $\Lambda_{v,1}$ ( or $\Lambda_v$). This makes it nontrivial to defined a
morphism ${\mathcal {N}}_0\to{\mathcal {N}}_1$ or ${\mathcal {N}}_0\to {\mathcal {N}}$.  The morphism ${\mathcal {N}}_0\to{\mathcal {N}}_1$  we use  is given by \cite[Section 12]{RSZ16}.  The nontriviality of   the morphism ${\mathcal {N}}_0\to{\mathcal {N}}_1$ is also explained in \cite[Remark 12.3]{RSZ16}.
\end{rmk}   

We have 6 steps before the main result \Cref{yll1} of this subsection \ref{ramplace}.

First, we specify ${\mathcal {N}}_1$, ${\mathcal {N}}$ and    ${\mathcal {N}}_1\to {\mathcal {N}}$. Assume that $\varpi_{E_v}^2=\varpi_{F_v}$.
The framing object ${\mathbb {X}}_1$  for the deformation space  ${\mathcal {N}}_1$ is the  Serre tensor ${\mathcal {O}}_{E_v}\otimes_{{\mathcal {O}}_{F_v}}\overline{\mathbb {E}}$, which is the conjugate of the framing object  \cite[(3.5)]{RSZ17}, 
with the polarization  
conjugate to  the one   in \cite[(3.6)]{RSZ17}. 
In the case that $n$ is odd (the case of Lemma \ref{jac} (1)), the framing object for ${\mathcal {N}}$ is ${\mathbb {X}}_n:={\mathbb {X}}_1\times({\mathbb {E}}^2)^{(n-1)/2}$ with the product polarization $\lambda_n$, where the polarization on ${\mathbb {E}}^2$ is given by  \begin{equation}\label{lambdadef} \lambda =   \begin{bmatrix}0&\lambda_{{\mathbb {E}}}\iota(\varpi_{E_v})\\
-\lambda_{{\mathbb {E}}}\iota(\varpi_{E_v})&0\end{bmatrix}.\end{equation} 
In the same way, we have  a polarization 
$\widetilde{\lambda} $  
on ${\mathcal {E}}^2$ using $\lambda_{\mathcal {E}}$.  This gives us  a morphism ${\mathcal {N}}_1\to {\mathcal {N}}$ by $X\mapsto X\times ({\mathcal {E}}^2)^{(n-1)/2}$ with the polarization $\widetilde{\lambda} $ on each of ${\mathcal {E}}^2$.
In the case that $n$ is even (the case of Lemma \ref{jac} (2)), the framing object for ${\mathcal {N}}$ is  ${\mathbb {X}}_n:={\mathbb {X}}_1\times({\mathbb {E}}^2)^{(n-2)/2} \times {\mathbb {E}}$ where the polarization  $\lambda_{{\mathbb {E}}}'$ on the last component is a multiple of $\lambda_{{\mathbb {E}}}$ so that the induced hermitian pairing on ${\mathrm{Hom}}({\mathbb {E}},{\mathbb {E}})_{{\mathbb {Q}}}$  (defined as in \eqref{hpair})  has determinant  $q(e_v)$ as in Lemma \ref{jac} (2).
This gives us a morphism ${\mathcal {N}}_1\to {\mathcal {N}}$ by $X\mapsto X\times ({\mathcal {E}}^2)^{(n-1)/2}\times {\mathcal {E}}$ with the unique lifting of  $\lambda_{{\mathbb {E}}}'$ on the last component ${\mathcal {E}}$.
% It is clearly a closed embedding.



Second, the uniformizations  of $\widehat{{\mathcal {X}}_{K, {\mathcal {O}}_{E_v^{\mathrm{ur}}}}^{ss}}$ and $Z_t(\phi)^{\mathrm{zar}}$ are as follows.
By  \cite[(3.10)]{RSZ17},  ${\mathrm{Hom}}_{{\mathcal {O}}_{E_v}}({\mathbb {E}},{\mathbb {X}}_n)_{{\mathbb {Q}}}\simeq  V(E_v)$
and  $U(V(E_v))$ is isomorphic to the group of ${\mathcal {O}}_{E_v}$-linear  self-quasi-isogenies of ${\mathbb {X}}_n$ preserving $\lambda_n$.  In particular $U(V)$ acts on ${\mathcal {N}}$.   The analog of the formal uniformization \eqref{ssun*} of $\widehat{{\mathcal {X}}_{K, {\mathcal {O}}_{E_v^{\mathrm{ur}}}}^{ss}}$ holds by \cite[(4.9)]{LL2}.
For every $x\in V(E_v)-\{0\} $, we have the  Kudla-Rapoport divisor ${\mathcal {Z}}(x)$ on $ {\mathcal {N}} $, which is a (possibly empty) relative Cartier divisor \cite[Lemma 2.41]{LL2}.
The analog of  Proposition \ref{czss} holds by 
\cite[Proposition 4.29]{LL2} combined with the argument in the proof of  Proposition \ref{czss}.
Though  \cite{LL2}   only uses even dimensional hermitian spaces,  the specific results that we cite hold in the general case by the same proof.  




Third, we recall  the morphisms   ${\mathcal {N}}_0\to {\mathcal {N}}_1$  defined in \cite[Section 12]{RSZ16}. 
This   is rather complicated for general ${\mathcal {N}}_{2m}\to {\mathcal {N}}_{2m+1}$. Fortunately, in our case, we have the following convenient description. By \cite[Example 12.2]{RSZ16},  $ {\mathcal {N}}_1$ is  isomorphic the disjoint union of two copies of 
the Lubin-Tate deformation space for the formal ${\mathcal {O}}_{F_v}$-module ${\mathbb {E}}$. We write ${\mathcal {N}}_1={\mathcal {N}}_1^+\coprod {\mathcal {N}}_1^{-}$. 
Recall that $B$ is the      unique  division quaternion algebra over $F_v $, and its maximal order ${\mathcal {O}}_B$ is the endomorphism ring of ${\mathbb {E}}$. 
For $c\in  B^\times$, we   have two closed embeddings (moduli of the canonical lifting) ${\mathcal {N}}_0\to {\mathcal {N}}_1^{\pm}$ associated    to $c\iota c^{-1}:E_v\hookrightarrow B$.  Let ${\mathcal {N}}_0^{c,\pm}$ be the union of the images.

Fourth, we  need  to specify $c$ so that we can use ${\mathcal {N}}_0^{c,\pm}$ to uniformize ${\mathcal {P}}$ (see \eqref{ascycle1} below).  
Let $e_v^{(1)}$ be as in   \ref{A useful description}. 
Then
$$B={\mathrm{Hom}}_{{\mathcal {O}}_{F_v}}({\mathbb {E}},\overline{\mathbb {E}})_{\mathbb {Q}}\simeq {\mathrm{Hom}}_{{\mathcal {O}}_{E_v}}({\mathbb {E}},{\mathbb {X}}_1)_{\mathbb {Q}}\simeq W(E_v)\oplus E_v e_v^{(1)},$$ 
where  the  middle is the adjunction isomorphism, and
the last isomorphism is compatible with   ${\mathrm{Hom}}_{{\mathcal {O}}_{E_v}}({\mathbb {E}},{\mathbb {X}}_n)_{{\mathbb {Q}}}\simeq  V(E_v)$.
And the hermitian form on $W(E_v)\oplus E_v e_v^{(1)}$ corresponds to $-2\varpi_{F_v}{\mathrm{Nm}}_B $ (see the proof of \cite[Lemma 3.5]{RSZ17}), where ${\mathrm{Nm}}_B$ is the reduced norm on 
$B$.
Let $c$  correspond to $\varpi_{E_v} e_v^{(1)}$. Since $q\left( e_v^{(1)}\right)\in {\mathcal {O}}_{F_v}^\times$ (see  \ref{Lattices at ramified places}), $c\in {\mathcal {O}}_B^\times$ (note that $v\nmid 2$ here).

Fifth, we uniformize  ${\mathcal {P}}$.
Comparing the moduli interpretation of ${\mathcal {N}}_0\to {\mathcal {N}}_1$ in \cite[Proposition 12.1]{RSZ16} and \eqref{5terms} (as well as   \Cref{cpcp} and Remark \ref{multichain} below it),
we have the following analog of \eqref{ascycle}: 
\begin{align}\label{ascycle1} {\mathcal {P}}_{{\mathcal {O}}_{E_v^{\mathrm{ur}}}} =\frac{1}{2d_{K_{\mathbb {W}}^{(0)}}}  U(W) \backslash \left( {\mathcal {N}}_{0,{\mathcal {O}}_{E_v^{\mathrm{ur}}}}^{c,\pm}\times U \left( {\mathbb {W}}^{\infty,v}\right)/ K_{\mathbb {W}}^v\right), \end{align} 
where $d_{K_{\mathbb {W}}^{(0)}} $ is  
is   the degree of the   fundamental cycle of  ${\mathrm{Sh}}({\mathbb {W}})_{K_{\mathbb {W}}^{(0)}}$ (see \eqref{5terms}).
Here the extra factor 2 comes from  Lemma \ref{index2}.

Finally,    we compute $ \left( {\mathcal {Z}}(x)\cdot {\mathcal {N}}_{0}^{c,\pm}\right)_{{\mathcal {N}}}$. 
Since  $c\in {\mathcal {O}}_B^\times$, by \cite[Lemma 6.5, Proposition 7.1]{RSZ17},  
\begin{equation}\label{ssuni411}{\mathcal {N}}_0^{c,\pm}={\mathcal {Y}}\left( \varpi_{E_v}e_v^{(1)}\right).\end{equation}
Here ${\mathcal {Y}}\left(\varpi_{E_v}e_v^{(1)}\right)$ is the Kudla-Rapoport divisor on ${\mathcal {N}}_1$, where $\varpi_{E_v}e_v^{(1)}$ lifts.
Let ${\mathbb {X}}^\perp$ be the direct complement of ${\mathbb {X}}_1$ in 
${\mathbb {X}}_n$, i.e. ${\mathbb {X}}^\perp=({\mathbb {E}}^2)^{(n-1)/2}$
if $n$ is odd, and ${\mathbb {X}}^\perp=({\mathbb {E}}^2)^{(n-2)/2} \times {\mathbb {E}}$  is $n$ is even. 
Let    $  \Lambda_{v,1}^\perp $   be as in \ref{A useful description}.
By Lemma \ref{jac} and \eqref{lambdadef},
$${\mathrm{Hom}}_{{\mathcal {O}}_{E_v}}({\mathbb {E}},{\mathbb {X}}^\perp) \subset {\mathrm{Hom}}_{{\mathcal {O}}_{E_v}}({\mathbb {E}},{\mathbb {X}}_n)_{{\mathbb {Q}}}\simeq  V(E_v)$$ 
corresponds to $\Lambda_v^\perp$.
Then 
by \eqref{ssuni411}
and Gross' result on  canonical lifting  \cite{Gro}, we  have    \begin{equation}\label{ssuni4} \left( {\mathcal {Z}}(x)\cdot {\mathcal {N}}_0^{c,\pm}\right)_{{\mathcal {N}}} = 2(v({q(x_1)})+1) 1_{{\mathcal {O}}_{F_v}}({q(x_1)}) 1_{{\varpi_{E_v}
{\mathcal {O}}_{E_v}e_v^{(1)}\oplus \Lambda_v^\perp}} (x_2)
\end{equation} for  $ x=(x_1,x_2)\in  W(E_v)\oplus V^\sharp (E_v) $  with $x_1\neq 0$.
Here    the extra factor 2 comes from  that ${\mathcal {N}}_0^{c,\pm}$ has 2 components.






# See Also

# Meta
## References
![[_reference_qiu_amsd]]


## Citations and Footnotes
[^1]: Citation, 105