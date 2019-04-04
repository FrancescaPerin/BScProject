import basics
import folOperator as op
import pars
import functionality as F

import copy

# BASIC CLASS

class Entailment:

	#rPremises corresponds to f+, lPremises to f-, 
	#rConclusions to X- and lConclusion to X+.
	def __init__(self, lPremises, rPremises, lConclusions, rConclusions):

		self.__rPremises = rPremises
		self.__lPremises = lPremises

		self.__rConclusions = rConclusions
		self.__lConclusions = lConclusions

		self.__children = []

		self.__rule =[]

		self.__side = bool


	def solve(self):

		# right rules
		
		r_Lconjs = RConj.canApply(self.getLeftConclusions())
		r_Rconjs = RConj.canApply(self.getRightConclusions())

		r_Ldisj = RDisj.canApply(self.getLeftConclusions())
		r_Rdisj = RDisj.canApply(self.getRightConclusions())

		r_Limpl = RImpl.canApply(self.getLeftConclusions())
		r_Rimpl = RImpl.canApply(self.getRightConclusions())

		r_Lneg = RNeg.canApply(self.getLeftConclusions())
		r_Rneg = RNeg.canApply(self.getRightConclusions())


		l_Lconjs = LConj.canApply(self.getLeftPremises())
		l_Rconjs = LConj.canApply(self.getRightPremises())

		l_Ldisj = LDisj.canApply(self.getLeftPremises())
		l_Rdisj = LDisj.canApply(self.getRightPremises())

		l_Limpl = LImpl.canApply(self.getLeftPremises())
		l_Rimpl = LImpl.canApply(self.getRightPremises())

		l_Lneg = LNeg.canApply(self.getLeftPremises())
		l_Rneg = LNeg.canApply(self.getRightPremises())

		#check if:
		#conjunction right rule (conclusions) can be applied to left part (before semicolon)
		if(any(r_Lconjs)):
			self.__children = RConj.stepLeft(self, self.getLeftConclusions()[r_Lconjs.index(True)])
			self.__rule=RConj.interpolate
			self.__side=True

		#conjunction right rule (conclusions) can be applied to right (after semicolon)
		elif(any(r_Rconjs)):
			self.__children = RConj.stepRight(self, self.getRightConclusions()[r_Rconjs.index(True)])
			self.__rule=RConj.interpolate
			self.__side=False

		#disjunction right rule (conclusions) can be applied to left 
		elif(any(r_Ldisj)):
			self.__children = RDisj.stepLeft(self, self.getLeftConclusions()[r_Ldisj.index(True)])
			self.__rule=RDisj.interpolate
			self.__side=True

		#disjunction right rule (conclusions) can be applied to right 
		elif(any(r_Rdisj)):
			self.__children = RDisj.stepRight(self, self.getRightConclusions()[r_Rdisj.index(True)])
			self.__rule= RDij.interpolate
			elf.__side=False

		elif(any(r_Limpl)):
			self.__children = RImpl.stepLeft(self, self.getLeftConclusions()[r_Limpl.index(True)])
			self.__rule= RImpl.interpolate
			self.__side=True

		elif(any(r_Rimpl)):
			self.__children = RImpl.stepRight(self, self.getRightConclusions()[r_Rimpl.index(True)])
			self.__rule= RImpl.interpolant
			elf.__side=False

		elif(any(r_Lneg)):
			self.__children = RNeg.stepLeft(self, self.getLeftConclusions()[r_Lneg.index(True)])
			self.__rule= RNeg.interpolate
			self.__side=True

		elif(any(r_Rneg)):
			self.__children = RNeg.stepRight(self, self.getRightConclusions()[r_Rneg.index(True)])
			self.__rule= RNeg.interpolate
			elf.__side=False
		# left rules

		
		elif(any(l_Lconjs)):
			self.__children = LConj.stepLeft(self, self.getLeftPremises()[l_Lconjs.index(True)])
			self.__rule= LConj.interpolate
			self.__side=True

		elif(any(l_Rconjs)):
			self.__children = LConj.stepRight(self, self.getRightPremises()[l_Rconjs.index(True)])
			self.__rule= LConj.interpolate
			elf.__side=False

		elif(any(l_Ldisj)):
			self.__children = LDisj.stepLeft(self, self.getLeftPremises()[l_Ldisj.index(True)])
			self.__rule= LDisj.interpolate
			self.__side=True

		elif(any(l_Rdisj)):
			self.__children = LDisj.stepRight(self, self.getRightPremises()[l_Rdisj.index(True)])
			self.__rule= LDisj.interpolate(self,interpolants,False)
			elf.__side=False

		
		elif(any(l_Limpl)):
			self.__children = LImpl.stepLeft(self, self.getLeftPremises()[l_Limpl.index(True)])
			self.__rule= LImpl.interpolate
			self.__side=True

		elif(any(l_Rimpl)):
			self.__children = LImpl.stepRight(self, self.getRightPremises()[l_Rimpl.index(True)])
			self.__rule= LImpl.interpolate
			elf.__side=False
				
		elif(any(l_Lneg)):
			self.__children = LNeg.stepLeft(self, self.getLeftPremises()[l_Lneg.index(True)])
			self.__rule= LNeg.interpolate
			self.__side=True

		elif(any(l_Rneg)):
			self.__children = LNeg.stepRight(self, self.getRightPremises()[l_Rneg.index(True)])
			self.__rule= LNeg.interpolate
			self.__side=False


		

		if self.__children == None:
			return False

		elif len(self.__children)>0:
			return True


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

	def getChildren(self):
		return self.__children


	def getRule(self):
		return self.__rule



	@staticmethod
	def copyEntailment(entailment):

		cLeftPremises=copy.copy(entailment.getLeftPremises())
		cRightPremises=copy.copy(entailment.getRightPremises())
		cLeftConcl=copy.copy(entailment.getLeftConclusions())
		cRightConcl=copy.copy(entailment.getRightConclusions())

		after=Entailment(cLeftPremises, cRightPremises, cLeftConcl, cRightConcl)

		return after

	def toString(self):

		a = ""
		b = ""
		c = ""
		d = ""

		for premise in self.getLeftPremises():

			a+=str(premise.toString()) + " "

		for premise in self.getRightPremises():
			c+=str(premise.toString()) + " "
		
		for conclusion in self.getLeftConclusions():

			b+=str(conclusion.toString()) + " "

		for conclusion in self.getRightConclusions():

			d+=str(conclusion.toString()) + " "

		return (a + " ; " + c + " |- " + b + " ; " + d )


	def isAxiom(self):

		if len(self.__children)==0:
			return True

		elif len(self.__children)>0:
			return False

	def axiomInterpolant(self):

		for premise in self.getPremises():
			if premise in self.getConclusions() and premise != None :
				interpolants=premise
				
		return interpolants

	def calcInterpolant (self):

		if self.isAxiom():
			return self.axiomInterpolant()

		else:
			interpolants=[child.calcInterpolant() for child in self.__children]


		return self.__rule(interpolants, self.__side)

# RULES

#	RIGHT-SIDE RULES

class RRule:

	@staticmethod
	def canApply(conclusions):
		pass

	@staticmethod
	def stepLeft(entailment, conclusion):
		pass

	@staticmethod
	def stepRight(entailment, conclusion):
		pass

	#rule for computing interpolant for R-L rule 
	@staticmethod
	def interpolate(interpolant, c=True):
		pass

	#rule for computing interpolant for R-R rule
	@staticmethod
	def interpolate(interpolant, c=False):
		pass

class RConj(RRule):

	@staticmethod
	def canApply(conclusions):
		return ([conclusion.getSymbol() == pars.CONJ_SYMBOL for conclusion in conclusions])

	@staticmethod
	def stepLeft(entailment, conclusion):


		left = Entailment.copyEntailment(entailment)
		right = Entailment.copyEntailment(entailment)

		left.getLeftConclusions().remove(conclusion)
		right.getLeftConclusions().remove(conclusion)

		left.getLeftConclusions().append(conclusion.getOperandLeft())
		right.getLeftConclusions().append(conclusion.getOperandRight())

		if (not left.solve() or not right.solve()):
			return None;
		
		return [left, right]

	def stepRight(entailment, conclusion):


		left = Entailment.copyEntailment(entailment)
		right = Entailment.copyEntailment(entailment)

		left.getRightConclusions().remove(conclusion)
		right.getRightConclusions().remove(conclusion)

		left.getRightConclusions().append(conclusion.getOperandLeft())
		right.getRightConclusions().append(conclusion.getOperandRight())

		if (not left.solve() or not right.solve()):
			return None;
		
		return [left, right]

	#interpolant rule if RConj is on the left of semicolon(f-)
	#interpolant is the disjunction of the interpolant of the two subfromulas
	def interpolate(interpolant, c=True):

		return op.Conj(interpolant[0],interpolant[1])

	#interpolant rule if RConj is on the right of semicolon(f+)
	#interpolant is the conjunction of the interpolant of the two subfromulas
	def interpolate (interpolant, c=False):

		return op.Disj(interpolant[0],interpolant[1])
		

class RDisj(RRule):

	@staticmethod
	def canApply(conclusions):
		return ([conclusion.getSymbol() == pars.DISJ_SYMBOL for conclusion in conclusions])

	@staticmethod
	def stepLeft(entailment, conclusion):

		new = Entailment.copyEntailment(entailment)

		new.getLeftConclusions().remove(conclusion)

		new.getLeftConclusions().append(conclusion.getOperandLeft())
		new.getLeftConclusions().append(conclusion.getOperandRight())

		if not new.solve():
			return None

		return [new]

	@staticmethod
	def stepRight(entailment, conclusion):

		new = Entailment.copyEntailment(entailment)

		new.getRigthConclusions().remove(conclusion)

		new.getRightConclusions().append(conclusion.getOperandLeft())
		new.getRightConclusions().append(conclusion.getOperandRight())

		if not new.solve():
			return None

		return [new]

	#interpolant rule if RDisj is on the left of semicolon(f-)
	#interpolant is not changed
	def interpolate (interpolant, c=True):
		
		return interpolant 

	#interpolant rule if RDisj is on the right of semicolon(f+)
	#interpolant is not changed
	def interpolate (interpolant, c=True):
		
		return interpolant 
		

class RImpl(RRule):

	@staticmethod
	def canApply(conclusions):
		return ([conclusion.getSymbol() == pars.IMPL_SYMBOL for conclusion in conclusions])

	@staticmethod
	def stepLeft(entailment, conclusion):

		new = Entailment.copyEntailment(entailment)

		new.getLeftConclusions().remove(conclusion)

		new.getLeftPremises().append(conclusion.getOperandLeft())
		new.getLeftConclusions().append(conclusion.getOperandRight())
		
		if not new.solve():
			return None

		return [new]

	@staticmethod
	def stepRight(entailment, conclusion):

		new = Entailment.copyEntailment(entailment)

		new.getRightConclusions().remove(conclusion)

		new.getRightPremises().append(conclusion.getOperandLeft())
		new.getRightConclusions().append(conclusion.getOperandRight())

		if not new.solve():
			return None

		return [new]

	#interpolant rule if RImpl is on the left of semicolon(f-)
	#interpolant is not changed
	def interpolate (interpolant, c=True):
		
		return interpolant 

	#interpolant rule if RImpl is on the right of semicolon(f+)
	#interpolant is not changed
	def interpolate (interpolant, c=True):
		
		return interpolant 

class RNeg(RRule):

	@staticmethod
	def canApply(conclusions):
		return ([conclusion.getSymbol() == pars.NOT_SYMBOL for conclusion in conclusions])

	@staticmethod
	def stepLeft(entailment, conclusion):

		new = Entailment.copyEntailment(entailment)

		new.getLeftConclusions().remove(conclusion)

		new.getRightPremises().append(conclusion.getOperand())

		if not new.solve():
			return None

		return [new]

	@staticmethod
	def stepRight(entailment, conclusion):

		new = Entailment.copyEntailment(entailment)

		new.getRightConclusions().remove(conclusion)

		new.getLeftPremises().append(conclusion.getOperand())

		if not new.solve():
			return None

		return [new]

	#interpolant rule if RNeg is on the left of semicolon(f-)
	#interpolant is not changed
	def interpolate (interpolant, c=True):
		
		return interpolant 

	#interpolant rule if RNeg is on the right of semicolon(f+)
	#interpolant is not changed
	def interpolate (interpolant, c=True):
		
		return interpolant 

class LRule:

	@staticmethod
	def canApply(premises):
		pass

	@staticmethod
	def stepLeft(entailment, premise):
		pass

	@staticmethod
	def stepRight(entailment, premise):
		pass

	#rule for computing interpolant for L-L rule 
	@staticmethod
	def interpolate(interpolant, c=True):
		pass

	#rule for computing interpolant for L-R rule
	@staticmethod
	def interpolate(interpolant, c=False):
		pass

class LConj(LRule):

	@staticmethod
	def canApply(premises):
		return ([premise.getSymbol() == pars.CONJ_SYMBOL for premise in premises])

	@staticmethod
	def stepLeft(entailment, premise):

		new = Entailment.copyEntailment(entailment)

		new.getLeftPremises().remove(premise)

		new.getLeftPremises().append(premise.getOperandLeft())
		new.getLeftPremises().append(premise.getOperandRight())

		if not new.solve():
			return None

		return [new]

	@staticmethod
	def stepRight(entailment, premise):

		new = Entailment.copyEntailment(entailment)

		new.getRightPremises().remove(premise)

		new.getRightPremises().append(premise.getOperandLeft())
		new.getRightPremises().append(premise.getOperandRight())

		if not new.solve():
			return None

		return [new]

	#interpolant rule if LConj is on the left of semicolon(f-)
	#interpolant is not changed
	def interpolate(interpolant, c=True):
		
		return interpolant 

	#interpolant rule if LConj is on the right of semicolon(f+)
	#interpolant is not changed
	def interpolate(interpolant, c=True):
		
		return interpolant 



class LDisj(LRule):

	@staticmethod
	def canApply(premises):
		return ([premise.getSymbol() == pars.DISJ_SYMBOL for premise in premises])

	@staticmethod
	def stepLeft(entailment, premise):

		left = Entailment.copyEntailment(entailment)
		right = Entailment.copyEntailment(entailment)

		left.getLeftPremises().remove(premise)
		right.getLeftPremises().remove(premise)

		left.getLeftPremises().append(premise.getOperandLeft())
		right.getLeftPremises().append(premise.getOperandRight())

		if (not left.solve() or not right.solve()):
			return None;
		
		return [left, right]

	@staticmethod
	def stepRight(entailment, premise):

		left = Entailment.copyEntailment(entailment)
		right = Entailment.copyEntailment(entailment)

		left.getRightPremises().remove(premise)
		right.getRightPremises().remove(premise)

		left.getRightPremises().append(premise.getOperandLeft())
		right.getRightPremises().append(premise.getOperandRight())

		if (not left.solve() or not right.solve()):
			return None;
		
		return [left, right]

	#interpolant rule if LDisj is on the left of semicolon(f-)
	#interpolant is the disjunction of the interpolant of the two subfromulas
	def interpolate(interpolant, c=True):
		
		return op.Disj(interpolant[0],interpolant[1])

	#interpolant rule if LDisj is on the right of semicolon(f+)
	#interpolant is the conjunction of the interpolant of the two subfromulas
	def interpolate(interpolant, c=False):
		
		return op.Conj(interpolant[0],interpolant[1])

class LImpl(LRule):

	@staticmethod
	def canApply(premises):
		return ([premise.getSymbol() == pars.IMPL_SYMBOL for premise in premises])

	@staticmethod
	def stepLeft(entailment, premise):

		left = Entailment.copyEntailment(entailment)
		right = Entailment.copyEntailment(entailment)

		left.getLeftPremises().remove(premise)
		right.getLeftPremises().remove(premise)

		left.getRightConclusions().append(premise.getOperandLeft())
		right.getLeftPremises().append(premise.getOperandRight())

		if (not left.solve() or not right.solve()):
			return None;
		
		return [left, right]

	@staticmethod
	def stepRight(entailment, premise):

		left = Entailment.copyEntailment(entailment)
		right = Entailment.copyEntailment(entailment)

		left.getRightPremises().remove(premise)
		right.getRightPremises().remove(premise)

		left.getLeftConclusions().append(premise.getOperandLeft())
		right.getRightPremises().append(premise.getOperandRight())

		if (not left.solve() or not right.solve()):
			return None;
		
		return [left, right]

	#interpolant rule if LImpl is on the left of semicolon(f-)
	#interpolant is the implication of the interpolant of the two subfromulas
	def interpolate(interpolant, c=True):
		
		return op.Impl(interpolant[0],interpolant[1])

	#interpolant rule if LImpl is on the right of semicolon(f+)
	#interpolant is the conjunction of the interpolant of the two subfromulas
	def interpolate(interpolant, c=False):

		return op.Conj(interpolant[0],interpolant[1])

class LNeg(LRule):

	@staticmethod
	def canApply(premises):
		return ([premise.getSymbol() == pars.NOT_SYMBOL for premise in premises])

	@staticmethod
	def stepLeft(entailment, premise):

		new = Entailment.copyEntailment(entailment)

		new.getLeftPremises().remove(premise)
		new.getRightConclusions().append(premise.getOperand())

		if not new.solve():
			return None

		return [new]

	@staticmethod
	def stepRight(entailment, premise):

		new = Entailment.copyEntailment(entailment)

		new.getRightPremises().remove(premise)
		new.getLeftConclusions().append(premise.getOperand())

		if not new.solve():
			return None

		return [new]

	#interpolant rule if LNeg is on the left of semicolon(f-)
	#interpolant is the negation of the interpolant of the subfromula
	def interpolate(interpolant, c=True):
		
		return op.Not(interpolant[0],interpolant[1])

	#interpolant rule if LNeg is on the right of semicolon(f+)
	#interpolant is not changed
	def interpolate(interpolant, c=False):
		
		return interpolant 

