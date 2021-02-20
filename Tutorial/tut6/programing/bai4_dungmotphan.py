class ASTGeneration(MPVisitor):
    # program: exp EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return ctx.exp().accept(self)

    # exp: term ASSIGN exp | term;    
    def visitExp(self,ctx:MPParser.ExpContext):
        if(ctx.getChildCount() == 1):
            return ctx.term().accept(self)
        else:
            left = ctx.term().accept(self)
            right = ctx.exp().accept(self)
            op = ctx.ASSIGN().getText()
            return Binary(op,left,right) 

    # term: factor COMPARE factor | factor;
    def visitTerm(self,ctx:MPParser.TermContext): 
        if(ctx.getChildCount() == 1):
            return ctx.factor(0).accept(self)
        else:
            left = ctx.factor(0).accept(self)
            right = ctx.factor(1).accept(self)
            op = ctx.COMPARE().getText()
            return Binary(op,left,right)

    # factor: factor ANDOR operand | operand; 
    def visitFactor(self,ctx:MPParser.FactorContext):
        if(ctx.getChildCount() == 1):
            return ctx.operand().accept(self)
        else:
            left = ctx.factor().accept(self)
            right = ctx.operand().accept(self)
            op = ctx.ANDOR().getText()
            return Binary(op,left,right)

    # operand: ID | INTLIT | BOOLIT | '(' exp ')';
    def visitOperand(self,ctx:MPParser.OperandContext):
        if(ctx.getChildCount() == 1):
            if(ctx.getChild(0) is ctx.ID()):
                return Id(ctx.getChild(0).getText())
            elif(ctx.getChild(0) is ctx.INTLIT()):
                return IntLiteral(ctx.getChild(0).getText())
            elif(ctx.getChild(0) is ctx.BOOLIT()):
                return BooleanLiteral(ctx.getChild(0).getText())
        else:
            return ctx.exp.accept(self)