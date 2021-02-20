# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_dec.
    def visitVar_dec(self, ctx:BKITParser.Var_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_list.
    def visitVar_list(self, ctx:BKITParser.Var_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variable.
    def visitVariable(self, ctx:BKITParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#non_initial.
    def visitNon_initial(self, ctx:BKITParser.Non_initialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_primitive.
    def visitVar_primitive(self, ctx:BKITParser.Var_primitiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_array.
    def visitVar_array(self, ctx:BKITParser.Var_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#initial.
    def visitInitial(self, ctx:BKITParser.InitialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#literal.
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#boolean_literal.
    def visitBoolean_literal(self, ctx:BKITParser.Boolean_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_literal.
    def visitArray_literal(self, ctx:BKITParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_dec.
    def visitFunc_dec(self, ctx:BKITParser.Func_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#list_vardec.
    def visitList_vardec(self, ctx:BKITParser.List_vardecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#list_stmt.
    def visitList_stmt(self, ctx:BKITParser.List_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt.
    def visitStmt(self, ctx:BKITParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assign_stmt.
    def visitAssign_stmt(self, ctx:BKITParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_stmt.
    def visitIf_stmt(self, ctx:BKITParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_stmt.
    def visitFor_stmt(self, ctx:BKITParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_stmt.
    def visitWhile_stmt(self, ctx:BKITParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#do_while_stmt.
    def visitDo_while_stmt(self, ctx:BKITParser.Do_while_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_stmt.
    def visitBreak_stmt(self, ctx:BKITParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continue_stmt.
    def visitContinue_stmt(self, ctx:BKITParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_stmt.
    def visitCall_stmt(self, ctx:BKITParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_stmt.
    def visitReturn_stmt(self, ctx:BKITParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp.
    def visitExp(self, ctx:BKITParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#relational_exp.
    def visitRelational_exp(self, ctx:BKITParser.Relational_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#logical_binary_exp.
    def visitLogical_binary_exp(self, ctx:BKITParser.Logical_binary_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#adding_exp.
    def visitAdding_exp(self, ctx:BKITParser.Adding_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#multiplying_exp.
    def visitMultiplying_exp(self, ctx:BKITParser.Multiplying_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#logical_unary_exp.
    def visitLogical_unary_exp(self, ctx:BKITParser.Logical_unary_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#sign_exp.
    def visitSign_exp(self, ctx:BKITParser.Sign_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_exp.
    def visitIndex_exp(self, ctx:BKITParser.Index_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operand.
    def visitOperand(self, ctx:BKITParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_call_exp.
    def visitFunc_call_exp(self, ctx:BKITParser.Func_call_expContext):
        return self.visitChildren(ctx)



del BKITParser