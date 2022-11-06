---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/qiu_amsd]
---
# Topic[^1]
\label{Motivation}
On the modular curve $X_0(N)$, let   $T_m$ be the $m$-th Hecke operator, $x,y$ Heegner points,   $\infty$ the cusp at infinity.
A key step in the proof   of the Gross-Zagier formula \cite{GZ} is the following numeric modularity result:  for $m$ coprime to $N$, the N\'eron-Tate  height pairing
\begin{equation*}\label{xTy}
\pair{x-\infty, T_m(y-\infty)}
\end{equation*}
is the $m$-th coefficient of an explicit   modular form involving theta series, Eisenstein series and derivatives of Eisenstein series. This is a precursor of our arithmetic mixed Siegel-Weil formula.

Regarding  $T_m$ as a cycle on $X_0(N)\times X_0(N)$, 
it follows from \cite{Bor} or \cite{YZZ1} that 
\begin{equation*}  \text{constant term}+\sum_{m> 0}T_m q^m
\end{equation*} is a modular form with a suitable constant term.  
Given an integral model of  $X_0(N)\times X_0(N)$,
Kudla's  arithmetic modularity problem asks if we can find 
a suitable   arithmetic extension ${\mathcal {T}}_m$, explicitly and canonically, such that the analogous modularity still holds. 





The starting point  of our work is the following observation: an  admissible  arithmetic extension
in the sense of \cite{Zha20}  has only 1-dimensional ambiguity. So if ${\mathcal {T}}_m$ is admissible, 
the modularity of  the generating series of arithmetic intersection numbers between  $ {\mathcal {T}}_m$'s and the Zariski closure of  any $(x,y)$  will imply the arithmetic modularity. 
The strategy of reducing the arithmetic modularity to numeric modularity
were also used in     \cite{Kud02}  \cite{KRY2}. The admissibility was  used in \cite{MZ} \cite{ZZY} from a different angle. % (see also \Cref{MZZ}).



Let us explain the  admissibility (see \Cref{htadm}).   
Recall that on a regular scheme  (or more generally Deligne-Mumford stack) ${\mathcal {X}}$  proper flat over ${\mathrm{Spec}} {\mathcal {O}}_E$, where $E$ is a number field,  
an arithmetic divisor on ${\mathcal {X}}$ is a divisor  equipped  with a Green function at each infinite place. 
%Let  $\widehat{\mathrm{Ch}}^1_{{\mathbb {C}}}({\mathcal {X}})$  be the arithmetic Chow group of arithmetic divisors with ${\mathbb {C}}$-coefficient.
Let $\overline{\mathcal {L}}=({\mathcal {L}},\|\cdot\|)$ be a  hermitian ${\mathbb {Q}}$-line bundle  on ${\mathcal {X}}$. Assume that ${\mathcal {L}}$ is ample  (we in fact only need generic ampleness and relative positivity).
At  each infinite place $v:E\hookrightarrow {\mathbb {C}}$,
equip  the complex manifold $ {\mathcal {X}}_v  $  with the K\"ahler form that is the curvature form  $c_1(\overline {\mathcal {L}}_v)$. 
A Green function  is called admissible if it has harmonic curvature.  Here,  the harmonicity of a closed $(1,1)$-form $\alpha
$  is equivalent to   that $c_1(\overline {\mathcal {L}}_v)^{n-1}\wedge \alpha$ is proportional to  $c_1(\overline {\mathcal {L}}_v)^{n}$, where $n=\dim {\mathcal {X}}_v$.
At each finite place $v$,  a divisor  $Y$ on  ${\mathcal {X}}_{ {\mathcal {O}}_{E_v}}$ is admissible if it  has ``harmonic curvature"  with respect to  $\overline {\mathcal {L}}_{ {\mathcal {O}}_{E_v}}$, in the sense that  the intersection linear form 
$?\cdot Y\cdot c_1( {\mathcal {L}}_{ {\mathcal {O}}_{E_v}})^{n-1}$  on the space of divisors supported on the special fiber of ${\mathcal {X}}_{ {\mathcal {O}}_{E_v}}$  is proportional to  $? \cdot c_1(  {\mathcal {L}}_{ {\mathcal {O}}_{E_v}})^{n}$.


Let $\widehat{\mathrm{Ch}}_{{\overline\cL},{\mathbb {C}}} ^1({\mathcal {X}}) $ be the space of   ${\mathbb {C}}$-coefficient admissible      arithmetic divisors   with respect to  $\overline {\mathcal {L}}$, modulo the ${\mathbb {C}}$-span of the principal ones. If ${\mathcal {X}}$ is connected, then    the  surjective natural map
\begin{equation}\label{natp}\widehat{\mathrm{Ch}}_{{\overline\cL},{\mathbb {C}}}^1({\mathcal {X}})\to {\mathrm{Ch}}^1({\mathcal {X}}_E)_{\mathbb {C}}\end{equation} has an 1-dimensional kernel.  It is the pullback of $   \widehat {\mathrm{Ch}}_{\mathbb {C}}^1\left( {\mathrm{Spec}} {\mathcal {O}}_{E} \right)\simeq {\mathbb {C}}$, where the isomorphism is by  taking degrees.










# See Also

# Meta
## References
![[_reference_qiu_amsd]]


## Citations and Footnotes
[^1]: Citation, 3