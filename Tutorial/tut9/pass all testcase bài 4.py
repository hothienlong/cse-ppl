from abc import ABC, abstractmethod, ABCMeta
class Type(ABC):
    __metaclass__ = ABCMeta
    pass
class Prim(Type):
    __metaclass__ = ABCMeta
    pass
class IntType(Prim):
    pass
class FloatType(Prim):
    pass
class StringType(Prim):
    pass
class BoolType(Prim):
    pass
class VoidType(Type):
    pass
class Unknown(Type):
    pass

class ArrayType(Type):
    def __init__(self, dimen, eletype):
        self.dimen = dimen
        self.eletype = eletype

class MType:
    def __init__(self, list_param_type, return_type):
        self.list_param_type = list_param_type
        self.return_type = return_type

class Symbol:
    def __init__(self, name, mtype):
        self.name = name
        self.mtype = mtype

from functools import reduce 
class StaticCheck(Visitor):

  
    #decl:List[VarDecl],stmts:List[Stmt]
    def visitProgram(self,ctx:Program,o):
        o = [[]]
        varenv = reduce(lambda acc,ele: self.visit(ele,acc),ctx.decl,o)
        bodyenv = reduce(lambda acc,ele: self.visit(ele,acc),ctx.stmts,varenv)
        # mỗi lần visit 1 stmt hay vardecl đều làm thay đổi môi trường nên phải reduce tích lũy
        # [self.visit(stmt, env) for stmt in ctx.stmts]
        
        # [self.visit(vardecl,o) for vardecl in ctx.decl]
        # [self.visit(stmt,o) for stmt in ctx.stmts]


    #name:str
    def visitVarDecl(self,ctx:VarDecl,o):
        for symbol in o[0]:
            if(ctx.name == symbol.name):
                raise Redeclared(ctx)
        o[0].append(Symbol(ctx.name,Unknown()))
        return o

    #decl:List[VarDecl],stmts:List[Stmt]
    def visitBlock(self,ctx:Block,o):
        new_env = [[]] + o
        varenv = reduce(lambda acc,ele: self.visit(ele,acc),ctx.decl, new_env)
        bodyenv = reduce(lambda acc,ele: self.visit(ele,acc),ctx.stmts, varenv)

        return bodyenv[1:]

    #lhs:Id,rhs:Exp
    def visitAssign(self,ctx:Assign,o): 
        rhs = self.visit(ctx.rhs, o)
        #lhs đc visit sau rhs để phòng trường hợp trong quá trình visit rhs suy diễn đc kiểu của lhs
        lhs = self.visit(ctx.lhs, o) 
        
        # kiểm tra typemismatch và suy diễn kiểu
        if(isinstance(lhs.mtype,Unknown) and isinstance(rhs.mtype,Unknown)):
            raise TypeCannotBeInferred(ctx)
        
        elif(isinstance(lhs.mtype,Unknown) and not isinstance(rhs.mtype,Unknown)):
            self.inferType(lhs,rhs.mtype)

        elif(isinstance(rhs.mtype,Unknown) and not isinstance(lhs.mtype,Unknown)):
            self.inferType(rhs,lhs.mtype)
        
        elif(type(lhs.mtype) != type(rhs.mtype)):
            raise TypeMismatchInStatement(ctx)

        return o


    #op:str,e1:Exp,e2:Exp 
    # #op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b
    def visitBinOp(self,ctx:BinOp,o):
        left = self.visit(ctx.e1, o)
        right = self.visit(ctx.e2, o)
        op = ctx.op

        # # suy diễn kiểu
        # if(isinstance(type1,Unknown)):
        #     type1 = self.inferTypeExp(ctx.e1, ctx.op, o)
        # if(isinstance(type2,Unknown)):
        #     type2 = self.inferTypeExp(ctx.e2, ctx.op, o)
        # đã hết Unknown

        # kiểm tra typemissmatch và suy diễn kiểu
        #if(op in ['+','-','*','/']):
            # self.inferType(left,IntType())
            # self.inferType(right,IntType())
            
        if(isinstance(left.mtype,IntType) and isinstance(right.mtype,IntType)):
                return Symbol(None,IntType())          
        elif(op in ['+.','-.','*.','/.']):
            self.inferType(left,FloatType())
            self.inferType(right,FloatType())
            if(isinstance(left.mtype,FloatType) and isinstance(right.mtype,FloatType)):
                return Symbol(None,FloatType())  
        elif(op in ['>','=']):
            self.inferType(left,IntType())
            self.inferType(right,IntType())
            if(isinstance(left.mtype,IntType) and isinstance(right.mtype,IntType)):
                return Symbol(None,BoolType())   
        elif(op in ['>.','=.']):
            self.inferType(left,FloatType())
            self.inferType(right,FloatType())
            if(isinstance(left.mtype,FloatType) and isinstance(right.mtype,FloatType)):
                return Symbol(None,BoolType())  
        elif(op in ['&&','||','>b','=b']):
            self.inferType(left,BoolType())
            self.inferType(right,BoolType())
            if(isinstance(left.mtype,BoolType) and isinstance(right.mtype,BoolType)):
                return Symbol(None,BoolType())  
        raise TypeMismatchInExpression(ctx)


    #op:str,e:Exp #op is -,-., !,i2f, floor
    def visitUnOp(self,ctx:UnOp,o):
        exp = self.visit(ctx.e, o)
        op = ctx.op

        # # suy diễn kiểu
        # if(isinstance(type,Unknown)):
        #     type = self.inferTypeExp(ctx.e, ctx.op, o)

        # kiểm tra typemissmatch và suy diễn kiểu
        if(op == '!'):
            self.inferType(exp,BoolType())
            if(isinstance(exp.mtype,BoolType)):
                return Symbol(None,BoolType())
        elif(op == '-'):
            self.inferType(exp,IntType())
            if(isinstance(exp.mtype,IntType)):
                return Symbol(None,IntType())
        elif(op == '-.'):
            self.inferType(exp,FloatType())
            if(isinstance(exp.mtype,FloatType)):
                return Symbol(None,FloatType())
        elif(op == 'i2f'):
            self.inferType(exp,IntType())
            if(isinstance(exp.mtype,IntType)):
                return Symbol(None,FloatType())
        elif(op == 'floor'):
            self.inferType(exp,FloatType())
            if(isinstance(exp.mtype,FloatType)):
                return Symbol(None,IntType())
        raise TypeMismatchInExpression(ctx) 



    #val:int
    def visitIntLit(self,ctx:IntLit,o):
        return Symbol(None,IntType())

    #val:float
    def visitFloatLit(self,ctx,o): 
        return Symbol(None,FloatType())

    #val:bool
    def visitBoolLit(self,ctx,o): 
        return Symbol(None,BoolType())

    #name:str
    def visitId(self,ctx,o):
        for lstSymbol in o:
            for symbol in lstSymbol:
                if(ctx.name == symbol.name):
                    return symbol   #trước và sau suy diễn
        raise UndeclaredIdentifier(ctx.name)

    # chỉ suy diễn nếu Unknown
    def inferType(self, symbol, type):
        if(isinstance(symbol.mtype,Unknown)):
            symbol.mtype = type
