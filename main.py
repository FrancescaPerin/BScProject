import basics
import folOperator as op
import functionality as F

import sequentCalc as sc

import basicInterpolant as bi

def main():
	"""
	p = basics.Atom("p")
	q = basics.Atom("q")

	phi = op.Impl(p,q)
	psi = op.Impl(p,q)


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
	"""

	b = basics.Atom("b")
	d = basics.Atom("d")

	phi = op.Mod(b ,"a")
	psi = op.Mod(b ,"a")


	entailment = sc.Entailment([phi],[], [psi], [])
	print(entailment.toString())
	val=entailment.solve()

	print(val)

	#if val:

		#interpolant= entailment.calcInterpolant()
		#print("final interpolant:"+ interpolant.toString())
		#print("check: ", entailment.checkInterpolant(phi, psi, interpolant))

	print("__________________________________")

	b = basics.Atom("b")
	d = basics.Atom("d")

	phi = op.Conj(op.Mod(b ,"a"), op.Mod(d ,"b"))
	psi = op.Mod(b ,"a")


	entailment = sc.Entailment([phi],[], [psi], [])
	print(entailment.toString())
	val=entailment.solve()

	print(val)

	#if val:

		#interpolant= entailment.calcInterpolant()
		#print("final interpolant:"+ interpolant.toString())
		#print("check: ", entailment.checkInterpolant(phi, psi, interpolant))



	"""

	entailment=F.randomGen(5, 3)

	psi=entailment[0]
	phi= entailment[1]

	bi.computeInterpolant(phi, psi)
	entailment = sc.Entailment([phi],[], [psi], [])

	entailment = sc.Entailment([phi],[], [psi], [])
	print(entailment.toString())
	val=entailment.solve()

	print(val)
	print

	if val:

		interpolant= entailment.calcInterpolant()
		print("final interpolant:"+ interpolant.toString())
		print("check: ", entailment.checkInterpolant(phi, psi, interpolant))
		entailment.latexProofAux()


	"""


if __name__ == '__main__':
	main()