---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/qiu_amsd]
---
# Topic[^1]



We  define ${{\mathfrak{b}}}=b_{v,1}.$
Then 
$E_{t,{\mathrm{qhol}}}'(0,g,\phi)(v)=({{\mathfrak{b}}} + \log |t|_v)
E_t(0,g,\phi),
$ 
and  we have \begin{equation*} J_{t,{\mathrm{qhol}}}'(0,g,\phi)=( 2{{\mathfrak{b}}}[F:{\mathbb {Q}}]-{{\mathfrak{c}}})E_t(0,g,\phi)-C_t(0,g,\phi)+2\left( E'_{t,{\mathrm{f}}}(0,g,\phi)+E_t(0,g,\phi) \log {\mathrm{Nm}}_{F/{\mathbb {Q}}}t\right) .
\end{equation*}
Combined with Lemma \ref{becom}, we have 
\begin{equation}\label{Final} \begin{split}&{E\theta}_{t,{\mathrm{qhol}}}'(0,g,\phi)-2\left( E'_{t,{\mathrm{f}}}(0,g,\phi) +E_t(0,g,\phi) \log {\mathrm{Nm}}_{F/{\mathbb {Q}}}t\right)\\
=&{E\theta}'_{{\mathrm{chol}},t}(0,g,\phi) +( 2{{\mathfrak{b}}}[F:{\mathbb {Q}}]-{{\mathfrak{c}}})E_t(0,g,\phi)-C_t(0,g,\phi).
\end{split}
\end{equation}
\begin{rmk}
The constant ${{\mathfrak{b}}}$ can be explicitly computed as follows. %For $n=1$, see  \cite[Lemma 3.3]{Yuan}. 
For $v|\infty$, $a\in E_v^\times$ and $y={\mathrm{Nm}}(a)\in {\mathbb {R}}$,
by \eqref{translaw} and  \cite[Proposition 2.11(1)]{YZZ}, a direct computation shows that 
$$\frac{W_{v,1 }' (0, m(a), \phi_v)}{\chi_{{\mathbb {W}},v}(a)\gamma_{{\mathbb {V}}_v}}=\frac{(2\pi  )^{n+1} y^{(n+1)/2} e^{-2\pi y}}{\Gamma(n+1)}\left( \sum_{j=1}^n \binom{n}{j} \Gamma(j) (4\pi y)^{-j}+ \log \pi-(\log\Gamma)'(n+1)\right).$$
Dividing both sides of  \eqref{Finalw}  by  \eqref{Wtt}   with $t=1$,
% $$\gamma_{{\mathbb {V}}_v} \frac{(2\pi)^{n+1}}{\Gamma(n+1)} W^{{\mathfrak{w}}_v}_{v, 1}(g)=\gamma_{{\mathbb {V}}_v} W_{v,1} (0, g, \phi_v),$$ 
we get 
\begin{align*}{{\mathfrak{b}}}&= \frac{(4\pi)^{n}}{\Gamma(n)}  \widetilde{\lim _{s\to 0}}  \int_{y=0}^\infty y^{s+n+1}e^{-4\pi y}\left( \sum_{j=1}^n \binom{n}{j} \Gamma(j) (4\pi y)^{-j}+ \log \pi-(\log\Gamma)'(n+1)\right) \frac{dy}{y^2} \\
&=  \frac{1}{\Gamma(n)}  \widetilde{\lim _{s\to 0}}  (4\pi)^{-s}\int_{y=0}^\infty y^{s+n}e^{-y}\left( \sum_{j=1}^n \binom{n}{j} \Gamma(j) y^{-j}+ \log \pi-(\log\Gamma)'(n+1)\right) \frac{dy}{y}.
\end{align*}  
The usual limit  exists  when $n=1$.
Thus we have
\begin{equation}\label{c1info}\begin{split} {{\mathfrak{b}}}&=1+2 \sum_{j=1}^{n-1}\frac{1}{j}+ \log \pi-(\log\Gamma)'(n+1),\ n\geq 2\\
{{\mathfrak{b}}}&=-({1+\log 4}),\ n=1.\end{split} 
\end{equation}
When $n=1$, this is twice of the corresponding number in \cite[Lemma 3.3 (2)]{Yuan} due to the difference  between the modulus characters mentioned in \ref{modulus character}.

\end{rmk}
%qcl  This term seems should compensate the $G^B-G^{OT}$ $C_0$ really comes from Hodge bundle.

\subsubsection{Properties of Eisenstein series}
The first  is an analog of \eqref{ktrivial}, whose proof is omitted.


# See Also

# Meta
## References
![[_reference_qiu_amsd]]


## Citations and Footnotes
[^1]: Citation, 38