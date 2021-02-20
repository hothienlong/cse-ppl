    def visitIntLiteral(self, ast, o):
        frame = o.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()