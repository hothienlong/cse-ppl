# Generated from c:\Users\ADMIN\Desktop\L02_09\initial\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write(".\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\3\2\3\2\3\3\3\3\3\4\5\4\31\n\4\3\4\6")
        buf.write("\4\34\n\4\r\4\16\4\35\3\5\6\5!\n\5\r\5\16\5\"\3\5\3\5")
        buf.write("\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\2\2\n\3\2\5\2\7\2\t\3")
        buf.write("\13\4\r\5\17\6\21\7\3\2\5\3\2c|\3\2\62;\5\2\13\f\17\17")
        buf.write("\"\"\2-\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\3\23\3\2\2\2\5\25\3\2\2\2\7\30\3\2\2")
        buf.write("\2\t \3\2\2\2\13&\3\2\2\2\r(\3\2\2\2\17*\3\2\2\2\21,\3")
        buf.write("\2\2\2\23\24\t\2\2\2\24\4\3\2\2\2\25\26\t\3\2\2\26\6\3")
        buf.write("\2\2\2\27\31\7/\2\2\30\27\3\2\2\2\30\31\3\2\2\2\31\33")
        buf.write("\3\2\2\2\32\34\t\3\2\2\33\32\3\2\2\2\34\35\3\2\2\2\35")
        buf.write("\33\3\2\2\2\35\36\3\2\2\2\36\b\3\2\2\2\37!\t\4\2\2 \37")
        buf.write("\3\2\2\2!\"\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#$\3\2\2\2$%")
        buf.write("\b\5\2\2%\n\3\2\2\2&\'\13\2\2\2\'\f\3\2\2\2()\13\2\2\2")
        buf.write(")\16\3\2\2\2*+\13\2\2\2+\20\3\2\2\2,-\13\2\2\2-\22\3\2")
        buf.write("\2\2\6\2\30\35\"\3\b\2\2")
        return buf.getvalue()


class BKIT(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    ERROR_CHAR = 2
    UNCLOSE_STRING = 3
    ILLEGAL_ESCAPE = 4
    UNTERMINATED_COMMENT = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "LETTER", "DIGIT", "EXPONENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

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


