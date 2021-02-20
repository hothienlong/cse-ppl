from functools import reduce
class ASTGeneration(MPVisitor):
    # program: exp EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return ctx.exp().accept(self)

    # exp: (term ASSIGN)* term;    
    #=> cách viết của kết hợp phải
    def visitExp(self,ctx:MPParser.ExpContext):
        if(ctx.ASSIGN()):
            lstTermDecs = ctx.term()[::-1] #{term1,term2}
            lastTerm = ctx.term(len(lstTermDecs)-1).accept(self) #term2
            lstOpDecs = ctx.ASSIGN()[::-1]
            lstZip = list(zip(lstOpDecs,lstTermDecs[1:]))
            #dùng zip để duyệt cả 2 danh sách song song tương hỗ nhau
                
            return reduce(lambda acc, zipItem: Binary(zipItem[0].getText(),zipItem[1].accept(self),acc), lstZip, lastTerm) 
            #acc là biến cộng dồn, bao gồm một nùi Binary
            #a := b := 4 là kết hợp phải => đảo ngược danh sách
            #lstTerm[-2::-1] => đảo ngược danh sách và bỏ đi phần tử cuối
            #giả sử lstTerm chỉ có 1 phần tử sẽ ko nhảy vào hàm lambda => operator.getText() sẽ ko thực thi
            #=> ko cần trường hợp if(childCount == 1)
        return ctx.term(0).accept(self)


    # term: factor COMPARE factor | factor;
    def visitTerm(self,ctx:MPParser.TermContext): 
        if(ctx.getChildCount() == 1):
            return ctx.factor(0).accept(self)
        else:
            left = ctx.factor(0).accept(self)
            right = ctx.factor(1).accept(self)
            op = ctx.COMPARE().getText()
            return Binary(op,left,right)

    # factor: operand (ANDOR operand)*; 
    #=> cách viết của kết hợp trái
    def visitFactor(self,ctx:MPParser.FactorContext):
        if(ctx.ANDOR()):
            lstOperand = ctx.operand()
            lstOp = ctx.ANDOR()
            lstZip = list(zip(lstOp,lstOperand[1:]))
            firstOperand = ctx.operand(0).accept(self)
            return reduce(lambda acc, zipItem: Binary(zipItem[0].getText(),acc,zipItem[1].accept(self)), lstZip, firstOperand)
        return ctx.operand(0).accept(self)
    # operand: ID | INTLIT | BOOLIT | '(' exp ')';
    def visitOperand(self,ctx:MPParser.OperandContext):
        if(ctx.getChildCount() == 1):
            if(ctx.getChild(0) is ctx.ID()):
                return Id(ctx.getChild(0).getText())
            elif(ctx.getChild(0) is ctx.INTLIT()):
                return IntLiteral(ctx.getChild(0).getText())
            elif(ctx.getChild(0) is ctx.BOOLIT()):
                return BooleanLiteral(ctx.getChild(0).getText())
		#ko nên ép bool("False") sẽ bằng True => dùng eval
        else:
            return ctx.exp().accept(self)
