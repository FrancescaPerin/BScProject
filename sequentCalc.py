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

		self.__latex=""

		self.__modsymbol =""


	def solve(self):

<<<<<<< Updated upstream
		# right rules
		
=======
		#weakening rule chack if to be applied
		#weakening=Weak.canApply(self.getPremises(),self.getConclusions())

		#modality rule check first before other operators
		all_Mod=LMod.canApply(self.getPremises(),self.getConclusions())

		# right rules
>>>>>>> Stashed changes
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

		#weakening rule can be applied
		"""if(weakening):
			print ("entering if weakening")
			self.__children = Weak.step(self, self.getLeftConclusions(), self.getRightConclusions())
			self.__rule=Weak.interpolate
			self.__side=True"""

		#modality rule can be applied
		if(all_Mod):
			self.__children, self.__modsymbol = LMod.step(self, self.getLeftConclusions(), self.getRightConclusions())
			self.__rule=LMod.interpolate
			self.__side=True


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
			self.__side=False

		elif(any(r_Limpl)):
			self.__children = RImpl.stepLeft(self, self.getLeftConclusions()[r_Limpl.index(True)])
			self.__rule= RImpl.interpolate
			self.__side=True

		elif(any(r_Rimpl)):
			self.__children = RImpl.stepRight(self, self.getRightConclusions()[r_Rimpl.index(True)])
			self.__rule= RImpl.interpolant
			self.__side=False

		elif(any(r_Lneg)):
			self.__children = RNeg.stepLeft(self, self.getLeftConclusions()[r_Lneg.index(True)])
			self.__rule= RNeg.interpolate
			self.__side=True

		elif(any(r_Rneg)):
			self.__children = RNeg.stepRight(self, self.getRightConclusions()[r_Rneg.index(True)])
			self.__rule= RNeg.interpolate
			self.__side=False
		# left rules

		
		elif(any(l_Lconjs)):
			self.__children = LConj.stepLeft(self, self.getLeftPremises()[l_Lconjs.index(True)])
			self.__rule= LConj.interpolate
			self.__side=True

		elif(any(l_Rconjs)):
			self.__children = LConj.stepRight(self, self.getRightPremises()[l_Rconjs.index(True)])
			self.__rule= LConj.interpolate
			self.__side=False

		elif(any(l_Ldisj)):
			self.__children = LDisj.stepLeft(self, self.getLeftPremises()[l_Ldisj.index(True)])
			self.__rule= LDisj.interpolate
			self.__side=True

		elif(any(l_Rdisj)):
			self.__children = LDisj.stepRight(self, self.getRightPremises()[l_Rdisj.index(True)])
			self.__rule= LDisj.interpolate
			self.__side=False

		
		elif(any(l_Limpl)):
			self.__children = LImpl.stepLeft(self, self.getLeftPremises()[l_Limpl.index(True)])
			self.__rule= LImpl.interpolate
			self.__side=True

		elif(any(l_Rimpl)):
			self.__children = LImpl.stepRight(self, self.getRightPremises()[l_Rimpl.index(True)])
			self.__rule= LImpl.interpolate
			self.__side=False
				
		elif(any(l_Lneg)):
			self.__children = LNeg.stepLeft(self, self.getLeftPremises()[l_Lneg.index(True)])
			self.__rule= LNeg.interpolate
			self.__side=True

		elif(any(l_Rneg)):
			self.__children = LNeg.stepRight(self, self.getRightPremises()[l_Rneg.index(True)])
			self.__rule= LNeg.interpolate
			self.__side=False


		print("After:"+self.toString())

		if self.__children == None:
			return False

		elif len(self.__children)>0:
			return True


		for premise in self.getPremises():
			if premise in self.getConclusions():
				return True

		print ("reaching False conclusion")
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


	def setPremises(self, premiseL, premiseR):

		self.__lPremises=premiseR
		self.__rPremises=premiseL
		return self

	def setConclusions(self, conclusionL, conclusionR):

		self.__lConclusions=conclusionR
		self.__rConclusions=conclusionL
		return self

	def addPremL(self, new, index):
		self.__lPremises.insert(index,new)

	def addPremR(self, new):
		self.__rPremises.append(new)

	def addConcL(self, new):
		self.__lConclusions.append(new)

	def addConcR(self, new):
		self.__rConclusions.append(new)

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

		len1=len(self.getLeftPremises())
		for premise in self.getLeftPremises():

			if len1>1:
				a+=str(premise.toString()) + ", "
			elif len1==1:

				a+=str(premise.toString())
			len1-=1

		len2=len(self.getRightPremises())
		for premise in self.getRightPremises():
			
			if len2>1:
				c+=str(premise.toString()) + ", "
			elif len2==1:
				c+=str(premise.toString())
			len2-=1
		
		len3=len(self.getLeftConclusions())
		for conclusion in self.getLeftConclusions():

			if len3>1:
				b+=str(conclusion.toString()) + ", "
			elif len3==1:
				b+=str(conclusion.toString())
			len3-=1

		len4=len(self.getRightConclusions())
		for conclusion in self.getRightConclusions():
			if len4>1:
				d+=str(conclusion.toString()) + ", "
			elif len4==1:
				d+=str(conclusion.toString())
			len4-=1

		return (a + " ; " + c + " |- " + b + " ; " + d )

	def isAxiom(self):

		if len(self.__children)==0:
			return True

		elif len(self.__children)>0:
			return False

	def axiomInterpolant(self):

		interpolants=None
		for premise in self.getLeftPremises():

			if premise in self.getLeftConclusions():

				interpolants=premise

				self.__latex=r"\AxiomC{$"+self.convertSymbols(interpolants)+"$}\n"

				print("")
				print("Axiom  " + self.toString() + " ")
				print (interpolants.toString())
				print(" ")

				return interpolants


		for premise in self.getRightPremises():

			if premise in self.getRightConclusions():

				interpolants=op.Not(premise)

				self.__latex=r"\AxiomC{$"+self.convertSymbols(interpolants)+"$}\n"

				print("")
				print("Axiom  " + self.toString() + " ")
				print (interpolants.toString())
				print(" ")

				return interpolants

		for premise in self.getLeftPremises():

			if premise in self.getRightConclusions():
				interpolants=basics.Atom("False")
				interpolants.setValue(False)

				self.__latex+=r"\AxiomC{$"+self.convertSymbols(interpolants)+"$}\n"

				print("")
				print("Axiom :" + self.toString())
				print(interpolants.toString())
				print("")
				
				return interpolants

		for premise in self.getRightPremises():

			if premise in self.getLeftConclusions():

				interpolants=basics.Atom("True")
				interpolants.setValue(True)

				self.__latex+=r"\AxiomC{$"+self.convertSymbols(interpolants)+"$}"+"\n"

				print("")
				print("Axiom :" + self.toString())
				print(interpolants.toString())
				print("")

				return interpolants

		return interpolants

	def calcInterpolant(self):

		if self.isAxiom():

			return self.axiomInterpolant()


		interpolants = [child.calcInterpolant() for child in self.__children]

		print("Interpolants for " + self.toString() + " with rule " + str(self.__rule) + "and side " +str(self.__side)+":")
		print ("len:"+ str(len(self.__children)))

		if (len(self.__children))==1:

			if(self.__rule.__qualname__[:-12]=="LMod"):
				self.__latex+=r"\RightLabel{$$}"+"\n"
				#self.__latex+=r"\RightLabel{$"+ self.convertRule(self.__side)+ "$}"+"\n"
				#self.__latex+=r"\UnaryInfC{$"+ self.convertSymbols(self.__rule(interpolants, self.__side, self.__modsymbol))+ "$}"+"\n"

			else:
				self.__latex+=r"\RightLabel{$"+ self.convertRule(self.__side)+ "$}"+"\n"
				self.__latex+=r"\UnaryInfC{$"+ self.convertSymbols(self.__rule(interpolants, self.__side))+ "$}"+"\n"

		if (len(self.__children))==2:
			self.__latex+=r"\RightLabel{$"+ self.convertRule(self.__side)+ "$}"+"\n"
			self.__latex+=r"\BinaryInfC{$"+ self.convertSymbols(self.__rule(interpolants, self.__side))+ "$}"+"\n"

<<<<<<< Updated upstream
		
		print(self.__rule(interpolants, self.__side).toString())
=======
		if(self.__rule.__qualname__[:-12]=="LMod"):
			print(self.__rule(interpolants, self.__side, self.__modsymbol).toString())
			print(" ")
			return self.__rule(interpolants, self.__side, self.__modsymbol)
		else:
			print(self.__rule(interpolants, self.__side).toString())
>>>>>>> Stashed changes

		print(" ")


		return self.__rule(interpolants, self.__side) 	

	@staticmethod
	def checkInterpolant(phi, psi, interpolant):



		entailment1=Entailment([phi],[], [interpolant], [])
		entailment2=Entailment([interpolant],[], [psi], [])

		print("entailment 1:"+ entailment1.toString())
		print("entailment 2:"+ entailment2.toString())

		print("entailment 1 is a tautology:"+ str(op.Impl(phi,interpolant).isTaut()))
		print("entailment 2 is a tautology:"+ str(op.Impl(interpolant,psi).isTaut()))

		if op.Impl(phi,interpolant).isTaut() and op.Impl(interpolant,psi).isTaut():
			if Entailment.checkVocabulary(phi, psi, interpolant):
				print("interpolant found respects the CI property and definiton")
				return True

		return False

	@staticmethod
	def checkVocabulary(phi, psi, interpolant):

		allAtoms = phi.getAtoms() + psi.getAtoms() 
		allAtoms.append(basics.Atom("True"))
		allAtoms.append(basics.Atom("False"))

		for atom in interpolant.getAtoms():
			if not any ([atom.getSymbol()==a.getSymbol() for a in allAtoms]):
				return False

		return True



	def convertSymbols(self, interpolant):

		newS=self.toString()
		interpolantStr=interpolant.toString()

		newS=newS.replace(r"|-", r"\overset{"+interpolantStr+ r"}{\vdash}")
		newS=newS.replace(pars.DISJ_SYMBOL, r"\lor")
		newS=newS.replace(pars.CONJ_SYMBOL, r"\land")
		newS=newS.replace(pars.IMPL_SYMBOL, r"\rightarrow")
		newS=newS.replace(pars.NOT_SYMBOL, r"\neg")
		newS=newS.replace(r"True", r"\top")
		newS=newS.replace(r"False", r"\bot")

		return newS

	def convertRule(self, side):

		name=self.__rule.__qualname__

		name=name[:-12]

		if side==True:

			name=name.replace("Impl", r"\rightarrow_{+}")
			name=name.replace("Neg", r"\neg_{+}")
			name=name.replace("Conj", r"\land_{+}")
			name=name.replace("Disj", r"\lor_{+}")

		elif side==False:

			name=name.replace("Impl", r"\rightarrow_{-}")
			name=name.replace("Neg", r"\neg_{-}")
			name=name.replace("Conj", r"\land_{-}")
			name=name.replace("Disj", r"\lor_{-}")


		return name 

	def latexProof(self):
		
		for child in self.__children:
			child.latexProof()
		
		print(self.__latex)

	def latexProofAux(self):

		print("\nBEGIN LATEX PROOF:\n")

		print(r"\begin{prooftree}")

		self.latexProof()

		print(r"\end{prooftree}")


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
	def interpolate(interpolant, c):
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
	#interpolant rule if RConj is on the right of semicolon(f+)
	#interpolant is the conjunction of the interpolant of the two subfromulas
	def interpolate(interpolant, c):

		if c:
			return op.Conj(interpolant[0],interpolant[1])
		else:
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
	#interpolant rule if RDisj is on the right of semicolon(f+)
	#interpolant is not changed
	def interpolate (interpolant, c):
		return interpolant[0]

class RImpl(RRule):

	@staticmethod
	def canApply(conclusions):
		return ([conclusion.getSymbol() == pars.IMPL_SYMBOL for conclusion in conclusions])

	@staticmethod
	def stepLeft(entailment, conclusion):

		new = Entailment.copyEntailment(entailment)

		new.getLeftConclusions().remove(conclusion)

		new.getRightPremises().append(conclusion.getOperandLeft())
		new.getLeftConclusions().append(conclusion.getOperandRight())
		
		if not new.solve():
			return None

		return [new]

	@staticmethod
	def stepRight(entailment, conclusion):

		new = Entailment.copyEntailment(entailment)

		new.getRightConclusions().remove(conclusion)

		new.getLeftPremises().append(conclusion.getOperandLeft())
		new.getRightConclusions().append(conclusion.getOperandRight())

		if not new.solve():
			return None

		return [new]

	#interpolant rule if RImpl is on the left of semicolon(f-)
	#interpolant is not changed
	#interpolant rule if RImpl is on the right of semicolon(f+)
	#interpolant is not changed
	def interpolate (interpolant, c):
		return interpolant[0]


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
	#interpolant rule if RNeg is on the right of semicolon(f+)
	#interpolant is not changed
	def interpolate (interpolant, c):
		return interpolant[0]
 

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
	def interpolate(interpolant, c):
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
	#interpolant rule if LConj is on the right of semicolon(f+)
	#interpolant is not changed
	def interpolate(interpolant, c):
		return interpolant[0]



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
	#interpolant rule if LDisj is on the right of semicolon(f+)
	#interpolant is the conjunction of the interpolant of the two subfromulas
	def interpolate(interpolant, c):

		if c:
			return op.Disj(interpolant[0],interpolant[1])
		else:
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

		left.setPremises(left.getLeftPremises(), left.getRightPremises())
		left.setConclusions(left.getLeftConclusions(), left.getRightConclusions())
		
		right.getLeftPremises().append(premise.getOperandRight())
		left.getLeftConclusions().append(premise.getOperandLeft())

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
	#interpolant rule if LImpl is on the right of semicolon(f+)
	#interpolant is the conjunction of the interpolant of the two subfromulas
	def interpolate(interpolant, c):

		if c:
			return op.Impl(interpolant[0],interpolant[1])
		else:
			return op.Conj(interpolant[0],interpolant[1])


class LNeg(LRule):

	@staticmethod
	def canApply(premises):
		return ([premise.getSymbol() == pars.NOT_SYMBOL for premise in premises])

	@staticmethod
	def stepLeft(entailment, premise):

		new = Entailment.copyEntailment(entailment)

		new.getLeftPremises().remove(premise)

		new.setPremises(new.getLeftPremises(), new.getRightPremises())
		new.setConclusions(new.getLeftConclusions(), new.getRightConclusions())

		new.getLeftConclusions().append(premise.getOperand())


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
	#interpolant rule if LNeg is on the right of semicolon(f+)
<<<<<<< Updated upstream
	#interpolant is not changed
	def interpolate(interpolant, c):
=======
	#interpolant is not change
	def interpolate(interpolant, c=True):
>>>>>>> Stashed changes

		if c:
			return op.Not(interpolant[0])
		else:
			return interpolant[0]

class MRule:

	@staticmethod
	def canApply(premises, conclusions):
		pass

	@staticmethod
	def step(entailment, conclusions):
		pass

	#rule for computing interpolant for box rule, adds a box(with appropriate symbol) to interpolant
	@staticmethod
	def interpolate(interpolant, c, symbol):
		pass

class LMod(MRule):

	@staticmethod
	def canApply(premises,conclusions):

		if len(conclusions)>1:
			return False

		if len(conclusions)<1  or not isinstance(conclusions[0], op.Mod):
			return False

		elif (len(conclusions)==1 and isinstance(conclusions[0], op.Mod)):
			conclusion = conclusions[0]

			for premise in premises:
				if (premise.getSymbol() != conclusion.getSymbol()):
					return False

		return True

	@staticmethod
	def step(entailment, lC, rC):

		new = Entailment.copyEntailment(entailment)
		symbol=new.getConclusions()[0].getSymbol()

		gotConcl = True
		index=0

		if len(rC)==1 and isinstance(rC[0], op.Mod) and len(lC)<1:

			conclusion = entailment.getRightConclusions()[0]

			new.getRightConclusions().remove(conclusion)
			new.addConcR(conclusion.getOperand())

		elif len(lC)==1 and isinstance(lC[0], op.Mod) and len(rC)<1:

			conclusion = entailment.getLeftConclusions()[0]

			new.getLeftConclusions().remove(conclusion)
			new.addConcL(conclusion.getOperand())

		else:
			gotConcl = False

		if gotConcl:
			for premise in new.getRightPremises():
				print("right premise")
				print(premise.toString())
				new.getRightPremises().remove(premise)
				new.addPremR(premise.getOperand())

			while index < len(new.getLeftPremises()):
				new.getLeftPremises()[index]=new.getLeftPremises()[index].getOperand()
				index += 1


			"""for premise in new.getLeftPremises():
				print("left premise")
				print(premise.toString())
				new.getLeftPremises().remove(premise)
				new.addPremL(premise.getOperand())"""

		print(new.toString())

		if not new.solve():
			return None

		return [new], symbol


	#interpolant rule if RNeg is on the left of semicolon(f-)
	#interpolant is not changed
	#interpolant rule if RNeg is on the right of semicolon(f+)
	#interpolant is not changed
	def interpolate (interpolant, c, symbol):
		symbol=symbol.replace("[", "")
		symbol=symbol.replace("]", "")
		return op.Mod(interpolant[0],symbol)

class Weak(MRule):

	@staticmethod
	def canApply(premises,conclusions):

		for conclusion in conclusions:
			if not isinstance(conclusion, op.Mod):
				return False

		for premise in premises:
			if not isinstance(premise, op.Mod):
				return False

		for conclusion in conclusions:
			found = False
			for premise in premises:
				if premise.getSymbol() == conclusion.getSymbol():
					found = True
					break

			if not found:
				return False

		return True

	@staticmethod
	def step(entailment, lC, rC):

		division = {}

		for conclusion in entailment.getConclusions():

			division[conclusion.getSymbol()] = {}

			if conclusion in entailment.getLeftConclusions():
				division[conclusion.getSymbol()]["lC"] = [copy.deepcopy(conclusion)]
				division[conclusion.getSymbol()]["rC"] = []
			else:
				division[conclusion.getSymbol()]["rC"] = [copy.deepcopy(conclusion)]
				division[conclusion.getSymbol()]["lC"] = []

			division[conclusion.getSymbol()]["lP"] = []
			division[conclusion.getSymbol()]["rP"] = []

			for premise in entailment.getLeftPremises():
				if premise.getSymbol() == conclusion.getSymbol():
					division[conclusion.getSymbol()]["lP"].append(copy.deepcopy(premise))

			for premise in entailment.getRightPremises():
				if premise.getSymbol() == conclusion.getSymbol():
					division[conclusion.getSymbol()]["rP"].append(copy.deepcopy(premise))

		for symbol, subdivision in division.keys():

			new = Entailment(subdivision["lP"], subdivision["rP"], subdivision["lC"], subdivision["rC"])

			if new.solve():
				return [new]
			else:
				del new

		return False


	#interpolant rule if RNeg is on the left of semicolon(f-)
	#interpolant is not changed
	#interpolant rule if RNeg is on the right of semicolon(f+)
	#interpolant is not changed
	def interpolate (interpolant,c,self):
		return interpolant[0]
