import basics
import folOperator as op
import functionality as F

import sequentCalc as sc

import basicInterpolant as bi

def main():

	"""	p = basics.Atom("p")
	q = basics.Atom("q")
	r = basics.Atom("r")

	phi = op.Conj(op.Not(op.Disj(p,q)), r)
	psi = op.Conj(op.Not(p), r)

	bi.computeInterpolant(phi, psi)

	entailment = sc.Entailment([phi],[], [psi], [])
	print(entailment.toString())
	print(entailment.solve())

	interpolant= entailment.calcInterpolant()

	print("final interpolant:"+ interpolant.toString())

	print("check: ", entailment.checkInterpolant(phi, psi, interpolant))


	print("__________________________________")
	
	
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
	
	print("__________________________________")
	"""

	f=basics.Atom("f")
	t=basics.Atom("t")

	phi = op.Disj(f,t)
	psi = op.Not(op.Not(op.Impl(t, t)))

	bi.computeInterpolant(phi, psi)

	entailment = sc.Entailment([phi],[], [psi], [])
	print(entailment.toString())
	print(entailment.solve())

	interpolant= entailment.calcInterpolant()

	print("final interpolant:"+ interpolant.toString())

	print("check: ", entailment.checkInterpolant(phi, psi, interpolant))
	"""

	print("__________________________________")
	
	p = basics.Atom("p")
	q = basics.Atom("q")

	phi = op.Conj(op.Not(p),q)
	psi = q

	bi.computeInterpolant(phi, psi)

	entailment = sc.Entailment([phi],[], [psi], [])
	print(entailment.toString())
	print(entailment.solve())


	interpolant= entailment.calcInterpolant()


	print("final interpolant:"+ interpolant.toString())
	entailment.checkInterpolant(interpolant)

	print("__________________________________")

	a = basics.Atom("a")
	b = basics.Atom("b")
	c = basics.Atom("c")

	phi = op.Conj(op.Not(a),op.Conj(b,c)) 
	psi = op.Conj(op.Disj(a,b),op.Disj(b,c))

	bi.computeInterpolant(phi, psi)

	entailment = sc.Entailment([phi],[], [psi], [])
	print(entailment.toString())
	print(entailment.solve())

	interpolant= entailment.calcInterpolant()


	print("final interpolant:"+ interpolant.toString())
	entailment.checkInterpolant(interpolant)

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
	
	interpolant= entailment.calcInterpolant()


	print("final interpolant:"+ interpolant.toString())
	entailment.checkInterpolant(interpolant)

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
	
	interpolant= entailment.calcInterpolant()


	print("final interpolant:"+ interpolant.toString())
	entailment.checkInterpolant(interpolant)

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
	
	interpolant= entailment.calcInterpolant()


	print("final interpolant:"+ interpolant.toString())
	entailment.checkInterpolant(interpolant)
	
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
	
	interpolant= entailment.calcInterpolant()
	print("final interpolant:"+ interpolant.toString())
	entailment.checkInterpolant(interpolant)

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
	val=entailment.solve()
	
	print(val)

	if val:

		interpolant= entailment.calcInterpolant()
		print("final interpolant:"+ interpolant.toString())
		entailment.checkInterpolant(interpolant)
	"""


if __name__ == '__main__':
	main()