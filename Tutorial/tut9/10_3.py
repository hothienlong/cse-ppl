from functools import reduce
from typing import List, Tuple
from abc import ABC, abstractmethod, ABCMeta

class Type(ABC):
    __metaclass__ = ABCMeta
    pass
class Prim(Type):
    __metaclass__ = ABCMeta
    pass
class IntType(Prim):
    pass
class FloatType(Prim):
    pass
class StringType(Prim):
    pass
class BoolType(Prim):
    pass
class Unknown(Type):
    pass

class MType:
    def __init__(self, ptype):
    	self.ptype = ptype

class Symbol:
    def __init__(self, name, stype):
    	self.name = name
    	self.stype = stype

class StaticCheck(Visitor):

	def visitProgram(self, ctx:Program, o):
		self.cur_param_list = []
		self.cur_func = None
		o = reduce(lambda scope, ele: scope + [self.visit(ele, scope)], ctx.decl, [])
		[self.visit(ele, o) for ele in ctx.stmts]

	def visitVarDecl(self, ctx:VarDecl, o):
		for decl in o:
			if type(decl) is not list and decl.name == ctx.name:
				raise Redeclared(ctx)
		return Symbol(ctx.name, Unknown())

	def visitFuncDecl(self,ctx:FuncDecl,o):
		for decl in o:
			if type(decl) is not list and decl.name == ctx.name:
				raise Redeclared(ctx)

		param_list = reduce(lambda scope, ele: scope + [self.visit(ele, scope)], ctx.param, [])
		func = Symbol(ctx.name, MType([param.stype for param in param_list]))
		self.cur_param_list = param_list
		self.cur_func = func

		local_scope = param_list + [[func] + o]
		local_scope = reduce(lambda scope, ele: [self.visit(ele, scope)] + scope, ctx.local, local_scope)

		[self.visit(ele, local_scope) for ele in ctx.stmts]

		self.cur_param_list = []
		self.cur_func = None

		return func 

	def visitCallStmt(self,ctx:CallStmt,o):
		symbol = self.findFuncDecl(ctx, o)
		if len(ctx.args) != len(symbol.stype.ptype):
			raise TypeMismatchInStatement(ctx)
		for (index, arg), param_type in zip(enumerate(ctx.args), symbol.stype.ptype):
			arg_type = self.visit(arg, o)
			if isinstance(arg_type, Unknown) and isinstance(param_type, Unknown):
				raise TypeCannotBeInferred(ctx)
			elif isinstance(arg_type, Unknown):
				arg_type = self.inferType(arg, param_type, o)
			elif isinstance(param_type, Unknown):
				param_type = arg_type
				symbol.stype.ptype[index] = arg_type
			elif type(param_type) != type(arg_type):
				raise TypeMismatchInStatement(ctx)

	def visitAssign(self,ctx:Assign,o):
		lhs = self.visit(ctx.lhs, o) #id
		rhs = self.visit(ctx.rhs, o) #id
		lhs = self.visit(ctx.lhs, o)

		if isinstance(lhs, Unknown) and isinstance(rhs, Unknown):
			raise TypeCannotBeInferred(ctx)
		elif isinstance(rhs, Unknown):
			rhs = self.inferType(ctx.rhs, lhs, o)
		elif isinstance(lhs, Unknown):
			lhs = self.inferType(ctx.lhs, rhs, o)

		if type(lhs) != type(rhs):
			raise TypeMismatchInStatement(ctx)

	def visitIntLit(self,ctx:IntLit,o):
		return IntType()

	def visitFloatLit(self,ctx,o):
		return FloatType()

	def visitBoolLit(self,ctx,o):
		return BoolType()

	def visitId(self,ctx,o):
		for symbol in o:
			if isinstance(symbol, list):
				return self.visitId(ctx, symbol)
			elif symbol.name == ctx.name:
				return symbol.stype
		raise UndeclaredIdentifier(ctx.name)

	def inferType(self, ctx, infertype, o):
		for symbol in o:
			if isinstance(symbol, list):
				return self.inferType(ctx, infertype, symbol)
			elif symbol.name == ctx.name:
				symbol.stype = infertype
				self.inferParamType(ctx, infertype, o)
				return symbol.stype
		raise UndeclaredIdentifier(ctx.name)

	def findFuncDecl(self, ctx, o):
		for symbol in o:
			if isinstance(symbol, list):
				return self.findFuncDecl(ctx, symbol)
			elif symbol.name == ctx.name:
				return symbol
		raise UndeclaredIdentifier(ctx.name)

	def inferParamType(self, ctx, inferType, o):
		for index, par in enumerate(self.cur_param_list):
			if par.name == ctx.name:
				self.cur_func.stype.ptype[index] = inferType