import sys
import basics
import folOperator as op
import functionality as F

import sequentCalc as sc

import basicInterpolant as bi


def main(argv):

    # loading all atoms name for user use
    a = basics.Atom("a")
    b = basics.Atom("b")
    c = basics.Atom("c")
    d = basics.Atom("d")
    e = basics.Atom("e")
    f = basics.Atom("f")
    g = basics.Atom("g")
    h = basics.Atom("h")
    i = basics.Atom("i")
    l = basics.Atom("l")
    m = basics.Atom("m")
    n = basics.Atom("n")
    o = basics.Atom("o")
    p = basics.Atom("p")
    q = basics.Atom("q")
    r = basics.Atom("r")
    s = basics.Atom("s")
    t = basics.Atom("t")
    u = basics.Atom("u")
    v = basics.Atom("v")
    z = basics.Atom("z")
    w = basics.Atom("w")
    k = basics.Atom("k")
    j = basics.Atom("j")
    y = basics.Atom("y")
    x = basics.Atom("x")

    # setting default name for false and true and setting boolean value

    false = basics.Atom("False")
    false.setValue(False)

    true = basics.Atom("True")
    true.setValue(True)

    # if user decide to test a formula then take phi and psi from command line

    if len(argv) < 2:
        raise Exception("Missing arguments")
        exit(-1)

    if argv[1] == "--manual":

        if len(argv) == 4:
            phiString = argv[2]
            psiString = argv[3]
        elif len(argv) == 2:
            phiString = input("Insert phi: ")
            psiString = input("Insert psi: ")
        else:
            raise Exception(
                "Wrong argument format, phi or psi not inserted or extra arguments")
            exit(-1)

        phi = eval(phiString)
        psi = eval(psiString)

        print("phi: ", phi.toString())
        print("psi: ", psi.toString())

        entailment = sc.Entailment([phi], [], [psi], [])
        print("Entailment: ", entailment.toString())

        val = entailment.solve()
        print("Value entailment: ", val)

        if val:

            interpolant = entailment.calcInterpolant()
            print("final interpolant:", interpolant.toString())
            print(
                "check: ",
                entailment.checkInterpolant(
                    phi,
                    psi,
                    interpolant))

            entailment.latexProofAux()

    elif argv[1] == "--random":

        i = 0
        validFormulas = 0
        correctInterpolant = 0
        countE1 = 0
        countE2 = 0

        count = int(argv[3])

        while i < count:

            if argv[2] == "--prop":

                entailment = F.randomGen(5, 3, False)

            elif argv[2] == "--modal":

                entailment = F.randomGen(5, 3, True)

            elif argv[2] == "--PDL":

                entailment = F.randomGenPDL(5, 3, 3, 3)

            else:
                raise Exception(
                    "Wrong argument format, logic to be used not specified")
                exit(-1)

            psi = entailment[0]
            phi = entailment[1]

            entailment = sc.Entailment([phi], [], [psi], [])
            print(entailment.toString())
            val = entailment.solve()

            print(val)

            i += 1

            if val:
                validFormulas += 1

                interpolant = entailment.calcInterpolant()
                print("final interpolant:" + interpolant.toString())

                entailment1 = sc.Entailment([phi], [], [interpolant], [])
                entailment2 = sc.Entailment([interpolant], [], [psi], [])

                if entailment1.solve():
                    countE1 += 1
                if entailment2.solve():
                    countE2 += 1

                check = entailment.checkInterpolant(phi, psi, interpolant)

                if check:

                    print("check: ", check)

                    correctInterpolant += 1
                else:
                    entailment.latexProofAux()
                    break

            print("Number of tested formulas:" + str(i))
            print("Number of valid formulas:" + str(validFormulas))
            print(
                "Number of valid formulas for which interpolant is correct and checked:" +
                str(correctInterpolant))
            print(
                "_________________________________________________________________________________________")


if __name__ == '__main__':
    main(sys.argv)
