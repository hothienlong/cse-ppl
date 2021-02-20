from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):
    # program: vardecl+ EOF;
    def visitProgram(self,ctx:MCParser.ProgramContext):
        return None # return a Program object

    # vardecl: mctype manyvar ;
    def visitVardecl(self,ctx:MCParser.VardeclContext):
        typ = self.visit(ctx.mctype())
        return None # return the list of VarDecl
  	
    # mctype: INTTYPE | FLOATTYPE ;
    def visitMctype(self,ctx:MCParser.MctypeContext):
        if ctx.INTTYPE():
            return IntType()
        else:
            return FloatType()

    # manyvar: var (COMMA var)* ;
    def visitManyvar(self,ctx:MCParser.ManyvarContext):
        return None

    # var: ID (LSB INTLIT RSB)? ;
    def visitVar(self,ctx:MCParser.VarContext):
        return None 