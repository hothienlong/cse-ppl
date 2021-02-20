from functools import reduce

class StaticCheck(Visitor):

	def visitProgram(self, ctx:Program, o):
		# o = reduce(lambda scope, ele: scope + [self.visit(ele, scope)], ctx.decl, [])
		o = [{'name': x.name, 'type': None} for x in ctx.decl]
		[self.visit(ele, o) for ele in ctx.stmts]

	def visitVarDecl(self, ctx:VarDecl, o):
		return {'name': ctx.name, 'type': None}

	def visitAssign(self,ctx:Assign,o):
		lhs = self.visit(ctx.lhs, o)
		rhs = self.visit(ctx.rhs, o)
		lhs = self.visit(ctx.lhs, o)

		if lhs is None:
			lhs = rhs
			for decl in o:
				if decl['name'] == ctx.lhs.name:
					decl['type'] = rhs
		
		# print("LHS", lhs)
		# print("RHS", rhs)
		if rhs is None:
			raise TypeCannotBeInferred(ctx)
		if lhs != rhs:
			raise TypeMismatchInStatement(ctx)

	def visitBinOp(self,ctx:BinOp,o):
		type1 = self.visit(ctx.e1, o)
		type2 = self.visit(ctx.e2, o)
		# print(ctx.e1, type1)
		# print(ctx.e2, type2)

		if type1 is None and isinstance(ctx.e1, Id):
			type1 = self.inferType(ctx.e1, ctx.op, o)
			# print("after", ctx.e1, type1)
		if type2 is None and isinstance(ctx.e2, Id):
			type2 = self.inferType(ctx.e2, ctx.op, o)
			# print("after", ctx.e2, type2)

		if ctx.op in ["+", "-", "*", "/"]:
			if type1 == "int" and type2 =="int":
				return "int"
		elif ctx.op in ["+.", "-.", "*.", "/."]:
			if type1 == "float" and type2 =="float":
				return "float"
		elif ctx.op in ["&&", "||", ">b", "=b"]:
			if type1 == "bool" and type2 == "bool":
				return "bool"
		elif ctx.op in [">", "="]:
			if type1 == "int" and type2 =="int":
				return "bool"
		elif ctx.op in [">.", "=."]:
			if type1 == "float" and type2 =="float":
				return "bool"
		raise TypeMismatchInExpression(ctx)

	def visitUnOp(self,ctx:UnOp,o):
		exp_type = self.visit(ctx.e, o)
		if exp_type is None and isinstance(ctx.e, Id):
			exp_type = self.inferType(ctx.e, ctx.op, o)

		if ctx.op == "-" and exp_type == "int":
			return "int"
		elif ctx.op == "-." and exp_type == "float":
			return "float"
		elif ctx.op == "!" and exp_type == "bool":
			return "bool"
		elif ctx.op == "i2f" and exp_type == "int":
			return "float"
		elif ctx.op == "floor" and exp_type == "float":
			return "int"
		raise TypeMismatchInExpression(ctx)

	def visitIntLit(self,ctx:IntLit,o):
		return "int"

	def visitFloatLit(self,ctx,o):
		return "float"

	def visitBoolLit(self,ctx,o):
		return "bool"

	def visitId(self,ctx,o):
		for decl in o:
			if decl['name'] == ctx.name:
				return decl['type']
		raise UndeclaredIdentifier(ctx.name)

	def inferType(self, ctx, op, o):
		for decl in o:
			if decl['name'] == ctx.name:
				if decl["type"] is not None:
					return None
				if op in ["+", "-", "*", "/", ">", "=", "i2f"]:
					decl["type"] = "int"
				elif op in ["+.", "-.", "*.", "/.", ">.", "=.", "floor"]:
					decl["type"] = "float"
				elif op in ["!", "&&", "||", ">b", "=b"]:
					decl["type"] = "bool"
				return decl['type']
		raise UndeclaredIdentifier(ctx.name)