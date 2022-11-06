---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/qiu_amsd]
---
# Topic[^1]
 


 \subsubsection{Siegel-Eisenstein series}  \label{Siegel-Eisenstein series} 
For $\phi\in {\mathcal {S}}({\mathbb {W}})$, we have a Siegel-Eisenstein series of $G$: 
\begin{equation}E(s,g,\phi)=\sum_{\gamma\in P(F)\backslash G(F)}\delta (\gamma  g)^{s }  \omega (\gamma g)\phi (0)\label{Edef}
\end{equation}
which is absolutely convergent if ${\mathrm{Re}} s>1-m/2$ and   has a meromorphic continuation to the entire  complex plane  \cite{Tan}. 
%and has a functional equation with center at $(1-m)/2$   \cite{Tan}.  (We do not use the functional equation.)
Moreover, it is
holomorphic at $s=0$  \cite[Proposition 4.1]{Tan}.




Let $E_t(s,g,\phi)$ be the $\psi_t$-Whittaker  function of $E(s,g,\phi)$. 
Let $W_{t} (s, g, \phi)$ be the global counterpart  of the Whittaker integral  \eqref{expandWT0} so that 
if $\phi$ is a pure tensor then $W_{t} (s, g, \phi)$ is the product of $W_{v,t} (s, g_v, \phi_v)$ over all places of $F$.
By the non-vanishing of $L(1,\eta)$ and Lemma \ref{lSWlem1}, $W_{0} (s, g, \phi)$ has a meromorphic continuation to the entire  complex plane, which is holomorphic at $s=0$. 
Then  we have 
\begin{equation}\label{E0t}E_{t} (s, g, \phi)=W_{t} (s, g, \phi),  \ t\neq 0 ;
\end{equation}
\begin{equation}\label{E0}E_0(s,g,\phi)=\delta (   g)^{s }  \omega ( g)\phi (0)+W_{0} (s, g, \phi).
\end{equation}
By  Lemma \ref {lSWlem} (2) and \eqref{E0t}, for $h\in U({\mathbb {W}})$, we have 
\begin{equation}\label{E0tk}
E_t(0,g,\omega(h)\phi)=E_t(0,g,\phi).
\end{equation}
    


For $t\neq 0$, define  \begin{equation}\label{etv}  E_t'(0,g,\phi)(v)=  W_{v,t} '(0, g_v, \phi_v) \prod_{u\neq v} W_{u,t} (0, g_u, \phi_u)\end{equation} 
if $\phi$ is a pure tensor, and extend the definition to all Schwartz functions by linearity.
Then
\begin{equation} \label{2.9}E_t'(0,g,\phi)=\sum_{v }   E_t'(0,g,\phi)(v). \end{equation}


\subsubsection{Coherent case:   Siegel-Weil formula} \label{TSW} 


%Extend the Weil representation  $\omega_{V^\sharp}=\omega_{\psi,\chi_{V^\sharp}} $ of $G$   on  the Schwartz space ${\mathcal {S}}(V^\sharp ({\mathbb {A}}_E))$ 
% to $G({\mathbb {A}}_F ) \times  U(V^\sharp)({\mathbb {A}}_F  )$ 
% by  $$\omega(g,h) \phi(x)=\omega(g) \phi(h^{-1}x).$$

%We still call $\omega $  the Weil representation of $G({\mathbb {A}}_F ) \times  U({\mathbb {W}}  )$ .

Assume that ${\mathbb {W}}=W({\mathbb {A}}_E)$ is coherent. 
For  $\phi \in {\mathcal {S}}(W ({\mathbb {A}}_E))$ and $(g,h)\in   G({\mathbb {A}}_F ) \times  U({\mathbb {W}}  ) $, we define a  theta series, which is absolutely convergent:
$$ 
\theta(g,h,\phi)=\sum_{x\in W{{}}%\newcommand{\qclE}{{(E)}}} \omega(g,h)
\phi ( x).$$
Then $ \theta(g,h,\phi)$ is  smooth, slowly increasing  and     $  G(F)\times U(W)  $-invariant.
%Let $$   \theta(g,\phi) =   \theta(g,1,\phi) .$$  

Assume that   $W$ is anisotropic. 
Then $E(s,g,\phi)$ is holomorphic at $s=0$, and the following equation is a special case of the regularized Siegel-Weil formula {\cite[Theorem 4.2]{Ich}}: \begin{equation}\label{Ichthm} E(0,g,\phi)=\frac{\kappa}{{\mathrm{Vol}}([U(W)])}  \int _{[U(W)]} \theta(g,h,\phi) dh ,\end{equation} 
where $\kappa=2$ if $ \dim W=1$ and $\kappa=1$ if $ \dim W>1$.
%We in fact will only need the case $r=m=1$, and we will not need the constant $\kappa$ explicitly. The absolute convergence of the right hand side of \eqref{gSW} is shown in \cite{Wei}.

\subsubsection{Incoherent case: derivative}
Assume that ${\mathbb {W}}$ is incoherent. 
By  Lemma \ref {lSWlem} (1), for $t\neq 0$, the summand in \eqref{2.9} corresponding $v$ is nonzero  only if $t$ is represented by ${\mathbb {W}}^v$. 
 



# See Also

# Meta
## References
![[_reference_qiu_amsd]]


## Citations and Footnotes
[^1]: Citation, 28