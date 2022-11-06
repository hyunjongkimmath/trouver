---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]

\label{sec: further remarks}
\paragraph{Comparison to Previous Work} 
The method of proving the Tate conjecture for K3's over finite fields by reducing to the Lefschetz $(1, 1)$-theorem via the Kuga-Satake construction first appeared in \cite{Nygaard} and was subsequently extended by \cite{NO}. The basic idea of both papers is that for ordinary or more generally finite height K3's, by an appropriate (canonical or quasi-canonical) lifting, both $(\star)$ and $(\star')$ (in the sketch of proofs) can be achieved. This method was not able to treat the supersingular case partially because it is impossible to lift line bundles on a supersingular K3 simultaneously. By using canonical integral models of Shimura varieties, Madapusi-Pera was able to prove $(\star')$ by lifting one divisor at each time, so that even the supersingular case can be treated uniformly. Our method relies crucially on lifting one divisor at each time---even for ordinary $h^{2, 0} = 1$ varieties, we do not expect that simultaneously lifting all line bundles is always possible, because the period image may not have big enough dimension. 


Our idea of studying monodromy by looking at certain curves in moduli spaces was initially inspired by Lyons' thesis \cite{Lyons}. Lyons proved that a class of surfaces discovered by Catanese-Ciliberto has the biggest possible monodromy group (the full orthogonal group). However, unlike Lyons, we do not make use of global Picard-Lefschetz theory. This is also not possible for elliptic surfaces for reasons explained below. We also remark that Lyons also made use of the signature of Betti cohomology towards the end of his proof of Thm~A. This argument, just like ours involving \cite{Andre}, is fundamentally transcendental. However, note that \cite{Lyons} and \cite{Moonen} both use monodromy to prove that the Kuga-Satake construction is motivated, whereas we use monodromy primarily to lift line bundles (once Kuga-Satake is set up). 

Finally, we discuss how our approach is compared to that of the recent paper \cite{FuMoonen} by Fu and Moonen. The key difference is that they do solve the ``local Schottky problem''. In particular, they showed that there are no global vector fields on these varieties in characteristic $p$, thereby showing that the integral period morphism is smooth. By contrast, our argument does not depend on the integral period morphism having good local properties (cf. Rmk~\ref{rmk: no good local property}). It also does not use crystalline cohomology, so we may circumvent certain small characteristic subtleties and treat the $p = 3$ case. However, the smoothness of the integral period morphism that Fu and Moonen proved  is very strong and has many potential arithmetic applications beyond the Tate conjecture. 

\paragraph{Influence of Birational Type} For the examples of general or Fano type considered by us or Lyons, the variety $X$ in question is naturally a divisor in another variety $Y$ of one-dimension bigger. Moreover, this divisor is ample. This ampleness was important for Lyons to apply global Picard-Lefschetz theory and the hard Lefschetz theorem, and for us to use Katz' criterion for Lefschetz embeddings. In these examples, the ampleness of $\mathcal{O}_Y(X)$ is related to that of the canonical bundle (or its dual) of $X$. It would be interesting to investigate if this is a general phenomenon for $h^{2, 0} = 1$ varieties of general or Fano type. 

For elliptic surfaces the picture is very different. Let $X$ be an elliptic surface over a base curve $C$ with fundamental line bundle $L$. The natural threefold $Y$ to be considered here is the $\mathbb{P}^2$-bundle $\mathbb{P}(L^2 \oplus L^3 \oplus \mathcal{O}_C)$ over $C$. Our analysis of the monodromy works under the assumption that $\mathrm{deg}(L)$ is sufficiently big with respect to $g(C)$, i.e., $L$ is sufficiently positive.  However, $X$ is not an ample divisor of $Y$. Let us view $C$ as a curve in $Y$ via the zero section. Then there is a relation 
\begin{equation}
    \label{eqn: }
    X.C=\text{deg\;}\mathcal{O}_Y(X)|_C=-3\text{deg}(L).
\end{equation}
To see this, note that $Y\cong \mathbb{P}(L^{-1} \oplus \mathcal{O}_C \oplus L^{-3})$, and under this isomorphism, $C$ is identified with the section $[0,1,0]$. Now the equation \ref{eqn: Weierstrass for elliptic surfaces} is homogeneous of degree $-3$, hence the computation. As a consequence, the line bundle $\mathcal{O}_Y(X)$ is not only not ample, it is in fact further from being ample as $L$ becomes more positive. This partially explains why the argument for elliptic surfaces gets much more involved (see also Rmk~\ref{rmk: fundamentally nonlinear}). 


Interestingly, from the above perspective, the case of K3 surfaces is yet more different. If $X$ is a K3, then there is no natural choice of a polarization on $X$ and there is no natural threefold $Y$ which contains $X$ as a divisor. In fact, as the work of Lieblich-Maulik-Snowden \cite{LMS} illustrates, the Tate conjecture is equivalent to being able to find polarizations of bounded degree on any K3 surfaces defined over a fixed finite field. This was taken up by Charles \cite{Charles2} to give a proof of the Tate conjecture for K3's of a different flavor compared to Madapusi-Pera's. 


\appendix



# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, 67