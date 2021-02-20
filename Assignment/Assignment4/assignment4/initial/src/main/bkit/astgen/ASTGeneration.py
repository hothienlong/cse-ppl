# 1812869
from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *
from functools import reduce

from main.bkit.utils.AST import ArrayCell, ArrayLiteral, BinaryOp, BooleanLiteral, CallExpr, CallStmt, FuncDecl

class ASTGeneration(BKITVisitor):# hiện thực tất cả hàm visit trong class BKITVisitor
#..........................................................
#.....................DECLARATION..........................
#..........................................................
    # program: var_dec*  func_dec* EOF;
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        # return Program([VarDecl(Id(ctx.ID().getText()),[],None)])
        lstVarDec = [x for varDec in ctx.var_dec() for x in varDec.accept(self)] #Var: x,y; Var: z; VarDecl(x), Vardecl(y), Vardec(z)
        lstFuncDec = [funcDec.accept(self) for funcDec in ctx.func_dec()] #func()
        lstDecl = lstVarDec + lstFuncDec
        return Program(lstDecl)
        # mỗi varDec là 1 list vì sẽ tách Var: a,b,c; thì 3 cái Var ([Vara,Varb,Varc])
        # funcDec ko có flatten vì ko khai báo nhiêu hàm trong 1 funcDec


    # var_dec: VAR COLON var_list SEMI;
    def visitVar_dec(self, ctx:BKITParser.Var_decContext):
        return ctx.var_list().accept(self)


    # var_list: variable (COMMA variable)* ;
    def visitVar_list(self, ctx:BKITParser.Var_listContext):
        lstVariable = ctx.variable()
        return [variable.accept(self) for variable in lstVariable]
        #variable là 1 Var đơn nên ko cần flatten
        # Program[Vardecl(Id(a),[],2),Vardecl(Id(b),[],None)] =>Var: a=2; Var: b;


     # variable: non_initial | initial ;
    def visitVariable(self, ctx:BKITParser.VariableContext):
        # if(ctx.non_initial()):
        #     return ctx.non_initial().accept(self)
        # else:
        #     return ctx.initial().accept(self)
        return self.visitChildren(ctx)


    # non_initial: var_primitive | var_array ;
    def visitNon_initial(self, ctx:BKITParser.Non_initialContext):
        varInit = None
        if(ctx.var_primitive()):
            id = ctx.var_primitive().accept(self)
            varDimen = []
            return VarDecl(id,varDimen,varInit)
        else:
            array = ctx.var_array().accept(self)
            id = array[0]
            varDimen = array[1]
            return VarDecl(id,varDimen,varInit)


    # var_primitive: IDENTIFIER ;
    def visitVar_primitive(self, ctx:BKITParser.Var_primitiveContext):
        return Id(ctx.IDENTIFIER().getText())


    # var_array: IDENTIFIER ('[' INTEGER_LITERAL ']')+ ;
    def visitVar_array(self, ctx:BKITParser.Var_arrayContext):
        id = Id(ctx.IDENTIFIER().getText())
        varDimen = [int(intLit.getText()) for intLit in ctx.INTEGER_LITERAL()]
        return id,varDimen
        #trả về 1 tuple(id,varDimen)


    # initial:  var_primitive ASSIGN literal 
            # | var_array ASSIGN literal 
            # ;
    def visitInitial(self, ctx:BKITParser.InitialContext):
        if(ctx.var_primitive()):
            id = ctx.var_primitive().accept(self)
            varDimen = []
            varInit = ctx.literal().accept(self)
            return VarDecl(id,varDimen,varInit)
        else:
            id,varDimen = ctx.var_array().accept(self) #(id,varDimen)
            varInit = ctx.literal().accept(self)
            return VarDecl(id,varDimen,varInit)           


    # literal
    # : INTEGER_LITERAL
    # | FLOAT_LITERAL
    # | boolean_literal
    # | STRING_LITERAL
    # | array_literal
    # ;
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        if(ctx.INTEGER_LITERAL()):
            return IntLiteral(int(ctx.INTEGER_LITERAL().getText(), 0)) # chỉ định số 0 để đoán tiền tố cho str
        elif(ctx.FLOAT_LITERAL()):
            return FloatLiteral(float(ctx.FLOAT_LITERAL().getText()))
        elif(ctx.boolean_literal()):
            return ctx.boolean_literal().accept(self)
        elif(ctx.STRING_LITERAL()):
            return StringLiteral(ctx.STRING_LITERAL().getText())
        elif(ctx.array_literal()):
            return ctx.array_literal().accept(self)


    # boolean_literal: TRUE | FALSE ;
    def visitBoolean_literal(self, ctx:BKITParser.Boolean_literalContext):
        # if(ctx.TRUE()):
        #     return BooleanLiteral(eval(ctx.TRUE().getText()))
        # else:
        #     return BooleanLiteral(eval(ctx.FALSE().getText()))
        return BooleanLiteral(eval(ctx.getChild(0).getText()))


    # array_literal: '{' (literal (',' literal)*)? '}' ;
    def visitArray_literal(self, ctx:BKITParser.Array_literalContext):
        lstLiteral = [literal.accept(self) for literal in ctx.literal()]
        return ArrayLiteral(lstLiteral)
    

    # func_dec: FUNCTION COLON IDENTIFIER 
            # (PARAMETER COLON var_list)? 
            # BODY COLON list_stmt ENDBODY '.'
            # ;
    def visitFunc_dec(self, ctx:BKITParser.Func_decContext):
        id = Id(ctx.IDENTIFIER().getText())
        if(ctx.var_list()):
            param = ctx.var_list().accept(self)
        else:
            param = []
        body = ctx.list_stmt().accept(self) #tuple(list[vardec],list[stmt])
        return FuncDecl(id,param,body)
        # trường hợp này var_list là 1 def trả về đối tượng, chỉ có thể null hoặc ko (ko có [])




#..........................................................
#..............FUNCTION_BODY----STATEMENT..................
#..........................................................  

    # list_stmt: list_vardec stmt* ;
    def visitList_stmt(self, ctx:BKITParser.List_stmtContext):
        lstVardec = ctx.list_vardec().accept(self)
        lstStmt = [stmt.accept(self) for stmt in ctx.stmt()]
        return lstVardec,lstStmt #tuple


    # list_vardec: var_dec* ;
    def visitList_vardec(self, ctx:BKITParser.List_vardecContext):
        lstVarDec = ctx.var_dec()
        return [var for var_dec in lstVarDec for var in var_dec.accept(self)]
        # bao gồm var_dec*, trong đó 1 vardec là 1 list var(a,b=2,c)


    # stmt: assign_stmt
        # | if_stmt
        # | for_stmt
        # | while_stmt 
        # | do_while_stmt
        # | break_stmt
        # | continue_stmt
        # | call_stmt
        # | return_stmt
        # ;
    def visitStmt(self, ctx:BKITParser.StmtContext):
        return self.visitChildren(ctx)
        # Visit a parse tree produced by BKITParser#stmt.


    # assign_stmt: var_primitive ASSIGN exp SEMI
            #    | index_exp ASSIGN exp  SEMI
            #    ;
    def visitAssign_stmt(self, ctx:BKITParser.Assign_stmtContext):
        if(ctx.var_primitive()):
            lhs = ctx.var_primitive().accept(self)
            rhs = ctx.exp().accept(self)
            return Assign(lhs,rhs)
        else:
            # lstExp = [exp.accept(self) for exp in ctx.exp()]
            # arrayCell = ArrayCell(ctx.exp(0).accept(self),lstExp[1:])
            lhs = ctx.index_exp().accept(self) #return arraycell
            rhs = ctx.exp().accept(self)
            return Assign(lhs,rhs)           


    # if_stmt: IF exp THEN list_stmt
            # (ELSEIF exp THEN list_stmt)*
            # (ELSE list_stmt)?
            # ENDIF DOT
            # ;
    def visitIf_stmt(self, ctx:BKITParser.If_stmtContext):
        # ifthenStmt:List[Tuple[Expr,List[VarDecl],List[Stmt]]]
        ifthenStmt = []
        for i in range(len(ctx.exp())):
            tupVardecStmt = ctx.list_stmt(i).accept(self)
            tup = ctx.exp(i).accept(self),tupVardecStmt[0],tupVardecStmt[1]
            ifthenStmt.append(tup)
        if(ctx.ELSE()):
            # elseStmt:Tuple[List[VarDecl],List[Stmt]]       
            elseStmt = ctx.list_stmt(len(ctx.list_stmt())-1).accept(self)
            return If(ifthenStmt,elseStmt)
        else:
            elseStmt = ([],[])
            return If(ifthenStmt,elseStmt)

        


    # for_stmt: FOR LP var_primitive ASSIGN exp COMMA exp COMMA exp RP DO
            #       list_stmt
            #   ENDFOR '.'
            #   ;
    def visitFor_stmt(self, ctx:BKITParser.For_stmtContext):
        idx1 = ctx.var_primitive().accept(self)
        expr1 = ctx.exp(0).accept(self)
        expr2 = ctx.exp(1).accept(self)
        expr3 = ctx.exp(2).accept(self)
        loop = ctx.list_stmt().accept(self)
        return For(idx1,expr1,expr2,expr3,loop)


    # while_stmt: WHILE exp DO list_stmt ENDWHILE '.' ;
    def visitWhile_stmt(self, ctx:BKITParser.While_stmtContext):
        exp = ctx.exp().accept(self)
        sl = ctx.list_stmt().accept(self)
        return While(exp,sl)


    # do_while_stmt: DO list_stmt WHILE exp ENDDO '.' ;
    def visitDo_while_stmt(self, ctx:BKITParser.Do_while_stmtContext):
        exp = ctx.exp().accept(self)
        sl = ctx.list_stmt().accept(self)
        return Dowhile(sl,exp)

    # break_stmt: BREAK SEMI ;
    def visitBreak_stmt(self, ctx:BKITParser.Break_stmtContext):
        return Break()


    # continue_stmt: CONTINUE SEMI ;
    def visitContinue_stmt(self, ctx:BKITParser.Continue_stmtContext):
        return Continue()


    # call_stmt: func_call_exp SEMI ;
    def visitCall_stmt(self, ctx:BKITParser.Call_stmtContext):
        funcCallExp = ctx.func_call_exp().accept(self)
        id = funcCallExp.method 
        lstExp = funcCallExp.param
        return CallStmt(id,lstExp)


    # return_stmt: RETURN exp? SEMI ;
    def visitReturn_stmt(self, ctx:BKITParser.Return_stmtContext):
        if(ctx.exp()):
            return Return(ctx.exp().accept(self))
        else:
            return Return(None)


    # exp: relational_exp ;
    def visitExp(self, ctx:BKITParser.ExpContext):
        return ctx.relational_exp().accept(self)


    # Visit a parse tree produced by BKITParser#relational_exp.
    def visitRelational_exp(self, ctx:BKITParser.Relational_expContext):
        if(ctx.getChildCount() == 1):
            return ctx.logical_binary_exp(0).accept(self)
        else:
            op = ctx.getChild(1).getText()
            left = ctx.logical_binary_exp(0).accept(self)
            right = ctx.logical_binary_exp(1).accept(self)
            return BinaryOp(op,left,right)


    # Visit a parse tree produced by BKITParser#logical_binary_exp.
    def visitLogical_binary_exp(self, ctx:BKITParser.Logical_binary_expContext):
        if(ctx.getChildCount() == 1):
            return ctx.adding_exp().accept(self)
        else:
            op = ctx.getChild(1).getText()
            left = ctx.logical_binary_exp().accept(self)
            right = ctx.adding_exp().accept(self)
            return BinaryOp(op,left,right)


    # Visit a parse tree produced by BKITParser#adding_exp.
    def visitAdding_exp(self, ctx:BKITParser.Adding_expContext):
        if(ctx.getChildCount() == 1):
            return ctx.multiplying_exp().accept(self)
        else:
            op = ctx.getChild(1).getText()
            left = ctx.adding_exp().accept(self)
            right = ctx.multiplying_exp().accept(self)
            return BinaryOp(op,left,right)


    # Visit a parse tree produced by BKITParser#multiplying_exp.
    def visitMultiplying_exp(self, ctx:BKITParser.Multiplying_expContext):
        if(ctx.getChildCount() == 1):
            return ctx.logical_unary_exp().accept(self)
        else:
            op = ctx.getChild(1).getText()
            left = ctx.multiplying_exp().accept(self)
            right = ctx.logical_unary_exp().accept(self)
            return BinaryOp(op,left,right)


    # Visit a parse tree produced by BKITParser#logical_unary_exp.
    def visitLogical_unary_exp(self, ctx:BKITParser.Logical_unary_expContext):
        if(ctx.getChildCount() == 1):
            return ctx.sign_exp().accept(self)
        else:
            op = ctx.getChild(0).getText()
            arg = ctx.logical_unary_exp().accept(self)
            return UnaryOp(op,arg)


    # Visit a parse tree produced by BKITParser#sign_exp.
    def visitSign_exp(self, ctx:BKITParser.Sign_expContext):
        if(ctx.getChildCount() == 1):
            return ctx.index_exp().accept(self)
        else:
            op = ctx.getChild(0).getText()
            arg = ctx.sign_exp().accept(self)
            return UnaryOp(op,arg)


    # index_exp
        # : operand ('[' exp ']')+ //muốn gọi biểu thức ko ()
        # | operand
        # ;
    def visitIndex_exp(self, ctx:BKITParser.Index_expContext):
        if(ctx.getChildCount() == 1):
            return ctx.operand().accept(self)
        else:
            lstExp = [exp.accept(self) for exp in ctx.exp()]
            arr = ctx.operand().accept(self)
            idx = lstExp
            return ArrayCell(arr,idx)
            # UnaryOp("[3]",Id("a")) => a[3]
            # UnaryOp("[6]",UnaryOp("[2]",Id("arr"))) => arr[2][6]


    # Visit a parse tree produced by BKITParser#operand.
    def visitOperand(self, ctx:BKITParser.OperandContext):
        if(ctx.IDENTIFIER()):
            return Id(ctx.IDENTIFIER().getText())
        elif(ctx.literal()):
            return ctx.literal().accept(self)
        elif(ctx.func_call_exp()):
            return ctx.func_call_exp().accept(self)
        else:
            return ctx.exp().accept(self)


    # func_call_exp
        # : IDENTIFIER '(' (exp (COMMA exp)*)? ')' 
        # ;
    def visitFunc_call_exp(self, ctx:BKITParser.Func_call_expContext):
        id = Id(ctx.IDENTIFIER().getText())
        lstExp = [exp.accept(self) for exp in ctx.exp()]
        return CallExpr(id,lstExp)
        #if(ctx.exp() == null)?
        # hay vẫn sinh ra def exp() nhưng trả về []


