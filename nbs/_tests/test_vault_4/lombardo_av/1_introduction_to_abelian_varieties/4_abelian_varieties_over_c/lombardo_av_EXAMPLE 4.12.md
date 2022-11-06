---
cssclass: clean-embeds
aliases: [lombardo_av_Canonical_polarisation_of_an_elliptic_curve]
tags: [_auto/notations_added, _auto/links_added, _meta/example, _meta/literature_note, _reference/lombardo_av, _meta/TODO/change_title]
---
# Canonical polarisation of an elliptic curve[^1]
EXAMPLE 4.12 (Canonical [[lombardo_av_DEFINITION 4.8|polarisation]] of an elliptic [[foag_11.1.3|curve]]). We now show that every elliptic [[foag_11.1.3|curve]] over $\mathbb{C}$ admits a canonical principal [[lombardo_av_DEFINITION 4.8|polarisation]]. Up to a $\mathbb{C}$-linear change of variables, we may assume that the [[18785_Definition 5.9|lattice]] $\Lambda$ is $\mathbb{Z} \cdot 1 \oplus \mathbb{Z} \cdot \tau$, with $\tau$ in the upper half-plane. To define a [[lombardo_av_DEFINITION 4.8|polarisation]] we need to define a positive-definite [[hermitian_form#Hermitian form 1|Hermitian form]] $\mathbb{C} \times \mathbb{C}$ whose imaginary part takes integer values on 1 and $\tau=a+b i .$ A Hermitian scalar product on $\mathbb{C}$ is uniquely defined by its value on $(1,1)$, so we look for a [[lombardo_av_DEFINITION 4.8|polarisation]] of the form
$$
\begin{aligned}
H: & \mathbb{C} \times \mathbb{C} \rightarrow \mathbb{C} \\
\left(z_{1}, z_{2}\right) & \mapsto \gamma z_{1} \overline{z_{2}}
\end{aligned}
$$
in order for $H$ to be Hermitian and positive definite, $\gamma$ needs to be real and positive.
Write $E:=\Im H ;$[^2]               one checks that $E$ is skew-symmetric (this is always true: if $H$ is a [[lombardo_av_DEFINITION 4.8|polarisation]], $E=\Im H$[^2]               is skew-symmetric), hence we have $E(1,1)=E(\tau, \tau)=0 ;$ the only requirement is then $E(\tau, 1) \in \mathbb{Z}$, that is, $\gamma \Im \tau \in \mathbb{Z} .$[^2]               Since $\Im>0$[^2]              , we can choose $\gamma:=\frac{1}{\Im T}$[^2]               We then obtain the [[lombardo_av_DEFINITION 4.8|polarisation]]
$$
H\left(z_{1}, z_{2}\right)=\frac{z_{1} \overline{z_{2}}}{\mathrm{~S} \tau}
$$
It is also easy to see that $H$ is a principal [[lombardo_av_DEFINITION 4.8|polarisation]] (and in fact it's the unique principal [[lombardo_av_DEFINITION 4.8|polarisation]] of $E$ ). Assuming the previous remark it would be enough to notice that in the basis $\{\tau, 1\}$ the matrix of $\Im H$[^2]               is $\left(\begin{array}{cc}0 & 1 \\ -1 & 0\end{array}\right)$ to deduce that $d(H)=1$[^3]               and that $H$ is a principal [[lombardo_av_DEFINITION 4.8|polarisation]]. We check this by hand by finding the [[18785_Definition 5.9|lattice]] $\Lambda^{\vee} . \mathrm{A}$[^4][^5]               linear functional $\psi$ lies in $\Lambda^{\vee}$[^4][^5]               if and only if $\Im \psi(1) \in \mathbb{Z}$[^2]               and $\Im \psi(\tau) \in \mathbb{Z} .$[^2]               Clearly $\psi$ is determined by $\psi(1)=a+b i$ with $b \in \mathbb{Z} ;$ writing $\tau=\Re \tau+i$ 3t we have
$$
\begin{aligned}
\psi(\tau) &=\psi(\Re \tau+i \Im \tau)=\Re \tau \psi(1)-i \Im \tau \psi(1) \\
&=\Re \tau(a+b i)-i \Im \tau(a+b i)=(a \Re \tau+b \Im \tau)+i(b \Re \tau-a \Im \tau)
\end{aligned}
$$
[^2]
so that $\Im \psi(\tau)=b \Re \tau-a \Im \tau$[^2]              . This is equal to an integer $n$ if and only if
$$
a=\frac{b \Re \tau-n}{\Im \tau}
$$
[^2]
Hence $\psi(1)=a+b i=\frac{b \Re \tau+b i \Im \tau-n}{\Im \tau}=\frac{b \tau-n}{\Im \tau}$[^2]              , and therefore $\psi=H(\lambda, \cdot)$ for $\lambda=$ $b \tau-n \in \Lambda$. This implies that $\lambda_{H}: V \rightarrow \bar{V}^{\vee}$[^6][^7]               induces an isomorphism of $\Lambda$ with $\Lambda^{\vee}$[^4][^5]              , hence an isomorphism $\lambda_{H}: V / \Lambda \cong \bar{V}^{\vee} / \Lambda^{\vee}$[^6][^7][^4][^5]               as claimed.

Finally, we remark that it is a general fact that an elliptic [[foag_11.1.3|curve]] over any field $K$ admits precisely one [[lombardo_av_DEFINITION 4.8|polarisation]] of [[degree_of_an_algebraic_field_extension|degree]] $d^{2}$ for every $d \geq 1$ (see e.g. [Con04]).

We conclude this section with a result which is actually valid over any algebraically closed field, but that is easier to prove over $\mathbb{C}:$


# See Also

# Meta
## References
![[_reference_lombardo_av]]

## Citations and Footnotes
[^1]: Lombardo, EXAMPLE 4.12, Page 14
[^2]: ![[lombardo_av_notation_Im]]
[^3]: ![[lombardo_av_notation_d_H]]
[^4]: ![[lombardo_av_notation_Lambda_vee]]
[^5]: ![[lombardo_av_notation_Lambda_vee_dual_complx_abelian_variety]]
[^6]: ![[lombardo_av_notation_bar_V_vee]]
[^7]: ![[lombardo_av_notation_lambda_H]]