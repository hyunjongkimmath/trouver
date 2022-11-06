---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]
\begin{proposition}
\label{prop: nonlinear Bertini}
Let $C$ be a smooth projective curve of genus $g$ over $k$ and let $L$ be a line bundle on $C$ with degree $h$. Set $V_r \coloneqq \mathrm{H}^0(L^r)$ for every $r \in \mathbb{N}$. For every $d \in \mathbb{N}$, consider the closed subset of $\mathbb{A}(V_4 \oplus V_6) \times C$ defined by
$$ \mathcal{K}_d \coloneqq \{ (a_4, a_6, c) \in V_4 \times V_6 \times C \mid \mathrm{val}_c(\Delta) \ge d \} $$
and endow it with the reduced subscheme structure. Likewise, let $D \subseteq C \times C$ be the diagonal and define a closed subscheme in $\mathbb{A}(V_4 \oplus V_6) \times (C \times C - D)$ by $$ \mathcal{K}_2^+ \coloneqq \{ (a_4, a_6, c) \in V_4 \times V_6 \times (C \times C - D) \mid \mathrm{val}_c(\Delta) \text{ and } \mathrm{val}_{c'}(\Delta) \text{ are both }\ge 2 \}. $$
If $2h \ge g + 1$, then we have the following: 
\begin{enumerate}[label=\upshape{(\alph*)}]
    \item $\mathcal{K}_d$ has codimension $d$ for $d \le 3$.
    \item $\mathcal{K}_2$ has two irreducible components $\mathcal{K}_2(\mathrm{I}_2)$ and $\mathcal{K}_2(\mathrm{II})$ characterized by conditions $\mathrm{val}_c(a_6) = 0$ and $\mathrm{val}_c(a_6) \ge 1$ respectively.
    \item $\mathcal{K}_2^+$ has codimension $4$. 
\end{enumerate}
\end{proposition}
\begin{proof}
We will repeatedly use the following simple consequence of the Riemann-Roch theorem: For any line bundle $M$ on $C$, if $\mathrm{deg}(M) \ge 2g - 1$, then $h^0(M) = \mathrm{deg}(M) - g + 1$; if $\mathrm{deg}(M) = 2g - 2$, then $h^0(M) = \mathrm{deg}(M) - g + 1$ unless $M \,{\cong}\, \omega_C$. 

Fix any point $c \in C$ and consider the projection $\mathcal{K}_d \to C$. It suffices to show that the fiber $\mathcal{K}_{d, c}$ over $c$, viewed naturally as a closed subscheme of $\mathbb{A}(V_4 \oplus V_6)$, has codimension $d$. We identify the completion of $C$ along $c$ with $\mathrm{Spf}(k[\![t]\!])$ by choosing a uniformizer $t$. After choosing a local generator of $L$, we may consider the Taylor series of any $\sigma \in \mathrm{H}^0(L^r)$, which is a power series $\sigma(t) \in k[\![t]\!]$. By the first paragraph, for $r \ge 4$ and $d \le 3$, we have 
$$ h^0(L^r((1-d)c)) = h^0(L^r(-dc)) + 1. $$
Therefore, we may choose a basis $\sigma_0, \cdots, \sigma_{4h - g}$ for $V_4$ such that $\mathrm{val}_c(\sigma_i) = 0$ for $i = 0, 1, 2$ and $\{ \sigma_i\}_{3 \le i \le 4h - g}$ forms a basis for $\mathrm{H}^0(L^4(-3c))$. We may assume that $\sigma_0(t) \equiv 1, \sigma_1(t) \equiv t$ and $\sigma_2(t) \equiv t^2$ modulo $t^3$. We choose a basis $\{ \theta_0, \cdots, \theta_{6h - g} \}$ in an entirely similar way. 

With the given choices of bases, we use $\{ \alpha_i \}$ and $\{ \beta_j \}$ for the coordinates of $V_4$ and $V_6$ respectively, so that $\Delta$ can be expressed as 
\begin{equation}
\label{eqn: express Delta}
    \Delta = 4 \left(\sum_{i = 0}^{4h - g} \alpha_i \sigma_i \right)^3 - 27 \left(\sum_{j = 0}^{6h - g} \beta_j \theta_j \right)^2.
\end{equation}
Then the fiber $\mathcal{K}_{d, c}$ ($d \le 3$) is cut out in $\mathbb{A}(V_4 \oplus V_6)$ by the first $d$ equations from below: 
\begin{align}
\begin{cases}
    \Delta(0) &= 4 \alpha_0^3 - 27 \beta_0^2 \\
    \Delta'(0) &= 3(4 \alpha_0^2 \alpha_1 - 18 \beta_0 \beta_1) \\
    \Delta''(0) &= 24(\alpha_0 \alpha_1^2 + \alpha_0^2 \alpha_2) - 54(\beta_1^2 + 2 \beta_0 \beta_2)
\end{cases}
\end{align}

The statement (a) is clear for $d = 0, 1$. For $d = 2$, it is clear that $\mathcal{K}_2$ contains the following subscheme 
$$ \mathcal{K}_2(\mathrm{II}) \coloneqq \{ (a_4, a_6, c) \in V_4 \times V_6 \times C \mid \mathrm{val}_c(a_4) \ge 1, \mathrm{val}_c(a_6) \ge 1 \}, $$
such that the fiber of $\mathcal{K}_{2}(\mathrm{II})$ over $c$ is simply cut out by $\alpha_0 = \beta_0 = 0$. Let $\mathbb{A}^2 \coloneqq \mathbb{A}(k\< \sigma_0, \theta_0 \>)$ be the affine space with coordinates $(\alpha_0, \beta_0)$ and $C' \subseteq \mathbb{A}^2$ be the cuspidal curve defined by $\Delta(0) = 0$. Then the fiber of $\mathcal{K}_2 - \mathcal{K}_2(\mathrm{II})$ over a point in $C' - \{(0, 0)\}$ is given by a codimension $1$ hyperplane in $\mathbb{A}(k\< \sigma_i, \beta_j \rangle_{i, j \ge 1})$. This implies that $\mathcal{K}_2 - \mathcal{K}_2(\mathrm{II})$ is irreducible of codimension $2$ in $\mathbb{A}(V_4 \oplus V_6)$, and we denote this component by $\mathcal{K}_2(\mathrm{I}_2)$. Note that this implies (b). To see the $d = 3$ case for (a), just note that $\Delta''(0)$ does not vanish identically on both $\mathcal{K}_2(\mathrm{I}_2)$ and $\mathcal{K}_2(\mathrm{II})$. 

Finally we treat (c). We consider the projection $\Phi \colon \mathcal{K}_2^+ \to (C \times C - D)$ and take a point $(c, c') \in (C \times C - D)$. Denote the fiber of $\Phi$ over $(c, c')$ by $\Phi_{(c, c')}$. We assume first that $ L^4 \not\cong \omega_C(2c + 2c')$. This condition is automatically satisfied when $2h > g + 1$ and ensures that $h^0(L^r(-2c - 2c')) = rh + g - 5$ for $ r \ge 4$. Then we may choose $\sigma_0, \cdots, \sigma_3 \in V_4$ with the following vanishing orders: 

\begin{equation}
\label{eqn: order of poles}
\begin{tabular}{ |c|c|c|c|c| } 
 \hline
  & $\sigma_0$ & $\sigma_1$ & $\sigma_2$ & $\sigma_3$ \\ \hline
 $\mathrm{val}_c$ & $0$ & $1$ & $\ge 2$ & $\ge 2$\\ \hline
 $\mathrm{val}_{c'}$ & $\ge 2$ & $\ge 2$ & $0$ & $1$ \\ \hline
\end{tabular}
\end{equation}
Then we complete $\{ \sigma_0, \cdots, \sigma_3 \}$ to a basis $\{ \sigma_i \}$ of $V_4$ by adjoining a basis for $\mathrm{H}^0(L^4(-2c - 2c'))$. Let $t, s$ be uniformizers of the completions of $C$ along $c$ and $c'$ respectively. After choosing local generators of $L$, we may consider Taylor series $\sigma_i(t) \in k[\![t]\!]$ and $\sigma_i(s) \in k[\![s]\!]$, and assume that $\sigma_0(t) \equiv 1, \sigma_1(t) \equiv t \mod t^2$ and $\sigma_2(s) \equiv 1, \sigma_3(s) \equiv s \mod s^2$. Choose an entirely similar basis $\{ \theta_j \}$ for $V_6$ and express $\Delta$ again as in (\ref{eqn: express Delta}). Then the defining equations for $\Phi_{(c, c')}$ in $\mathbb{A}(V_4 \oplus V_6)$ are 
\begin{align}
    \begin{cases}
    & 4 \alpha_0^3 - 27 \beta_0^2 = 4 \alpha_2^3 - 27 \beta_2^2 = 0 \\
    & 3(4 \alpha_0^2 \alpha_1 - 18 \beta_0 \beta_1) = 3(4 \alpha_2^2 \alpha_3 - 18 \beta_2 \beta_3) = 0 
    \end{cases}
\end{align}
By the same argument for the $d = 2$ case in (a), the above equations define a codimension $4$ subscheme. The point is that the variables with indices $0, 1$ do not interfere with those with $2, 3$.  

It remains to deal with the case when $2h = g + 1$ and $L^4 \,{\cong}\, \omega_C(2c + 2c')$. Note that in this case $g \ge 1$, so the condition $L^4 \,{\cong}\, \omega_C(2c + 2c')$ defines a closed subscheme of $(C \times C - D)$ of codimension at least $1$. Therefore, it is enough to show that the codimension of $\Phi_{(c, c')}$ is at least $3$. Note that we are able to choose a basis $\{ \theta_j \}$ just as before, but this time choose $\{\sigma_0, \sigma_1, \sigma_2\}$ with the following vanishing orders: 
\begin{equation}
\label{eqn: order of poles}
\begin{tabular}{ |c|c|c|c| } 
 \hline
  & $\sigma_0$ & $\sigma_1$ & $\sigma_2$ \\ \hline
 $\mathrm{val}_c$ & $0$ & $1$ & $2$ \\ \hline
 $\mathrm{val}_{c'}$ & $2$ & $1$ & $0$ \\ \hline
\end{tabular}
\end{equation}
and complete it to a basis of $V_4$ by adjoining a basis of $H^0(L^4(-2c - 2c'))$. Assume that $\sigma_0(t) = 1, \sigma_1(t) = t \mod t^3$ and $\sigma_2(s) = 1 \mod s$. Then the conditions $\mathrm{val}_c(\Delta) \ge 2$ and $\mathrm{val}_{c'}(\Delta) \ge 1$ give us $3$ equations which are necessarily satisfied by $\Phi_{(c, c')}$: 
\begin{align}
    \begin{cases}
    & 4 \alpha_0^3 - 27 \beta_0^2 = 4 \alpha_2^3 - 27 \beta_2^2 = 0 \\
    & 3(4 \alpha_0^2 \alpha_1 - 18 \beta_0 \beta_1) = 0 
    \end{cases}
\end{align}
It is clear that these indeed cut out a subscheme of codimension $3$. 
\end{proof}

# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, proposition 8.6