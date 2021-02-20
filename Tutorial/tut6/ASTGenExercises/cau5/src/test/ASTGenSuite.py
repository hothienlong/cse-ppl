import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """int a,b"""
        expect = str(Program([VarDecl(IntType(),'a'),VarDecl(IntType(),'b')]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_with_array(self):
        input = """int a,b[3],c"""
        expect = str(Program([VarDecl(IntType(),'a'),
        	VarDecl(ArrayType(IntType(),3),'b'),
        	VarDecl(IntType(),'c')]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_many_declarations(self):
        input = """int a,b[3],c
        		   float d[2],e
        """
        expect = str(Program([VarDecl(IntType(),'a'),
        	VarDecl(ArrayType(IntType(),3),'b'),
        	VarDecl(IntType(),'c'),
        	VarDecl(ArrayType(FloatType(),2),'d'),
        	VarDecl(FloatType(),'e')]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

       