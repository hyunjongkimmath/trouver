---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/qiu_amsd]
---
# Topic[^1]
\begin{prop}\label{nctprop} 
Assume that    
$S$
consists of 4 places split in $E$. 
 There exists $ \phi_v'  \in {\mathcal {S}}\left( W(v)\oplus V^\sharp\right) $, $ v\in {{\mathfrak{Ram}}}$, 
such that   
\begin{itemize}\item
\eqref{entryc} holds;
\item  for every 
$\phi\in \overline {\mathcal {S}}\left( {\mathbb {V}}  \right)^{K}$  that is a pure tensor  with    $\phi^\infty$ being $\overline{\mathbb {Q}}$-valued  and $\phi_v=1_{\Lambda_v}$
      for every finite place $v$ nonsplit in $E$,  
  we have the following equation for $K'=K_S K_\Lambda^S$ and all $t\in F_{>0}$, $g\in G\left({\mathbb {A}}_F^{{{\mathfrak{Ram}}} \cup \infty }\right) P\left({\mathbb {A}}_{F,{{\mathfrak{Ram}}} }\right) $:        \begin{align}\label{entry4mod} \left( 2   z_t(g, \phi^\infty)_{\mathfrak{e}}^{{\mathcal {L}},{\mathrm {aut}}}\cdot \pi_{K,K'}^*{\mathcal {P}}_{{\mathbb {W}},K'} \right) \mathrm{mod}\overline{\mathbb {Q}}\log {{S}} =  f_{{\mathbb {W}},K',t}^\infty(g) \mathrm{mod}\overline{\mathbb {Q}}\log {{S}}  ,\end{align} 
  \end{itemize}   
\end{prop}
\begin{proof}[Proof of Theorem \ref{nct} assuming \Cref{nctprop}] 
It is enough to  prove Theorem \ref{nct}  assuming that $\phi^\infty$ is $\overline{\mathbb {Q}}$-valued. 
We use \Cref{nctprop}      for  $l^{-1}{\mathbb {W}}$'s   where $l\in U({\mathbb {W}})\backslash K_\Lambda/ K'$.
Note that  though the corresponding $ \phi_v' $  for $l^{-1}{\mathbb {W}}$ may depend on $l$, the truth of \eqref{entryc} does not.  
 Thus we   focus on the relation between $ \eqref{entry4mod}_l$, that is \eqref{entry4mod} with ${\mathbb {W}}$ replaced by $l^{-1}{\mathbb {W}}$,      and \eqref{entry4}.
 Indeed, $ \eqref{entry4} $ modulo $\overline{\mathbb {Q}}\log {{S}}$   is a ${\mathbb {Q}}$-linear  combination of $ \eqref{entry4mod}_l$'s, more precisely explained as follows. 
Note that $$\pi_{K,K_\Lambda}^*{\mathcal {P}}_{{\mathbb {W}},K_{\Lambda}} =\pi_{K,K'}^* \pi_{K',K_\Lambda}^*{\mathcal {P}}_{{\mathbb {W}},K_{\Lambda}} ,$$
and $\pi_{K',K_\Lambda}^*{\mathcal {P}}_{{\mathbb {W}},K_{\Lambda}}$ is a ${\mathbb {Q}}$-linear combination of ${\mathcal {P}}_{l^{-1}{\mathbb {W}},K'}$'s  with $l\in U({\mathbb {W}})\backslash K_\Lambda/ K'$, as in \eqref{PWK}. Thus the left hand side of $ \eqref{entry4} $ modulo $\overline{\mathbb {Q}}\log {{S}}$    is  the   ${\mathbb {Q}}$-linear combination of the left hand sides of  $ \eqref{entry4mod}_l$'s with the same index set 
and coefficients.     To match the right hand sides, use the   coset decomposition  
$$U({\mathbb {W}})\backslash K_\Lambda/ K 
%  =\coprod_{l\in U({\mathbb {W}})\backslash K_\Lambda/ K'}U({\mathbb {W}})\backslash K'/ K  
=\coprod_{l\in U({\mathbb {W}})\backslash K_\Lambda/ K'}
l\left(  U({l^{-1}{\mathbb {W}}})\backslash K'\right)/ K  ,$$
(the reader should note that this double coset notation is  clarified    below \eqref{PWK},)
%and the following obvious product relation 
% between the  coefficients in \eqref{fh}:
%  $$  \frac{d_{k^{-1}l^{-1}{\mathbb {W}},K}}{ d_{{\mathbb {W}},K_\Lambda}} %= \frac{d_{k^{-1}l^{-1}{\mathbb {W}},K}}{ d_{k^{-1}l^{-1}{\mathbb {W}},K'}}  \frac{d_{k^{-1}l^{-1}{\mathbb {W}},K'}}{ d_{k^{-1}l^{-1}{\mathbb {W}},K_\Lambda}}
%  = \frac{d_{k^{-1}l^{-1}{\mathbb {W}},K}}{ d_{ l^{-1}{\mathbb {W}},K'}}
% \frac{d_{l^{-1}{\mathbb {W}},K'}}{ d_{{\mathbb {W}},K_\Lambda}},\ k\in U({l^{-1}{\mathbb {W}}})\backslash K',$$
to rewrite  the right   hand side of $ \eqref{entry4} $ modulo $\overline{\mathbb {Q}}\log {{S}}$    (i.e. \eqref{fh} modulo $\overline{\mathbb {Q}}\log {{S}}$) 
into a linear combination  of  the right hand sides of $ \eqref{entry4mod}_l$'s,
still with the same index set 
and coefficients.  
Thus, we proved   \eqref{entry4}
modulo $\overline{\mathbb {Q}}\log {{S}}$  in  Theorem \ref{nct}.
Then Theorem \ref{nct} also holds for another set  $S'$ of 4 places split in $E$ modulo $\overline{\mathbb {Q}}\log {{S'}}$. By   requiring $S$ and $S'$ to have   no same residue characteristics, \eqref{entry4}
follows from  \Cref{baker}, i.e. $\overline{{\mathbb {Q}}}$-linear  independence of $\log p$'s.
 \end{proof}

# See Also

# Meta
## References
![[_reference_qiu_amsd]]


## Citations and Footnotes
[^1]: Citation, prop 5.13