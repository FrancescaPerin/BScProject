import basics
import folOperator as op
import functionality as F

import sequentCalc as sc

import basicInterpolant as bi

def main():




	i = basics.Atom("i")

	phi = op.Impl(i,i)
	psi = op.Mod(op.Impl(i,i),"((b U b) U (i ; (p ; b)))")

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


	f = basics.Atom("False")
	s = basics.Atom("s")
	f.setValue(False)


	phi = op.Mod(f,"a")
	psi = s


	entailment = sc.Entailment([phi],[], [psi], [])
	print(entailment.toString())
	val=entailment.solve()

	print(val)

	if val:

		interpolant= entailment.calcInterpolant()
		print("final interpolant:"+ interpolant.toString())
		print("check: ", entailment.checkInterpolant(phi, psi, interpolant))

		entailment.latexProofAux()



	p = basics.Atom("p")
	q = basics.Atom("q")
	r = basics.Atom("r")
	f = basics.Atom("False")
	f.setValue(False)

	phi = op.Mod(op.Not(op.Disj(p,q)), "a " )
	psi = op.Impl(op.Mod(f, "c"), op.Mod(op.Disj(q,r),"b "))


	entailment = sc.Entailment([phi],[], [psi], [])
	print(entailment.toString())
	val=entailment.solve()

	print(val)

	if val:

		interpolant= entailment.calcInterpolant()
		print("final interpolant:"+ interpolant.toString())
		print("check: ", entailment.checkInterpolant(phi, psi, interpolant))

		entailment.latexProofAux()


	print("_________________________________________________________")



	i=0
	validFormulas=0
	correctInterpolant=0
	countE1=0
	countE2=0
	while i< 10000:
		entailment=F.randomGen(5, 3, 3, 3)

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