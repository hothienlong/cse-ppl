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
    def __init__(self, list_param, return_type):
        self.list_param = list_param
        self.return_type = return_type

class Symbol:
    def __init__(self, name, mtype):
        self.name = name
        self.mtype = mtype

from functools import reduce 
class StaticCheck(Visitor):

  
    #decl:List[Decl],stmts:List[Stmt]
    def visitProgram(self,ctx:Program,o):
        o = [[]]
        varenv = reduce(lambda acc,ele: self.visit(ele,acc),ctx.decl,o)
        bodyenv = reduce(lambda acc,ele: self.visit(ele,acc),ctx.stmts,varenv)
        # mỗi lần visit 1 stmt hay vardecl đều làm thay đổi môi trường nên phải reduce tích lũy



    #name:str
    def visitVarDecl(self,ctx:VarDecl,o):
        for symbol in o[0]:
            if(symbol.name == ctx.name):
                raise Redeclared(ctx)
        o[0].append(Symbol(ctx.name,Unknown()))
        return o

    #name:str,param:List[VarDecl],local:List[Decl],stmts:List[Stmt]
    def visitFuncDecl(self,ctx:FuncDecl,o):
        for symbol in o[0]:
            if(symbol.name == ctx.name):
                raise Redeclared(ctx)
        new_env = [[]] + o
        params = reduce(lambda acc,ele: self.visit(ele,acc),ctx.param,new_env)[0].copy()
        func = Symbol(ctx.name,MType([param for param in params],Unknown()))

        new_env[1].append(func)
        inside_env = reduce(lambda acc,ele: self.visit(ele,acc),ctx.local+ctx.stmts,new_env)
        

        return inside_env[1:]

    #name:str,args:List[Exp]
    def visitCallStmt(self,ctx:CallStmt,o):
        funcSymbol = self.getSymbolByName(ctx.name,o)

        if(not isinstance(funcSymbol.mtype,MType)):
            raise UndeclaredIdentifier(funcSymbol.name)


        lstParam = funcSymbol.mtype.list_param

        if(len(lstParam) != len(ctx.args)):
            raise TypeMismatchInStatement(ctx)

        for i in range(len(lstParam)):
            argSym = self.visit(ctx.args[i],o)
            if(isinstance(argSym.mtype,Unknown) and isinstance(lstParam[i].mtype,Unknown)):
                raise TypeCannotBeInferred(ctx)
            elif(isinstance(argSym.mtype,Unknown) and not isinstance(lstParam[i].mtype,Unknown)):
                self.inferType(argSym,lstParam[i].mtype)
            elif(isinstance(lstParam[i].mtype,Unknown) and not isinstance(argSym.mtype,Unknown)):
                self.inferType(lstParam[i],argSym.mtype)
            elif(type(lstParam[i].mtype) != type(argSym.mtype)):
                raise TypeMismatchInStatement(ctx)

        return o
            



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
        return self.getSymbolByName(ctx.name,o)

    # chỉ suy diễn nếu Unknown
    def inferType(self, symbol, type):
        if(isinstance(symbol.mtype,Unknown)):
            symbol.mtype = type


    def getSymbolByName(self, symName, o):
        for lstSymbol in o:
            for symbol in lstSymbol:
                if(symName == symbol.name):
                    return symbol
        raise UndeclaredIdentifier(symName)
