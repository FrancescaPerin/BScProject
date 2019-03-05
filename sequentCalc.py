import basics
import folOperator as op

import copy

# BASIC CLASS

class Entailment:

	def __init__(self, premises, conclusions):

		self.__premises = premises
		self.__conclusions = conclusions

	def solve(self):
		
		# right rules

		rconjs = RConj.canApply(self.getConclusions())
		if(any(rconjs)):
			return RConj.step(self, self.getConclusions()[rconjs.index(True)])

		rdisj = RDisj.canApply(self.getConclusions())
		if(any(rdisj)):
			return RDisj.step(self, self.getConclusions()[rdisj.index(True)])

		rimpl = RImpl.canApply(self.getConclusions())
		if(any(rimpl)):
			return RImpl.step(self, self.getConclusions()[rimpl.index(True)])

		rneg = RNeg.canApply(self.getConclusions())
		if(any(rneg)):
			return RNeg.step(self, self.getConclusions()[rneg.index(True)])

		# left rules

		lconjs = LConj.canApply(self.getPremises())
		if(any(lconjs)):
			return LConj.step(self, self.getPremises()[lconjs.index(True)])

		ldisj = LDisj.canApply(self.getPremises())
		if(any(ldisj)):
			return LDisj.step(self, self.getPremises()[ldisj.index(True)])

		limpl = LImpl.canApply(self.getPremises())
		if(any(limpl)):
			return LImpl.step(self, self.getPremises()[limpl.index(True)])

		lneg = LNeg.canApply(self.getPremises())
		if(any(lneg)):
			return LNeg.step(self, self.getPremises()[lneg.index(True)])


		# axioms

		for premise in self.getPremises():
			if premise in self.getConclusions():
				return True

		return False

	def getPremises(self):
		return self.__premises

	def getConclusions(self):
		return self.__conclusions

	@staticmethod
	def copyEntailment(entailment):
		return Entailment(copy.copy(entailment.getPremises()), copy.copy(entailment.getConclusions()))

	def toString(self):

		a = ""
		b = ""

		for premise in self.getPremises():

			a+=str(premise.toString()) + " "
		
		for conclusion in self.getConclusions():

			b+=str(conclusion.toString()) + " "

		return (a + " |- " + b)

# RULES

#	RIGHT-SIDE RULES

class RRule:

	@staticmethod
	def canApply(conclusions):
		pass

	@staticmethod
	def step(entailment, conclusion):
		pass

class RConj(RRule):

	@staticmethod
	def canApply(conclusions):
		return [conclusion.getSymbol() == "^" for conclusion in conclusions]

	@staticmethod
	def step(entailment, conclusion):

		left = Entailment.copyEntailment(entailment)
		right = Entailment.copyEntailment(entailment)

		left.getConclusions().remove(conclusion)
		right.getConclusions().remove(conclusion)

		left.getConclusions().append(conclusion.getOperandLeft())
		right.getConclusions().append(conclusion.getOperandRight())

		return left.solve() and right.solve()

class RDisj(RRule):

	@staticmethod
	def canApply(conclusions):
		return [conclusion.getSymbol() == "v" for conclusion in conclusions]

	@staticmethod
	def step(entailment, conclusion):

		new = Entailment.copyEntailment(entailment)
		new.getConclusions().remove(conclusion)

		new.getConclusions().append(conclusion.getOperandLeft())
		new.getConclusions().append(conclusion.getOperandRight())

		return new.solve()

class RImpl(RRule):

	@staticmethod
	def canApply(conclusions):
		return [conclusion.getSymbol() == "->" for conclusion in conclusions]

	@staticmethod
	def step(entailment, conclusion):

		new = Entailment.copyEntailment(entailment)

		new.getConclusions().remove(conclusion)

		new.getPremises().append(conclusion.getOperandLeft())
		new.getConclusions().append(conclusion.getOperandRight())

		return new.solve()

class RNeg(RRule):

	@staticmethod
	def canApply(conclusions):
		return [conclusion.getSymbol() == "~" for conclusion in conclusions]

	@staticmethod
	def step(entailment, conclusion):

		new = Entailment.copyEntailment(entailment)

		new.getConclusions().remove(conclusion)

		new.getPremises().append(conclusion.getOperand())

		return new.solve()

class LRule:

	@staticmethod
	def canApply(premises):
		pass

	@staticmethod
	def step(entailment, premise):
		pass

class LConj(LRule):

	@staticmethod
	def canApply(premises):
		return [premise.getSymbol() == "^" for premise in premises]

	@staticmethod
	def step(entailment, premise):

		new = Entailment.copyEntailment(entailment)
		new.getPremises().remove(premise)

		new.getPremises().append(premise.getOperandLeft())
		new.getPremises().append(premise.getOperandRight())

		return new.solve()

class LDisj(LRule):

	@staticmethod
	def canApply(premises):
		return [premise.getSymbol() == "v" for premise in premises]

	@staticmethod
	def step(entailment, premise):

		left = Entailment.copyEntailment(entailment)
		right = Entailment.copyEntailment(entailment)

		left.getPremises().remove(premise)
		right.getPremises().remove(premise)

		left.getPremises().append(premise.getOperandLeft())
		right.getPremises().append(premise.getOperandRight())

		return left.solve() and right.solve()

class LImpl(LRule):

	@staticmethod
	def canApply(premises):
		return [premise.getSymbol() == "->" for premise in premises]

	@staticmethod
	def step(entailment, premise):

		left = Entailment.copyEntailment(entailment)
		right = Entailment.copyEntailment(entailment)

		left.getPremises().remove(premise)
		right.getPremises().remove(premise)

		left.getConclusions().append(premise.getOperandLeft())
		right.getPremises().append(premise.getOperandRight())

		return left.solve() and right.solve()

class LNeg(LRule):

	@staticmethod
	def canApply(premises):
		return [premise.getSymbol() == "~" for premise in premises]

	@staticmethod
	def step(entailment, premise):

		new = Entailment.copyEntailment(entailment)

		new.getPremises().remove(premise)
		new.getConclusions().append(premise.getOperand())

		return new.solve()
