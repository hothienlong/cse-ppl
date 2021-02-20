# Generated from c:\Users\ADMIN\Desktop\tut6\programing\bai 1\src\main\mc\parser\MC.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write("\'\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4\31\n\4\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\5\7%\n\7\3\7\2\2\b")
        buf.write("\2\4\6\b\n\f\2\3\3\2\5\6\2\"\2\16\3\2\2\2\4\21\3\2\2\2")
        buf.write("\6\30\3\2\2\2\b\32\3\2\2\2\n\36\3\2\2\2\f$\3\2\2\2\16")
        buf.write("\17\5\4\3\2\17\20\7\2\2\3\20\3\3\2\2\2\21\22\5\b\5\2\22")
        buf.write("\23\5\6\4\2\23\5\3\2\2\2\24\25\5\b\5\2\25\26\5\6\4\2\26")
        buf.write("\31\3\2\2\2\27\31\3\2\2\2\30\24\3\2\2\2\30\27\3\2\2\2")
        buf.write("\31\7\3\2\2\2\32\33\5\n\6\2\33\34\5\f\7\2\34\35\7\3\2")
        buf.write("\2\35\t\3\2\2\2\36\37\t\2\2\2\37\13\3\2\2\2 !\7\7\2\2")
        buf.write("!\"\7\4\2\2\"%\5\f\7\2#%\7\7\2\2$ \3\2\2\2$#\3\2\2\2%")
        buf.write("\r\3\2\2\2\4\30$")
        return buf.getvalue()


class MCParser ( Parser ):

    grammarFileName = "MC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "'int'", "'float'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "INTTYPE", 
                      "FLOATTYPE", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_vardecls = 1
    RULE_vardecltail = 2
    RULE_vardecl = 3
    RULE_mptype = 4
    RULE_ids = 5

    ruleNames =  [ "program", "vardecls", "vardecltail", "vardecl", "mptype", 
                   "ids" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    INTTYPE=3
    FLOATTYPE=4
    ID=5
    WS=6
    ERROR_CHAR=7
    UNCLOSE_STRING=8
    ILLEGAL_ESCAPE=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecls(self):
            return self.getTypedRuleContext(MCParser.VardeclsContext,0)


        def EOF(self):
            return self.getToken(MCParser.EOF, 0)

        def getRuleIndex(self):
            return MCParser.RULE_program




    def program(self):

        localctx = MCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.vardecls()
            self.state = 13
            self.match(MCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MCParser.VardeclContext,0)


        def vardecltail(self):
            return self.getTypedRuleContext(MCParser.VardecltailContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_vardecls




    def vardecls(self):

        localctx = MCParser.VardeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_vardecls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.vardecl()
            self.state = 16
            self.vardecltail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardecltailContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MCParser.VardeclContext,0)


        def vardecltail(self):
            return self.getTypedRuleContext(MCParser.VardecltailContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_vardecltail




    def vardecltail(self):

        localctx = MCParser.VardecltailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecltail)
        try:
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.INTTYPE, MCParser.FLOATTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.vardecl()
                self.state = 19
                self.vardecltail()
                pass
            elif token in [MCParser.EOF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mptype(self):
            return self.getTypedRuleContext(MCParser.MptypeContext,0)


        def ids(self):
            return self.getTypedRuleContext(MCParser.IdsContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_vardecl




    def vardecl(self):

        localctx = MCParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.mptype()
            self.state = 25
            self.ids()
            self.state = 26
            self.match(MCParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MptypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(MCParser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(MCParser.FLOATTYPE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_mptype




    def mptype(self):

        localctx = MCParser.MptypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_mptype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            _la = self._input.LA(1)
            if not(_la==MCParser.INTTYPE or _la==MCParser.FLOATTYPE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def ids(self):
            return self.getTypedRuleContext(MCParser.IdsContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_ids




    def ids(self):

        localctx = MCParser.IdsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ids)
        try:
            self.state = 34
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.match(MCParser.ID)
                self.state = 31
                self.match(MCParser.T__1)
                self.state = 32
                self.ids()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.match(MCParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





