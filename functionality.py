
def atomsIsSubset(phi, psi):
	for atomPhi in phi.getAtoms():
		if atomPhi.getValue() == None and not psi.hasAtom(atomPhi):
			return False
	return True