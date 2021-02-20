from functools import reduce
class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o):
        # o = []
        # new_env = reduce(lambda acc, ele: self.visit(ele, acc), ctx.decl, o)
        self.visit(ctx.exp, ctx.decl)

    def visitVarDecl(self,ctx:VarDecl,o): pass
    
    #op:str,e1:Exp,e2:Exp #op is +,-,*,/,&&,||, >, <, ==, or  !=
    def visitBinOp(self,ctx:BinOp,o):
        op = ctx.op
        type1 = self.visit(ctx.e1, o)
        type2 = self.visit(ctx.e2, o)
        if op in ["+","-","*"]:
            if isinstance(type1,FloatType) or isinstance(type2,FloatType):
                return FloatType()
            elif isinstance(type1,IntType) and isinstance(type2,IntType):
                return IntType()
        elif op is "/":
            if not isinstance(type1,BoolType) and not isinstance(type2,BoolType):
                return FloatType()
        elif op in ["&&","||"]:
            if isinstance(type1,BoolType) and isinstance(type2,BoolType):
                return BoolType()
        elif op in [">","<","==","!="]:
            if type(type1) == type(type2):
                return BoolType()
        raise TypeMismatchInExpression(ctx)

    def visitUnOp(self,ctx:UnOp,o):
        op = ctx.op
        type = self.visit(ctx.e, o)
        if op == "-":
            if isinstance(type,FloatType):
                return FloatType()
            elif isinstance(type,IntType):
                return IntType()
        elif op == "!":
            if isinstance(type,BoolType):
                return BoolType()
        raise TypeMismatchInExpression(ctx)

    def visitIntLit(self,ctx:IntLit,o):
        return IntType()

    def visitFloatLit(self,ctx,o):
        return FloatType()

    def visitBoolLit(self,ctx,o):
        return BoolType()
        
    def visitId(self,ctx,o):
        for symbol in o:
            if symbol.name == ctx.name:
                return symbol.typ
        raise UndeclaredIdentifier(ctx.name)