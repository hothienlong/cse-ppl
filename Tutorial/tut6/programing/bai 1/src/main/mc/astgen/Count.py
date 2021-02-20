from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):

    def visitProgram(self,ctx:MCParser.ProgramContext):
        return self.visit(ctx.vardecls())

    def visitVardecls(self,ctx:MCParser.VardeclsContext):
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    def visitVardecltail(self,ctx:MCParser.VardecltailContext): 
        if(ctx.vardecltail() is None):
            return 0
        else:
            return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    def visitVardecl(self,ctx:MCParser.VardeclContext): 
        return self.visit(ctx.mptype()) + self.visit(ctx.ids()) + 1
#đếm dấu ';' ko?

    def visitMptype(self,ctx:MCParser.MptypeContext):
            return 1
            #int hoặc float

    def visitIds(self,ctx:MCParser.IdsContext):
        if(ctx.getChildCount() == 3):
            return 2 + self.visit(ctx.ids())
        else:
            return 1
