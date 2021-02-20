import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        self.assertTrue(TestLexer.checkLexeme("a bc'{' '","a,bc,<EOF>",101))
    #     self.assertTrue(TestLexer.checkLexeme("ab213c","ab213c,<EOF>",102))
    #     self.assertTrue(TestLexer.checkLexeme("a b!213c","a,b,Error Token !",111))
    #     self.assertTrue(TestLexer.checkLexeme("9a b213c","Error Token 9",112))
    
    # def test_lower_upper_id(self):
    #     self.assertTrue(TestLexer.checkLexeme("Varc viet hoa dc","Error Token V",103))

    # def test_real_number(self):
    #     self.assertTrue(TestLexer.checkLexeme("1.02E-4","1.02E-4,<EOF>",104))
    #     self.assertTrue(TestLexer.checkLexeme("1.00001","1.00001,<EOF>",105))
    #     self.assertTrue(TestLexer.checkLexeme("1E-10","1E-10,<EOF>",106))
    #     self.assertTrue(TestLexer.checkLexeme(".02E-4",".02E-4,<EOF>",107))
    #     self.assertTrue(TestLexer.checkLexeme(".E-3","Error Token .",113))
    #     self.assertTrue(TestLexer.checkLexeme("34","Error Token 3",114))

    # def test_integer(self):
    #     """Do no thing"""
        
    # '''3 hàm sau định nghĩa lỗi'''
    # def test_illegal_escape(self):
    #     self.assertTrue(TestLexer.checkLexeme(" 'abc def' ","'abc def',<EOF>",108))
    #     self.assertTrue(TestLexer.checkLexeme(" 'abc'' def' ","'abc'' def',<EOF>",109))
    #     # self.assertTrue(TestLexer.checkLexeme(" 'abc def'' ","'abc def',<EOF>",115))
    #     self.assertTrue(TestLexer.checkLexeme(" 'abc'ccc' def' ","'abc'' def',<EOF>",116))
    # def test_unterminated_string(self):
    #     self.assertTrue(TestLexer.checkLexeme(" 'ab'c def'  ","'ab',Error Token c",110))

    # def test_normal_string_with_escape(self):
    #     """Do nothing"""
