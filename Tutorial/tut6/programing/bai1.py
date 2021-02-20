class ASTGeneration(MPVisitor):
    # program: vardecls EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return 1 + ctx.vardecls().accept(self)

    # vardecls: vardecl vardecltail;
    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        return ctx.vardecl().accept(self) + ctx.vardecltail().accept(self)

    # vardecltail: vardecl vardecltail | ;
    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
        if(ctx.getChildCount() == 0):
            return 0
        else:
            return ctx.vardecl().accept(self) + ctx.vardecltail().accept(self)

    # vardecl: mptype ids ';' ;
    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return 1 + ctx.mptype().accept(self) + ctx.ids().accept(self)

    # mptype: INTTYPE | FLOATTYPE;
    def visitMptype(self,ctx:MPParser.MptypeContext):
        return 1

    # ids: ID ',' ids | ID; 
    def visitIds(self,ctx:MPParser.IdsContext):
        if(ctx.getChildCount() == 1):
            return 1
        else:
            return 2 + ctx.ids().accept(self)