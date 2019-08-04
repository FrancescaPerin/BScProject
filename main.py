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


	phi = op.Conj(op.Conj(p,q),r)
	psi = op.Disj(op.Disj(r,s),t)


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


    #[a U b]~(p v q) -> ([c]False -> [b U c](q v r))
    #~(x) ;  |- ([(j ; p)](b) -> [(u U u)](s)) ;
    #[(z U ((z U d) U y))](k) ;  |- ([(d U z)](a) -> [z](y)) ;
    #(w ^ k) ;  |- [((p ; (n U n)) ; w)]((p -> p)) ;
    #(k | k) ;  |- [((s ; (s ; k)) U w)]((i -> i)) ;
    ##~(q) ;  |- ((q -> t) | ~(t)) ;
    #(i -> i) ;  |- [((b U b) U (i ; (p ; b)))]((i -> i)) ;

    #(i -> i) ;  |- (([(b U b) ](False) ^ [ (i ; (p ; b))](False)) -> ([(b U b) ](True) ^ [ (i ; (p ; b))](True))) ;

    """

	i = basics.Atom("i")
	f = basics.Atom("False")
	f.setValue(False)

	t = basics.Atom("True")
	t.setValue(True)

	phi = op.Impl(i,i)
	psi = op.Impl(op.Conj(op.Mod(f,"(b U b)"),op.Mod(f, "(i ; (p ; b))")), op.Conj(op.Mod(t,"(b U b"),op.Mod(t, "(i ; (p ; b))")))


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
	while i< 100:
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