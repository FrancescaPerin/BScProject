# Theorem Prover of interpolation for propositional logic, modal logic and PDL.

This project consists in a theorem prover which aims to show that Craig' interpolation property holds for propositional logic, modal logic and PDL. The program given a logic sentence first determines it's validity, and if valid computes one of the possible interpolants and checks if it respects the general definition of interpolant.


## Python

This project was built on **python 3.7.3**. In order to run the following packages are needed:

* pdfTeX **Version 3.14159265-2.6-1.40.16 (TeX Live 2015)**

## Running the project

To run the code alway run the script 'main.py'. The user can then decide to test a desired formula or to run an experiment with randomly generated formulas (choosing the desired logic and number of formulas to test).

### Testing specific formula

If the user decides to input a formula, this should be given in a very specific format, if the format is not followed it could lead to wrong results as the code is very sensitive in particular when using the modality operator.

The formula is given in prefix notation. The operators used are the following:

* Negation(~): op.Not()
* Modality([]): op.Mod()

* Conjunction(^): op.Conj()
* Disjunction(|): op.Disj()
* Implication (->): op.Impl()


