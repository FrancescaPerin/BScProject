import folOperator as op
import functionality as F
import copy

def interpolateAux(phi, psi):

	if(F.atomsIsSubset(phi, psi)):
		return phi

	# get p
	for atomPhi in phi.getAtoms():
		if atomPhi.getValue() == None and not psi.hasAtom(atomPhi):
			p = atomPhi
			break
		
	phiTrue = copy.deepcopy(phi).setAtomBySymbol(p.getSymbol(), True)
	phiFalse = copy.deepcopy(phi).setAtomBySymbol(p.getSymbol(), False)

	return interpolateAux(op.Disj(phiTrue, phiFalse), psi)

def interpolate(phi, psi):

	if not op.Impl(phi, psi).isTaut():
		print("Not Valid!")
		return None

	return interpolateAux(copy.copy(phi), psi)

def computeInterpolant(phi, psi):
	print("phi: " + phi.toString())
	print("psi: " + psi.toString())

	interpolated = interpolate(phi, psi)
	print("interpolant: " + interpolated.toString())
	print("simplified interpolant: " + interpolated.simplify().toString())

	return interpolated
