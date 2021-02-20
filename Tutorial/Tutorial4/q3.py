from abc import ABC, abstractmethod

class Expr(ABC): 
    @abstractmethod
    def eval(self):
        pass

class Var(Expr):
    
    def __init__(self, name):
        self.name = name

    def eval(self):
        return Number(1)

class Number(Expr):

    def __init__(self, num):
        self.num = num

    def eval(self):
        return self

    def print(self):
        print(self.num)

    def __neg__(self):
        return Number(-self.num)

    def __add__(self, other):
        return Number(self.num + other.num)
    
    def __sub__(self, other):
        return Number(self.num - other.num)

    def __mul__(self, other):
        return Number(self.num * other.num)

    def __floordiv__(self, other):
        return Number(self.num / other.num)

class UnOp(Expr):

    def __init__(self, op, arg):
        self.op = op
        self.arg = arg

    def eval(self):
        if self.op == '-':
            return - self.arg.eval()
        elif self.op == '+':
            return self.arg.eval()
        else:
            raise Exception('Invalid operator:' + self.op)

class BinOp(Expr):

    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def eval(self):
        if self.op == '-':
            return self.left.eval() - self.right.eval()
        elif self.op == '+':
            return self.left.eval() + self.right.eval()
        elif self.op == '*':
            return self.left.eval() * self.right.eval()
        elif self.op == '/':
            return self.left.eval() / self.right.eval()
        else:
            raise Exception('Invalid operator:' + self.op)


