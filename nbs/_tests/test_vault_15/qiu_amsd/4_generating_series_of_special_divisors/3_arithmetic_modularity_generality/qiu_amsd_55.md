---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/qiu_amsd]
---
# Topic[^1]



\label{Arithmetic modularity}
\subsubsection{Kudla's arithmetic modularity problem}
 \label{integral modeldef}
A  (regular) integral model  of  ${\mathrm{Sh}}({\mathbb {V}})_{K}$ over an integral domain $R$ with fraction field $E$ is  a (regular) Deligne-Mumford stack  proper flat over ${\mathrm{Spec}} R$    with a fixed isomorphism of its generic fiber to $ {\mathrm{Sh}}({\mathbb {V}})_{K }.$ An isomorphism between integral models  is  an isomorphism over ${\mathrm{Spec}} R$  that  respects the  fixed isomorphisms  to $ {\mathrm{Sh}}({\mathbb {V}})_{K }.$
 
Let  ${\mathcal {X}}_K$ be a regular integral model  of  ${\mathrm{Sh}}({\mathbb {V}})_{K}$ over ${\mathrm{Spec}} {\mathcal {O}}_E$.
Let   $\widehat {\mathrm{Ch}}^1_{{\mathbb {C}}}({\mathcal {X}}_K) $ be  the Chow group of 
   ${\mathbb {C}}$-coefficient arithmetic divisors, see Definition \ref{CCH}.
   In particular, we have an isomorphism $$ \deg:  \widehat {\mathrm{Ch}}^1_{{\mathbb {C}}}\left(   {\mathrm{Spec}} {\mathcal {O}}_{E}  \right)\simeq {\mathbb {C}}$$ by taking degrees (see Remark \ref{cmc}), and  an arithmetic  intersection
    pairing 
    \begin{align*}\widehat{\mathrm{Ch}}^1_{\mathbb {C}}({\mathcal {X}}_K)\times Z_1({\mathcal {X}}_K)_{\mathbb {C}} \to {\mathbb {C}},\ 
(\widehat z,Y) \mapsto \widehat z\cdot Y \end{align*}
 (see Appendix \ref{arithmetic  intersection
    pairing}).
Here we recall that $Z_1({\mathcal {X}}_K)$ is  the    group of 1-cycles on ${\mathcal {X}}_K$. 



Let   $   {\mathcal {L}}= {\mathcal {L}}_K$ be  an     extension  of $L=L_K $ to ${\mathcal {X}}_K$,
 which we allow to be a ${\mathbb {Q}}$-bundle. 
Let   $  \overline{\mathcal {L}} $ be    ${\mathcal {L}}$ equipped with a hermitian metric. Let  $c_1(\overline {\mathcal {L}}^\vee)\in \widehat {\mathrm{Ch}}^{1}_{{\mathbb {C}}}({\mathcal {X}}_K) $ be the first arithmetic Chern class of the dual of  $\overline {\mathcal {L}}$, see  Example \ref{admextinf}.
As suggested by Kudla \cite{Kud02}\cite{Kud03}, we consider the following arithmetic modularity problem: find   
an  arithmetic divisor $\widehat {\mathcal {Z}}(x)$  on ${\mathcal {X}}$  extending $Z(x)$,    explicitly and canonically, such that   
\begin{equation*}   \omega(g)\phi(0)c_1(\overline {\mathcal {L}}^\vee)+\sum_{x\in K\backslash {\mathbb {V}}^{ \infty}_{>0}}
\omega(g)\phi( x_\infty x)  \widehat {\mathcal {Z}}(x) , \end{equation*} where
$ x_\infty \in   {\mathbb {V}}_\infty$ such that $q(x_\infty)={q(x)}\in F_{>0}$,
lies in   $  {\mathcal {A}}_{{\mathrm{hol}}}(G,{\mathfrak{w}}) \otimes    \widehat {\mathrm{Ch}}^{1}_{{\mathbb {C}}}({\mathcal {X}}_K) $. 
The existence of such $\widehat {\mathcal {Z}}(x)$  is obvious, by  choosing a section of the natural surjection  $\widehat{\mathrm{Ch}}^1_{{\mathbb {C}}}({\mathcal {X}}_K)\to {\mathrm{Ch}}^1({\mathrm{Sh}}({\mathbb {V}})_K)_{\mathbb {C}}$.  However, it is only    defined  at the level of   divisor classes, and not explicit.
%For example, S. Zhang   defined     $\mathsf{L}$-liftings of divisor classes in  \cite[Corollary 3.5.7]{Zha20}. 
%The computation of  $\mathsf{L}$-liftings is rather  hard,  as it involves   Faltings heights of Shimura varieties. Indeed, this is one potential application of our work, see \ref{Faltings heights of Shimura varieties and Arithmetic Siegel-Weil formula}.


\subsubsection{Admissible cycles} \label{Admissible cycles} 



%We    refine  Kudla's arithmetic modularity  problem  \cite{Kud02}\cite{Kud03} using S. Zhang's theory of admissible  cycles.   
We only use admissible divisors, see
Appendix \ref{until}. In particular, we assume Assumption \ref{A11asmp11} for ${\mathcal {X}}_K$.
Assume that $  {\mathcal {L}}$   is ample. Let    $ \widehat {\mathrm{Ch}}^{1}_{{\overline\cL},{\mathbb {C}}}({\mathcal {X}}_K)  \subset \widehat{\mathrm{Ch}}^1_{\mathbb {C}}({\mathcal {X}}_K)$ be the   Chow group of  ${\mathbb {C}}$-coefficient  admissible arithmetic
divisors   with respect to   $\overline {\mathcal {L}}$, see Definition \ref{CCH}.
%We use  $ \widehat {\mathrm{Ch}}^{1}_{{\overline\cL},{\mathbb {C}}}(\cxX_K) $ to denote $ \widehat {\mathrm{Ch}}^{1}_{{\overline\cL},{\mathbb {C}}}({\mathcal {X}}_K) $ for simplicity. 
By    Lemma \ref{fdime},  the natural  map   \begin{equation}  \label{lebo Lebo Lebo label hey hey hey hey} \widehat {\mathrm{Ch}}^{1}_{{\overline\cL},{\mathbb {C}}}({\mathcal {X}}_K) \to  {\mathrm{Ch}}^1({\mathcal {X}}_{K,E })_{{\mathbb {C}}}
 \end{equation}
 is  surjective, and  the kernel  is the  image of the pullback 
 \begin{equation}  \label{lebo Lebo Lebo label hey hey hey hey hey} \widehat {\mathrm{Ch}}^1_{\mathbb {C}}\left( {\mathrm{Spec}} {\mathcal {O}}_{E} \right)\simeq \widehat {\mathrm{Ch}}^1_{\mathbb {C}}\left( {\mathrm{Spec}} {\mathcal {O}}_{{\mathcal {X}}_K}({\mathcal {X}}_K)\right)_{\mathbb {C}}\hookrightarrow \widehat{\mathrm{Ch}}^1_{{\overline\cL},{\mathbb {C}}}({\mathcal {X}}_K). 
 \end{equation}
% In particular  $ \widehat {\mathrm{Ch}}^{1}_{{\overline\cL},{\mathbb {C}}}({\mathcal {X}}_K) $  is finite  dimensional.



# See Also

# Meta
## References
![[_reference_qiu_amsd]]


## Citations and Footnotes
[^1]: Citation, 55