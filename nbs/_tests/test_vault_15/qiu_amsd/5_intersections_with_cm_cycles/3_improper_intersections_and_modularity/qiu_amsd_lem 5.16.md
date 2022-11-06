---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/qiu_amsd]
---
# Topic[^1]
\begin{lem} \label{tech2} 
We have the following equality in $ {\mathcal {A}}_{{\mathrm{hol}}}(G,{\mathfrak{w}})_{\overline{\mathbb {Q}}}\otimes _{\overline{\mathbb {Q}}} {\mathbb {C}}/ \overline{\mathbb {Q}}\log {{S}} $: 
\begin{align}\label{entry1} \left[ 2   z(\cdot , \phi)_{{\mathfrak{e}}}^{{\mathcal {L}},{\mathrm {aut}}}\cdot \left({\mathcal {P}}_{{\mathbb {W}}^{(i,j)}}-{\mathcal {P}}_{{\mathbb {W}}^{(i',j')}}\right)\right]= \left[ f_{{\mathbb {W}}^{(i,j)}} - f_{{\mathbb {W}}^{(i',j')}}\right].  \end{align}    
%Here $f_{{\mathbb {W}}^{(i,j)}} $ is   defined using \eqref{fh}, with $K_\Lambda$ replaced by $f$ with ${\mathbb {W}}$ replaced by ${{\mathbb {W}}^{(i,j)}}$. 
\end{lem}
\begin{proof}[Proof of \Cref{tech2}] 
Consider  the  difference  $$f=2   z(\cdot , \phi )_{{\mathfrak{e}}}^{{\mathcal {L}},{\mathrm {aut}}}\cdot \left({\mathcal {P}}_{{\mathbb {W}}^{(i,j)}}-{\mathcal {P}}_{{\mathbb {W}}^{(i',j')}}\right)- \left( f_{{\mathbb {W}}^{(i,j)}} - f_{{\mathbb {W}}^{(i',j')}}\right)
\in {\mathcal {A}}_{{\mathrm{hol}}}(G,{\mathfrak{w}})  $$   of the two sides of \eqref{entry1}, before passing to ${\mathcal {A}}_{{\mathrm{hol}}}(G,{\mathfrak{w}})_{\overline{\mathbb {Q}}}\otimes _{\overline{\mathbb {Q}}} {\mathbb {C}}/ \overline{\mathbb {Q}}\log {{S}} $. 
By the cuspidality of  \eqref{zPA} and Lemma \ref{wr1} (2),   the $0$-th Fourier coefficient satisfies  $ f_0^\infty(g)  =0$  for $g\in {\mathbb {G}}_{\{v_1,v_2\}} .$ % For all 



For the moment, we
assume that   $\phi_{{{v_k}}} $  is ${\mathbb {W}}_{v_k}$-regular for $k=1,2$.  Then   for $t\in F_{>0}$, 
by   Proposition \ref{tech1},  the $t$-th Fourier coefficient  $f_t^\infty$ of $f$ satisfies 
$f_t^\infty(g)\in \overline{\mathbb {Q}}\log {{S}}$ for $g\in {\mathbb {G}}_{\{v_1,v_2\}} .$ 
With the  ${\mathbb {W}}_{v_k}$-regularity on $\phi_{{{v_k}}} $'s,  let us prove \eqref{entry1} for all $g\in G({\mathbb {A}}_F)$.
%  one should be able to check this directly modulo log S. This is implied by the prop.
Write  \begin{equation}\label{fmod1}[f]=\sum_{i} f_i\otimes a_i\end{equation} as a finite sum, where  $f_i\in {\mathcal {A}}_{{\mathrm{hol}}}(G,{\mathfrak{w}})_{\overline{\mathbb {Q}}}$ and $a_i\in    {\mathbb {C}}/ \overline{\mathbb {Q}}\log {{S}}$ are $\overline{{\mathbb {Q}}}$-linearly independent. Then 
for $t\in F_{>0}\cup\{0\}$,
the $t$-th Fourier coefficient of \eqref{fmod1} is 
\begin{equation*} 
f_t^\infty  \mathrm{mod}\overline{\mathbb {Q}}\log {{S}} =\sum_{i} f_{i,t}^\infty a_i 
\end{equation*}
where the left hand side comes from the  discussion above the proposition, and the right hand side from definition of the Fourier coefficient. 
So
$\sum _i f_{i,t}^\infty (g)  a_i=0$ for $t\in F_{>0}\cup \{0\}$  and $g\in {\mathbb {G}}_{\{v_1,v_2\}}$.  Thus $f_{i,t}^\infty(g)=0$ for $t\in F_{>0}\cup \{0\}$ and $g\in {\mathbb {G}}_{\{v_1,v_2\}}$ by the $\overline{{\mathbb {Q}}}$-linear independence of $a_i$'s. So $f_i=0$ by  the density of ${\mathbb {G}}_{\{v_1,v_2\}}  $ in $G(F)\backslash G({\mathbb {A}}_F)$.
So \eqref{entry1} holds.

\begin{rmk} The density argument can not be applied directly to  $[f].$
\end{rmk}
In particular, with the  ${\mathbb {W}}_{v_k}$-regularity on $\phi_{{{v_k}}} $'s, \eqref{entry1} holds
if we replace $g$ by $gw_{v_1}$, where $w_{v_1} \in G(F_{v_1})$ is as in \ref{Group} and  acts on ${\mathcal {S}}({\mathbb {V}}_{v_1}) $ by  Fourier transform multiplied by the Weil index.  Then by  Lemma \ref{wr},  \eqref{entry1} holds
if we replace $\phi$ by $\omega(w_{v_1})\phi$.    By Lemma \ref{Fourier}, we can remove the ${\mathbb {W}}_{v_1}$-regularity on  $\phi_{{{v_1}}} $. %So, if $\phi_{{{v_2}}} $  is supported outside $V^\sharp(E_{v_2})$,  then \eqref{entry1} holds for all $g\in G({\mathbb {A}}_F)$. 
By the same reasoning for $v_2$, we can remove the assumption on  $\phi_{{{v_2}}} $. So
\eqref{entry1} holds   without the  regularity assumption on $\phi$. \end{proof}

# See Also

# Meta
## References
![[_reference_qiu_amsd]]


## Citations and Footnotes
[^1]: Citation, lem 5.16