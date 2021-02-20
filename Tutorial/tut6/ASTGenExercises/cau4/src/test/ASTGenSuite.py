import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_exp(self):
        input = """true && false"""
        expect = str(Binary('&&',BoolLit(True),BoolLit(False)))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_more_complicated_exp(self):
        input = """3 ^ 4 > 5"""
        expect = str(Binary('>',Binary('^',IntLit(3),IntLit(4)),IntLit(5)))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_full_exp(self):
        input = """(3 ^ 4 > 5) && (4 <= 5 ^ 2)"""
        expect = str(Binary('&&',
        	Binary('>',Binary('^',IntLit(3),IntLit(4)),IntLit(5)),
        	Binary('<=',IntLit(4),Binary('^',IntLit(5),IntLit(2)))))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
       