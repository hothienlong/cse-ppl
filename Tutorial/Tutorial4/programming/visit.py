from abc import ABC, abstractmethod

@abstractmethod
class Exp(ABC):
  def accept(self, visitor):
    pass
  
class IntLit(Exp):
  def __init__(self, num):
    self.num = num
  def accept(self, visitor):
    return visitor.visitIntLit(self)

class FloatLit(Exp):
  def __init__(self, num):
    self.num = num
  def accept(self, visitor):
    return visitor.visitFloatLit(self)

class UnExp(Exp):
  def __init__(self, op, arg):
    self.arg = arg
    self.op = op
  def accept(self, visitor):
    return visitor.visitUnExp(self)

class BinExp(Exp):
  def __init__(self, left, op, right):
    self.op = op
    self.left = left
    self.right = right
  def accept(self, visitor):
    return visitor.visitBinaryExp(self)

class Visitor(ABC):
  def visitIntLit(self, intlit): pass
  def visitFloatLit(self, floatlit): pass
  def visitUnExp(self, unexp): pass
  def visitBinaryExp(self, binaryexp): pass
  
class Eval(Visitor):
  def visitIntLit(self, intlit):
    return intlit.num
  def visitFloatLit(self, floatlit):
    return floatlit.num
  def visitUnExp(self, unexp):
    if(unexp.op == '-'):
      return -unexp.arg.accept(Eval())
    elif(unexp.op == '+'):
      return unexp.arg.accept(Eval())
  def visitBinaryExp(self, binaryexp):
    if(binaryexp.op == '+'):
      return binaryexp.left.accept(Eval()) + binaryexp.right.accept(Eval())   #self.visit(binaryexp.right) == binaryexp.right.accept(self)
    elif(binaryexp.op == '-'):
      return binaryexp.left.accept(Eval()) - binaryexp.right.accept(Eval())
    elif(binaryexp.op == '*'):
      return binaryexp.left.accept(Eval()) * binaryexp.right.accept(Eval())
    elif(binaryexp.op == '/'):
      return binaryexp.left.accept(Eval()) / binaryexp.right.accept(Eval())
  
class PrintPrefix(Visitor):
  def visitIntLit(self, intlit):
    return str(intlit.num)
  def visitFloatLit(self, floatlit):
    return str(floatlit.num)
  def visitUnExp(self, unexp):
    return unexp.op + ". " + unexp.arg.accept(PrintPrefix())
  def visitBinaryExp(self, binaryexp):
    return binaryexp.op + " " + binaryexp.left.accept(PrintPrefix()) + " " + binaryexp.right.accept(PrintPrefix())
  
class PrintPostfix(Visitor):
  def visitIntLit(self, intlit):
    return str(intlit.num)
  def visitFloatLit(self, floatlit):
    return str(floatlit.num)
  def visitUnExp(self, unexp):
    return unexp.arg.accept(PrintPostfix()) + " " + unexp.op + "."
  def visitBinaryExp(self, binaryexp):
    return binaryexp.left.accept(PrintPostfix()) + " " + binaryexp.right.accept(PrintPostfix()) + " " + binaryexp.op