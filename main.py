import basics
import folOperator as op
import functionality as F

import sequentCalc as sc

import basicInterpolant as bi

def main():
	"""

	r = basics.Atom("r")
	p = basics.Atom("p")
	m = basics.Atom("m")


	phi = op.Impl(r,p)
	psi = op.Disj(op.Impl(p,m),op.Impl(m,p))


	entailment = sc.Entailment([phi],[], [psi], [])
	print(entailment.toString())
	print(entailment.solve())

	interpolant= entailment.calcInterpolant()

	print("final interpolant:"+ interpolant.toString())
	entailment.latexProofAux()

	print("check: ", entailment.checkInterpolant(phi, psi, interpolant))


	k = basics.Atom("k")
	a = basics.Atom("a")
	s = basics.Atom("s")


	phi = op.Not(s)
	psi = op.Impl(op.Conj(k,a),op.Conj(k,a))


	entailment = sc.Entailment([phi],[], [psi], [])
	print(entailment.toString())
	print(entailment.solve())

	interpolant= entailment.calcInterpolant()

	print("final interpolant:"+ interpolant.toString())

	print("check: ", entailment.checkInterpolant(phi, psi, interpolant))

	#entailment.latexProofAux()



	u = basics.Atom("u")
	t = basics.Atom("t")
	v = basics.Atom("v")
	s = basics.Atom("s")


	phi = op.Conj(op.Disj(u,op.Conj(v,s)),u)
	psi = op.Disj(op.Disj(v,s),u)


	entailment = sc.Entailment([phi],[], [psi], [])
	print(entailment.toString())
	print(entailment.solve())

	interpolant= entailment.calcInterpolant()

	print("final interpolant:"+ interpolant.toString())

	print("check: ", entailment.checkInterpolant(phi, psi, interpolant))

	#entailment.latexProofAux()


	print("__________________________________")

	p = basics.Atom("p")
	q = basics.Atom("q")
	r = basics.Atom("r")

	phi = op.Mod(op.Conj(op.Mod(p),op.Mod(q)))
	psi = op.Mod(op.Mod(op.Disj(p,r)))


	entailment = sc.Entailment([phi],[], [psi], [])
	print(entailment.toString())
	print(entailment.solve())

	interpolant= entailment.calcInterpolant()

	print("final interpolant:"+ interpolant.toString())

	print("check: ", entailment.checkInterpolant(phi, psi, interpolant))

	print("__________________________________")


	p = basics.Atom("p")
	q = basics.Atom("q")
	r = basics.Atom("r")

	phi = op.Conj(op.Mod(op.Mod(p)), op.Mod(op.Mod(q)))
	psi = op.Mod(op.Conj(op.Mod(q),op.Mod(p)))


	entailment = sc.Entailment([phi],[], [psi], [])
	print(entailment.toString())
	print(entailment.solve())

	interpolant= entailment.calcInterpolant()

	print("final interpolant:"+ interpolant.toString())

	print("check: ", entailment.checkInterpolant(phi, psi, interpolant))

	#entailment.latexProofAux()


	print("__________________________________")


	b = basics.Atom("b")
	d = basics.Atom("d")

	phi = op.Mod(b ,"aUb")
	psi = op.Mod(b ,"b")

	entailment = sc.Entailment([phi],[], [psi], [])
	print(entailment.toString())
	val=entailment.solve()

	print(val)

	if val:

		interpolant= entailment.calcInterpolant()
		print("final interpolant:"+ interpolant.toString())
		print("check: ", entailment.checkInterpolant(phi, psi, interpolant))

		entailment.latexProofAux()


	print("__________________________________")

	p = basics.Atom("p")
	q = basics.Atom("q")
	r = basics.Atom("r")

	phi = op.Conj(op.Mod(op.Mod(p)), op.Mod(op.Mod(q)))
	psi = op.Mod(op.Disj(op.Mod(q),op.Mod(r)))


	entailment = sc.Entailment([phi],[], [psi], [])
	print(entailment.toString())
	val=entailment.solve()

	print(val)

	if val:

		interpolant= entailment.calcInterpolant()
		print("final interpolant:"+ interpolant.toString())
		print("check: ", entailment.checkInterpolant(phi, psi, interpolant))

	entailment.latexProofAux()

	print("__________________________________")

	"""
	i=0
	validFormulas=0
	correctInterpolant=0
	countE1=0
	countE2=0
	while i< 100:
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
		print ("count entailment 1 valid: "+ str(countE2))
		print("_________________________________________________________________________________________")



if __name__ == '__main__':
	main()