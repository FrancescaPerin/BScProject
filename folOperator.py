import basics
import pars

# Class for unary operators (modality and negation)


class UnaryOperator(basics.Element):

    def __init__(self, symbol, func, operand):
        super(UnaryOperator, self).__init__(symbol)

        self.__operand = operand
        self.__func = func

    def getOperand(self):
        if self == basics.Atom:
            return self
        return self.__operand

    def setOperand(self, operand):
        self.__operand = operand
        return self

    def getValue(self):
        return self.__func(self.__operand.getValue())

    def getAtoms(self):
        return self.__operand.getAtoms()

    def toString(self):
        if isinstance(self.__operand, bool):
            return self.getSymbol() + "(" + str(self.__operand) + ")"

        return self.getSymbol() + "(" + self.__operand.toString() + ")"

    # Function simplify() given a sentence try to simplify it for instance
    # (p ^ p)-> q is simplified to p -> q

    # Function never called in final version of the code

    def simplify(self):
        selfVal = self.getValue()
        if selfVal is not None:
            atm = basics.Atom(self.toString())
            atm.setValue(selfVal)
            return atm

        self.setOperand(self.getOperand().simplify())
        return self

# Class for binary operators (conjunction, disjunction, implication)


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
        return self.__func(
            self.__operand1.getValue(),
            self.__operand2.getValue())

    def getAtoms(self):

        atoms = []

        atoms += self.__operand1.getAtoms()
        atoms += self.__operand2.getAtoms()

        return atoms

    # Function simplify() given a sentence try to simplify it for instance
    # (p ^ p)-> q is simplified to p -> q

    # Function never called in final version of the code

    def simplify(self):

        selfValue = self.getValue()

        if selfValue is not None:
            return basics.Atom(self.toString()).setValue(selfValue)

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

# Defining conjunction operator


class Conj(Operator):

    def __init__(self, operand1, operand2):

        def OP(a, b):
            if a == False or b == False:
                return False

            return a and b

        super(Conj, self).__init__("^", OP, operand1, operand2)


# Defining disjunction operator
class Disj(Operator):

    def __init__(self, operand1, operand2):

        def OP(a, b):
            if a or b:
                return True

            if a == False and b == False:
                return False

            return None

        super(Disj, self).__init__(pars.DISJ_SYMBOL, OP, operand1, operand2)

# Defining implication operator


class Impl(Operator):

    def __init__(self, operand1, operand2):

        def OP(a, b):
            if a == False or b == True:
                return True

            if a and b == False:
                return False

            return None

        super(Impl, self).__init__(pars.IMPL_SYMBOL, OP, operand1, operand2)

# Defining negation operator


class Not(UnaryOperator):

    def __init__(self, operand):

        def OP(a):

            if a is None:
                return None

            return not a

        super(Not, self).__init__(pars.NOT_SYMBOL, OP, operand)


# Defining modality operator (symbol is a program or complex program )
# Exeption raised because the code should never have to reach that function.
class Mod(UnaryOperator):

    def __init__(self, operand, symbol=""):

        def OP(a):
            try:
                raise NameError('HiThere')
            except NameError:
                print("An exception flew by!")
                raise

            return a

        super(Mod, self).__init__("[" + symbol + "]", OP, operand)
