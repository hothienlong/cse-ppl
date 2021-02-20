    def visitBinExpr(self,ctx,o):
        lcode, ltype = self.visit(ctx.e1, o)
        rcode, rtype = self.visit(ctx.e2, o)
        
        if(isinstance(ltype,FloatType) and not isinstance(rtype,FloatType)):
            mtype = FloatType()
            rcode = rcode + self.emit.emitI2F(o.frame)
        elif(isinstance(rtype,FloatType) and not isinstance(ltype,FloatType)):
            mtype = FloatType()
            lcode = lcode + self.emit.emitI2F(o.frame)
        elif(ctx.op == '/'):
            lcode = lcode + self.emit.emitI2F(o.frame)
            rcode = rcode + self.emit.emitI2F(o.frame)
            mtype = FloatType()
        else:
            mtype = ltype
        
        if(ctx.op in ['+','-']):
            return lcode + rcode + self.emit.emitADDOP(ctx.op, mtype, o.frame), mtype
        elif(ctx.op in ['*','/']):
            return lcode + rcode + self.emit.emitMULOP(ctx.op, mtype, o.frame), mtype
        elif(ctx.op in ['>','<','>=','<=','==','!=']):
            return lcode + rcode + self.emit.emitREOP(ctx.op, mtype, o.frame), BoolType()
