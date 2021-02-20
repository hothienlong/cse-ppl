import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """int a,b"""
        expect = str(Program([VarDecl(IntType(),'a'),VarDecl(IntType(),'b')]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_more_complicated_program(self):
        input = """int a,b
        float c,d,e
        int m,n"""
        expect = str(Program([VarDecl(IntType(),'a'),
		arDecl(IntType(),'b'),
        	VarDecl(FloatType(),'c'),
		VarDecl(FloatType(),'d'),
		VarDecl(FloatType(),'e'),
        	VarDecl(IntType(),'m'),
		VarDecl(IntType(),'n')]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_single_variable_program(self):
        input = """int a
        float c
        int b"""
        expect = str(Program([VarDecl(IntType(),'a'),
        	VarDecl(FloatType(),'c'),
        	VarDecl(IntType(),'b')]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

       