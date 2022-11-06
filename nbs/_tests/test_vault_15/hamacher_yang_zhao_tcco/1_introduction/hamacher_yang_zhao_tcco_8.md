---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]


For example, the $r = 1$ and $d = 2$ case of theorem simply says that the discriminant $b^2 - 4ac$ for the quadratic equation $a x^2 + b xy + c y^2 = 0$ is a square of an irreducible polynomial modulo $2$. In \cite{Saitodisc}, Saito proved that for general $d \ge 2$ and odd $r \ge 1$, $\mathrm{disc}_d(F)$ is always a square modulo $4$ up to a sign. The theorem above provides a refinement which says that $\mathrm{disc}_d(F)$ modulo $2$ can not be further factorized. Interestingly, our proof of this simple statement involves a quite recent theorem of Beilinson (\cite{Beilinson}). 

%Let $r \ge 1, d \ge 2$ be positive integers. Let $\mathbb{P}^r$ be the $r$-dimensional projective space over $\mathbb{Z}$ and let $\mathbb{P} := |\mathcal{O}_{\mathbb{P}^r}(d)|$ be the projective space over $\mathbb{Z}$ parametrizing the degree $d$ hypersurfaces of $\mathbb{P}^r$. Let $\mathfrak{D} \subseteq \mathbb{P}$ be the closed subset of $\mathbb{P}$ whose points correspond to singular hypersurfaces and endow $\mathfrak{D}$ with the reduced scheme structure. If $r$ is odd, then $\mathfrak{D} {\otimes} \bar{\mathbb{F}}_2$ is the square of an irreducible polynomial. 


\paragraph{Sketch of Proofs} We take the overall strategy of \cite{MPTate} as a starting point and interpret it as follows: Suppose that $\mathsf{M}$ is the moduli space over $\mathrm{Spec}(\mathbb{Z})$ for some type of smooth projective varieties and let $f \colon \mathscr{X} \to \mathsf{M}$ be the universal family.
Let $k$ be a finite extension of $\mathbb{F}_p$, and let $s \in \mathsf{M}$ be a closed point with residue field $k$. Suppose that the fiber $X \coloneqq \mathscr{X}_s$ has the following property: 
\begin{equation}
\label{eqn: lifting exists}
\textit{For any $\xi \in \mathrm{NS}(X)$, $X$ can be lifted to a $\mathbb{C}$-fiber of $\mathscr{X}$ together with $\xi$.}   \tag{$\star$} 
\end{equation}
By the Lefschetz $(1, 1)$-theorem and the specialization of line bundles, the Tate conjecture for $X$ is equivalent to: 
\begin{equation}
    \label{eqn: Tate in (1, 1)}
    \textit{The image of} \bigcup_{\widetilde{s} \rightsquigarrow s} \mathrm{H}^2(\mathscr{X}_{\widetilde{s}}, \mathbb{Q})^{(1, 1)} \textit{ under specialization spans } \mathrm{H}^2_\mathrm{{\acute{e}}t}(X_{\bar{k}}, \mathbb{Q}_\ell)^{\mathrm{Gal}_k}, \tag{$\star'$}
\end{equation}
where $\widetilde{s}$ runs through all $\mathbb{C}$-points which specialize to $s$. Note that $(\star')$ is a condition which only concerns cohomology. So ideally, if we know enough about the cohomology sheaves of $\mathscr{X}$ over $\mathsf{M}$, we obtain the Tate conjecture for $X$ under assumption (\ref{eqn: lifting exists}). 

%Choose an isomorphism $\bar{\mathbb{Q}}_p \,{\cong}\, \mathbb{C}$ and embed all finite extensions of $W(k)$ into $\bar{\mathbb{Q}}_p$.

We now explain the difficulties in generalizing the above strategy to general $h^{2, 0} = 1$ varieties and how to overcome them. 

\subparagraph{Step I: Prove $(\star)$} The $h^{2, 0} = 1$ condition implies that the obstruction to deforming $\xi$ is given by a power series $\widehat{f}_\xi$ on $\widehat{\mathsf{M}}_s$, the formal completion of $\mathsf{M}$ at $s$. It is enough to show that $p \nmid \widehat{f}_\xi$. For K3 surfaces, this was proved by Deligne (\cite{Del02}). However, Deligne's method relies crucially on the fact that K3 surfaces have unobstructed deformation and the Kodaira-Spencer map is an isomorphism. This method is not possible in our case: In general, deformations of $h^{2, 0} = 1$ varieties may well be obstructed, and understanding the Kodaira-Spencer map is essentially a \textit{local Schottky problem}, which is famously hard. In fact, the map can indeed be quite chaotic (e.g., not flat) for natural families of complex $p_g = 1$ surfaces.  

To circumvent the local Schottky problem, we take instead a topological approach torwards the lifting question. The key observation is that $\widehat{f}_\xi$ algebraizes to a local section $f_\xi$ of $\mathcal{O}_\mathsf{M}$. For simplicity, assume that $\mathsf{M}_{\mathbb{F}_p}$ and $\mathsf{M}_\mathbb{Q}$ are geometrically irreducible, and let $\bar{\eta}_p$ and $\bar{\eta}$ be their geometric generic points respectively. If $p \mid f_\xi$ and $\xi$ does not lift to characteristic $0$, then $\mathrm{NS}(\mathscr{X}_{\bar{\eta}_p})$ is strictly bigger than $\mathrm{NS}(\mathscr{X}_{\bar{\eta}})$, and we have an inequality
\begin{equation}
\label{eqn: geometric Picard jump}
    \dim \left( \varinjlim_{U \subseteq \pi_1^{\mathrm{{\acute{e}}t}}(\mathsf{M}_{\bar{\mathbb{F}}_p}, \bar{\eta}_p)} \mathrm{H}^2_\mathrm{{\acute{e}}t}(\mathscr{X}_{\bar{\eta}_p}, \mathbb{Q}_\ell)^U \right) > \dim \left( \varinjlim_{U' \subseteq \pi_1^{\mathrm{{\acute{e}}t}}(\mathsf{M}_{\bar{\mathbb{Q}}}, \bar{\eta})} \mathrm{H}^2_\mathrm{{\acute{e}}t}(\mathscr{X}_{\bar{\eta}}, \mathbb{Q}_\ell)^{U'} \right)
\end{equation}
where the limits are taken as $U, U'$ run through compact open subgroups. The crucial fact we are using is that the right hand side is equal to $\mathrm{rank\,} \mathrm{NS}(\mathscr{X}_{\bar{\eta}})$, which follows from a suitable version of the theoerem of the fixed part due to Andr\'e and the classification of possible Mumford-Tate groups due to Zarhin. Hence to show $(\star)$ for a prime $p$ it is sufficient to show that the above inequality is impossible. 

Our main tool to compare $\pi_1^\mathrm{{\acute{e}}t}(\mathsf{M}_{\bar{\mathbb{F}}_p}, \bar{\eta}_p)$ with $\pi_1^\mathrm{{\acute{e}}t}(\mathsf{M}_{\bar{\mathbb{Q}}}, \bar{\eta})$ is Grothendieck's specialization theorem on tame fundamental groups, provided that $\mathsf{M}$ admits a good compactification $\bar{\mathsf{M}}$ relative to $\mathbb{Z}_p$. By ``good'' we mean that the boundary is a (relative) simple normal crossing divisor. By a spreading out argument, such a compactification can always be found for $p \gg 0$. In particular, (\ref{eqn: geometric Picard jump}) fails for $p \gg 0$. Combined with step II, this gives Thm~\ref{thm: generic}. 

However, for any fixed $p$, it is easy to construct counterexamples where the inequality (\ref{eqn: geometric Picard jump}) \textit{does} hold, and some consequences of the theorem of the fixed part in characteristic $0$ fails in characteristic $p$ (Ex.~\ref{ex: supersingular} and~\ref{ex: quaternion}). Therefore, for concretely given $\mathsf{M}$, it is a subtle problem to effectively determine a range for $p$, away from which (\ref{eqn: geometric Picard jump}) cannot possibly hold. 

\subparagraph{Step I+: Analyze Discriminant Varieties} Interestingly, for all the examples we consider, the moduli $\mathsf{M}$ admits a natural \textit{relative compactification}. More precisely, $\mathsf{M}$ admits a morphism to a certain base $B$ such that $\mathsf{M}$ embeds as an open subscheme into a projective bundle $\mathscr{P}$ over $B$. Moreover, the boundary $\mathfrak{D} \coloneqq \mathscr{P} - \mathsf{M}$ is a discriminant variety. That is, there exists an extension $\overline{\mathscr{X}}$ of the family $\mathscr{X}$ to $\mathscr{P}$ such that $\mathfrak{D}$ is the image of the singular locus of the morphism $\overline{\mathscr{X}} \to \mathscr{P}$. 

We may disprove inequality (\ref{eqn: geometric Picard jump}) if we find a smooth proper curve $\mathcal{C}$ over $W := W(\bar{\mathbb{F}}_p)$ with a morphism $\mathcal{C} \to \mathscr{P}_W$ such that (a) the geometric special fiber $C \coloneqq \mathcal{C}_{\bar{\mathbb{F}}_p}$ intersects $\mathfrak{D}_{\bar{\mathbb{F}}_p}$ transversely, and (b) $(\mathcal{C} - \mathcal{C} \cap \mathfrak{D}_W)_\mathbb{C}$ is not contracted by the period morphism and does not lie in the Noether-Lefschetz loci, for some (and hence any) embedding $W \hookrightarrow \mathbb{C}$.

We construct $\mathcal{C}$ backwards. Namely, we construct the $\bar{\mathbb{F}}_p$-curve $C$ first and then lift it appropriately to $W$. To start, we construct a family of proper rational curves on $\mathsf{M}$ parametrized by a smooth $W$-scheme $T$, i.e., a morphism $\varphi \colon \mathbb{P}^1_T \to \mathsf{M}$, such that the special and generic fibers of $\varphi$ \textit{homogeneously dominate} those of $\mathsf{M}$ (see Def.~\ref{def: homogeneously dominates}). This means that there is the same amount of curves in this family which pass through any point on $\mathsf{M}$ in any given tangent direction. By Bertini-type arguments, a general $\bar{\mathbb{F}}_p$-point $t$ on $T$ gives a curve which satisfies (a) as long as 
\begin{equation}
\label{eqn: reducedness}
\text{the codimenstion $1$ irreducible components of $\mathfrak{D}_{\bar{\mathbb{F}}_p}$ are generically reduced modulo $p$.} \tag{$\spadesuit$}
\end{equation}
Then we apply the Baire category theorem to find an appropriate lifting which satisfies (b). The key is that the ``bad'' locus on the generic fiber of $T$ to be avoided is contained in countably many proper subvarieties. 

The most intricate part of the proof is to find a sufficient condition on $p$ for (\ref{eqn: reducedness}) to hold, as sometimes even natural discriminant varieties may become nonreduced modulo certain $p$ (see Appendix A). We draw ideas from enumerative geometry to detect possibly problematic $p$. By applying the Grothendieck-Ogg-Shafarevich (GOS) formula, we show that (\ref{eqn: reducedness}) holds as long as the singular fibers of the morphism $\overline{\mathscr{X}} \to \mathscr{P}$ lying over $\mathfrak{D}_{\bar{\mathbb{F}}_p}$ generically have the same total dimension of vanishing cycles as those over $\mathfrak{D}_\mathbb{C}$. Note that the total dimension of vanishing cycles incorporates both the ``topological'' vanishing cycles and the Swan conductors (\cite[{\S}XVI]{SGA7II}). 
\begin{itemize}
    \item For elliptic surfaces of height $h$ over a base curve of genus $g$, we show that ($\spadesuit$) holds if $p \ge 5$ and $2h \ge g + 1$. More precisely, with the aid of Kodaira's classification of singular fibers in an elliptic fibration, we prove the key intermediate statement that the generic singular fiber over $\mathfrak{D}_{\bar{\mathbb{F}}_p}$ is the Weierstrass normal form of an elliptic surface with a single $\mathrm{I}_2$-fiber (in Kodaira's table), so that this singular fiber is smooth away from an ordinary double point (ODP). The proof suggests that this statement may well fail if $h$ were not sufficiently big relative to $g$, but luckily $h = g = 1$ is right at the boundary for which we can verify the statement, so we obtain Thm~\ref{thm: BSD}. 
    \item For Thm~\ref{thm: general type} and~\ref{thm: Gushel-Mukai}, $\mathfrak{D}$ is the discriminant variety of certain linear system and we may use linear pencils for $\varphi$. We may simply analyze the singularieties by mildly extending Katz' existence criterion for Lefshetz pencils. 
\end{itemize}
In the appendix, we show the effectiveness of our enumerative approach to study the mod $p$ behavior of discriminant varieties through examples where (\ref{eqn: reducedness}) fails. We prove Thm~\ref{thm: improve Saito} and prove a similar result for Katz' nonexample of Lefschetz embedding.

\subparagraph{Step II : Prove (\ref{eqn: Tate in (1, 1)})} This is where we make use of the Kuga-Satake (KS) construction, which is a long tradition in the field. For a suitable lattice $L$, the orthogonal Shimura variety $\mathrm{Sh}(L)_\mathbb{C}$ parametrizes Hodge structures of K3-type on $L$, such that there is a complex period map $\rho_\mathbb{C} \colon \mathsf{M}_\mathbb{C} \to \mathrm{Sh}(L)_\mathbb{C}$. The Shimura variety $\mathrm{Sh}(L)$ has reflex field $\mathbb{Q}$ and admits a canonical integral model $\mathscr{S}(L)$ over $\mathbb{Z}_{(p)}$. As in \cite{MPTate}, we proceed in $3$ broad steps: (i) Show that $\rho_\mathbb{C}$ descends to $\mathbb{Q}$ and extends to $\mathbb{Z}_{(p)}$. (ii) Show that the cohomology sheaves on $\mathsf{M}$ given by $\mathscr{X}$ can be recovered by certain automorphic sheaves on $\mathscr{S}(L)$. (iii) Convert $(\star')$ to a question about automorphic sheaves, and prove it by appealing to Kuga-Satake abelian varieties, whose cohomology gives a different realization of these automorphic sheaves. 

Step (iii) will work verbatim as in \textit{loc. cit.} for us once (i) and (ii) are done, but (i) and (ii) require new ideas. For K3 surfaces, these two steps were built upon the fact that the moduli of K3 surfaces have maximal monodromy, and the motive of a K3 surface is \textit{abelian} in Deligne's category of motives with absolute Hodge cycles. These inputs are not available to us for general $h^{2, 0} = 1$ varieties. Problems arise when that the motives in question have a totally real endomorphism field $E$ bigger than $\mathbb{Q}$. However, we extract from Moonen's work \cite{Moonen} that certain ``$E/\mathbb{Q}$-norm'' of these motives is still abelian. This allows us to show that $\mathrm{Sh}(L)$ contains some Shimura subvarieties $\mathrm{Sh}'$, whose reflex field is $E$, such that $\rho_\mathbb{C}$ factors as 
$$ \mathsf{M}_\mathbb{C} \to \coprod_{\sigma \colon E \hookrightarrow \mathbb{C}} \mathrm{Sh}' {\otimes}_\sigma \mathbb{C} \to \mathrm{Sh}(L)_\mathbb{C}, $$
and both morphisms descend to $\mathbb{Q}$. This gives (i). Morally speaking, $\mathrm{Sh}'$ should be viewed as moduli spaces of these ``norm'' motives. We make crucial use of the theory of \textit{conjugate} Shimura varieties, and show that the coproduct of a Shimura variety with all its conjugates admits a natural moduli interpretation (see \S\ref{sec: Shimura}) under some mild assumptions. 

After we do step (i), we may identify the norm of cohomology sheaves with that of the automorphic sheaves, so step (ii) is essentially about salvaging a comparison of the original sheaves from that of their norms. This is relatively straightforward for the Betti and $\ell$-adic sheaves (including $p$-adic sheaves whenever in characteristic $0$), but gets subtle for the de Rham sheaves---one needs to prove that the $p$-adic Riemann-Hilbert (RH) correspondence and the classical one gives the same identification of de Rham sheaves. In fact, this would follow from the general conjecture that ``Hodge cycles are de Rham''. To this end, we extend Blasius' notion of de Rham cycles to a relative setting, and apply a trick of deforming transcendental classes in Hodge structures to algebraic classes. 



# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, 8