import basics 

#Class for unary operators (for now only not)
class UnaryOperator(basics.Element):

	def __init__(self, symbol, func, operand):
		super(UnaryOperator, self).__init__(symbol)

		self.__operand = operand
		self.__func = func

	def getOperand(self):
		return self.__operand

	def setOperand(self, operand):
		self.__operand = operand
		return self

	def getValue(self):
		return self.__func(self.__operand.getValue())

	def getAtoms(self):
		return self.__operand.getAtoms()

	def toString(self):
		return self.getSymbol() + "(" + self.__operand.toString() + ")"

	def simplify(self):
		selfVal = self.getValue()
		if selfVal != None:
			return Atom(selfVal)

		self.setOperand(self.getOperand().simplify())
		return self

#Class for binary operators (conjunction, disjunction, implication)
class Operator(basics.Element):

	def __init__(self, symbol, func, operand1, operand2):
		super(Operator, self).__init__(symbol)

		self.__operand1 = operand1
		self.__operand2 = operand2

		self.__func = func

	def getOperandLeft(self):
		return self.__operand1

	def setOperandLeft(self, operand):
		self.__operand1 = operand
		return self

	def getOperandRight(self):
		return self.__operand2

	def setOperandRight(self, operand):
		self.__operand2 = operand
		return self

	def getValue(self):
		return self.__func(self.__operand1.getValue(), self.__operand2.getValue())

	def getAtoms(self):

		atoms = []

		atoms += self.__operand1.getAtoms()
		atoms += self.__operand2.getAtoms()

		return atoms

	def simplify(self):

		selfValue = self.getValue()

		if selfValue!= None:
			return basics.Atom(self.toString()).setValue(selfValue)

		self.setOperandRight(self.getOperandRight().simplify())
		self.setOperandLeft(self.getOperandLeft().simplify())

		valOperRight=self.getOperandRight().getValue()
		valOperLeft=self.getOperandLeft().getValue()

		if valOperRight!=None and valOperLeft==None:

			if self.__func(True, valOperRight):
				return self.getOperandLeft()
			else :
				return Not(self.getOperandLeft())

		if valOperRight==None and valOperLeft!=None:

			if self.__func(valOperLeft, True):
				return self.getOperandRight()
			else :
				return Not(self.getOperandRight())

		return self

	def toString(self):
		return "(" + self.__operand1.toString() + " " + self.getSymbol() + " " + self.__operand2.toString() + ")"


class Conj(Operator):

	def __init__(self, operand1, operand2):

		def OP(a,b):
			if a==False or b==False:
				return False

			return a and b

		super(Conj, self).__init__("^", OP, operand1, operand2)

class Disj(Operator):

	def __init__(self, operand1, operand2):

		def OP(a,b):
			if a==True or b==True:
				return True

			if a==False and b==False:
				return False

			return None

		super(Disj, self).__init__("v", OP, operand1, operand2)

class Impl(Operator):

	def __init__(self, operand1, operand2):

		def OP(a,b):
			if a==False or b==True:
				return True

			if a==True and b==False:
				return False

			return None

		super(Impl, self).__init__("->", OP, operand1, operand2)

class Not(UnaryOperator):

	def __init__(self, operand):

		def OP(a):

			if a == None:
				return None

			return not a

		super(Not, self).__init__("~", OP, operand)



