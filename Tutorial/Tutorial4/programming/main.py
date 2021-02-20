from abc import ABC, abstractmethod

class Expr(ABC): 
    @abstractmethod
    def eval(self):
        pass
    @abstractmethod
    def printPrefix(self):
      pass


class IntLit(Expr):

    def __init__(self, num):
        self.num = int(num)

    def eval(self):
        return self.num

    def print(self):
        print(self.num)
      
    def printPrefix(self):
      return str(self.num)



class FloatLit(Expr):

    def __init__(self, num):
        self.num = float(num)

    def eval(self):
        return self.num

    def print(self):
        print(self.num)

    def printPrefix(self):
      return str(self.num)



class UnExp(Expr):

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
    
    def printPrefix(self):
      return str(self.op) + ". " + self.arg.printPrefix()


class BinExp(Expr):

    def __init__(self, left, op, right):
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

    def printPrefix(self):
      return str(self.op)  + " " + self.left.printPrefix() + " " + self.right.printPrefix()


x = BinExp(UnExp("-", IntLit(4)), "+", BinExp(IntLit(3), "*", IntLit(2)))
print(x.printPrefix())