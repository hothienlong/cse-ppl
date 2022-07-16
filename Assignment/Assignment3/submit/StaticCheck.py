"""
 * @author nhphung
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from main.bkit.utils.AST import CallExpr
from main.bkit.checker.StaticError import Function, NoEntryPoint, TypeCannotBeInferred, TypeMismatchInExpression, TypeMismatchInStatement
from typing import List, Tuple
from AST import * 
from Visitor import *
from StaticError import *
from functools import *
#-------------------------------------------------------------------------#
#---------------------AUTHOR: HO THIEN LONG (1812869)---------------------#
#-------------------------------------------------------------------------#
# Var: x = {1,2,3} thuộc Type nào
# Var: arr[3] = 3
class Type(ABC):
    __metaclass__ = ABCMeta
    pass
class Prim(Type):
    __metaclass__ = ABCMeta
    pass
class IntType(Prim):
    def __str__(self) -> str:
        return "IntType"

class FloatType(Prim):
    def __str__(self) -> str:
        return "FloatType"

class StringType(Prim):
    def __str__(self) -> str:
        return "StringType"

class BoolType(Prim):
    def __str__(self) -> str:
        return "BoolType"

class VoidType(Type):
    def __str__(self) -> str:
        return "VoidType"

class Unknown(Type):
    def __str__(self) -> str:
        return "Unknown"


@dataclass
class Symbol:
    name: str
    mtype:Type
    kind: Kind = None
    def __str__(self) -> str:
        symname = self.name if(self.name != None) else "None"
        return "Symbol(" + \
                symname + \
                ", " + \
                str(self.mtype) + \
                ")"

@dataclass
class MType:
    list_param:List[Symbol] #list param
    return_type:Type #kiểu return
    def __str__(self):
        return 'MType([' + ','.join([str(i) for i in self.list_param]) + '],' + str(self.return_type) + ')'

@dataclass
class ArrayType(Type):
    dimen:List[int]
    eleSymbol: Symbol
    def __str__(self) -> str:
        return "ArrayType([" + "," .join([str(i) for i in self.dimen]) + "]," + str(self.eleSymbol) + ")"


# static: suy diễn kiểu chỉ suy diễn lần đầu tiên sử dụng
class StaticChecker(BaseVisitor):
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
Symbol("int_of_float",MType([Symbol(None,FloatType())],IntType())),
Symbol("float_to_int",MType([Symbol(None,IntType())],FloatType())),
Symbol("int_of_string",MType([Symbol(None,StringType())],IntType())),
Symbol("string_to_int",MType([Symbol(None,IntType())],StringType())),
Symbol("float_of_string",MType([Symbol(None,StringType())],FloatType())),
Symbol("string_of_float",MType([Symbol(None,FloatType())],StringType())),
Symbol("bool_of_string",MType([Symbol(None,StringType())],BoolType())),
Symbol("string_of_bool",MType([Symbol(None,BoolType())],StringType())),
Symbol("read",MType([],StringType())),
Symbol("printLn",MType([],VoidType())),
Symbol("print",MType([Symbol(None,StringType())],VoidType())),
Symbol("printStrLn",MType([Symbol(None,StringType())],VoidType()))]                           
   
    def check(self):
        return self.visit(self.ast,self.global_envi)

    def print_list_env(self, o):
        new_env = []
        for lstSymbol in o:
            new_lst_symbol = list(map(lambda symbol: str(symbol), lstSymbol))
            new_env.append(new_lst_symbol)
        print(new_env)


    def getSymbolById(self, ast, o, kind):
        for lstSymbol in o:
            for symbol in lstSymbol:
                if(ast.name == symbol.name):
                    return symbol

        raise Undeclared(kind, ast.name)

    # chỉ suy diễn nếu Unknown
    def inferType(self, symbol, type):
        if(isinstance(symbol.mtype,Unknown)):
            symbol.mtype = type
        elif(isinstance(symbol.mtype,MType) and isinstance(symbol.mtype.return_type,Unknown)):
            symbol.mtype.return_type = type
        elif(isinstance(symbol.mtype,ArrayType) and isinstance(symbol.mtype.eleSymbol.mtype,Unknown)):
            symbol.mtype.eleSymbol.mtype = type
            

    def infer2Side(self, lhs, rhs, ast):
        funcSymbolLeft = None
        if(isinstance(lhs.mtype,MType)):
            funcSymbolLeft = lhs
            lhs = Symbol(lhs.name,lhs.mtype.return_type)
        
        funcSymbolRight = None
        if(isinstance(rhs.mtype,MType)):
            funcSymbolRight = rhs
            rhs = Symbol(rhs.name,rhs.mtype.return_type) # biến foo(a,b){return 1;} => Symbol(foo,IntType)

        if(isinstance(lhs.mtype,Unknown)): # TypeCannotBeInferred hoặc suy diễn
            if(isinstance(rhs.mtype,Unknown)):
                raise TypeCannotBeInferred(ast)
            elif(isinstance(rhs.mtype,VoidType)):
                if(funcSymbolLeft == None): # left là scalar
                    raise TypeMismatchInStatement(ast)
                else: # left là Mtype (trường hợp Return)
                    self.inferType(lhs,rhs.mtype)
                    self.inferType(funcSymbolLeft,rhs.mtype)
            elif(isinstance(rhs.mtype,ArrayType)):
                raise TypeMismatchInStatement(ast)
            else:
                self.inferType(lhs,rhs.mtype)

        elif(isinstance(lhs.mtype,ArrayType)):     
            if(isinstance(rhs.mtype,Unknown)):
                if(funcSymbolRight == None):
                    raise TypeMismatchInStatement(ast)
                else:
                    self.inferType(funcSymbolRight,lhs.mtype)
            elif(isinstance(rhs.mtype,VoidType)):
                raise TypeMismatchInStatement(ast)
            elif(isinstance(rhs.mtype,ArrayType)):
                if(lhs.mtype.dimen != rhs.mtype.dimen):
                    raise TypeMismatchInStatement(ast)
                elif(isinstance(lhs.mtype.eleSymbol.mtype,Unknown) and isinstance(rhs.mtype.eleSymbol.mtype,Unknown)):
                    raise TypeCannotBeInferred(ast)
                elif(isinstance(lhs.mtype.eleSymbol.mtype,Unknown) and not isinstance(rhs.mtype.eleSymbol.mtype,Unknown)):
                    self.inferType(lhs,rhs.mtype.eleSymbol.mtype)
                elif(isinstance(rhs.mtype.eleSymbol.mtype,Unknown) and not isinstance(lhs.mtype.eleSymbol.mtype,Unknown)):
                    self.inferType(rhs,lhs.mtype.eleSymbol.mtype)
                    if(funcSymbolRight != None): # suy diễn funcSymbol gốc
                        self.inferType(funcSymbolRight,lhs.mtype)
                elif(type(lhs.mtype.eleSymbol.mtype) != type(rhs.mtype.eleSymbol.mtype)):
                    raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInStatement(ast)
        ##################################################################
        elif(isinstance(lhs.mtype,VoidType)): # trường hợp riêng của return
            if(isinstance(rhs.mtype,Unknown)):
                self.inferType(rhs,lhs.mtype)
                if(funcSymbolRight != None):
                    self.inferType(funcSymbolRight,lhs.mtype)
            elif(isinstance(rhs.mtype,VoidType)):
                pass
            else:
                raise TypeMismatchInStatement(ast)
        ##################################################################
        else: # scalar có type
            if(isinstance(rhs.mtype,Unknown)):
                self.inferType(rhs,lhs.mtype)
                if(funcSymbolRight != None):
                    self.inferType(funcSymbolRight,lhs.mtype)
            elif(isinstance(rhs.mtype,VoidType)):
                raise TypeMismatchInStatement(ast)
            elif(isinstance(rhs.mtype,ArrayType)):
                raise TypeMismatchInStatement(ast)
            elif(type(lhs.mtype) != type(rhs.mtype)):
                raise TypeMismatchInStatement(ast)

    def infer2SideExp(self, lhs, rhs, ast):
        funcSymbolLeft = None
        if(isinstance(lhs.mtype,MType)):
            funcSymbolLeft = lhs
            lhs = Symbol(lhs.name,lhs.mtype.return_type)
        
        funcSymbolRight = None
        if(isinstance(rhs.mtype,MType)):
            funcSymbolRight = rhs
            rhs = Symbol(rhs.name,rhs.mtype.return_type) # biến foo(a,b){return 1;} => Symbol(foo,IntType)

        if(isinstance(lhs.mtype,Unknown)): # TypeCannotBeInferred hoặc suy diễn
            if(isinstance(rhs.mtype,Unknown)):
                raise TypeCannotBeInferred(self.cur_stmt)
            elif(isinstance(rhs.mtype,VoidType)):
                if(funcSymbolLeft == None): # left là scalar
                    raise TypeMismatchInExpression(ast)
                else: # left là Mtype (trường hợp Return)
                    self.inferType(lhs,rhs.mtype)
                    self.inferType(funcSymbolLeft,rhs.mtype)
            elif(isinstance(rhs.mtype,ArrayType)):
                raise TypeMismatchInExpression(ast)
            else:
                self.inferType(lhs,rhs.mtype)

        elif(isinstance(lhs.mtype,ArrayType)):     
            if(isinstance(rhs.mtype,Unknown)):
                if(funcSymbolRight == None):
                    raise TypeMismatchInExpression(ast)
                else:
                    self.inferType(funcSymbolRight,lhs.mtype)
            elif(isinstance(rhs.mtype,VoidType)):
                raise TypeMismatchInExpression(ast)
            elif(isinstance(rhs.mtype,ArrayType)):    
                if(lhs.mtype.dimen != rhs.mtype.dimen):
                    raise TypeMismatchInExpression(ast)
                elif(isinstance(lhs.mtype.eleSymbol.mtype,Unknown) and isinstance(rhs.mtype.eleSymbol.mtype,Unknown)):
                    raise TypeCannotBeInferred(self.cur_stmt)
                elif(isinstance(lhs.mtype.eleSymbol.mtype,Unknown) and not isinstance(rhs.mtype.eleSymbol.mtype,Unknown)):
                    self.inferType(lhs,rhs.mtype.eleSymbol.mtype)
                elif(isinstance(rhs.mtype.eleSymbol.mtype,Unknown) and not isinstance(lhs.mtype.eleSymbol.mtype,Unknown)):
                    self.inferType(rhs,lhs.mtype.eleSymbol.mtype)
                    if(funcSymbolRight != None): # suy diễn funcSymbol gốc
                        self.inferType(funcSymbolRight,lhs.mtype)
                elif(type(lhs.mtype.eleSymbol.mtype) != type(rhs.mtype.eleSymbol.mtype)):
                    raise TypeMismatchInExpression(ast)
            else:
                raise TypeMismatchInExpression(ast)
        ##################################################################
        elif(isinstance(lhs.mtype,VoidType)): # trường hợp riêng của return
            if(isinstance(rhs.mtype,Unknown)):
                self.inferType(rhs,lhs.mtype)
                if(funcSymbolRight != None):
                    self.inferType(funcSymbolRight,lhs.mtype)
            elif(isinstance(rhs.mtype,VoidType)):
                pass
            else:
                raise TypeMismatchInExpression(ast)
        ##################################################################
        else: # scalar có type
            if(isinstance(rhs.mtype,Unknown)):
                self.inferType(rhs,lhs.mtype)
                if(funcSymbolRight != None):
                    self.inferType(funcSymbolRight,lhs.mtype)
            elif(isinstance(rhs.mtype,VoidType)):
                raise TypeMismatchInExpression(ast)
            elif(isinstance(rhs.mtype,ArrayType)):
                raise TypeMismatchInExpression(ast)
            elif(type(lhs.mtype) != type(rhs.mtype)):
                raise TypeMismatchInExpression(ast)
#--------------------------------------------------------------------------------------#
#-----------------------------------FUNCTION VISIT-------------------------------------#
#--------------------------------------------------------------------------------------#
    # decl : List[Decl]
    def visitProgram(self, ast, o): # o = [[Symbol(),..],[],..]
        o = [[]]
        o[0] = o[0] + self.global_envi

        lstVardecl = list(filter(lambda x: isinstance(x,VarDecl), ast.decl))
        lstFuncdecl = list(filter(lambda x: isinstance(x,FuncDecl), ast.decl))

        self.isParamDecl = False
        env = reduce(lambda acc,ele: self.visit(ele,acc),lstVardecl,o)

        # cưỡi ngựa xem hoa
        isNoEntryPoint = True
        for decl in lstFuncdecl:
            funcName = decl.name.name
            for symbol in env[0]:          
                if(funcName == symbol.name):
                    raise Redeclared(Function(), funcName)
                
            if(funcName == "main"):
                isNoEntryPoint = False
            self.isParamDecl = True
            params = reduce(lambda acc,ele: self.visit(ele,acc), decl.param, [[]]+env)[0]
            self.isParamDecl = False
            func = Symbol(funcName,MType([param for param in params],Unknown()), Function())
            env[0].append(func)

        print("cưỡi ngựa xem hoa: ",end="")
        self.print_list_env(env)

        if(isNoEntryPoint == True):
            raise NoEntryPoint()
        env = reduce(lambda acc,ele: self.visit(ele,acc),lstFuncdecl,env)        

#----------------------------Declaration-------------------------------------#
#----------------------------------------------------------------------------#

    # variable : Id => varType = visit(Id) và varName = variable.name
    # varDimen : List[int] # empty list for scalar variable
    # varInit  : Literal   # null if no initial  
    def visitVarDecl(self, ast, o):
        varName = ast.variable.name

        for symbol in o[0]:
            if(varName == symbol.name):
                if(self.isParamDecl == True):
                    raise Redeclared(Parameter(), varName)
                else:
                    raise Redeclared(Variable(), varName)

        if(ast.varDimen == [] and ast.varInit is None):
            if(self.isParamDecl == True):
                o[0].append(Symbol(varName, Unknown(),Parameter()))
            else:
                o[0].append(Symbol(varName, Unknown(),Variable()))
        elif(ast.varDimen == []):
            varSym = self.visit(ast.varInit, o)
            varType = varSym.mtype
            if(self.isParamDecl == True):
                o[0].append(Symbol(varName, varType,Parameter()))
            else:
                o[0].append(Symbol(varName, varType,Variable()))
        elif(ast.varInit is None): #Var: arr[3][4];
            dimen = ast.varDimen
            eleSymbol = Symbol(None,Unknown())
            if(self.isParamDecl == True):
                o[0].append(Symbol(varName, ArrayType(dimen, eleSymbol), Parameter()))
            else:
                o[0].append(Symbol(varName, ArrayType(dimen, eleSymbol), Variable()))
        else:
            varSym = self.visit(ast.varInit, o)
            varType = varSym.mtype
            o[0].append(Symbol(varName, varType))
        print("end vardecl: ",end="")
        
        self.print_list_env(o)
        return o
    
    # name: Id
    # param: List[VarDecl]
    # body: Tuple[List[VarDecl],List[Stmt]]
    def visitFuncDecl(self, ast, o):
        func = self.getSymbolById(ast.name, o, Function())
        self.cur_function = func
        params = [param for param in func.mtype.list_param] #chỉ tham chiếu từng đối tượng trong list
        new_env = [params] + o

        lstVardecl = ast.body[0]
        lstStmt = ast.body[1]   
        inside_env = reduce(lambda acc,ele: self.visit(ele,acc),lstVardecl+lstStmt,new_env)

        print("end func",end="")
        self.print_list_env(inside_env)
        return inside_env[1:]
    
#----------------------------------------EXPRESSION------------------------------------#
#--------------------------------------------------------------------------------------#
    # op:str
    # left:Expr
    # right:Expr
    def visitBinaryOp(self, ast, o):
        left = self.visit(ast.left, o)
        # right = self.visit(ast.right, o)
        op = ast.op
        
        # kiểm tra typemissmatch và suy diễn kiểu
        if(op in ['+','-','*','\\','==','<','>','<=','>=','!=']):
            # check left
            self.inferType(left,IntType())
            
            if(isinstance(left.mtype,MType)):
                leftType = left.mtype.return_type
            else:
                leftType = left.mtype

            if(isinstance(leftType,IntType)):
                # check right
                right = self.visit(ast.right, o)
                self.inferType(right,IntType())
                if(isinstance(right.mtype,MType)):
                    rightType = right.mtype.return_type
                else:
                    rightType = right.mtype

                if(isinstance(rightType,IntType)):
                    if(op in ['+','-','*','\\']):
                        return Symbol(None,IntType())          
                    else:
                        return Symbol(None,BoolType())


        elif(op in ['+.','-.','*.','\\.','=/=','<.','>.','<=.','>=.']):
            # check left
            self.inferType(left,FloatType())
            
            if(isinstance(left.mtype,MType)):
                leftType = left.mtype.return_type
            else:
                leftType = left.mtype

            if(isinstance(leftType,FloatType)):
                # check right
                right = self.visit(ast.right, o)
                self.inferType(right,FloatType())
                if(isinstance(right.mtype,MType)):
                    rightType = right.mtype.return_type
                else:
                    rightType = right.mtype

                if(isinstance(rightType,FloatType)):
                    if(op in ['+.','-.','*.','\\.']):
                        return Symbol(None,FloatType())  
                    else:
                        return Symbol(None,BoolType())
        elif(op in ['&&','||']):
            self.inferType(left,BoolType())

            if(isinstance(left.mtype,MType)):
                leftType = left.mtype.return_type
            else:
                leftType = left.mtype

            if(isinstance(leftType,BoolType)):
                right = self.visit(ast.right, o)
                self.inferType(right,BoolType())
                if(isinstance(right.mtype,MType)):
                    rightType = right.mtype.return_type
                else:
                    rightType = right.mtype

                if(isinstance(rightType,BoolType)):
                    return Symbol(None,BoolType())  
        
        print("binop typemismatch: ",end="")
        self.print_list_env(o)
        raise TypeMismatchInExpression(ast)
    
    # op:str
    # body:Expr
    def visitUnaryOp(self, ast, o):
        exp = self.visit(ast.body, o)
        op = ast.op

        # kiểm tra typemissmatch và suy diễn kiểu
        if(op == '!'):
            self.inferType(exp,BoolType())
            if(isinstance(exp.mtype,MType)):
                expType = exp.mtype.return_type
            else:
                expType = exp.mtype
            if(isinstance(expType,BoolType)):
                return Symbol(None,BoolType())
        elif(op == '-'):
            self.inferType(exp,IntType())
            if(isinstance(exp.mtype,MType)):
                expType = exp.mtype.return_type
            else:
                expType = exp.mtype
            if(isinstance(expType,IntType)):
                return Symbol(None,IntType())
        elif(op == '-.'):
            self.inferType(exp,FloatType())
            if(isinstance(exp.mtype,MType)):
                expType = exp.mtype.return_type
            else:
                expType = exp.mtype
            if(isinstance(expType,FloatType)):
                return Symbol(None,FloatType())
        raise TypeMismatchInExpression(ast) 
    
    # method:Id
    # param:List[Expr] => lấy type thôi
    def visitCallExpr(self, ast, o):
        # param (Unknown, ArrayType) <====> arg (Unknown, Mtype, ArrayType, Exp khác)
        funcSymbol = self.getSymbolById(ast.method,o,Function())

        if(not isinstance(funcSymbol.mtype,MType)):
            raise Undeclared(Function(),funcSymbol.name)
        
        lstParam = funcSymbol.mtype.list_param


        if(len(lstParam) != len(ast.param)):
            raise TypeMismatchInExpression(ast)


        for i in range(len(lstParam)): # arg là function thì check return_type nó trước (từ trái qua phải, ngoài vào trong)
            if(isinstance(ast.param[i],CallExpr)):
                argSym = self.getSymbolById(ast.param[i].method,o,Function())
            else:
                argSym = self.visit(ast.param[i],o)


            self.infer2SideExp(lstParam[i],argSym,ast)

            if(isinstance(ast.param[i],CallExpr)): # infer trước visit sau (đối với call exp)
                self.visit(ast.param[i],o)
            print("end call exp : ",lstParam[i],"---------",argSym)
            
        return funcSymbol
    
    def visitId(self, ast, o):
        idSym = self.getSymbolById(ast,o,Identifier())
        if(isinstance(idSym.kind,Function)):
            raise Undeclared(Identifier(),idSym.name)
        return idSym
    
    # arr:Expr
    # idx:List[Expr]
    def visitArrayCell(self, ast, o): # arr[3][5]
        arrSymbol = self.visit(ast.arr,o)
        # idx = [self.visit(exp,o) for exp in ast.idx]
        # Check array
        if(isinstance(arrSymbol.mtype,ArrayType)):
            pass
        elif(isinstance(arrSymbol.mtype,MType)):
            if(isinstance(arrSymbol.mtype.return_type,Unknown)):
                raise TypeCannotBeInferred(ast)
            elif(isinstance(arrSymbol.mtype.return_type,ArrayType)):            
                arrSymbol = Symbol(arrSymbol.name, arrSymbol.mtype.return_type)
            else:
                raise TypeMismatchInExpression(ast)
        elif(isinstance(arrSymbol.mtype,Unknown)):
            raise TypeCannotBeInferred(ast) # 2 lỗi
        else:
            raise TypeMismatchInExpression(ast)

        #  E[E1]...[En], E must be in array type with n dimensions
        if(len(arrSymbol.mtype.dimen) != len(ast.idx)):
            print("array cell : ",arrSymbol,"--------",ast.idx)
            raise TypeMismatchInExpression(ast)
        
        # E1...En must be integer
        for idx in ast.idx :
            idxSymbol = self.visit(idx,o)
            if(not isinstance(idxSymbol.mtype,ArrayType)):
                self.inferType(idxSymbol,IntType())

            if(isinstance(idxSymbol.mtype,MType)):
                if(not isinstance(idxSymbol.mtype.return_type,IntType)):
                    raise TypeMismatchInExpression(ast)
            else:
                if(not isinstance(idxSymbol.mtype,IntType)):
                    raise TypeMismatchInExpression(ast)

        return arrSymbol.mtype.eleSymbol
    
#-------------------------------Statement--------------------------------------#
#------------------------------------------------------------------------------#
    # lhs: LHS (Id, Index) => Identifier()
    # rhs: Expr        ##trường hợp gặp callexp đã tự động getsymbol(kind = Func()) rồi##
    def visitAssign(self, ast, o):
        # lhs (Unknown, ArrayType, Exp khác) <====> rhs (Unknown, Mtype, ArrayType, Exp khác)
        self.cur_stmt = ast
        rhs = self.visit(ast.rhs, o)
        #lhs đc visit sau rhs để phòng trường hợp trong quá trình visit rhs suy diễn đc kiểu của lhs
        lhs = self.visit(ast.lhs, o) 

        print("lhs : ",lhs, "------- rhs : ",rhs)

        self.infer2Side(lhs,rhs,ast)
        # funcSymbolTemp = None
        # if(isinstance(rhs.mtype,MType)):
        #     funcSymbolTemp = rhs
        #     rhs = Symbol(rhs.name,rhs.mtype.return_type) # biến foo(a,b){return 1;} => Symbol(foo,IntType)

        # if(isinstance(lhs.mtype,Unknown)): # TypeCannotBeInferred hoặc suy diễn
        #     if(isinstance(rhs.mtype,Unknown)):
        #         raise TypeCannotBeInferred(ast)
        #     elif(isinstance(rhs.mtype,VoidType)):
        #         raise TypeMismatchInStatement(ast)
        #     elif(isinstance(rhs.mtype,ArrayType)):
        #         raise TypeMismatchInStatement(ast)
        #     else:
        #         self.inferType(lhs,rhs.mtype)

        # elif(isinstance(lhs.mtype,ArrayType)):     
        #     if(isinstance(rhs.mtype,Unknown)):
        #         if(funcSymbolTemp == None):
        #             raise TypeMismatchInStatement(ast)
        #         else:
        #             self.inferType(funcSymbolTemp,lhs.mtype)
        #     elif(isinstance(rhs.mtype,VoidType)):
        #         raise TypeMismatchInStatement(ast)
        #     elif(isinstance(rhs.mtype,ArrayType)):
        #         if(len(lhs.mtype.dimen) != len(rhs.mtype.dimen)):
        #             raise TypeMismatchInStatement(ast)
        #         elif(isinstance(lhs.mtype.eleSymbol.mtype,Unknown) and isinstance(rhs.mtype.eleSymbol.mtype,Unknown)):
        #             raise TypeCannotBeInferred(ast)
        #         elif(isinstance(lhs.mtype.eleSymbol.mtype,Unknown) and not isinstance(rhs.mtype.eleSymbol.mtype,Unknown)):
        #             self.inferType(lhs,rhs.mtype.eleSymbol.mtype)
        #         elif(isinstance(rhs.mtype.eleSymbol.mtype,Unknown) and not isinstance(lhs.mtype.eleSymbol.mtype,Unknown)):
        #             self.inferType(rhs,lhs.mtype.eleSymbol.mtype)
        #             if(funcSymbolTemp != None):
        #                 self.inferType(funcSymbolTemp,lhs.mtype)
        #         elif(type(lhs.mtype.eleSymbol.mtype) != type(rhs.mtype.eleSymbol.mtype)):
        #             raise TypeMismatchInStatement(ast)
        #     else:
        #         raise TypeMismatchInStatement(ast)

        # else: # scalar có type
        #     if(isinstance(rhs.mtype,Unknown)):
        #         self.inferType(rhs,lhs.mtype)
        #         if(funcSymbolTemp != None):
        #             self.inferType(funcSymbolTemp,lhs.mtype)
        #     elif(isinstance(rhs.mtype,VoidType)):
        #         raise TypeMismatchInStatement(ast)
        #     elif(isinstance(rhs.mtype,ArrayType)):
        #         raise TypeMismatchInStatement(ast)
        #     elif(type(lhs.mtype) != type(rhs.mtype)):
        #         raise TypeMismatchInStatement(ast)
            
        print("end assign: ",end="")
        self.print_list_env(o)  
        return o
    
    # ifthenStmt:List[Tuple[Expr,List[VarDecl],List[Stmt]]]
    # elseStmt:Tuple[List[VarDecl],List[Stmt]] # for Else branch, empty list if no Else
    def visitIf(self, ast, o):
        self.cur_stmt = ast
        inside_env = o
        for tup in ast.ifthenStmt:
            if(isinstance(tup[0],CallExpr)): # check lỗi từ trái sang phải (vì callexp mới phải check bên ngoài trước (bằng idsymbol ko visit))
                idSymbol = self.getSymbolById(tup[0].method,o,Function())
            else:
                idSymbol = self.visit(tup[0],o)
                
                
            if(not isinstance(idSymbol.mtype,ArrayType)):
                self.inferType(idSymbol,BoolType())

            if(isinstance(idSymbol.mtype,MType)):
                if(not isinstance(idSymbol.mtype.return_type,BoolType)):
                    raise TypeMismatchInStatement(ast)
            else:
                if(not isinstance(idSymbol.mtype,BoolType)):
                    raise TypeMismatchInStatement(ast)

            if(isinstance(tup[0],CallExpr)):
                self.visit(tup[0],o)
            
            lstVardecl = tup[1]
            lstStmt = tup[2]
            new_env = [[]] + o
            inside_env = reduce(lambda acc,ele: self.visit(ele,acc),lstVardecl+lstStmt,new_env)
            o = inside_env[1:] # thay đổi scope ElseIf
            print("#"*20,"end if","#"*20)
            self.print_list_env(o)

        new_env = [[]] + o
        lstVardeclElse = ast.elseStmt[0]
        lstStmtElse = ast.elseStmt[1]
        inside_env = reduce(lambda acc,ele: self.visit(ele,acc),lstVardeclElse+lstStmtElse,new_env)
        print("#"*20,"end else","#"*20)
        self.print_list_env(o)
        return inside_env[1:]
    
    # idx1: Id
    # expr1:Expr
    # expr2:Expr
    # expr3:Expr
    # loop: Tuple[List[VarDecl],List[Stmt]]
    def visitFor(self, ast, o):
        self.cur_stmt = ast
        ########### idx ###########
        idx = self.visit(ast.idx1,o)

        self.inferType(idx,IntType())
        if(not isinstance(idx.mtype,IntType)):
            raise TypeMismatchInStatement(ast)

        print("end idx : ",end="")
        self.print_list_env(o)

        ########### exp1 ###########
        if(isinstance(ast.expr1,CallExpr)): # infer trước visit sau
            exp1 = self.getSymbolById(ast.expr1.method,o,Function())
        else:
            exp1 = self.visit(ast.expr1,o)

        self.inferType(exp1,IntType())

        if(isinstance(exp1.mtype,MType)):
            if(isinstance(exp1.mtype.return_type,IntType)):
                pass
            else:
                raise TypeMismatchInStatement(ast)
        else:
            if(not isinstance(exp1.mtype,IntType)):
                raise TypeMismatchInStatement(ast)
        
        if(isinstance(ast.expr1,CallExpr)):
            exp1 = self.visit(ast.expr1,o)

        print("end exp1 : ",end="")
        self.print_list_env(o)  

        ########### exp2 ###########
        if(isinstance(ast.expr2,CallExpr)):
            exp2 = self.getSymbolById(ast.expr2.method,o,Function())
        else:
            exp2 = self.visit(ast.expr2,o)

        self.inferType(exp2,BoolType())

        if(isinstance(exp2.mtype,MType)):
            if(isinstance(exp2.mtype.return_type,BoolType)):
                pass 
            else:
                raise TypeMismatchInStatement(ast)
        else:
            if(not isinstance(exp2.mtype,BoolType)):
                raise TypeMismatchInStatement(ast)

        if(isinstance(ast.expr2,CallExpr)):
            exp2 = self.visit(ast.expr2,o)

        print("end exp2 : ",end="")
        self.print_list_env(o)

        ########### exp3 ###########
        if(isinstance(ast.expr3,CallExpr)):
            exp3 = self.getSymbolById(ast.expr3.method,o,Function())
        else:
            exp3 = self.visit(ast.expr3,o)

        self.inferType(exp3,IntType())

        if(isinstance(exp3.mtype,MType)):
            if(isinstance(exp3.mtype.return_type,IntType)):
                pass
            else:
                raise TypeMismatchInStatement(ast)
        else:
            if(not isinstance(exp3.mtype,IntType)):
                raise TypeMismatchInStatement(ast)
        
        if(isinstance(ast.expr3,CallExpr)):
            exp3 = self.visit(ast.expr3,o)

        print("end exp3 : ",end="")
        self.print_list_env(o)

        ########### vardecl & stmt ###########
        lstVardecl = ast.loop[0]
        lstStmt = ast.loop[1]
        new_env = [[]] + o
        inside_env = reduce(lambda acc,ele: self.visit(ele,acc),lstVardecl,new_env)
        inside_env = reduce(lambda acc,ele: self.visit(ele,acc),lstStmt,inside_env)

        print("end for: ",end="")
        self.print_list_env(inside_env[1:])
        return inside_env[1:]
    
    def visitContinue(self, ast, o):
        return o
    
    def visitBreak(self, ast, o):
        return o
    
    # expr:Expr # None if no expression
    def visitReturn(self, ast, o):
        # return exp (Unknown, ArrayType, Exp khác) <====> return_type (Unknown, Mtype, ArrayType, Exp khác)
        self.cur_stmt = ast
        if(ast.expr == None):
            returnSym = Symbol(None,VoidType())
        elif(isinstance(ast.expr,CallExpr)): # infer trước visit sau
            returnSym = self.getSymbolById(ast.expr.method,o,Function())
        else:
            returnSym = self.visit(ast.expr,o)

        print("in return : ",returnSym,"----",self.cur_function)
        self.infer2Side(returnSym,self.cur_function,ast)
        if(isinstance(ast.expr,CallExpr)):
            self.visit(ast.expr,o)
        print("end return : ",end="")
        self.print_list_env(o)
        return o
    
    # sl:Tuple[List[VarDecl],List[Stmt]]
    # exp: Expr
    def visitDowhile(self, ast, o):
        self.cur_stmt = ast
        lstVardecl = ast.sl[0]
        lstStmt = ast.sl[1]
        new_env = [[]] + o
        inside_env = reduce(lambda acc,ele: self.visit(ele,acc),lstVardecl,new_env)
        inside_env = reduce(lambda acc,ele: self.visit(ele,acc),lstStmt,inside_env)

        if(isinstance(ast.exp,CallExpr)): # infer trước visit sau
            exp = self.getSymbolById(ast.exp.method,o,Function())
        else:
            exp = self.visit(ast.exp,o)

        self.inferType(exp,BoolType())

        if(isinstance(ast.exp,CallExpr)):
            self.visit(ast.exp,o)

        if(isinstance(exp.mtype,MType)):
            if(isinstance(exp.mtype.return_type,BoolType)):
                pass 
            else:
                raise TypeMismatchInStatement(ast)
        else:
            if(not isinstance(exp.mtype,BoolType)):
                raise TypeMismatchInStatement(ast)

        return inside_env[1:]

    # exp: Expr
    # sl:Tuple[List[VarDecl],List[Stmt]]
    def visitWhile(self, ast, o):
        self.cur_stmt = ast

        if(isinstance(ast.exp,CallExpr)): #infer trước visit sau
            exp = self.getSymbolById(ast.exp.method,o,Function())
        else:
            exp = self.visit(ast.exp,o)

        self.inferType(exp,BoolType())

        if(isinstance(ast.exp,CallExpr)):
            self.visit(ast.exp,o)

        if(isinstance(exp.mtype,MType)):
            if(isinstance(exp.mtype.return_type,BoolType)):
                pass 
            else:
                raise TypeMismatchInStatement(ast)
        else:
            if(not isinstance(exp.mtype,BoolType)):
                raise TypeMismatchInStatement(ast)

        lstVardecl = ast.sl[0]
        lstStmt = ast.sl[1]
        new_env = [[]] + o
        inside_env = reduce(lambda acc,ele: self.visit(ele,acc),lstVardecl,new_env)
        inside_env = reduce(lambda acc,ele: self.visit(ele,acc),lstStmt,inside_env)

        print("end while: ",end="")
        self.print_list_env(inside_env[1:])
        return inside_env[1:]

    # method:Id
    # param:List[Expr]
    def visitCallStmt(self, ast, o):
        # param (Unknown, ArrayType) <====> arg (Unknown, Mtype, ArrayType, Exp khác)
        self.cur_stmt = ast
        funcSymbol = self.getSymbolById(ast.method,o,Function())

        if(not isinstance(funcSymbol.mtype,MType)):
            raise Undeclared(Function(),funcSymbol.name)

        self.inferType(funcSymbol,VoidType()) # check lỗi từ trái sang phải
        if(not isinstance(funcSymbol.mtype.return_type,VoidType)):
            raise TypeMismatchInStatement(ast)


        
        lstParam = funcSymbol.mtype.list_param


        if(len(lstParam) != len(ast.param)):
            raise TypeMismatchInStatement(ast)


        for i in range(len(lstParam)):
            if(isinstance(ast.param[i],CallExpr)): # infer trước visit sau
                argSym = self.getSymbolById(ast.param[i].method,o,Function())
            else:
                argSym = self.visit(ast.param[i],o)
            print("call stmt : ",argSym,"------",lstParam[i])
            self.infer2Side(lstParam[i],argSym,ast)

            if(isinstance(ast.param[i],CallExpr)):
                self.visit(ast.param[i],o)    


        print("end funcCall: ",end="")
        self.print_list_env(o)  
        return o
#---------------------------------------LITERAL (exp)----------------------------------#
#--------------------------------------------------------------------------------------#
    
    # value:int
    def visitIntLiteral(self, ast, o):
        return Symbol(None,IntType())
    
    # value:float
    def visitFloatLiteral(self, ast, o):
        return Symbol(None,FloatType())
    
    # value:bool
    def visitBooleanLiteral(self, ast, o):
        return Symbol(None,BoolType())
    
    # value:str
    def visitStringLiteral(self, ast, o):
        return Symbol(None,StringType())

    # value:List[Literal]
    def visitArrayLiteral(self, ast, o):
        list_arr = ast.value[:]
        dimen = []
        dimen.append(len(list_arr))
        list_arr = list_arr[0]

        while isinstance(list_arr,ArrayLiteral) :
            dimen.append(len(list_arr.value))
            list_arr = list_arr.value[0]

        eleSymbol = Symbol(None,self.visit(list_arr, o).mtype)
        return Symbol(None,ArrayType(dimen,eleSymbol))
        # dimen:List[int]
        # eleSymbol: Symbol
