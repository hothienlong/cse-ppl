    def visitId(self,ctx,o):
        for symbol in o.sym:
            if(ctx.name == symbol.name):
                sym = symbol
                break
                
        if(isinstance(sym.value,Index)):
            return self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, o.frame), sym.mtype
        else:
            return self.emit.emitGETSTATIC(sym.value.value + "." + sym.name, sym.mtype, o.frame), sym.mtype