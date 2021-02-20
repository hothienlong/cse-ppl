# Generated from c:\Users\ADMIN\Desktop\tut6\programing\bai 1\src\main\mc\parser\MC.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("\65\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\6\6%\n\6\r\6\16\6&\3")
        buf.write("\7\6\7*\n\7\r\7\16\7+\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n")
        buf.write("\2\2\13\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\3\2\4")
        buf.write("\3\2c|\5\2\13\f\17\17\"\"\2\66\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\3\25\3\2\2\2\5\27\3")
        buf.write("\2\2\2\7\31\3\2\2\2\t\35\3\2\2\2\13$\3\2\2\2\r)\3\2\2")
        buf.write("\2\17/\3\2\2\2\21\61\3\2\2\2\23\63\3\2\2\2\25\26\7=\2")
        buf.write("\2\26\4\3\2\2\2\27\30\7.\2\2\30\6\3\2\2\2\31\32\7k\2\2")
        buf.write("\32\33\7p\2\2\33\34\7v\2\2\34\b\3\2\2\2\35\36\7h\2\2\36")
        buf.write("\37\7n\2\2\37 \7q\2\2 !\7c\2\2!\"\7v\2\2\"\n\3\2\2\2#")
        buf.write("%\t\2\2\2$#\3\2\2\2%&\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\'\f")
        buf.write("\3\2\2\2(*\t\3\2\2)(\3\2\2\2*+\3\2\2\2+)\3\2\2\2+,\3\2")
        buf.write("\2\2,-\3\2\2\2-.\b\7\2\2.\16\3\2\2\2/\60\13\2\2\2\60\20")
        buf.write("\3\2\2\2\61\62\13\2\2\2\62\22\3\2\2\2\63\64\13\2\2\2\64")
        buf.write("\24\3\2\2\2\5\2&+\3\b\2\2")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    INTTYPE = 3
    FLOATTYPE = 4
    ID = 5
    WS = 6
    ERROR_CHAR = 7
    UNCLOSE_STRING = 8
    ILLEGAL_ESCAPE = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "','", "'int'", "'float'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "FLOATTYPE", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "INTTYPE", "FLOATTYPE", "ID", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


