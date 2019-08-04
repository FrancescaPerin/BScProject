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

    def isTaut(self):
        pass

    def hasAtom(self, atom):
        for selfAtom in self.getAtoms():
            if selfAtom.getSymbol() == atom.getSymbol():
                return True

        return False

    def setAtomBySymbol(self, symbol, value):
        for atom in self.getAtoms():
            if atom.getSymbol() == symbol and atom.getValue() is None:
                atom.setValue(value)

        return self

    def getWorlds(self):
        atoms = self.getAtoms()

        worlds = [[copy.deepcopy(atoms[0]).setValue(True)], [
            copy.deepcopy(atoms[0]).setValue(False)]]
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

    def setValue(self, newVal):
        self.__value = newVal
        return self

    def getAtoms(self):
        return [self]

    def isTaut(self):
        return False

    def toString(self):
        if self.getValue() is None:
            return self.getSymbol()
        else:
            return str(self.getValue())


class UnaryOperator(Element):

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
        if selfVal is not None:
            return Atom(selfVal)

        self.setOperand(self.getOperand().simplify())
        return self


class Operator(Element):

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
        return self.__func(
            self.__operand1.getValue(),
            self.__operand2.getValue())

    def getAtoms(self):

        atoms = []

        atoms += self.__operand1.getAtoms()
        atoms += self.__operand2.getAtoms()

        return atoms

    def simplify(self):

        selfValue = self.getValue()
        if selfValue is not None:
            return Atom(self.toString()).setValue(selfValue)

        self.setOperandRight(self.getOperandRight().simplify())
        self.setOperandLeft(self.getOperandLeft().simplify())

        valOperRight = self.getOperandRight().getValue()
        valOperLeft = self.getOperandLeft().getValue()

        if valOperRight is not None and valOperLeft is None:

            if self.__func(True, valOperRight):
                return self.getOperandLeft()
            else:
                return Not(self.getOperandLeft())

        if valOperRight is None and valOperLeft is not None:

            if self.__func(valOperLeft, True):
                return self.getOperandRight()
            else:
                return Not(self.getOperandRight())

        return self

    def toString(self):
        return "(" + self.__operand1.toString() + " " + \
            self.getSymbol() + " " + self.__operand2.toString() + ")"


class Conj(Operator):

    def __init__(self, operand1, operand2):

        def OP(a, b):
            if a == False or b == False:
                return False

            return a and b

        super(Conj, self).__init__("^", OP, operand1, operand2)


class Disj(Operator):

    def __init__(self, operand1, operand2):

        def OP(a, b):
            if a or b:
                return True

            if a == False and b == False:
                return False

            return None

        super(Disj, self).__init__("v", OP, operand1, operand2)


class Impl(Operator):

    def __init__(self, operand1, operand2):

        def OP(a, b):
            if a == False or b == True:
                return True

            return not a or b

        super(Impl, self).__init__("->", OP, operand1, operand2)


class Not(UnaryOperator):

    def __init__(self, operand):

        def OP(a):

            if a is None:
                return None

            return not a

        super(Not, self).__init__("~", OP, operand)


def atomsIsSubset(phi, psi):
    for atomPhi in phi.getAtoms():
        if atomPhi.getValue() is None and not psi.hasAtom(atomPhi):
            return False
    return True


def interpolateAux(phi, psi):

    if(atomsIsSubset(phi, psi)):
        return phi

    # get p
    for atomPhi in phi.getAtoms():
        if atomPhi.getValue() is None and not psi.hasAtom(atomPhi):
            p = atomPhi
            break

    phiTrue = copy.deepcopy(phi).setAtomBySymbol(p.getSymbol(), True)
    phiFalse = copy.deepcopy(phi).setAtomBySymbol(p.getSymbol(), False)

    return interpolateAux(Disj(phiTrue, phiFalse), psi)


def interpolate(phi, psi):

    if not Impl(phi, psi).isTaut():
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


def main():

    a = Atom("a")
    b = Atom("b")
    c = Atom("c")
    d = Atom("d")

    phi = Conj(Disj(b, Not(b)), Conj(a, d))
    psi = Disj(a, Conj(b, c))

    computeInterpolant(phi, psi)

    print("__________________________________")

    t = Atom("t")
    s = Atom("s")
    q = Atom("q")
    r = Atom("r")

    phi = Disj(q, Conj(r, s))
    psi = Impl(Not(q), Disj(t, s))

    computeInterpolant(phi, psi)

    print("__________________________________")

    p = Atom("p")
    q = Atom("q")
    r = Atom("r")

    phi = Disj(Impl(p, r), Impl(q, r))
    psi = Impl(Conj(p, q), r)

    computeInterpolant(phi, psi)


if __name__ == '__main__':
    main()
