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

		if isinstance(self.__symbol,bool):
			return str(self.__symbol)

		return self.__symbol

	def getValue(self):
		pass

	def getAtoms(self):
		pass

	def isTaut(self):
		pass

	# check if a sentence as a particular atom or not
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

	def isTaut(self):

		with tempEval(self):
			for world in self.getWorlds():
				for atom in world:
					self.setAtomBySymbol(atom.getSymbol(), atom.getValue())

				if(not self.getValue()):
					return False

		return True

	def simplify(self):
		return self

	def toString(self):
		pass

class Atom(Element):

	def __init__(self, symbol):
		super(Atom, self).__init__(symbol)
		self.__value = None

	def getValue(self):
		return self.__value

	def getOperand(self):
		return self

	def setValue(self, newVal):
		self.__value = newVal
		return self

	def getAtoms(self):
		return [self]

	def isTaut(self):
		return False

	def toString(self):
		if self.getValue() == None:	
			return self.getSymbol()
		else:
			return str(self.getValue())
