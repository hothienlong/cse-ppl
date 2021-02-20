import sys,os
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener,ErrorListener
if not './main/bkit/parser/' in sys.path:
    sys.path.append('./main/bkit/parser/')
if os.path.isdir('../target/main/bkit/parser') and not '../target/main/bkit/parser/' in sys.path:
    sys.path.append('../target/main/bkit/parser/')
from BKITLexer import BKITLexer
from BKITParser import BKITParser
from lexererr import *
from ASTGeneration import ASTGeneration
from CodeGenerator import CodeGenerator
from CodeGenError import *
import subprocess

JASMIN_JAR = "./external/jasmin.jar"

class TestUtil:
    @staticmethod
    def makeSource(inputStr,num):
        filename = "./test/testcases/" + str(num) + ".txt"
        file = open(filename,"w")
        file.write(inputStr)
        file.close()
        return FileStream(filename)


class TestLexer:
    @staticmethod
    def checkLexeme(input,expect,num):
        inputfile = TestUtil.makeSource(input,num)
        dest = open("./test/solutions/" + str(num) + ".txt","w")
        lexer = BKITLexer(inputfile)
        try:
            TestLexer.printLexeme(dest,lexer)
        except (ErrorToken,UncloseString,IllegalEscape) as err:
            dest.write(err.message)
        finally:
            dest.close() 
        dest = open("./test/solutions/" + str(num) + ".txt","r")
        line = dest.read()
        return line == expect

    @staticmethod    
    def printLexeme(dest,lexer):
        tok = lexer.nextToken()
        if tok.type != Token.EOF:
            dest.write(tok.text+",")
            TestLexer.printLexeme(dest,lexer)
        else:
            dest.write("<EOF>")
class NewErrorListener(ConsoleErrorListener):
    INSTANCE = None
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException("Error on line "+ str(line) + " col " + str(column)+ ": " + offendingSymbol.text)
NewErrorListener.INSTANCE = NewErrorListener()

class SyntaxException(Exception):
    def __init__(self,msg):
        self.message = msg

class TestParser:
    @staticmethod
    def createErrorListener():
         return NewErrorListener.INSTANCE

    @staticmethod
    def checkParser(input,expect,num):
        inputfile = TestUtil.makeSource(input,num)
        dest = open("./test/solutions/" + str(num) + ".txt","w")
        lexer = BKITLexer(inputfile)
        listener = TestParser.createErrorListener()

        tokens = CommonTokenStream(lexer)

        parser = BKITParser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)
        try:
            parser.program()
            dest.write("successful")
        except SyntaxException as f:
            dest.write(f.message)
        except Exception as e:
            dest.write(str(e))
        finally:
            dest.close()
        dest = open("./test/solutions/" + str(num) + ".txt","r")
        line = dest.read()
        return line == expect

class TestAST:
    @staticmethod
    def checkASTGen(input,expect,num):
        inputfile = TestUtil.makeSource(input,num)
        dest = open("./test/solutions/" + str(num) + ".txt","w")
        lexer = BKITLexer(inputfile)
        tokens = CommonTokenStream(lexer)
        parser = BKITParser(tokens)
        tree = parser.program()
        asttree = ASTGeneration().visit(tree)
        #dest.write(str(asttree))
        dest.close()
        dest = open("./test/solutions/" + str(num) + ".txt","r")
        line = dest.read()
        return line == expect


"""
class TestChecker:
    @staticmethod
    def test(input,expect,num):
        dest = open("./test/solutions/" + str(num) + ".txt","w")
        
        if type(input) is str:
            inputfile = TestUtil.makeSource(input,num)
            lexer = BKITLexer(inputfile)
            tokens = CommonTokenStream(lexer)
            parser = BKITParser(tokens)
            tree = parser.program()
            asttree = ASTGeneration().visit(tree)
        else:
            inputfile = TestUtil.makeSource(str(input),num)
            asttree = input
        
        
        checker = StaticChecker(asttree)
        try:
            res = checker.check()
            #dest.write(str(list(res)))
        except StaticError as e:
            dest.write(str(e))
        finally:
            dest.close()
        dest = open("./test/solutions/" + str(num) + ".txt","r")
        line = dest.read()
        return line == expect
"""
class TestCodeGen():
    @staticmethod
    def test(input, expect, num):
        solpath = "./test/solutions/"
        dest = open(solpath + str(num) + ".txt","w")
        
        if type(input) is str:
            inputfile = TestUtil.makeSource(input,num)
            lexer = BKITLexer(inputfile)
            tokens = CommonTokenStream(lexer)
            parser = BKITParser(tokens)
            tree = parser.program()
            asttree = ASTGeneration().visit(tree)
        else:
            inputfile = TestUtil.makeSource(str(input),num)
            asttree = input
        
        
        codeGen = CodeGenerator()
        
        path = solpath + str(num)
        if not os.path.isdir(path):
            os.mkdir(path)
        try:
            codeGen.gen(asttree, path)
            
            subprocess.call("java  -jar "+ JASMIN_JAR + " " + path + "/MCClass.j",shell=True,stderr=subprocess.STDOUT)
            

            f = open(solpath + str(num) + ".txt","w")
            subprocess.call("java -cp ./lib" + os.pathsep + ". MCClass",shell=True, stdout = f)
            f.close()
        except StaticError as e:
            dest.write(str(e))
        except subprocess.CalledProcessError as e:
            raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        finally:
            dest.close()
        dest = open(solpath + str(num) + ".txt","r")
        line = dest.read()
        return line == expect
