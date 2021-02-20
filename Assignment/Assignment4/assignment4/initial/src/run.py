import sys,os

import platform
import subprocess
import unittest
from antlr4 import *
import shutil

os.environ['ANTLR_JAR'] = 'C:\Javalib\\antlr-4.8-complete.jar'
ANTLR_JAR = os.environ.get('ANTLR_JAR')
TARGET = '../target/main/bkit/parser' if os.name == 'posix' else os.path.normpath('../target/')
locpath = ['test','./main/bkit/parser/','./main/bkit/astgen/','./main/bkit/utils/','./main/bkit/codegen']
for p in locpath:
    if not p in sys.path:
        sys.path.append(p)
def main(argv):
    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'gen':
        subprocess.run(["java","-jar",ANTLR_JAR,"-o","../target","-no-listener","-visitor","main/bkit/parser/BKIT.g4"])
    elif argv[0] == 'clean':
        subprocess.run(["rm","-rf","../target/main"])
    elif argv[0] == 'test':
        if os.path.isdir(TARGET) and not TARGET in sys.path:
            sys.path.append(TARGET)
        if len(argv) < 2:
            printUsage()
        elif argv[1] == 'LexerSuite':
            from LexerSuite import LexerSuite
            suite = unittest.makeSuite(LexerSuite)
            test(suite)
        elif argv[1] == 'ParserSuite':
            from ParserSuite import ParserSuite
            suite = unittest.makeSuite(ParserSuite)
            test(suite)
        elif argv[1] == 'ASTGenSuite':
            from ASTGenSuite import ASTGenSuite
            suite = unittest.makeSuite(ASTGenSuite)
            test(suite)
        elif argv[1] == 'CodeGenSuite':
            from CodeGenSuite import CheckCodeGenSuite
            suite = unittest.makeSuite(CheckCodeGenSuite)
            test(suite)
        else:
            printUsage()
    else:
        printUsage()
    

def test(suite):
    from pprint import pprint
    from io import StringIO
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream)
    result = runner.run(suite)
    print('Tests run ', result.testsRun)
    print('Errors ', result.errors)
    pprint(result.failures)
    stream.seek(0)
    print('Test output\n', stream.read())

def printUsage():
    print("python3 run.py gen")
    print("python3 run.py test LexerSuite")
    print("python3 run.py test ParserSuite")
    print("python3 run.py test ASTGenSuite")
#    print("python3 run.py test CheckSuite")
    print("python3 run.py test CodeGenSuite")

if __name__ == "__main__":
   main(sys.argv[1:])
