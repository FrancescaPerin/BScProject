import basics
import folOperator as op

import sequentCalc as sc

import basicInterpolant as bi

def main():
	
	a = basics.Atom("a")
	b = basics.Atom("b")
	c = basics.Atom("c")

	phi = op.Conj(a,op.Conj(b,c)) 
	psi = op.Conj(op.Disj(a,c),op.Disj(b,c))

	bi.computeInterpolant(phi, psi)

	entailment = sc.Entailment([phi],[], [psi], [])
	print(entailment.toString())
	print(entailment.solve())


	entailment.calcInterpolant()

	print("__________________________________")

	a = basics.Atom("a")
	b = basics.Atom("b")
	c = basics.Atom("c")
	d = basics.Atom("d")

	phi = op.Conj(op.Disj(b,op.Not(b)),op.Conj(a,d)) 
	psi = op.Disj(a,op.Conj(b,c))

	bi.computeInterpolant(phi, psi)

	entailment = sc.Entailment([phi],[], [psi], [])
	print(entailment.toString())
	print(entailment.solve())


	entailment.calcInterpolant()


	print("__________________________________")

	t = basics.Atom("t")
	s = basics.Atom("s")
	u = basics.Atom("u")
	v = basics.Atom("v")

	phi = op.Disj(u, op.Conj(v,s))
	psi = op.Impl(op.Not(u), op.Disj(t,s))

	bi.computeInterpolant(phi, psi)

	entailment = sc.Entailment([phi],[], [psi],[])

	print(entailment.toString())
	print(entailment.solve())


	print("__________________________________")

	p = basics.Atom("p")
	q = basics.Atom("q")
	r = basics.Atom("r")

	phi = op.Disj(op.Impl(p,r),op.Impl(q,r))
	psi = op.Impl(op.Conj(p,q), r)

	bi.computeInterpolant(phi, psi)

	entailment = sc.Entailment([phi],[], [psi],[])
	print(entailment.toString())
	print(entailment.solve())
	

	print("__________________________________")

	p = basics.Atom("p")
	q = basics.Atom("q")
	r = basics.Atom("r")
	s = basics.Atom("s")

	phi = op.Conj(p,q)
	psi = op.Impl(op.Not(s),op.Conj(p,op.Impl(r,q)))

	bi.computeInterpolant(phi, psi)

	entailment = sc.Entailment([phi],[], [psi],[])
	print(entailment.toString())
	print(entailment.solve())


	print("__________________________________")

	d = basics.Atom("d")
	e = basics.Atom("e")
	f = basics.Atom("f")
	g = basics.Atom("g")
	h = basics.Atom("h")

	phi = op.Conj(d,op.Impl(e,f))
	psi = op.Disj(op.Not(g),h)

	bi.computeInterpolant(phi, psi)

	entailment = sc.Entailment([phi],[], [psi],[])
	print(entailment.toString())
	print(entailment.solve())
	


if __name__ == '__main__':
	main()