import basics
import folOperator as op
import functionality as F

import sequentCalc as sc

import basicInterpolant as bi

def main():



	p = basics.Atom("p")
	q = basics.Atom("q")
	t = basics.Atom("t")
	r = basics.Atom("r")
	s = basics.Atom("s")


	phi = op.Disj(op.Disj(p,q),r)
	psi = op.Conj(op.Conj(r,s),t)


	entailment = sc.Entailment([phi],[], [psi], [])
	print(entailment.toString())
	val=entailment.solve()

	print(val)

	if val:

		interpolant= entailment.calcInterpolant()
		print("final interpolant:"+ interpolant.toString())
		print("check: ", entailment.checkInterpolant(phi, psi, interpolant))

		entailment.latexProofAux()

	"""
	False -> True
	False -> p
	p -> True
    True -> p v ~p
    True -> ~(p ^ ~p)
    p -> p
    (p ^ q) -> (q v r)
    (p ^ q ^ r) -> (q v r v s)
    (p ^ q ^ r) -> (r v s v t)
    (p -> q) -> (~q -> ~p)
    ((p v t) -> (q v r)) -> ((~r ^ s) -> (~q -> ~p))

	not provable:

    p -> q
    q -> ~q
    q v (r ^ s)
    (p v q v r) -> (r ^ s ^ t)
    ((p v t) -> (q v r)) -> (~r -> (~q -> ~p))




	print("__________________________________")


	i=0
	validFormulas=0
	correctInterpolant=0
	countE1=0
	countE2=0
	while i< 150000:
		entailment=F.randomGen(5, 3)

		psi=entailment[0]
		phi= entailment[1]

		entailment = sc.Entailment([phi],[], [psi], [])
		print(entailment.toString())
		val=entailment.solve()

		print(val)

		i+=1

		if val:
			validFormulas+=1

			interpolant= entailment.calcInterpolant()
			print("final interpolant:"+ interpolant.toString())

			#if interpolant.simplify():
				#interpolant=interpolant.simplify()

			entailment1=sc.Entailment([phi],[], [interpolant], [])
			entailment2=sc.Entailment([interpolant],[], [psi], [])

			if entailment1.solve():
				countE1+=1
			if entailment2.solve():
				countE2+=1

			check=entailment.checkInterpolant(phi, psi, interpolant)

			if check:

				print("check: ", check)

				correctInterpolant+=1
			else:
				entailment.latexProofAux()
				break




		print ("Number of tested formulas:"+ str(i))
		print ("Number of valid formulas:"+ str(validFormulas))
		print ("Number of valid formulas for which interpolant is correct and checked:"+ str(correctInterpolant))
		print ("count entailment 1 valid: "+ str(countE1))
		print ("count entailment 2 valid: "+ str(countE2))
		print("_________________________________________________________________________________________")
		"""


if __name__ == '__main__':
	main()