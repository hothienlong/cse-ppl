from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):

    # program: vardecls EOF;
    def visitProgram(self,ctx:MCParser.ProgramContext):
        return None # return a Program object
    
    # vardecls: vardecl vardecls | vardecl ;
    def visitVardecls(self,ctx:MCParser.VardeclsContext):
        if ctx.getChildCount() == 2:
            return None # return the list of VarDecl for the first right hand side
        else:
            return None # return the list of VarDecl for the second right hand side  

    # vardecl: mctype ids ;
    def visitVardecl(self,ctx:MCParser.VardeclContext):
        return None # return the list of VarDecl objects
  
  	# mctype: INTTYPE | FLOATTYPE ;
    def visitMctype(self,ctx:MCParser.MctypeContext):
        return None # return IntType() or FloatType()

    # ids: ID (COMMA ID)* ;
    def visitIds(self,ctx:MCParser.IdsContext):
        return None # return the list of identifier's lexemes