from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

#đếm node trên cây AST
class Count(MCVisitor):
    # program: vardecls EOF;
    def visitProgram(self,ctx:MCParser.ProgramContext):
        return 2 + self.visit(ctx.vardecls())
    #ctx.vardecls() trả về danh sách node trên cây parsetree

    # mctype: INTTYPE | FLOATTYPE | ARRAY LB INTLIT RB OF mctype ;
    def visitMctype(self,ctx:MCParser.MctypeContext):
        if ctx.getChildCount() == 6:
            # return number of leaf nodes from the third right hand side
            return 6 + self.visit(ctx.mctype())
        else:
            # return number of leaf nodes from the first or second right hand side
            return 1

    # vardecls: vardecl vardecls | vardecl ;
    def visitVardecls(self,ctx:MCParser.VardeclsContext):
        if ctx.getChildCount() == 2:
            # return number of leaf nodes from the first right hand side
            return 2 + self.visit(ctx.vardecl()) + self.visit(ctx.vardecls())
        else:
            # return number of leaf nodes from the first right hand side
            return 2 + self.visit(ctx.vardecl())
  	
    # vardecl: mctype ids SEMI ;
    def visitVardecl(self,ctx:MCParser.VardeclContext):
        return 3 + self.visit(ctx.mctype()) + self.visit(ctx.ids()) 

    # ids: ID (COMMA ID)* ;
    def visitIds(self,ctx:MCParser.IdsContext):
        return 2
        #(comma id)*

