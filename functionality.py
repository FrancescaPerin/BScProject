import folOperator as op
import basics

import random
import string
import itertools

import sys

binOp = [op.Conj, op.Disj, op.Impl]
unOp = [op.Not, op.Mod]
opProg = ["U", ";"]

def getAllCombs(l):
    comb = []
    for i in range(len(l),0,-1):
        comb.extend(list(itertools.combinations(l,i)))

    return comb


def atomsIsSubset(phi, psi):

    for atomPhi in phi.getAtoms():
        if atomPhi.getValue() is None and not psi.hasAtom(atomPhi):
            return False
    return True

def genProgram(atoms, maxDepth):

    if maxDepth < 1:
        return random.choice(atoms)

    sample = random.choice(atoms + opProg)

    if sample not in atoms:

        operand1 = genProgram(atoms, maxDepth - 1)
        operand2 = genProgram(atoms, maxDepth - 1)

        return "(" + operand1 + " " + sample + " " + operand2 + ")"

    return sample


def randomGen(maxLen, nAtoms, maxLenProg, nAtomsProg):

    atoms = []
    prevSymbols = []

    for i in range(nAtoms):

        letter = None

        while not letter or letter in prevSymbols:
            letter = random.choice(
                string.ascii_letters[0:int((len(string.ascii_letters) / 2))])

        atoms.append(basics.Atom(letter))
        prevSymbols.append(letter)

    atomsProg = []

    for i in range(nAtomsProg):

        letter = None

        while not letter or letter in atomsProg:
            letter = random.choice(
                string.ascii_letters[0:int((len(string.ascii_letters) / 2))])

        atomsProg.append(letter)

    phi = randomGenAux(maxLen, atoms, maxLenProg, atomsProg)
    psi = randomGenAux(int(maxLen / 2), atoms, maxLenProg, atomsProg)

    return (phi, psi)


def randomGenAux(maxLen, atoms, maxLenProg, atomsProg):

    if maxLen > 1:

        operator = random.choice(binOp + unOp)

        if operator in binOp:

            operand1 = randomGenAux(
                int(maxLen / 2), atoms, maxLenProg, atomsProg)
            operand2 = randomGenAux(
                int(maxLen / 2), atoms, maxLenProg, atomsProg)

            return operator(operand1, operand2)

        # elif isinstance(op, op.Mod):

        else:
            operand = randomGenAux(maxLen - 2, atoms, maxLenProg, atomsProg)
            return operator(operand) if operator != op.Mod else operator(
                operand, genProgram(atomsProg, maxLenProg))

    else:

        return random.choice(atoms)


if __name__ == '__main__':
    s = randomGen(int(sys.argv[1]), int(sys.argv[2]),
                  int(sys.argv[3]), int(sys.argv[4]))
