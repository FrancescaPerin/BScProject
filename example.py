import copy

class tempEval:

	def __init__(self, element):
		self.__element = element
		self.__vals = []

	def __enter__(self):
		atoms = self.__element.getAtoms()
		for i in range(len(atoms)):
			self.__vals.append(atoms[i].getValue())

	def __exit__(self, type, value, tb):
		atoms = self.__element.getAtoms()
		for i in range(len(atoms)):
			atoms[i].setValue(self.__vals[i]) 

class Element:

	def __init__(self, symbol):
		self.__symbol = symbol

	def getSymbol(self):
		return self.__symbol

	def getValue(self):
		pass

	def getAtoms(self):
		pass

	def isValid(self):
		pass

	def hasAtom(self, atom):
		for selfAtom in self.getAtoms():
			if selfAtom.getSymbol() == atom.getSymbol():
				return True

		return False

	def setAtomBySymbol(self, symbol, value):
		for atom in self.getAtoms():
			if atom.getSymbol() == symbol and atom.getValue() == None:
				atom.setValue(value)

		return self

	def getWorlds(self):
		atoms = self.getAtoms()

		worlds = [[copy.deepcopy(atoms[0]).setValue(True)], [copy.deepcopy(atoms[0]).setValue(False)]]
		atoms = atoms[1:len(atoms)]

		for atom in atoms:
			tempWorlds = copy.copy(worlds)
			for world in tempWorlds:
				worlds.remove(world)
				worlds.append(world + [copy.deepcopy(atom).setValue(True)])
				worlds.append(world + [copy.deepcopy(atom).setValue(False)])

		return worlds

	def isValid(self):

		with tempEval(self):
			for world in self.getWorlds():
				for atom in world:
					self.setAtomBySymbol(atom.getSymbol(), atom.getValue())

				if(not self.getValue()):
					return False

		return True

	def toString(self):
		pass

class Atom(Element):

	def __init__(self, symbol):
		super(Atom, self).__init__(symbol)
		self.__value = None

	def getValue(self):
		return self.__value

	def setValue(self, newVal):
		self.__value = newVal
		return self

	def getAtoms(self):
		return [self]

	def isValid(self):
		return True

	def toString(self):
		if self.getValue() == None:	
			return self.getSymbol()
		else:
			return str(self.getValue())

class UnaryOperator(Element):

	def __init__(self, symbol, func, operand):
		super(UnaryOperator, self).__init__(symbol)

		self.__operand = operand
		self.__func = func

	def getValue(self):
		return self.__func(self.__operand.getValue())

	def getAtoms(self):
		return self.__operand.getAtoms()

	def toString(self):
		return self.getSymbol() + "(" + self.__operand.toString() + ")"

class Operator(Element):

	def __init__(self, symbol, func, operand1, operand2):
		super(Operator, self).__init__(symbol)

		self.__operand1 = operand1
		self.__operand2 = operand2

		self.__func = func

	def getValue(self):
		return self.__func(self.__operand1.getValue(), self.__operand2.getValue())

	def getAtoms(self):

		atoms = []

		atoms += self.__operand1.getAtoms()
		atoms += self.__operand2.getAtoms()

		return atoms

	def toString(self):
		return "(" + self.__operand1.toString() + " " + self.getSymbol() + " " + self.__operand2.toString() + ")"


class Conj(Operator):

	def __init__(self, operand1, operand2):
		super(Conj, self).__init__("^", lambda a,b : a and b, operand1, operand2)

class Disj(Operator):

	def __init__(self, operand1, operand2):
		super(Disj, self).__init__("v", lambda a,b : a or b, operand1, operand2)

class Impl(Operator):

	def __init__(self, operand1, operand2):
		super(Impl, self).__init__("->", lambda a,b : not a or b, operand1, operand2)

class Not(UnaryOperator):

	def __init__(self, operand):
		super(Not, self).__init__("~", lambda a : not a, operand)

def atomsIsSubset(phi, psi):
	for atomPhi in phi.getAtoms():
		if atomPhi.getValue() == None and not psi.hasAtom(atomPhi):
			return False
	return True

def interpolateAux(phi, psi):

	if(atomsIsSubset(phi, psi)):
		return phi

	# get p
	for atomPhi in phi.getAtoms():
		if atomPhi.getValue() == None and not psi.hasAtom(atomPhi):
			p = atomPhi
			break
		
	phiTrue = copy.deepcopy(phi).setAtomBySymbol(p.getSymbol(), True)
	phiFalse = copy.deepcopy(phi).setAtomBySymbol(p.getSymbol(), False)

	return interpolateAux(Disj(phiTrue, phiFalse), psi)

def interpolate(phi, psi):

	if not Impl(phi, psi).isValid():
		print("Not Valid!")
		return None

	return interpolateAux(copy.copy(phi), psi)


def main():

	t = Atom("t")
	s = Atom("s")
	q = Atom("q")
	r = Atom("r")

	phi = Disj(q, Conj(r,s))
	psi = Impl(Not(q), Disj(t,s))

	print(phi.toString())
	print(psi.toString())

	print(interpolate(phi, psi).toString())

if __name__ == '__main__':
	main()
