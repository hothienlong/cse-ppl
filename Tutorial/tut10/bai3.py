    def visitBinExpr(self,ctx,o):
        lcode, ltype = self.visit(ctx.e1, o)
        rcode, rtype = self.visit(ctx.e2, o)
        
        if(ctx.op in ['+','-']):
            if(isinstance(ltype,IntType) and isinstance(rtype,IntType)):
                return lcode + rcode + self.emit.emitADDOP(ctx.op, IntType(), o.frame), IntType()
            else:
                return self.emit.emitADDOP(ctx.op, FloatType(), o.frame), FloatType()
        elif(ctx.op in ['*','/']):
            if(isinstance(ltype,IntType) and isinstance(rtype,IntType)):
                return lcode + rcode + self.emit.emitMULOP(ctx.op, IntType(), o.frame), IntType()
            else:
                return lcode + rcode + self.emit.emitMULOP(ctx.op, FloatType(), o.frame), FloatType()
        elif(ctx.op in ['+.','-.']):
            return lcode + rcode + self.emit.emitADDOP(ctx.op[0], FloatType(), o.frame), FloatType()
        elif(ctx.op in ['*.','/.']):
            return lcode + rcode + self.emit.emitMULOP(ctx.op[0], FloatType(), o.frame), FloatType()
