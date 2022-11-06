---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/hamacher_yang_zhao_tcco]
---
# Topic[^1]
\begin{lemma}
\label{lem: Dirichlet}
Let $p$ be a prime number and $n \ge 1$ be any natural number. Then there exists a prime $\ell$ such that $p \nmid |\mathrm{GL}_n(\mathbb{F}_\ell)|$ if and only if $p - 1> n$.  
\end{lemma}
\begin{proof}
Recall the well known formula: 
$$ |\mathrm{GL}_n(\mathbb{F}_\ell)| = \prod_{j = 0}^{n - 1}(\ell^n - \ell^j). $$
Then it is easy to see that $p \nmid |\mathrm{GL}_n(\mathbb{F}_\ell)|$ if and only if $\{ 1, \ell, \ell^2, \cdots, \ell^n \}$ all have different residues modulo $p$, i.e., the order of $\ell$ in $\mathbb{F}_p^\times$ is greater than $n$. Therefore, if $p - 1 > n$, by Dirichlet's theorem there are infinitely many such $\ell$, but otherwise such $\ell$ does not exist by the pigeonhole principle. 
\end{proof}

# See Also

# Meta
## References
![[_reference_hamacher_yang_zhao_tcco]]


## Citations and Footnotes
[^1]: Citation, lemma 6.4