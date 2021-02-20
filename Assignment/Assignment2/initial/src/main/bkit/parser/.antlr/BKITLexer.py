# Generated from c:\Users\ADMIN\Desktop\assignment2_real\initial\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write(" \b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\6")
        buf.write("\6\35\n\6\r\6\16\6\36\2\2\7\3\3\5\4\7\5\t\6\13\7\3\2\3")
        buf.write("\3\2c|\2 \2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\3\r\3\2\2\2\5\17\3\2\2\2\7\21\3\2\2")
        buf.write("\2\t\25\3\2\2\2\13\34\3\2\2\2\r\16\7=\2\2\16\4\3\2\2\2")
        buf.write("\17\20\7.\2\2\20\6\3\2\2\2\21\22\7k\2\2\22\23\7p\2\2\23")
        buf.write("\24\7v\2\2\24\b\3\2\2\2\25\26\7h\2\2\26\27\7n\2\2\27\30")
        buf.write("\7q\2\2\30\31\7c\2\2\31\32\7v\2\2\32\n\3\2\2\2\33\35\t")
        buf.write("\2\2\2\34\33\3\2\2\2\35\36\3\2\2\2\36\34\3\2\2\2\36\37")
        buf.write("\3\2\2\2\37\f\3\2\2\2\4\2\36\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    INTTYPE = 3
    FLOATTYPE = 4
    ID = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "','", "'int'", "'float'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "FLOATTYPE", "ID" ]

    ruleNames = [ "T__0", "T__1", "INTTYPE", "FLOATTYPE", "ID" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


