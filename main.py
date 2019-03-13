import basics
import folOperator as op

import sequentCalc as sc

import basicInterpolant as bi

def main():

	a = basics.Atom("a")
	b = basics.Atom("b")
	c = basics.Atom("c")
	d = basics.Atom("d")

	phi = op.Conj(op.Disj(b,op.Not(b)),op.Conj(a,d)) 
	psi = op.Disj(a,op.Conj(b,c))

	bi.computeInterpolant(phi, psi)

	entailment = sc.Entailment([phi], [psi])
	print(entailment.toString())
	print(entailment.solve())

	print("__________________________________")

	t = basics.Atom("t")
	s = basics.Atom("s")
	u = basics.Atom("u")
	v = basics.Atom("v")

	phi = op.Disj(u, op.Conj(v,s))
	psi = op.Impl(op.Not(u), op.Disj(t,s))

	bi.computeInterpolant(phi, psi)

	print("__________________________________")

	p = basics.Atom("p")
	q = basics.Atom("q")
	r = basics.Atom("r")

	phi = op.Disj(op.Impl(p,r),op.Impl(q,r))
	psi = op.Impl(op.Conj(p,q), r)

	bi.computeInterpolant(phi, psi)


	print("__________________________________")

	entailment = sc.Entailment([phi], [psi])
	print(entailment.toString())
	print(entailment.solve())


if __name__ == '__main__':
	main()