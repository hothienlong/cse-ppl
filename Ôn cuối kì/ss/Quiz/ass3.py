#Cau1
from functools import reduce
class Visitor:
    def visit(self, ast, o):
        return ast.accept(self, o)
    
    def visitDecls(self, ast, o):
        o = [[]]
        reduce(lambda acc, ele: self.visit(ele, acc), ast.lst, o)

    def visitTypeDecls(self, ast, o):
        name = ast.name
        if name in o[0]:
            raise RedeclareVariable(name)
        o[0].append(name)
        typ = self.visit(ast.rhs, o)
        return o

    def visitVarDecls(self, ast, o):
        name = ast.name
        if name in o[0]:
            raise RedeclareVariable(name)
        o[0].append(name)
        typ = self.visit(ast.rhs, o)
        return o
    
    def visitStructType(self, ast, o):
        o = [] + o #o = [[], [xxx]]
        reduce(lambda acc, ele : self.visit(ele, acc), ast.ele, o)
        return o[1:]
    
    def visitIntType(self, ast, o):
        return IntType()
    
    def visitFloatType(self, ast, o):
        return FloatType()
    
#Cau2
from functools import reduce
class Visitor:
    def visit(self, ast, o):
        return ast.accept(self, o)
    
    def visitDecls(self, ast, o):
        o = [[]]
        reduce(lambda acc, ele: self.visit(ele, acc), ast.lst, o)

    def visitTypeDecls(self, ast, o):
        name = ast.name
        if name in o[0]:
            raise RedeclareVariable(name)
        o[0].append(name)
        typ = self.visit(ast.rhs, o)
        return o

    def visitVarDecls(self, ast, o):
        name = ast.name
        if name in o[0]:
            raise RedeclareVariable(name)
        o[0].append(name)
        typ = self.visit(ast.rhs, o)
        return o
    
    def visitStructType(self, ast, o):
        o = [] + o #o = [[], [xxx]]
        reduce(lambda acc, ele : self.visit(ele, acc), ast.ele, o)
        return o[1:]
    
    def visitIntType(self, ast, o):
        return IntType()
    
    def visitFloatType(self, ast, o):
        return FloatType()
    
    def visitId(self, ast, o):
        for i in o:
            for j in i:
                if ast.name == j:
                    return 
        raise UndeclareType(ast.name)


#Cau 3
from functools import reduce
class Visitor:
    def visit(self, ast, o):
        return ast.accept(self, o)
    
    def visitDecls(self, ast, o):
        o = 0
        reduce(lambda acc, ele: acc +self.visit(ele, acc), ast.lst, o)

    def visitTypeDecls(self, ast, o):
        return self.visit(ast.rhs)

    def visitVarDecls(self, ast, o):
        return self.visit(ast.rhs)
    
    def visitStructType(self, ast, o):
        sizeStruct = reduce(lambda acc, ele: acc + self.visit(ele, acc), ast.lst, o)
        return sizeStruct
    
    def visitIntType(self, ast, o):
        return 2
    
    def visitFloatType(self, ast, o):
        return 6
    
    def visitArrayType(self, ast, o):
        return (ast.upper - ast.lower + 1) * self.visit(ast.eleType)
    
    

    