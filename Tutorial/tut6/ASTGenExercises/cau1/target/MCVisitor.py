# Generated from main/mc/parser/MC.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var_dec.
    def visitVar_dec(self, ctx:MCParser.Var_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var_list.
    def visitVar_list(self, ctx:MCParser.Var_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#variable.
    def visitVariable(self, ctx:MCParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#non_initial.
    def visitNon_initial(self, ctx:MCParser.Non_initialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var_primitive.
    def visitVar_primitive(self, ctx:MCParser.Var_primitiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var_array.
    def visitVar_array(self, ctx:MCParser.Var_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#initial.
    def visitInitial(self, ctx:MCParser.InitialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#literal.
    def visitLiteral(self, ctx:MCParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#boolean_literal.
    def visitBoolean_literal(self, ctx:MCParser.Boolean_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#array_literal.
    def visitArray_literal(self, ctx:MCParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#func_dec.
    def visitFunc_dec(self, ctx:MCParser.Func_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#list_vardec.
    def visitList_vardec(self, ctx:MCParser.List_vardecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#list_stmt.
    def visitList_stmt(self, ctx:MCParser.List_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#stmt.
    def visitStmt(self, ctx:MCParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#assign_stmt.
    def visitAssign_stmt(self, ctx:MCParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#if_stmt.
    def visitIf_stmt(self, ctx:MCParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#for_stmt.
    def visitFor_stmt(self, ctx:MCParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#while_stmt.
    def visitWhile_stmt(self, ctx:MCParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#do_while_stmt.
    def visitDo_while_stmt(self, ctx:MCParser.Do_while_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#break_stmt.
    def visitBreak_stmt(self, ctx:MCParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#continue_stmt.
    def visitContinue_stmt(self, ctx:MCParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#call_stmt.
    def visitCall_stmt(self, ctx:MCParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#return_stmt.
    def visitReturn_stmt(self, ctx:MCParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp.
    def visitExp(self, ctx:MCParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#relational_exp.
    def visitRelational_exp(self, ctx:MCParser.Relational_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#logical_binary_exp.
    def visitLogical_binary_exp(self, ctx:MCParser.Logical_binary_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#adding_exp.
    def visitAdding_exp(self, ctx:MCParser.Adding_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#multiplying_exp.
    def visitMultiplying_exp(self, ctx:MCParser.Multiplying_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#logical_unary_exp.
    def visitLogical_unary_exp(self, ctx:MCParser.Logical_unary_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#sign_exp.
    def visitSign_exp(self, ctx:MCParser.Sign_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#index_exp.
    def visitIndex_exp(self, ctx:MCParser.Index_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#operand.
    def visitOperand(self, ctx:MCParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#func_call_exp.
    def visitFunc_call_exp(self, ctx:MCParser.Func_call_expContext):
        return self.visitChildren(ctx)



del MCParser