    def visitFloatLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(ast.value, frame), FloatType()