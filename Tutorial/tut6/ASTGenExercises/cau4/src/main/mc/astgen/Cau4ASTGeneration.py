from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *
import functools

class ASTGeneration(MCVisitor):
	# exp: term COMPARE term | term ;
    def visitExp(self,ctx:MCParser.ExpContext):
        if ctx.getChildCount() == 3:
            return None # return a Binary object for the first right hand side
        else:
            return None # generate code for the second right hand side

    # term: factor EXPONENT term | factor ;
    def visitTerm(self,ctx:MCParser.TermContext):
        if ctx.getChildCount() == 3:
            return None # return a Binary object for the first right hand side
        else:
            return None # generate code for the second right hand side

    # factor: operand (ANDOR operand)* ; 
    def visitFactor(self,ctx:MCParser.FactorContext):
        return None # return a Binary object 
  
  	# operand: INTLIT | BOOLIT | LB exp RB ;
    def visitOperand(self,ctx:MCParser.OperandContext):
        if ctx.getChildCount() == 3:
            return None # generate code for the third right hand side
        elif ctx.INTLIT():
            return None # return a IntLit object
        return None # return a BoolLit object

