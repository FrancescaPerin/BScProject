import basics
import folOperator as op
import pars

import copy

# BASIC CLASS

class Entailment:

	#rPremises corresponds to f+, lPremises to f-, 
	#rConclusions to X- and lConclusion to X+.
	def __init__(self, lPremises, lConclusions):

		self.__rPremises = []
		self.__lPremises = lPremises

		self.__rConclusions = []
		self.__lConclusions = lConclusions

		self.__children = []

	def solve(self):
		
		# right rules
		
		rconjs = RConj.canApply(self.getLeftConclusions())
		rdisj = RDisj.canApply(self.getLeftConclusions())
		rimpl = RImpl.canApply(self.getLeftConclusions())
		rneg = RNeg.canApply(self.getLeftConclusions())

		lconjs = LConj.canApply(self.getLeftPremises())
		ldisj = LDisj.canApply(self.getLeftPremises())
		limpl = LImpl.canApply(self.getLeftPremises())
		lneg = LNeg.canApply(self.getLeftPremises())


		if(any(rconjs)):
			self.__children = RConj.step(self, self.getLeftConclusions()[rconjs.index(True)])

		
		elif(any(rdisj)):
			self.__children = RDisj.step(self, self.getLeftConclusions()[rdisj.index(True)])

		
		elif(any(rimpl)):
			self.__children = RImpl.step(self, self.getLeftConclusions()[rimpl.index(True)])

		
		elif(any(rneg)):
			self.__children = RNeg.step(self, self.getLeftConclusions()[rneg.index(True)])

		# left rules

		
		elif(any(lconjs)):
			self.__children = LConj.step(self, self.getLeftPremises()[lconjs.index(True)])

		
		elif(any(ldisj)):
			self.__children = LDisj.step(self, self.getLeftPremises()[ldisj.index(True)])

		
		elif(any(limpl)):
			self.__children = LImpl.step(self, self.getLeftPremises()[limpl.index(True)])

		
		elif(any(lneg)):
			self.__children = LNeg.step(self, self.getLeftPremises()[lneg.index(True)])


		if self.__children == None:
			return False
		elif len(self.__children)>0:
			return True

		# axioms

		for premise in self.getPremises():
			if premise in self.getConclusions():
				return True

		return False

	def getRightPremises(self):
		return self.__rPremises

	def getLeftPremises(self):
		return self.__lPremises

	def getPremises(self):
		return self.__lPremises + self.__rPremises

	def getRightConclusions(self):
		return self.__rConclusions

	def getLeftConclusions(self):
		return self.__lConclusions

	def getConclusions(self):
		return self.__lConclusions + self.__rConclusions

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
		return [conclusion.getSymbol() == pars.CONJ_SYMBOL for conclusion in conclusions]

	@staticmethod
	def step(entailment, conclusion):

		left = Entailment.copyEntailment(entailment)
		right = Entailment.copyEntailment(entailment)

		left.getLeftConclusions().remove(conclusion)
		right.getLeftConclusions().remove(conclusion)

		left.getLeftConclusions().append(conclusion.getOperandLeft())
		right.getLeftConclusions().append(conclusion.getOperandRight())

		if (not left.solve() or not right.solve()):
			return None;
		
		return [left, right]

class RDisj(RRule):

	@staticmethod
	def canApply(conclusions):
		return [conclusion.getSymbol() == pars.DISJ_SYMBOL for conclusion in conclusions]

	@staticmethod
	def step(entailment, conclusion):

		new = Entailment.copyEntailment(entailment)

		new.getLeftConclusions().remove(conclusion)

		new.getLeftConclusions().append(conclusion.getOperandLeft())
		new.getLeftConclusions().append(conclusion.getOperandRight())

		if not new.solve():
			return None

		return [new]

class RImpl(RRule):

	@staticmethod
	def canApply(conclusions):
		return [conclusion.getSymbol() == pars.IMPL_SYMBOL for conclusion in conclusions]

	@staticmethod
	def step(entailment, conclusion):

		new = Entailment.copyEntailment(entailment)

		new.getLeftConclusions().remove(conclusion)

		new.getRightPremises().append(conclusion.getOperandLeft())
		new.getLeftConclusions().append(conclusion.getOperandRight())

		if not new.solve():
			return None

		return [new]

class RNeg(RRule):

	@staticmethod
	def canApply(conclusions):
		return [conclusion.getSymbol() == pars.NOT_SYMBOL for conclusion in conclusions]

	@staticmethod
	def step(entailment, conclusion):

		new = Entailment.copyEntailment(entailment)

		new.getLeftConclusions().remove(conclusion)

		new.getRightPremises().append(conclusion.getOperand())

		if not new.solve():
			return None

		return [new]

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
		return [premise.getSymbol() == pars.CONJ_SYMBOL for premise in premises]

	@staticmethod
	def step(entailment, premise):

		new = Entailment.copyEntailment(entailment)
		new.getLeftPremises().remove(premise)

		new.getLeftPremises().append(premise.getOperandLeft())
		new.getLeftPremises().append(premise.getOperandRight())

		if not new.solve():
			return None

		return [new]

class LDisj(LRule):

	@staticmethod
	def canApply(premises):
		return [premise.getSymbol() == pars.DISJ_SYMBOL for premise in premises]

	@staticmethod
	def step(entailment, premise):

		left = Entailment.copyEntailment(entailment)
		right = Entailment.copyEntailment(entailment)

		left.getLeftPremises().remove(premise)
		right.getLeftPremises().remove(premise)

		left.getLeftPremises().append(premise.getOperandLeft())
		right.getLeftPremises().append(premise.getOperandRight())

		if (not left.solve() or not right.solve()):
			return None;
		
		return [left, right]

class LImpl(LRule):

	@staticmethod
	def canApply(premises):
		return [premise.getSymbol() == pars.IMPL_SYMBOL for premise in premises]

	@staticmethod
	def step(entailment, premise):

		left = Entailment.copyEntailment(entailment)
		right = Entailment.copyEntailment(entailment)

		left.getLeftPremises().remove(premise)
		right.getLeftPremises().remove(premise)

		left.getRightConclusions().append(premise.getOperandLeft())
		right.getLeftPremises().append(premise.getOperandRight())

		if (not left.solve() or not right.solve()):
			return None;
		
		return [left, right]

class LNeg(LRule):

	@staticmethod
	def canApply(premises):
		return [premise.getSymbol() == pars.NOT_SYMBOL for premise in premises]

	@staticmethod
	def step(entailment, premise):

		new = Entailment.copyEntailment(entailment)

		new.getLeftPremises().remove(premise)
		new.getRightConclusions().append(premise.getOperand())

		if not new.solve():
			return None

		return [new]
