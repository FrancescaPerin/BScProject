import folOperator as op
import basics

import random
import string

import sys

binOp = [op.Conj, op.Disj, op.Impl]
unOp = [op.Not]

def atomsIsSubset(phi, psi):

	for atomPhi in phi.getAtoms():
		if atomPhi.getValue() == None and not psi.hasAtom(atomPhi):
			return False
	return True


def randomGen(maxLen, nAtoms):

	atoms = []
	prevSymbols = []

	for i in range(nAtoms):

		letter = None

		while not letter or letter in prevSymbols:
			letter = random.choice(string.ascii_letters[0:int((len(string.ascii_letters)/2))])

		atoms.append(basics.Atom(letter))
		prevSymbols.append(letter)

	phi = randomGenAux(maxLen, atoms)
	psi = randomGenAux(int(maxLen/2), atoms)

	return (phi, psi)

def randomGenAux(maxLen, atoms):

	if maxLen > 1:

		op = random.choice(binOp + unOp)

		if op in binOp:

			operand1 = randomGenAux(int(maxLen/2), atoms)
			operand2 = randomGenAux(int(maxLen/2), atoms)

			return op(operand1, operand2)

		else:

			operand = randomGenAux(maxLen-1, atoms)
			return op(operand)

	else:

		return random.choice(atoms)


if __name__ == '__main__':
	s = randomGen(int(sys.argv[1]), int(sys.argv[2]))
