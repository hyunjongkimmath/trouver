---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/qiu_amsd]
---
# Topic[^1]
\begin{lem}  \label {YZ7.41'}
Assume that $v\in {\mathfrak{Ram}}_{E/F}$.
Then $\phi_v'$     extends to a Schwartz function on  $ V(E_v)$  such that 
$c(1,\phi_v)-2\phi_v'(0)=2 \log|D_v|_{F_v} $.  

\end{lem}
\begin{proof}The computation for $\phi_v'(x)$ is indeed only on the  component $\Lambda_{v,1}$ of $\Lambda_v$. For simplicity, we assume that $n=2$ so that we do not have the component $ \Lambda_{v,1}^\perp$.

Consider a larger lattice $A={\mathcal {O}}_{E_v}e_v^{(0)}\oplus {\mathcal {O}}_{E_v}e_v^{(1)}$.  
For $x=(x_1,x_2)\in V(E_v)-V^\sharp(E_v) ,$ let  
$$ \varphi(x)= {W\theta}_{v,x} '(0, 1, 1_{A})-    (v({q(x_1)})+1) 1_{{\mathcal {O}}_{F_v}}({q(x_1)}) 1_{{
{\mathcal {O}}_{E_v}e_v^{(1)} } } (x_2)
\log q _{F_v}.$$
By 
\cite[Lemma 9.2]{YZ}, $ \varphi$ extends to a Schwartz function on  $ V(E_v)$  such that 
$c(1,1_{A})-2 \varphi(0)=2\log|D_v|_{F_v}$.
It is enough to extend $\varphi(x) 1_{{
\varpi_{E_v}{\mathcal {O}}_{E_v}  e_v^{(1)} } } (x_2)-\phi_v'(x)$ to a Schwartz function on  $ V(E_v)$,    and show that the twice of its value at $0$ is    $c(1,1_{A})-c(1,\phi_v) $.
First,     \begin{align*} &\varphi(x) 1_{{
\varpi_{E_v}{\mathcal {O}}_{E_v}  e_v^{(1)} } } (x_2)-\phi_v'(x)\\
=
& {W\theta}_{v,x} '(0, 1, 1_{A}) 1_{{
\varpi_{E_v}{\mathcal {O}}_{E_v}  e_v^{(1)} } } (x_2)- {W\theta}_{v,x} '(0, 1, \phi_v)\\
=&{W\theta}_{v,x} '(0, 1, 1_{A}) 1_{{
\varpi_{E_v}{\mathcal {O}}_{E_v}  e_v^{(1)} } } (x_2)- {W\theta}_{v,x} '(0, 1, \phi_v)1_{{
\varpi_{E_v}{\mathcal {O}}_{E_v}  e_v^{(1)} } } (x_2)  \\
-&{W\theta}_{v,x} '(0, 1, \phi_v)1_{{
{\mathcal {O}}_{E_v}^\times  e_v^{(1)} } } (x_2) . 
\end{align*}
By    Lemma \ref{mylem1} and \eqref{Schwartz}, 
${W\theta}_{v,x} '(0, 1, \phi_v)1_{{
{\mathcal {O}}_{E_v}^\times  e_v^{(1)} } } (x_2)$ extends to a Schwartz function on  $ V(E_v)$.
It  is supported on $\{x_2\in  {\mathcal {O}}_{E_v}^\times  e_v^{(1)}\} $ so that its value at 0 is 0. 
By \eqref{Wood0},\eqref{thetaw1} and \eqref{Schwartz1}, 
\begin{align} \label{p23}& {W\theta}_{v,x} '(0, 1, 1_{A}) 1_{{
\varpi_{E_v}{\mathcal {O}}_{E_v}  e_v^{(1)} } } (x_2)- {W\theta}_{v,x} '(0, 1, \phi_v)1_{{
\varpi_{E_v}{\mathcal {O}}_{E_v}  e_v^{(1)} } } (x_2)\\
=& \gamma_{{\mathbb {W}}_v}^{-1}\frac{1}{  {\mathrm{Vol}}(U(W(E_v))}  
{ W_{v,q(x_1)}}'(0,1,1_{ {\mathcal {O}}_{E_v}^\times e_v^{(0)}})   1_{{
\varpi_{E_v}{\mathcal {O}}_{E_v}  e_v^{(1)} } } (x_2).\nonumber
\end{align}  
Here we used that $L(s,\eta_v)=1$ due to the ramification of $v$ in $E$.
By Lemma \ref{mylem1}, \eqref{p23}  extends to a Schwartz function on  $ V(E_v)$. 
  

Second, by a direct computation with the definition of  $c(g,\phi_v)$ below \eqref{cphiv}, and using \eqref{Wood}, Lemma \ref{mylem1} and \eqref{Schwartz1}, we have   $$c(1,1_{A})-c(1,\phi_v) =\gamma_{{\mathbb {W}}_v}^{-1}|D_vd_v|_{F_v}^{-1/2} 
{ W _{v,0}}'(0,1,1_{ {\mathcal {O}}_{E_v}^\times e_v^{(0)}}).$$ 
By \cite[p 23]{YZZ},   which says ${\mathrm{Vol}}(U(W(E_v))=2|D_vd_v|_{F_v}^{1/2} 
$, the lemma follows. 
\end{proof}

# See Also

# Meta
## References
![[_reference_qiu_amsd]]


## Citations and Footnotes
[^1]: Citation, lem 6.3