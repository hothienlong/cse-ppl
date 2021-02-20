class ASTGeneration(MPVisitor):
    # program: vardecls EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program(ctx.vardecls().accept(self))

    # vardecls: vardecl vardecltail;
    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        return ctx.vardecl().accept(self) + ctx.vardecltail().accept(self)
        #1 list [1 đối tượng] + 1 list [nhiều đối tượng], gom vô 1 list

    # vardecltail: vardecl vardecltail | ;
    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
        if(ctx.getChildCount() == 0):
            return []
        else:
            return ctx.vardecl().accept(self) + ctx.vardecltail().accept(self)

    # vardecl: mptype ids ';' ;
    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        var_type = ctx.mptype().accept(self)
        id_list = ctx.ids().accept(self)
        return list(map(lambda x: VarDecl(x,var_type),id_list))
                        #x là 1 id trong list            

    # mptype: INTTYPE | FLOATTYPE;
    def visitMptype(self,ctx:MPParser.MptypeContext):
        if(ctx.INTTYPE() != None):
            return IntType() #1 đối tượng ko có định nghĩa
        else:
            return FloatType()

    # ids: ID ',' ids | ID; 
    def visitIds(self,ctx:MPParser.IdsContext):
        if(ctx.getChildCount() == 1):
            return [Id(ctx.ID().getText())] #bắt đầu định nghĩa phần tử nhỏ nhất nằm trong list
        else:
            return [Id(ctx.ID().getText())] + ctx.ids().accept(self)

