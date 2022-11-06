---
cssclass: clean-embeds
aliases: []
tags: [_meta/literature_note, _reference/qiu_amsd]
---
# Topic[^1]


For our application, we will let $X$ be ${\mathbb {W}}_v$ and let  $X'$ be  $V^\sharp(E_v)$ for $v$ split in $E$.
In this case, we can also consider an  ``enhanced version  of Lemma \ref{Fourier}", by  removing the orthogonal complements of several $k_v^{-1}{\mathbb {W}}_v$'s in ${\mathbb {V}}_v$, rather than just ${\mathbb {W}}_v$. Moreover, instead of Fourier transform, which is the action of an element of $  G(F_v)$ 
under the Weil representation (up to the Weil index),   one can use the whole $G(F_v)$.   However, we do not see the truth/a direct proof of the ``enhanced version of Lemma \ref{Fourier}".


Now we discuss the strategy to prove \Cref{nct}, informally.
The main difficulty in proving \eqref{entry4}  is from improper-intersections. Assuming  the ``enhanced version of Lemma \ref{Fourier}", an ideal approach is as follows.
We choose   $\phi$  such that  at some finite places $v$, $\phi_v$ is regular  with respect to  the decomposition  ${\mathbb {V}}_v=k_v^{-1}{\mathbb {W}}_v\oplus k^{-1} V^\sharp(E_v)$ for all $k\in U({\mathbb {W}})\backslash K_\Lambda/K$,  
in the sense that $\phi_v$ is supported outside $k_v^{-1}  V^\sharp(E_v)$. 
Then no 
self-intersection appears. 
After proving Theorem \ref{nct} in this setting,  we need  to remove the regularity condition on $\phi$.
We consider  different CM 1-cycles  by modifying ${\mathbb {W}}$ at some places  and use their differences which have degree 0 on the generic fiber. Then    the generating series of arithmetic intersection numbers  are modular by \Cref{fdimeadd}.
 This fact helps us   use  the ``enhanced version of Lemma \ref{Fourier}" to remove regularity, when replacing the CM 1-cycle by
 the differences of CM 1-cycles.   Then we can switch  the     CM 1-cycle without changing the regularity condition, equivalently,   change  the regularity condition  without switching   the     CM 1-cycle! This finally enables us to remove  the regularity condition.
    %Combining it with Proposition \ref{tech1}, we can get \eqref{entry4} for the desired test functions and CM 1-cycle. %, modulo $\overline{\mathbb {Q}}$-span of the $\log p$'s for $p$ runs over the residue characteristics of the  remove places.
Note that in this strategy, it is not necessary to use $\overline{\mathbb {Q}}$-valued Schwartz functions at finite places.

Without the ``enhanced version of Lemma \ref{Fourier}", 
we can not allow pullback of the CM cycle at places where we put regularity.  Thus we consider a $(\mathrm{mod} \overline{\mathbb {Q}}\log S)$-version of   Theorem \ref{nct} (see \cref{nctprop}), where $S$ will be a finite set where we put regularity condition.  This is why  it is  necessary to use $\overline{\mathbb {Q}}$-valued Schwartz functions at finite places.

We will use the following theorem. It is a  corollary of Baker's celebrated theorem on transcendence of logarithms of algebraic numbers
(see \cite[Theorem 1.1]{Waldsch}), and the fact that logarithms of prime numbers are ${\mathbb {Q}}$-linearly independent. 


# See Also

# Meta
## References
![[_reference_qiu_amsd]]


## Citations and Footnotes
[^1]: Citation, 86