import basics
import folOperator as op

import basicInterpolant as bi

def main():

	a = basics.Atom("a")
	b = basics.Atom("b")
	c = basics.Atom("c")
	d = basics.Atom("d")

	phi = op.Conj(op.Disj(b,op.Not(b)),op.Conj(a,d)) 
	psi = op.Disj(a,op.Conj(b,c))

	bi.computeInterpolant(phi, psi)

	print("__________________________________")

	t = basics.Atom("t")
	s = basics.Atom("s")
	q = basics.Atom("q")
	r = basics.Atom("r")

	phi = op.Disj(q, op.Conj(r,s))
	psi = op.Impl(op.Not(q), op.Disj(t,s))

	bi.computeInterpolant(phi, psi)

	print("__________________________________")

	p = basics.Atom("p")
	q = basics.Atom("q")
	r = basics.Atom("r")

	phi = op.Disj(op.Impl(p,r),op.Impl(q,r))
	psi = op.Impl(op.Conj(p,q), r)

	bi.computeInterpolant(phi, psi)


if __name__ == '__main__':
	main()