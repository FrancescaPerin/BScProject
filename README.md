# Theorem Prover of interpolation for propositional logic, modal logic and PDL.

This project consists in a theorem prover which aims to show that Craig' interpolation property holds for propositional logic, modal logic and PDL. The program given a logic sentence first determines it's validity, and if valid computes one of the possible interpolants and checks if it respects the general definition of interpolant.


## Python

This project was built on **python 3.7.3**. In order to run the following packages are needed:

* pdfTeX **Version 3.14159265-2.6-1.40.16 (TeX Live 2015)**

## Running the project

To run the code alway run the script 'main.py'. The user can then decide to test a desired formula or to run an experiment with randomly generated formulas (choosing the desired logic and number of formulas to test).

### Testing specific formula

#### How to input a formula

If the user decides to input a formula, this should be given in a very specific format, if the format is not followed it could lead to wrong results as the code is very sensitive in particular when using the modality operator.

The formula is given similarly to prefix notation. The operators used are the following:

* Negation(~a): op.Not(a)
* Modality([]a): op.Mod(a)
* Modality([b]a): op.Mod(a, "b")

* Conjunction(a^b): op.Conj(a,b)
* Disjunction(a|b): op.Disj(a,b)
* Implication (a->b): op.Impl(a,b)

Here are some easy and some more complicated examples to understad the fomat required:

* (p ^ q ^ r): op.Conj(op.Conj(p,q),r) - op.Conj(p,op.Conj(q,r))
* (p ^ q ^ r ^ s): op.Conj(op.Conj(p,q),op.Conj(r,s)) or op.Conj(op.Conj(op.Conj(p,q),r),s)
* ((p | q)->p): op.Impl(op.Disj(p,q),p)
* ([a][b]p ->[a U b]p): op.Impl(op.Mod(op.Mod(p,"b"),"a"), op.Mod(p, "(a U b)"))



