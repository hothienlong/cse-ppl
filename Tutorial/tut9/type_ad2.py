from functools import reduce

class Type(ABC):
    pass
class IntType(Type):
    pass
class FloatType(Type):
    pass
class BoolType(Type):
    pass
class UnknownType(Type):
    pass



class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o):
        o = [{}]
        varenv = reduce(lambda x, y: self.visit(y, x), ctx.decl, o)
        bodyenv = reduce(lambda x, y: self.visit(y, x), ctx.stmts, varenv)
 
    def visitVarDecl(self,ctx:VarDecl,o):
        if ctx.name in o[0]:
            raise Redeclared(ctx)
        o[0][ctx.name] = UnknownType()
        return o
 
    def visitBlock(self,ctx:Block,o):
        o = [{}] + o
 
        varenv = reduce(lambda x, y: self.visit(y, x), ctx.decl, o)
        bodyenv = reduce(lambda x, y: self.visit(y, x), ctx.stmts, varenv)
 
        return o[1:]

    def visitAssign(self, ctx: Assign, o):
        tr = self.visit(ctx.rhs, o)
        tl = self.visit(ctx.lhs, o)
        if type(tr) == UnknownType and type(tl) == UnknownType:
            raise TypeCannotBeInferred(ctx)

        if type(tr) != UnknownType and type(tl) == UnknownType:
            for x in o:
                if ctx.lhs.name in x:
                    x[ctx.lhs.name] = tr
                    break
            tl = tr
        if type(tr) == UnknownType and type(tl) != UnknownType:
            for x in o:
                if ctx.rhs.name in x:
                    x[ctx.rhs.name] = tl
                    break
            tr = tl

        if type(tl) != type(tr):
            raise TypeMismatchInStatement(ctx)

        return o

    def visitBinOp(self, ctx: BinOp, o):
        te1 = self.visit(ctx.e1, o)
        te2 = self.visit(ctx.e2, o)

        if type(te1) == UnknownType:
            te1 = self.setType(ctx.op, ctx.e1, o)
        if type(te2) == UnknownType:
            te2 = self.setType(ctx.op, ctx.e2, o)

        if (ctx.op in ["+", "-", "*", "/"]):
            if (type(te1) == IntType and type(te2) == IntType):
                return IntType()
        elif (ctx.op in ["+.", "-.", "*.", "/."]):
            if (type(te1) == FloatType and type(te2) == FloatType):
                return FloatType()
        elif (ctx.op in [">", "="]):
            if (type(te1) == IntType and type(te2) == IntType):
                return BoolType()
        elif (ctx.op in [">.", "=."]):
            if (type(te1) == FloatType and type(te2) == FloatType):
                return BoolType()
        elif (ctx.op in [">b", "=b", "||", "&&"]):
            if (type(te1) == BoolType and type(te2) == BoolType):
                return BoolType()        
        raise TypeMismatchInExpression(ctx)

    def visitUnOp(self, ctx: UnOp, o):
        te = self.visit(ctx.e, o)
        if type(te) == UnknownType:
            te = self.setType(ctx.op, ctx.e, o)

        if ctx.op == "-" and type(te) == IntType:
            return te
        elif ctx.op == "-." and type(te) == FloatType:
            return te
        elif ctx.op == "!" and type(te) == BoolType:
            return te
        elif ctx.op == "i2f" and type(te) == IntType:
            return FloatType()
        elif ctx.op == "floor" and type(te) == FloatType:
            return IntType()
        raise TypeMismatchInExpression(ctx)

    def visitIntLit(self, ctx, o):
        return IntType()

    def visitFloatLit(self, ctx, o):
        return FloatType()

    def visitBoolLit(self, ctx, o):
        return BoolType()

    def visitId(self, ctx, o):
        for arr in o:
            if ctx.name in arr:
                return arr[ctx.name]
        raise UndeclaredIdentifier(ctx.name)

    def setType(self, op, e, o):
        for arr in o:
            if e.name in arr:
                if op in ["+", "-", "*", "/", ">", "=", "i2f"]:
                    arr[e.name] = IntType()
                elif op in ["+.", "-.", "*.", "/.", ">.", "=.", "floor"]:
                    arr[e.name] = FloatType()
                elif op in ["!", "&&","||",">b","=b"]:
                    arr[e.name] = BoolType()
                return arr[e.name]
