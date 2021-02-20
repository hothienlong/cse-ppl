from abc import ABC, abstractmethod

class Exp(ABC):
    def accept(self,visitor):
        pass

class IntLit(Exp):
    def __init__(self, num):
        self.num = num
    def accept(self,visitor):
        return visitor.visitIntLit(self)

class FloatLit(Exp):
    def __init__(self,num):
        self.num = num
    def accept(self,visitor):
        return visitor.visitFloatLit(self)

class UnExp(Exp):
    def __init__(self, operator, arg):
        self.operator = operator
        self.arg = arg
    def accept(self,visitor):
        return visitor.visitUnExp(self)


class BinExp(Exp):
    def __init__(self,left,operator,right):
        self.operator = operator
        self.left = left
        self.right = right
    def accept(self,visitor):
        return visitor.visitBinExp(self)
    

class Visitor(ABC):
    def visitIntLit(self,obj):
        pass
    def visitFloatLit(self,obj):
        pass
    def visitUnExp(self,obj):
        pass
    def visitBinExp(self,obj):
        pass
class Eval(Visitor):
    def visitIntLit(self,obj):
        return obj.num
    def visitFloatLit(self,obj):
        return obj.num
    def visitUnExp(self,obj):
        op = obj.operator
        arg = obj.arg.accept(Eval())
        if op == '-':
            return -1*arg
        elif op == '+':
            return arg
    def visitBinExp(self,obj):
        left = obj.left.accept(Eval())
        right = obj.right.accept(Eval())
        op = obj.operator
        if op == '+':
            return left + right
        if op == '-':
            return left - right
        if op == '*':
            return left*right
        if op == '/':
            return left/right
class PrintPrefix(Visitor):
    def visitIntLit(self,obj):
        return str(obj.num)
    def visitFloatLit(self,obj):
        return str(obj.num)
    def visitUnExp(self,obj):
        return obj.operator + '. ' + obj.arg.accept(PrintPrefix())
    def visitBinExp(self,obj):
        return obj.operator + ' ' + obj.left.accept(PrintPrefix()) + ' ' + obj.right.accept(PrintPrefix())
class PrintPostfix(Visitor):
    def visitIntLit(self,obj):
        return str(obj.num)
    def visitFloatLit(self,obj):
        return str(obj.num)
    def visitUnExp(self,obj):
        return obj.arg.accept(PrintPostfix())+ ' ' + obj.operator + '.'
    def visitBinExp(self,obj):
        return obj.left.accept(PrintPostfix()) + ' ' + obj.right.accept(PrintPostfix()) + ' ' + obj.operator



x = BinExp(UnExp('-',IntLit(4)),'+',BinExp(IntLit(3),'*',IntLit(2)))

print(x.accept(Eval()))
print(x.accept(PrintPrefix()))
print(x.accept(PrintPostfix()))