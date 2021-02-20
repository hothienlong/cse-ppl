import unittest
from TestUtils import TestAST
from AST import *
#2(vardecs,EOF) + 1(1 vardec) + 3(mctype,ids,SEMI) + 6(...,mctype) + 1(mctype=INTTYPE) + 4(a,b;)
#1(vardec) + 2(mctype,ids) + 2(intlit,mctype) + 1(mctype=intlit) + 2(ids=a,b)
class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """array[1]of int a,b;"""
        expect = "11"
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_more_complicated_program(self):
        """Simple program: int main() {} """
        input = """array[1] of int a,b;
        			int c,d;
        			float m;"""
        expect = "19"
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_1(self):
        """Simple program: int main() {} """
        input = """array[1] of int a;
        			int c;
        			float m;"""
        expect = "19"
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
     
    def test_2(self):
        """Simple program: int main() {} """
        input = """int a,b;"""
        expect = "5"
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    
   