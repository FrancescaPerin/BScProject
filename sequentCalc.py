import basics
import folOperator as op
import pars
import functionality as F

from sys import platform
import subprocess
import copy
import collections
import itertools


# BASIC CLASS


class Entailment:

    # rPremises corresponds to f+, lPremises to f-,
    # rConclusions to X- and lConclusion to X+.
    def __init__(self, lPremises, rPremises, lConclusions, rConclusions):

        self.__rPremises = rPremises
        self.__lPremises = lPremises

        self.__rConclusions = rConclusions
        self.__lConclusions = lConclusions

        self.__children = []

        self.__rule = []

        self.__side = bool

        self.__latex = ""

        self.__modsymbol = ""

    def solve(self):

        entailment = self.toString()

        new = entailment.replace("|-", "")
        string = "~^|->"

        print ("proof:"+ self.toString())

        if not any(elem in new for elem in string):
            #print(self.toString())
            for premise in self.getPremises():
                for conclusion in self.getConclusions():
                    if premise.toString() == conclusion.toString():
                        print(self.toString())
                        return True

        if len(self.getConclusions()) >= 1 and len(self.getPremises()) > 0:

            for itemC in self.getConclusions():
                if "True" in itemC.toString():
                    return True

        if len(self.getPremises()) >= 1 and len(self.getConclusions()) > 0:

            for itemP in self.getPremises():
                if "False" in itemP.toString():
                    return True

        # check if:

        # right rules who have only one children

        # disjunction right rule (conclusions) can be applied to left
        if(any(RDisj.canApply(self.getLeftConclusions()))):
            r_Ldisj = RDisj.canApply(self.getLeftConclusions())
            self.__children = RDisj.stepLeft(
                self, self.getLeftConclusions()[
                    r_Ldisj.index(True)])
            self.__rule = RDisj.interpolate
            self.__side = True

        # disjunction right rule (conclusions) can be applied to right
        elif(any(RDisj.canApply(self.getRightConclusions()))):
            r_Rdisj = RDisj.canApply(self.getRightConclusions())
            self.__children = RDisj.stepRight(
                self, self.getRightConclusions()[
                    r_Rdisj.index(True)])
            self.__rule = RDisj.interpolate
            self.__side = False

        elif(any(RImpl.canApply(self.getLeftConclusions()))):
            r_Limpl = RImpl.canApply(self.getLeftConclusions())
            self.__children = RImpl.stepLeft(
                self, self.getLeftConclusions()[
                    r_Limpl.index(True)])
            self.__rule = RImpl.interpolate
            self.__side = True

        elif(any(RImpl.canApply(self.getRightConclusions()))):
            r_Rimpl = RImpl.canApply(self.getRightConclusions())
            self.__children = RImpl.stepRight(
                self, self.getRightConclusions()[
                    r_Rimpl.index(True)])
            self.__rule = RImpl.interpolate
            self.__side = False

        elif(any(RNeg.canApply(self.getLeftConclusions()))):
            r_Lneg = RNeg.canApply(self.getLeftConclusions())
            self.__children = RNeg.stepLeft(
                self, self.getLeftConclusions()[
                    r_Lneg.index(True)])
            self.__rule = RNeg.interpolate
            self.__side = True

        elif(any(RNeg.canApply(self.getRightConclusions()))):
            r_Rneg = RNeg.canApply(self.getRightConclusions())
            self.__children = RNeg.stepRight(
                self, self.getRightConclusions()[
                    r_Rneg.index(True)])
            self.__rule = RNeg.interpolate
            self.__side = False

        # left rules who create only one children

        elif(any(LConj.canApply(self.getLeftPremises()))):
            l_Lconjs = LConj.canApply(self.getLeftPremises())
            self.__children = LConj.stepLeft(
                self, self.getLeftPremises()[
                    l_Lconjs.index(True)])
            self.__rule = LConj.interpolate
            self.__side = True

        elif(any(LConj.canApply(self.getRightPremises()))):
            l_Rconjs = LConj.canApply(self.getRightPremises())
            self.__children = LConj.stepRight(
                self, self.getRightPremises()[
                    l_Rconjs.index(True)])
            self.__rule = LConj.interpolate
            self.__side = False

        elif(any(LNeg.canApply(self.getLeftPremises()))):
            l_Lneg = LNeg.canApply(self.getLeftPremises())
            self.__children = LNeg.stepLeft(
                self, self.getLeftPremises()[
                    l_Lneg.index(True)])
            self.__rule = LNeg.interpolate
            self.__side = True

        elif(any(LNeg.canApply(self.getRightPremises()))):
            l_Rneg = LNeg.canApply(self.getRightPremises())
            self.__children = LNeg.stepRight(
                self, self.getRightPremises()[
                    l_Rneg.index(True)])
            self.__rule = LNeg.interpolate
            self.__side = False

        # right rules which produce two childrens
        # conjunction right rule (conclusions) can be applied to left part
        # (before semicolon)
        elif(any(RConj.canApply(self.getLeftConclusions()))):
            r_Lconjs = RConj.canApply(self.getLeftConclusions())
            self.__children = RConj.stepLeft(
                self, self.getLeftConclusions()[
                    r_Lconjs.index(True)])
            self.__rule = RConj.interpolate
            self.__side = True

        # conjunction right rule (conclusions) can be applied to right (after
        # semicolon)
        elif(any(RConj.canApply(self.getRightConclusions()))):
            r_Rconjs = RConj.canApply(self.getRightConclusions())
            self.__children = RConj.stepRight(
                self, self.getRightConclusions()[
                    r_Rconjs.index(True)])
            self.__rule = RConj.interpolate
            self.__side = False

        # left rules which produce two childrens
        elif(any(LDisj.canApply(self.getLeftPremises()))):
            l_Ldisj = LDisj.canApply(self.getLeftPremises())
            self.__children = LDisj.stepLeft(
                self, self.getLeftPremises()[
                    l_Ldisj.index(True)])
            self.__rule = LDisj.interpolate
            self.__side = True

        elif(any(LDisj.canApply(self.getRightPremises()))):
            l_Rdisj = LDisj.canApply(self.getRightPremises())
            self.__children = LDisj.stepRight(
                self, self.getRightPremises()[
                    l_Rdisj.index(True)])
            self.__rule = LDisj.interpolate
            self.__side = False

        elif(any(LImpl.canApply(self.getLeftPremises()))):
            l_Limpl = LImpl.canApply(self.getLeftPremises())
            self.__children = LImpl.stepLeft(
                self, self.getLeftPremises()[
                    l_Limpl.index(True)])
            self.__rule = LImpl.interpolate
            self.__side = True

        elif(any(LImpl.canApply(self.getRightPremises()))):
            l_Rimpl = LImpl.canApply(self.getRightPremises())
            self.__children = LImpl.stepRight(
                self, self.getRightPremises()[
                    l_Rimpl.index(True)])
            self.__rule = LImpl.interpolate
            self.__side = False

        # modality rule can be applied
        elif(LMod.canApply(self.getPremises(), self.getConclusions())):
            self.__children, self.__modsymbol = LMod.step(
                self, self.getLeftConclusions(), self.getRightConclusions())
            self.__rule = LMod.interpolate
            self.__side = True

        # semicolon rule can be applied
        elif (Semicolon.canApply(self.getPremises(), self.getConclusions())):
            self.__children = Semicolon.step(
                self, self.getLeftConclusions(), self.getRightConclusions())
            self.__rule = Semicolon.interpolate
            self.__side = True

        elif (UnionL.canApply(self.getPremises(), self.getConclusions())):
            self.__children = UnionL.step(
                self, self.getLeftConclusions(), self.getRightConclusions())
            self.__rule = UnionL.interpolate
            self.__side = True

        elif (UnionR.canApply(self.getPremises(), self.getConclusions())):
            self.__children = UnionR.step(
                self, self.getLeftConclusions(), self.getRightConclusions())
            self.__rule = UnionR.interpolate
            self.__side = True

        # weakening rule can be applied
        elif (Weak.canApply(self.getPremises(), self.getConclusions())):
            self.__children = Weak.step(
                self, self.getLeftConclusions(), self.getRightConclusions())
            self.__rule = Weak.interpolate
            self.__side = True

        if self.__children is None:
            print("NOT provable1:" + self.toString())
            return False



        if len(self.__children) > 0:
            for child in self.__children:
                if not child.solve():
                    print("NOT provable2:" + self.toString())
                    return False
            return True

        if len(self.__children)==1:
            if self.toString()==self.__children[0].toString():
                return False


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

        self.__lPremises = premiseR
        self.__rPremises = premiseL
        return self

    def setConclusions(self, conclusionL, conclusionR):

        self.__lConclusions = conclusionR
        self.__rConclusions = conclusionL
        return self

    def addPremL(self, new):
        self.__lPremises.append(new)

    def addPremR(self, new):
        self.__rPremises.append(new)

    def addConcL(self, new):
        self.__lConclusions.append(new)

    def addConcR(self, new):
        self.__rConclusions.append(new)

    @staticmethod
    def copyEntailment(entailment):

        cLeftPremises = copy.copy(entailment.getLeftPremises())
        cRightPremises = copy.copy(entailment.getRightPremises())
        cLeftConcl = copy.copy(entailment.getLeftConclusions())
        cRightConcl = copy.copy(entailment.getRightConclusions())

        return Entailment(
            cLeftPremises,
            cRightPremises,
            cLeftConcl,
            cRightConcl)

    def toString(self):

        a = ""
        b = ""
        c = ""
        d = ""

        len1 = len(self.getLeftPremises())
        for premise in self.getLeftPremises():

            if len1 > 1:
                a += str(premise.toString()) + ", "
            elif len1 == 1:

                a += str(premise.toString())
            len1 -= 1

        len2 = len(self.getRightPremises())
        for premise in self.getRightPremises():

            if len2 > 1:
                c += str(premise.toString()) + ", "
            elif len2 == 1:
                c += str(premise.toString())
            len2 -= 1

        len3 = len(self.getLeftConclusions())
        for conclusion in self.getLeftConclusions():

            if len3 > 1:
                b += str(conclusion.toString()) + ", "
            elif len3 == 1:
                b += str(conclusion.toString())
            len3 -= 1

        len4 = len(self.getRightConclusions())
        for conclusion in self.getRightConclusions():
            if len4 > 1:
                d += str(conclusion.toString()) + ", "
            elif len4 == 1:
                d += str(conclusion.toString())
            len4 -= 1

        return (a + " ; " + c + " |- " + b + " ; " + d)

    def isAxiom(self):

        entailment = self.toString()

        new = entailment.replace("|-", "")
        string = "~^|>"

        if any(elem in new for elem in string):

            if len(self.getConclusions()) >= 1 and len(self.getPremises()) > 0:
                for item in self.getConclusions():
                    if "True" in item.toString():
                        return True

            elif len(self.getPremises()) >= 1 and len(self.getConclusions()) > 0:
                for item in self.getPremises():
                    if "False"in item.toString():
                        return True

            else:
                return False

        if len(self.__children) == 0 or self.__children is None:

            for conclusion in self.getConclusions():
                for premise in self.getPremises():
                    if premise.toString() == conclusion.toString():
                        return True

        if len(self.getConclusions()) >= 1 and len(self.getPremises()) > 0:
            for item in self.getConclusions():
                if "True" in item.toString():
                    return True

        if len(self.getPremises()) >= 1 and len(self.getConclusions()) > 0:
            for item in self.getPremises():
                if "False" in item.toString():
                    return True

        if len(self.__children) > 0:
            return False

    def axiomInterpolant(self):

        interpolants = None

        for premise in self.getLeftPremises():
            for conclusion in self.getLeftConclusions():

                if premise.toString() == conclusion.toString():

                    interpolants = premise

                    self.__latex = r"\AxiomC{$" + \
                        self.convertSymbols(interpolants) + "$}\n"

                    print("")
                    print("Axiom  " + self.toString() + " ")
                    print(interpolants.toString())
                    print(" ")

                    return interpolants

        for premise in self.getRightPremises():
            for conclusion in self.getRightConclusions():

                if premise.toString() == conclusion.toString():

                    interpolants = op.Not(premise)

                    self.__latex = r"\AxiomC{$" + \
                        self.convertSymbols(interpolants) + "$}\n"

                    print("")
                    print("Axiom  " + self.toString() + " ")
                    print(interpolants.toString())
                    print(" ")

                    return interpolants

        for premise in self.getLeftPremises():
            for conclusion in self.getRightConclusions():

                if premise.toString() == conclusion.toString():

                    interpolants = basics.Atom("False")
                    interpolants.setValue(False)

                    self.__latex += r"\AxiomC{$" + \
                        self.convertSymbols(interpolants) + "$}\n"

                    print("")
                    print("Axiom :" + self.toString())
                    print(interpolants.toString())
                    print("")

                    return interpolants

        for premise in self.getRightPremises():

            for conclusion in self.getLeftConclusions():

                if premise.toString() == conclusion.toString():

                    interpolants = basics.Atom("True")
                    interpolants.setValue(True)

                    self.__latex += r"\AxiomC{$" + \
                        self.convertSymbols(interpolants) + "$}" + "\n"

                    print("")
                    print("Axiom :" + self.toString())
                    print(interpolants.toString())
                    print("")

                    return interpolants

        for itemRC in self.getRightConclusions():

            if "True" in itemRC.toString() and len(self.getPremises()) > 0:

                interpolants = basics.Atom("False")
                interpolants.setValue(False)

                self.__latex += r"\AxiomC{$" + \
                    self.convertSymbols(interpolants) + "$}" + "\n"

                print("")
                print("Axiom :" + self.toString())
                print(interpolants.toString())
                print("")

                return interpolants

        for itemLC in self.getLeftConclusions():

            if "True" in itemLC.toString() and len(self.getPremises()) > 0:

                interpolants = basics.Atom("True")
                interpolants.setValue(True)

                self.__latex += r"\AxiomC{$" + \
                    self.convertSymbols(interpolants) + "$}" + "\n"

                print("")
                print("Axiom :" + self.toString())
                print(interpolants.toString())
                print("")

                return interpolants

        for itemRP in self.getRightPremises():

            if ("False" in itemRP.toString()) and len(
                    self.getConclusions()) > 0:
                interpolants = basics.Atom("True")
                interpolants.setValue(True)

                self.__latex += r"\AxiomC{$" + \
                    self.convertSymbols(interpolants) + "$}\n"

                print("")
                print("Axiom :" + self.toString())
                print(interpolants.toString())
                print("")

                return interpolants

        for itemLP in self.getLeftPremises():

            if ("False" in itemLP.toString()) and len(
                    self.getConclusions()) > 0:
                interpolants = basics.Atom("False")
                interpolants.setValue(False)

                self.__latex += r"\AxiomC{$" + \
                    self.convertSymbols(interpolants) + "$}\n"

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

        print("Interpolants for " + self.toString() + " with rule " +
              str(self.__rule) + "and side " + str(self.__side) + ":")
        print("len:" + str(len(self.__children)))

        if (len(self.__children)) == 1:

            if(self.__rule.__qualname__[:-12] == "LMod"):
                self.__latex += r"\RightLabel{$ Mod " + \
                    self.__modsymbol + "$}" + "\n"
                self.__latex += r"\UnaryInfC{$" + self.convertSymbols(
                    self.__rule(interpolants, self.__side, self.__modsymbol)) + "$}" + "\n"

            elif(self.__rule.__qualname__[:-12] == "Weak"):
                self.__latex += r"\RightLabel{$ Weakening $}" + "\n"
                self.__latex += r"\UnaryInfC{$" + self.convertSymbols(
                    self.__rule(interpolants, self.__side, self.__modsymbol)) + "$}" + "\n"

            elif(self.__rule.__qualname__[:-12] == "Semicolon"):
                self.__latex += r"\RightLabel{$ ; $}" + "\n"
                self.__latex += r"\UnaryInfC{$" + self.convertSymbols(
                    self.__rule(interpolants, self.__side, self.__modsymbol)) + "$}" + "\n"

            elif(self.__rule.__qualname__[:-12] == "UnionL"):
                self.__latex += r"\RightLabel{$ \cup L$}" + "\n"
                self.__latex += r"\UnaryInfC{$" + self.convertSymbols(
                    self.__rule(interpolants, self.__side, self.__modsymbol)) + "$}" + "\n"

            else:
                self.__latex += r"\RightLabel{$" + \
                    self.convertRule(self.__side) + "$}" + "\n"
                self.__latex += r"\UnaryInfC{$" + self.convertSymbols(
                    self.__rule(interpolants, self.__side)) + "$}" + "\n"

        if (len(self.__children)) == 2:

            if(self.__rule.__qualname__[:-12] == "UnionR"):
                self.__latex += r"\RightLabel{$ \cup R$}" + "\n"
                self.__latex += r"\BinaryInfC{$" + self.convertSymbols(
                    self.__rule(interpolants, self.__side, self.__modsymbol)) + "$}" + "\n"
                print(
                    self.__rule(
                        interpolants,
                        self.__side,
                        self.__modsymbol).toString())
                print(" ")

            else:
                self.__latex += r"\RightLabel{$" + \
                    self.convertRule(self.__side) + "$}" + "\n"
                self.__latex += r"\BinaryInfC{$" + self.convertSymbols(
                    self.__rule(interpolants, self.__side)) + "$}" + "\n"

                print(self.__rule(interpolants, self.__side).toString())

        if((self.__rule.__qualname__[:-12] == "LMod") | (self.__rule.__qualname__[:-12] == "Weak") | (self.__rule.__qualname__[:-12] == "Semicolon") | (self.__rule.__qualname__[:-12] == "UnionL") | (self.__rule.__qualname__[:-12] == "UnionR")):
            print(
                self.__rule(
                    interpolants,
                    self.__side,
                    self.__modsymbol).toString())
            print(" ")
            return self.__rule(interpolants, self.__side, self.__modsymbol)
        else:
            print(self.__rule(interpolants, self.__side).toString())

        print(" ")

        return self.__rule(interpolants, self.__side)

    @staticmethod
    def checkInterpolant(phi, psi, interpolant):

        entailment1 = Entailment([phi], [], [interpolant], [])
        entailment2 = Entailment([interpolant], [], [psi], [])

        print("entailment 1:" + entailment1.toString())
        e1 = bool(entailment1.solve())

        print(" ")

        print("entailment 2:" + entailment2.toString())
        e2 = bool(entailment2.solve())

        print("entailment 1 is a tautology:" + str(e1))
        print("entailment 2 is a tautology:" + str(e2))

        if e1 and e2:
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
            if not any([atom.getSymbol() == a.getSymbol() for a in allAtoms]):
                return False

        return True

    def convertSymbols(self, interpolant):

        interpolantStr = interpolant.toString()

        newS = self.toString()

        newS = newS.replace(
            r"|-", r"\overset{" + interpolantStr + r"}{\vdash}")
        newS = newS.replace(pars.DISJ_SYMBOL, r"\lor")
        newS = newS.replace("U", r"\cup")
        newS = newS.replace(pars.CONJ_SYMBOL, r"\land")
        newS = newS.replace(pars.IMPL_SYMBOL, r"\rightarrow")
        newS = newS.replace(pars.NOT_SYMBOL, r"\neg")
        newS = newS.replace(r"True", r"\top")
        newS = newS.replace(r"False", r"\bot")

        return newS

    def convertRule(self, side):

        name = self.__rule.__qualname__

        name = name[:-12]

        if side:

            name = name.replace("Impl", r"\rightarrow_{+}")
            name = name.replace("Neg", r"\neg_{+}")
            name = name.replace("Conj", r"\land_{+}")
            name = name.replace("Disj", r"\lor_{+}")

        elif side == False:

            name = name.replace("Impl", r"\rightarrow_{-}")
            name = name.replace("Neg", r"\neg_{-}")
            name = name.replace("Conj", r"\land_{-}")
            name = name.replace("Disj", r"\lor_{-}")

        return name

    def latexProof(self):

        result = ""
        for child in self.__children:
            result = result + "\n" + child.latexProof()

        return result + self.__latex

    def latexProofAux(self):
        theLaTeXproof = self.latexProof()
        with open("proof.tex", "w") as myfile:
            myfile.write(
                "\\documentclass[border=10pt,varwidth=200cm]{standalone}\n"
                "\\usepackage{bussproofs}\n"
                "\\usepackage{amsmath}\n"
                "\\begin{document}\n"
                "\\begin{prooftree}\n")
            myfile.write(theLaTeXproof)
            myfile.write("\\end{prooftree}\n"
                         "\\end{document}\n")
        subprocess.run(["pdflatex", "-interaction=nonstopmode", "proof.tex"])
        if platform.startswith('darwin'):
            subprocess.run(["open", "proof.pdf"])
        elif platform.startswith('linux'):
            subprocess.run(["xdg-open", "proof.pdf"])


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

    # rule for computing interpolant for R-L rule
    @staticmethod
    def interpolate(interpolant, c):
        pass


class RConj(RRule):

    @staticmethod
    def canApply(conclusions):
        return ([conclusion.getSymbol() ==
                 pars.CONJ_SYMBOL for conclusion in conclusions])

    @staticmethod
    def stepLeft(entailment, conclusion):

        left = Entailment.copyEntailment(entailment)
        right = Entailment.copyEntailment(entailment)

        left.getLeftConclusions().remove(conclusion)
        right.getLeftConclusions().remove(conclusion)

        left.getLeftConclusions().append(conclusion.getOperandLeft())
        right.getLeftConclusions().append(conclusion.getOperandRight())

        if (not left.solve() or not right.solve()):
            return None

        return [left, right]

    def stepRight(entailment, conclusion):

        left = Entailment.copyEntailment(entailment)
        right = Entailment.copyEntailment(entailment)

        left.getRightConclusions().remove(conclusion)
        right.getRightConclusions().remove(conclusion)

        left.getRightConclusions().append(conclusion.getOperandLeft())
        right.getRightConclusions().append(conclusion.getOperandRight())

        if (not left.solve() or not right.solve()):
            return None

        return [left, right]

    # interpolant rule if RConj is on the left of semicolon(f-)
    # interpolant is the disjunction of the interpolant of the two subfromulas
    # interpolant rule if RConj is on the right of semicolon(f+)
    # interpolant is the conjunction of the interpolant of the two subfromulas
    def interpolate(interpolant, c):

        if c:
            return op.Conj(interpolant[0], interpolant[1])
        else:
            return op.Disj(interpolant[0], interpolant[1])


class RDisj(RRule):

    @staticmethod
    def canApply(conclusions):
        return ([conclusion.getSymbol() ==
                 pars.DISJ_SYMBOL for conclusion in conclusions])

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

        new.getRightConclusions().remove(conclusion)

        new.getRightConclusions().append(conclusion.getOperandLeft())
        new.getRightConclusions().append(conclusion.getOperandRight())

        if not new.solve():
            return None

        return [new]

    # interpolant rule if RDisj is on the left of semicolon(f-)
    #interpolant is not changed
    # interpolant rule if RDisj is on the right of semicolon(f+)
    #interpolant is not changed
    def interpolate(interpolant, c):
        return interpolant[0]


class RImpl(RRule):

    @staticmethod
    def canApply(conclusions):
        return ([conclusion.getSymbol() ==
                 pars.IMPL_SYMBOL for conclusion in conclusions])

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

    # interpolant rule if RImpl is on the left of semicolon(f-)
    #interpolant is not changed
    # interpolant rule if RImpl is on the right of semicolon(f+)
    #interpolant is not changed
    def interpolate(interpolant, c):
        return interpolant[0]


class RNeg(RRule):

    @staticmethod
    def canApply(conclusions):
        return ([conclusion.getSymbol() ==
                 pars.NOT_SYMBOL for conclusion in conclusions])

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

    # interpolant rule if RNeg is on the left of semicolon(f-)
    #interpolant is not changed
    # interpolant rule if RNeg is on the right of semicolon(f+)
    #interpolant is not changed
    def interpolate(interpolant, c):
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

    # rule for computing interpolant for L-L rule
    @staticmethod
    def interpolate(interpolant, c):
        pass


class LConj(LRule):

    @staticmethod
    def canApply(premises):

        return[premise.getSymbol() == pars.CONJ_SYMBOL for premise in premises]

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

    # interpolant rule if LConj is on the left of semicolon(f-)
    #interpolant is not changed
    # interpolant rule if LConj is on the right of semicolon(f+)
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
            return None

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
            return None

        return [left, right]

    # interpolant rule if LDisj is on the left of semicolon(f-)
    # interpolant is the disjunction of the interpolant of the two subfromulas
    # interpolant rule if LDisj is on the right of semicolon(f+)
    # interpolant is the conjunction of the interpolant of the two subfromulas
    def interpolate(interpolant, c):

        if c:
            return op.Disj(interpolant[0], interpolant[1])
        else:
            return op.Conj(interpolant[0], interpolant[1])


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
        left.setConclusions(
            left.getLeftConclusions(),
            left.getRightConclusions())

        right.getLeftPremises().append(premise.getOperandRight())
        left.getLeftConclusions().append(premise.getOperandLeft())

        if (not left.solve() or not right.solve()):
            return None

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
            return None

        return [left, right]

    # interpolant rule if LImpl is on the left of semicolon(f-)
    # interpolant is the implication of the interpolant of the two subfromulas
    # interpolant rule if LImpl is on the right of semicolon(f+)
    # interpolant is the conjunction of the interpolant of the two subfromulas
    def interpolate(interpolant, c):

        if c:
            return op.Impl(interpolant[0], interpolant[1])
        else:
            return op.Conj(interpolant[0], interpolant[1])


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

    # interpolant rule if LNeg is on the left of semicolon(f-)
    # interpolant is the negation of the interpolant of the subfromula
    # interpolant rule if LNeg is on the right of semicolon(f+)

    #interpolant is not change
    def interpolate(interpolant, c=True):

        if c:
            return op.Not(interpolant[0])
        else:
            return interpolant[0]


class MRule:

    @staticmethod
    def canApply(premises, conclusions):
        pass

    @staticmethod
    def step(entailment, lC, rC):
        pass

    # rule for computing interpolant for box rule, adds a box(with appropriate
    # symbol) to interpolant
    @staticmethod
    def interpolate(interpolant, c, symbol):
        pass


class LMod(MRule):

    @staticmethod
    def canApply(premises, conclusions):

        if len(conclusions) > 1:
            return False

        elif len(conclusions) == 1 and not isinstance(conclusions[0], op.Mod):
            return False

        elif (len(conclusions) == 1 and isinstance(conclusions[0], op.Mod)):

            symbolConc = conclusions[0].getSymbol()
            newsymbolConc = symbolConc.replace(" ", "")

            if len(premises) == 0:
                return False

            for premise in premises:

                newmod = premise.getSymbol()
                newmodSymbol = newmod.replace(" ", "")

                if not (isinstance(premise, op.Mod)
                        ) or newmodSymbol != newsymbolConc:

                    return False

        elif(len(conclusions) == 0):

            if len(premises) > 1:
                symbol = premises[0].getSymbol()
                symbol.replace(" ", "")

                for premise in premises:

                    newmod = premise.getSymbol()
                    newmod.replace(" ", "")

                    if not (isinstance(premise, op.Mod)) or newmod != symbol:
                        return False

            else:
                if len(premises) == 1 and isinstance(premises[0], op.Mod):
                    return True
                else:
                    return False

        return True

    @staticmethod
    def step(entailment, lC, rC):

        new = Entailment.copyEntailment(entailment)

        gotConcl = True
        index = 0

        if len(rC) == 1 and isinstance(rC[0], op.Mod) and len(lC) < 1:
            symbol = new.getRightConclusions()[0].getSymbol()
            conclusion = entailment.getRightConclusions()[0]

            new.getRightConclusions().remove(conclusion)
            new.addConcR(conclusion.getOperand())

        elif len(lC) == 1 and isinstance(lC[0], op.Mod) and len(rC) < 1:
            symbol = new.getLeftConclusions()[0].getSymbol()

            conclusion = entailment.getLeftConclusions()[0]

            new.getLeftConclusions().remove(conclusion)
            new.addConcL(conclusion.getOperand())

        else:
            gotConcl = False

            symbol = new.getPremises()[0].getSymbol()
            while index < len(new.getRightPremises()):
                new.getRightPremises()[index] = new.getRightPremises()[
                    index].getOperand()
                index += 1

            index = 0
            while index < len(new.getLeftPremises()):
                new.getLeftPremises()[index] = new.getLeftPremises()[
                    index].getOperand()
                index += 1

        if gotConcl:

            while index < len(new.getRightPremises()):
                new.getRightPremises()[index] = new.getRightPremises()[
                    index].getOperand()
                index += 1

            index = 0
            while index < len(new.getLeftPremises()):
                new.getLeftPremises()[index] = new.getLeftPremises()[
                    index].getOperand()
                index += 1

        if not new.solve():
            return None, None

        return [new], symbol

    # interpolant rule if Modality rule applied, modality added to interpolant

    def interpolate(interpolant, c, symbol):

        if ("True" in interpolant[0].toString()) or (
                "False" in interpolant[0].toString()):

            return interpolant[0]

        symbol = symbol.replace("[", "")
        symbol = symbol.replace("]", "")
        return op.Mod(interpolant[0], symbol)


class Weak(MRule):

    @staticmethod
    def canApply(premises, conclusions):

        atomsPrem = []
        atomsConcl = []

        for premise in premises:

            for atom in premise.getAtoms():

                if ("True" in atom.toString()) or ("False" in atom.toString()):
                    return True
                else:
                    atomsPrem.append(atom)

        for conclusion in conclusions:

            for atom in conclusion.getAtoms():

                if ("True" in atom.toString()) or ("False" in atom.toString()):
                    return True
                else:
                    atomsConcl.append(atom)

        # this is an heuristic. If there are no common atoms in the premises and
        # conlusions weakening will not lead to finding a solution. Therefore rule
        # is not applied
        if (bool(set(atomsPrem).intersection(atomsConcl))):
            return True
        else:
            return False

        return ((premises != []) | (conclusions != []))

    @staticmethod
    def step(entailment, lC, rC):

        possibleWeakenings = []

        ent = entailment.getPremises() + entailment.getConclusions()

        for toEliminate in F.getAllCombs(ent):
            new = entailment.copyEntailment(entailment)

            for primitive in toEliminate:

                if primitive in new.getLeftConclusions():
                    new.getLeftConclusions().remove(primitive)
                elif primitive in new.getRightConclusions():
                    new.getRightConclusions().remove(primitive)
                elif primitive in new.getLeftPremises():
                    new.getLeftPremises().remove(primitive)
                elif primitive in new.getRightPremises():
                    new.getRightPremises().remove(primitive)

            Lrules = [LConj, LDisj, LNeg, LImpl]
            Rrules = [RNeg, RImpl, RConj, RDisj]
            Prules = [LMod, Semicolon, UnionL, UnionR]

            for rule in Prules:
                if rule.canApply(new.getPremises(), new.getConclusions()):
                    if new.solve():
                        return [new]

            for rule in Lrules:
                if rule.canApply(
                        new.getRightPremises()) or rule.canApply(
                        new.getLeftPremises()):
                    if new.solve():
                        return [new]

            for rule in Rrules:
                if rule.canApply(
                        new.getRightConclusions()) or rule.canApply(
                        new.getLeftConclusions()):
                    if new.solve():
                        return [new]

        return None

    # interpolant rule if weakening interpolant is not changed
    def interpolate(interpolant, c, self):
        return interpolant[0]


class Semicolon(MRule):

    @staticmethod
    def canApply(premises, conclusions):

        for conclusion in premises + conclusions:

            if isinstance(conclusion, op.Mod):

                new = conclusion.getSymbol()
                new = new[1:-1]

                if new.startswith('(') and new.endswith(')'):

                    new = new[1:-1]

                semicolon = [
                    semicolon for semicolon,
                    x in enumerate(new) if x == ";"]
                union = [union for union, x in enumerate(new) if x == "U"]

                semicolonMin = 100
                unionMin = 100

                for index in semicolon:

                    new1 = list(new)
                    list1a = new1[:int(index) - 1]
                    list1b = new1[int(index) + 2:]

                    str1 = ''.join(list1a)
                    str2 = ''.join(list1b)

                    sub1 = "("
                    sub2 = ")"

                    countOpenSemi = list1a.count(sub1)
                    countCloseSemi = list1a.count(sub2)

                    countSemi = countOpenSemi - countCloseSemi

                    if countSemi < semicolonMin:

                        semicolonMin = countSemi

                for index in union:

                    new1 = list(new)
                    list1a = new1[:int(index) - 1]
                    list1b = new1[int(index) + 2:]

                    str1 = ''.join(list1a)
                    str2 = ''.join(list1b)

                    sub1 = "("
                    sub2 = ")"

                    countOpenUnion = list1a.count(sub1)
                    countCloseUnion = list1a.count(sub2)

                    countUnion = countOpenUnion - countCloseUnion

                    if countUnion <= unionMin:

                        unionMin = countUnion

                if (semicolonMin < unionMin):
                    return True

        return False

    @staticmethod
    def step(entailment, lC, rC):

        new = entailment.copyEntailment(entailment)

        for item in entailment.getPremises() + entailment.getConclusions():

            if isinstance(item, op.Mod):

                newSymb = item.getSymbol()
                newSymb = newSymb[1:-1]

                if newSymb.startswith('(') and newSymb.endswith(')'):

                    newSymb = newSymb[1:-1]

                semicolon = [
                    semicolon for semicolon,
                    x in enumerate(newSymb) if x == ";"]
                union = [union for union, x in enumerate(newSymb) if x == "U"]

                semicolonMin = 100
                unionMin = 100
                indexMin = 100

                for index in semicolon:

                    new1 = list(newSymb)
                    list1a = new1[:int(index) - 1]
                    list1b = new1[int(index) + 2:]

                    str1 = ''.join(list1a)
                    str2 = ''.join(list1b)

                    sub1 = "("
                    sub2 = ")"

                    countOpenSemi = list1a.count(sub1)
                    countCloseSemi = list1a.count(sub2)

                    countSemi = countOpenSemi - countCloseSemi

                    if countSemi < semicolonMin:

                        indexMin = index

                        semicolonMin = countSemi

                for index in union:

                    new1 = list(newSymb)
                    list1a = new1[:int(index) - 1]
                    list1b = new1[int(index) + 2:]

                    str1 = ''.join(list1a)
                    str2 = ''.join(list1b)

                    sub1 = "("
                    sub2 = ")"

                    countOpenUnion = list1a.count(sub1)
                    countCloseUnion = list1a.count(sub2)

                    countUnion = countOpenUnion - countCloseUnion

                    if countUnion <= unionMin:

                        unionMin = countUnion

                if semicolonMin < unionMin:

                    listA = new1[:int(indexMin) - 1]
                    listB = new1[int(indexMin) + 2:]

                    strFin1 = ''.join(listA)
                    strFin2 = ''.join(listB)

                    if item in entailment.getPremises():

                        if item in entailment.getLeftPremises():

                            new.getLeftPremises().remove(item)
                            new.addPremL(
                                op.Mod(
                                    op.Mod(
                                        item.getOperand(),
                                        strFin2),
                                    strFin1))
                            return [new]
                        else:
                            new.getRightPremises().remove(item)
                            new.addPremR(
                                op.Mod(
                                    op.Mod(
                                        item.getOperand(),
                                        strFin2),
                                    strFin1))
                            return [new]

                    elif item in entailment.getConclusions():

                        if item in entailment.getLeftConclusions():
                            new.getLeftConclusions().remove(item)
                            new.addConcL(
                                op.Mod(
                                    op.Mod(
                                        item.getOperand(),
                                        strFin2),
                                    strFin1))
                            return [new]
                        else:
                            new.getRightConclusions().remove(item)
                            new.addConcR(
                                op.Mod(
                                    op.Mod(
                                        item.getOperand(),
                                        strFin2),
                                    strFin1))
                            return [new]

        if not new.solve():
            return None

    # interpolant does not change the Semicolon rule just rewrites the formula
    # in a different fromat
    def interpolate(interpolant, c, self):
        return interpolant[0]


class UnionL(MRule):

    @staticmethod
    def canApply(premises, conclusions):

        for premise in premises:

            if isinstance(premise, op.Mod):

                new = premise.getSymbol()
                new = new[1:-1]

                if new.startswith('(') and new.endswith(')'):

                    new = new[1:-1]

                semicolon = [
                    semicolon for semicolon,
                    x in enumerate(new) if x == ";"]
                union = [union for union, x in enumerate(new) if x == "U"]

                semicolonMin = 100
                unionMin = 100

                for index in semicolon:

                    new1 = list(new)
                    list1a = new1[:int(index) - 1]
                    list1b = new1[int(index) + 2:]

                    str1 = ''.join(list1a)
                    str2 = ''.join(list1b)

                    sub1 = "("
                    sub2 = ")"

                    countOpenSemi = list1a.count(sub1)
                    countCloseSemi = list1a.count(sub2)

                    countSemi = countOpenSemi - countCloseSemi

                    if countSemi < semicolonMin:

                        semicolonMin = countSemi

                for index in union:

                    new1 = list(new)
                    list1a = new1[:int(index) - 1]
                    list1b = new1[int(index) + 2:]

                    str1 = ''.join(list1a)
                    str2 = ''.join(list1b)

                    sub1 = "("
                    sub2 = ")"

                    countOpenUnion = list1a.count(sub1)
                    countCloseUnion = list1a.count(sub2)

                    countUnion = countOpenUnion - countCloseUnion

                    if countUnion <= unionMin:

                        unionMin = countUnion

                if (unionMin < semicolonMin):
                    return True

        return False

    @staticmethod
    def step(entailment, lC, rC):

        new = entailment.copyEntailment(entailment)

        for item in entailment.getPremises():

            if isinstance(item, op.Mod):

                newSymb = item.getSymbol()
                newSymb = newSymb[1:-1]

                if newSymb.startswith('(') and newSymb.endswith(')'):

                    newSymb = newSymb[1:-1]

                semicolon = [
                    semicolon for semicolon,
                    x in enumerate(newSymb) if x == ";"]
                union = [union for union, x in enumerate(newSymb) if x == "U"]

                semicolonMin = 100
                unionMin = 100
                indexMin = 100

                for index in semicolon:

                    new1 = list(newSymb)
                    list1a = new1[:int(index) - 1]
                    list1b = new1[int(index) + 2:]

                    str1 = ''.join(list1a)
                    str2 = ''.join(list1b)

                    sub1 = "("
                    sub2 = ")"

                    countOpenSemi = list1a.count(sub1)
                    countCloseSemi = list1a.count(sub2)

                    countSemi = countOpenSemi - countCloseSemi

                    if countSemi < semicolonMin:

                        semicolonMin = countSemi

                for index in union:

                    new1 = list(newSymb)
                    list1a = new1[:int(index) - 1]
                    list1b = new1[int(index) + 2:]

                    str1 = ''.join(list1a)
                    str2 = ''.join(list1b)

                    sub1 = "("
                    sub2 = ")"

                    countOpenUnion = list1a.count(sub1)
                    countCloseUnion = list1a.count(sub2)

                    countUnion = countOpenUnion - countCloseUnion

                    if countUnion <= unionMin:

                        indexMin = index

                        unionMin = countUnion

                if unionMin < semicolonMin:

                    listA = new1[:int(indexMin) - 1]
                    listB = new1[int(indexMin) + 2:]

                    strFin1 = ''.join(listA)
                    strFin2 = ''.join(listB)

                    if item in entailment.getLeftPremises():
                        new.getLeftPremises().remove(item)
                        new.addPremL(op.Mod(item.getOperand(), strFin1))
                        new.addPremL(op.Mod(item.getOperand(), strFin2))

                        return[new]

                    else:
                        new.getRightPremises().remove(item)
                        new.addPremR(op.Mod(item.getOperand(), strFin1))
                        new.addPremR(op.Mod(item.getOperand(), strFin2))
                        return[new]

        if not new.solve():
            return None

    # interpolant does not change the Semicolon rule just rewrites the formula
    # in a different fromat

    def interpolate(interpolant, c, self):
        return interpolant[0]


class UnionR(MRule):

    @staticmethod
    def canApply(premises, conclusions):

        for conclusion in conclusions:

            if isinstance(conclusion, op.Mod):

                new = conclusion.getSymbol()
                new = new[1:-1]

                if new.startswith('(') and new.endswith(')'):

                    new = new[1:-1]

                semicolon = [
                    semicolon for semicolon,
                    x in enumerate(new) if x == ";"]
                union = [union for union, x in enumerate(new) if x == "U"]

                semicolonMin = 100
                unionMin = 100

                for index in semicolon:

                    new1 = list(new)
                    list1a = new1[:int(index)]
                    list1b = new1[int(index) + 1:]

                    str1 = ''.join(list1a)
                    str2 = ''.join(list1b)

                    sub1 = "("
                    sub2 = ")"

                    countOpenSemi = list1a.count(sub1)
                    countCloseSemi = list1a.count(sub2)

                    countSemi = countOpenSemi - countCloseSemi

                    if countSemi < semicolonMin:

                        semicolonMin = countSemi

                for index in union:

                    new1 = list(new)
                    list1a = new1[:int(index)]
                    list1b = new1[int(index) + 1:]

                    str1 = ''.join(list1a)
                    str2 = ''.join(list1b)

                    sub1 = "("
                    sub2 = ")"

                    countOpenUnion = list1a.count(sub1)
                    countCloseUnion = list1a.count(sub2)

                    countUnion = countOpenUnion - countCloseUnion

                    if countUnion <= unionMin:

                        unionMin = countUnion

                if (unionMin < semicolonMin):
                    return True

        return False

    @staticmethod
    def step(entailment, lC, rC):

        left = entailment.copyEntailment(entailment)
        right = entailment.copyEntailment(entailment)

        for item in entailment.getConclusions():

            if isinstance(item, op.Mod):

                newSymb = item.getSymbol()
                newSymb = newSymb[1:-1]

                if newSymb.startswith('(') and newSymb.endswith(')'):

                    newSymb = newSymb[1:-1]

                semicolon = [
                    semicolon for semicolon,
                    x in enumerate(newSymb) if x == ";"]
                union = [union for union, x in enumerate(newSymb) if x == "U"]

                semicolonMin = 100
                unionMin = 100
                indexMin = 100

                for index in semicolon:

                    new1 = list(newSymb)
                    list1a = new1[:int(index) - 1]
                    list1b = new1[int(index) + 2:]

                    str1 = ''.join(list1a)
                    str2 = ''.join(list1b)

                    sub1 = "("
                    sub2 = ")"

                    countOpenSemi = list1a.count(sub1)
                    countCloseSemi = list1a.count(sub2)

                    countSemi = countOpenSemi - countCloseSemi

                    if countSemi < semicolonMin:

                        semicolonMin = countSemi

                for index in union:

                    new1 = list(newSymb)
                    list1a = new1[:int(index)]
                    list1b = new1[int(index) + 1:]

                    str1 = ''.join(list1a)
                    str2 = ''.join(list1b)

                    sub1 = "("
                    sub2 = ")"

                    countOpenUnion = list1a.count(sub1)
                    countCloseUnion = list1a.count(sub2)

                    countUnion = countOpenUnion - countCloseUnion

                    if countUnion <= unionMin:
                        indexMin = index

                        unionMin = countUnion

                if unionMin < semicolonMin:

                    listA = new1[:int(indexMin) - 1]
                    listB = new1[int(indexMin) + 2:]

                    strFin1 = ''.join(listA)
                    strFin2 = ''.join(listB)

                    if item in entailment.getConclusions():

                        if item in entailment.getLeftConclusions():
                            left.getLeftConclusions().remove(item)
                            right.getLeftConclusions().remove(item)
                            left.addConcL(op.Mod(item.getOperand(), strFin1))
                            right.addConcL(op.Mod(item.getOperand(), strFin2))

                            return[left, right]
                        else:
                            left.getRightConclusions().remove(item)
                            right.getRightConclusions().remove(item)
                            left.addConcR(op.Mod(item.getOperand(), strFin1))
                            right.addConcR(op.Mod(item.getOperand(), strFin2))

                            return[left, right]

        if (not right.solve() or not left.solve()):
            return None

    # interpolant does not change the Semicolon rule just rewrites the formula
    # in a different fromat
    def interpolate(interpolant, c, self):
        if c:
            return op.Conj(interpolant[0], interpolant[1])
        else:
            return op.Disj(interpolant[0], interpolant[1])
