---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/qiu_amsd]
---
# Topic[^1]
\begin{lem} \label{AGPK} % (1) For $h\in U({\mathbb {V}}_\Xi)$, where $\Xi$ is as in  \Cref{hypo1}, $  A(g,\omega(h)\phi)=A(g,\phi)$;
 
(1)    For $g'\in {\mathbb {G}}^\infty$,  $  A(gg', \phi)=A(g ,\omega(g')\phi)$.

(2) For $h\in K_{\Lambda}$,   $  A(g,\omega(h)\phi)=A(g,\phi)$.

          \end{lem}
\begin{proof}  % (1)   The     ``right translation by $h$" automorphism ${\mathcal {X}}_{hKh^{-1}}\simeq {\mathcal {X}}_{K}$ in \Cref{hypo1}   induces an automorphism  on $\widehat Z^{1}_{{\overline\cL},{\mathbb {C}}}(\widetilde{\mathcal {X}}),$ and $ \widehat{\mathrm{Ch}}^{1}_{{\overline\cL},{\mathbb {C}}}(\widetilde{\mathcal {X}}) $ which  fixes $c_1(\overline{\mathcal {L}}^\vee)$.
%   It is clear that  the automorphism sends $z_t(g ,\phi )_{\mathfrak{e}}^{\overline\cL}$ to 
%   $z_t(g ,\omega(h)\phi )_{\mathfrak{e}}^{\overline\cL}$, and induces the identity map on  $ {\mathbb {C}}\subset {\mathrm{Ch}}^{1}_{{\overline\cL},{\mathbb {C}}}(\widetilde{\mathcal {X}})$ as in  \eqref{line}.  
%  Applying the automorphism to \eqref{AGGZ} and taking difference, we have $  A(g,\omega(h)\phi)-A(g,\phi)\in W_0({\mathbb {G}})\cap{\mathcal {A}}_{{\mathrm{hol}}}({\mathbb {G}},{\mathfrak{w}}).$
%Now  (1) follows from   \eqref{constterm}.
 
       
(1)   The second term on the right hand side of $$B(g,\phi):= A(g,\phi) +  \omega(g )\phi(0) \big(-\log \delta_\infty(g_\infty)+ [F:{\mathbb {Q}}]\left( \log \pi-(\log\Gamma)'(n+1)\right) \big) $$
          lies in $ W_0({\mathbb {G}})$. Then so does $B(g,\phi)$.
    Similar to Lemma \ref{diffag1}, \eqref{AGGZ} implies that 
\begin{equation} \label{fadefB}
B(g,\phi)+\sum_{x\in {\mathbb {V}}^\infty,\ q(x)\in F^\times}  \omega(g^\infty)\phi^\infty (   x)  [Z(x,g_\infty)_{\mathfrak{t}}^{\overline\cL}] W^{{\mathfrak{w}}}_{\infty, q(x)}(g_\infty) \in    {\mathcal {A}} ({\mathbb {G}},{\mathfrak{w}})   \otimes\widehat {\mathrm{Ch}}^{1}_{{\overline\cL},{\mathbb {C}}}(\widetilde{\mathcal {X}}) 
\end{equation}
Apply \eqref{fadefB} in two ways: first, replace $\phi $ by $\omega(g')\phi $ and call the resulted series $S_1$; second  
replace $g$ by $gg'$ can call the resulted series $S_2$.  Then 
$$  B(g,\omega(g')\phi)-B(gg', \phi) =S_1-S_2\in {\mathcal {A}}_{{\mathrm{hol}}}({\mathbb {G}},{\mathfrak{w}}).$$
But  $$  B(g,\omega(g')\phi)-B(gg', \phi) =A(g,\omega(g')\phi)-A(gg', \phi) \in W_0({\mathbb {G}}) .$$
It must be 0 by \eqref{constterm}. This gives (1).   
     
     (2) The proof for (2) is similar to (1) (but we do not use $B(g,\phi)$, rather only use $A(g,\phi) $), by combining the proof of \Cref{equiva}.
           \end{proof}

# See Also

# Meta
## References
![[_reference_qiu_amsd]]


## Citations and Footnotes
[^1]: Citation, lem 5.19