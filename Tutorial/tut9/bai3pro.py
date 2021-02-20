from functools import reduce
class Symbol:
    def __init__(self, name, mtype):
        self.name = name
        self.mtype = mtype

class IntType():
    def __str__(self):
        "IntType"
class FloatType():
    def __str__(self):
        "FloatType"
class BoolType():
    def __str__(self):
        "BoolType"
        
class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o):
        o = []
        new_env = reduce(lambda acc, ele: self.visit(ele, acc), ctx.decl + ctx.stmts, o)
        
    def visitVarDecl(self,ctx:VarDecl,o):
        o.append(Symbol(ctx.name, None))
        return o
        
    def visitAssign(self,ctx:Assign,o):
        right = self.visit(ctx.rhs, o)
        left = self.visit(ctx.lhs, o)
        
        if left.mtype is None and right.mtype is None:
            raise TypeCannotBeInferred(ctx)
        elif left.mtype is None and right.mtype is not None:
            self.inferType(left, right.mtype)
        elif left.mtype is not None and right.mtype is None:
            self.inferType(right, left.mtype)
        elif type(left.mtype) != type(right.mtype):
            raise TypeMismatchInStatement(ctx)
            
        return o
    
    #op:str,e1:Exp,e2:Exp #op is +,-,*,/,&&,||, >, <, ==, or  !=
    def visitBinOp(self,ctx:BinOp,o):
        op = ctx.op
        left = self.visit(ctx.e1, o)
        right = self.visit(ctx.e2, o)
        
        if op in ["+","-","*","/"]:
            self.inferType(left,IntType())
            self.inferType(right,IntType())
            if isinstance(left.mtype,IntType) and isinstance(right.mtype,IntType):
                return Symbol(None,IntType())
        elif op in ["+.","-.","*.","/."]:
            self.inferType(left,FloatType())
            self.inferType(right,FloatType())
            if isinstance(left.mtype,FloatType) and isinstance(right.mtype,FloatType):
                return Symbol(None,FloatType())
        elif op in [">","="]:
            self.inferType(left,IntType())
            self.inferType(right,IntType())
            if isinstance(left.mtype,IntType) and isinstance(right.mtype,IntType):
                return Symbol(None,BoolType())
        elif op in [">.","=."]:
            self.inferType(left,FloatType())
            self.inferType(right,FloatType())
            if isinstance(left.mtype,FloatType) and isinstance(right.mtype,FloatType):
                return Symbol(None,BoolType())
        elif op in ["&&","||",">b","=b"]:
            self.inferType(left,BoolType())
            self.inferType(right,BoolType())
            if isinstance(left.mtype,BoolType) and isinstance(right.mtype,BoolType):
                return Symbol(None,BoolType())
        raise TypeMismatchInExpression(ctx)

    def visitUnOp(self,ctx:UnOp,o):
        op = ctx.op
        exp = self.visit(ctx.e, o)
        if op == "-":
            self.inferType(exp,IntType())
            if isinstance(exp.mtype,IntType):
                return Symbol(None,IntType())
        elif op == "-.":
            self.inferType(exp,FloatType())
            if isinstance(exp.mtype,FloatType):
                return Symbol(None,FloatType())
        elif op == "!":
            self.inferType(exp,BoolType())
            if isinstance(exp.mtype,BoolType):
                return Symbol(None,BoolType())
        elif op == "i2f":
            self.inferType(exp,IntType())
            if isinstance(exp.mtype,IntType):
                return Symbol(None,FloatType())
        elif op == "floor":
            self.inferType(exp,FloatType())
            if isinstance(exp.mtype,FloatType):
                return Symbol(None,IntType())
        raise TypeMismatchInExpression(ctx)

    def visitIntLit(self,ctx:IntLit,o):
        return Symbol(None,IntType())

    def visitFloatLit(self,ctx,o):
        return Symbol(None,FloatType())

    def visitBoolLit(self,ctx,o):
        return Symbol(None,BoolType())
        
    def visitId(self,ctx,o):
        for symbol in o:
            if symbol.name == ctx.name:
                return symbol
        raise UndeclaredIdentifier(ctx.name)
    
    def inferType(self, symbol, type):
        if symbol.mtype == None:
            symbol.mtype = type