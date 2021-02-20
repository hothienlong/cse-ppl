from functools import reduce
class ASTGeneration(MPVisitor):
    # program: vardecl+ EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program(reduce(
            lambda acc,vardeclItem: acc+vardeclItem.accept(self), ctx.vardecl()[1:],ctx.vardecl(0).accept(self))
            )
        # list_vardecl = ctx.vardecl()
        # return Program([x for vardecl in list_vardecl for x in vardecl.accept(self)])
        # ctx.vardecl() để lấy 1 list
        # vardecl_list là [[vardecl1,vardecl2],[vardecl3],[vardecl4]] => phải flatten

    # vardecl: mptype ids ';' ; ids,vardecl+ là list=>list của list=>flatten
    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        var_type = ctx.mptype().accept(self)
        id_list = ctx.ids().accept(self) #ctx.ids() ko phải 1 list nhưng ctx.ids().accept là 1 list
        return [VarDecl(id, var_type) for id in id_list]
        #[VarDecl([Ids(a)],IntType),VarDecl([Id(b),Id(c)],FloatType)]  

    # mptype: INTTYPE | FLOATTYPE;
    def visitMptype(self,ctx:MPParser.MptypeContext):
        if ctx.INTTYPE() :
            return IntType()
        else:
            return FloatType()

    # ids: ID (',' ID)*; 
    def visitIds(self,ctx:MPParser.IdsContext):
        return [Id(id.getText()) for id in ctx.ID()]
        #có 2 ID => ctx.ID() là 1 list
