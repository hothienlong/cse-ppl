from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *
from functools import reduce

from main.bkit.utils.AST import ArrayCell, ArrayLiteral, BinaryOp, BooleanLiteral, CallExpr, CallStmt, FuncDecl
class ASTGeneration(BKITVisitor):
    # program: vardecls EOF;
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        return Program(ctx.vardecls().accept(self))

    # vardecls: vardecl vardecltail;
    def visitVardecls(self,ctx:BKITParser.VardeclsContext):
        return ctx.vardecl().accept(self) + ctx.vardecltail().accept(self)

    # vardecltail: vardecl vardecltail | ;
    def visitVardecltail(self,ctx:BKITParser.VardecltailContext): 
        if(ctx.getChildCount() == 0):
            return []
        else:
            return ctx.vardecl().accept(self) + ctx.vardecltail().accept(self)

    # vardecl: mptype ids ';' ;
    def visitVardecl(self,ctx:BKITParser.VardeclContext): 
        return [VarDecl(id,ctx.mptype().accept(self)) for id in ctx.ids().accept(self)]

    # mptype: INTTYPE | FLOATTYPE;
    def visitMptype(self,ctx:BKITParser.MptypeContext):
        return ctx.getChild(0).getText()

    # ids: ID ',' ids | ID; 
    def visitIds(self,ctx:BKITParser.IdsContext):
        if(ctx.getChildCount() == 1):
            return [Id(ctx.ID().getText())]
        else:
            return [Id(ctx.ID().getText())] + ctx.ids().accept(self)
