import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_AST_300(self):
        input = """ Var:x; """
        expect = Program([VarDecl(variable=Id(name='x'), varDimen=[], varInit=None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,300)) 
    def test_AST_301(self):
        input = """ Function: sumArr
            Parameter:  arrA, arrB
            Body:
                Var: diffLen = 0, isA = False, smaller, sum;
                diffLen = len(arrA) - len(arrB);
                If diffLen > 0 Then 
                    isA = True; 
                    smaller = len(arrA);
                Else 
                    isA = False; 
                    smaller = len(arrB);
                EndIf.
                For (i = 0, i < smaller, 1) Do
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
            EndBody. 
            """
        expect = Program([FuncDecl(name=Id(name='sumArr'), param=[VarDecl(variable=Id(name='arrA'), varDimen=[], varInit=None), VarDecl(variable=Id(name='arrB'), varDimen=[], varInit=None)], body=([VarDecl(variable=Id(name='diffLen'), varDimen=[], varInit=IntLiteral(value=0)), VarDecl(variable=Id(name='isA'), varDimen=[], varInit=BooleanLiteral(value=True)), VarDecl(variable=Id(name='smaller'), varDimen=[], varInit=None), VarDecl(variable=Id(name='sum'), varDimen=[], varInit=None)], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), If(ifthenStmt=[(BinaryOp(op='>', left=Id(name='diffLen'), right=IntLiteral(value=0)), [], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]))])], elseStmt=([], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))])), For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='smaller')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,301)) 
    def test_AST_302(self):
        input = """ Function: sumArr
            Parameter:  arrA, arrB
            Body:
                Var: diffLen = 0, isA = False, smaller, sum;
                diffLen = len(arrA) - len(arrB);
                If diffLen > 0 Then 
                    isA = True; 
                    smaller = len(arrA);
                Else 
                    isA = False; 
                    smaller = len(arrB);
                EndIf.
                diffLen = abs(diffLen);
                For (i = 0, i < smaller, 1) Do
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
                For (i = 0, i < diffLen, 1) Do
                    If isA Then 
                    Else
                    EndIf.
                EndFor.
            EndBody. 
            """
        expect = Program([FuncDecl(name=Id(name='sumArr'), param=[VarDecl(variable=Id(name='arrA'), varDimen=[], varInit=None), VarDecl(variable=Id(name='arrB'), varDimen=[], varInit=None)], body=([VarDecl(variable=Id(name='diffLen'), varDimen=[], varInit=IntLiteral(value=0)), VarDecl(variable=Id(name='isA'), varDimen=[], varInit=BooleanLiteral(value=True)), VarDecl(variable=Id(name='smaller'), varDimen=[], varInit=None), VarDecl(variable=Id(name='sum'), varDimen=[], varInit=None)], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), If(ifthenStmt=[(BinaryOp(op='>', left=Id(name='diffLen'), right=IntLiteral(value=0)), [], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]))])], elseStmt=([], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))])), Assign(lhs=Id(name='diffLen'), rhs=CallStmt(method=Id(name='abs'), param=[Id(name='diffLen')])), For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='smaller')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='diffLen')), expr3=IntLiteral(value=1), loop=([], [If(ifthenStmt=[(Id(name='isA'), [], [])], elseStmt=([], []))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,302)) 
    def test_AST_303(self):
        input = """ Function: sumArr
            Parameter:  arrA, arrB
            Body:
                Var: diffLen = 0, isA = False, smaller, sum;
                diffLen = len(arrA) - len(arrB);
                If diffLen > 0 Then 
                    isA = True; 
                    smaller = len(arrA);
                Else 
                    isA = False; 
                    smaller = len(arrB);
                EndIf.
                diffLen = abs(diffLen);
                For (i = 0, i < smaller, 1) Do
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
                For (i = smaller, i < smaller + diffLen, 1) Do
                    If isA Then 
                        sum = sum + arrB[i];
                    Else
                        sum = sum + arrA[i];
                    EndIf.
                EndFor.
            EndBody. 
            """
        expect = Program([FuncDecl(name=Id(name='sumArr'), param=[VarDecl(variable=Id(name='arrA'), varDimen=[], varInit=None), VarDecl(variable=Id(name='arrB'), varDimen=[], varInit=None)], body=([VarDecl(variable=Id(name='diffLen'), varDimen=[], varInit=IntLiteral(value=0)), VarDecl(variable=Id(name='isA'), varDimen=[], varInit=BooleanLiteral(value=True)), VarDecl(variable=Id(name='smaller'), varDimen=[], varInit=None), VarDecl(variable=Id(name='sum'), varDimen=[], varInit=None)], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), If(ifthenStmt=[(BinaryOp(op='>', left=Id(name='diffLen'), right=IntLiteral(value=0)), [], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]))])], elseStmt=([], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))])), Assign(lhs=Id(name='diffLen'), rhs=CallStmt(method=Id(name='abs'), param=[Id(name='diffLen')])), For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='smaller')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), For(idx1=Id(name='i'), expr1=Id(name='smaller'), expr2=BinaryOp(op='<', left=Id(name='i'), right=BinaryOp(op='+', left=Id(name='smaller'), right=Id(name='diffLen'))), expr3=IntLiteral(value=1), loop=([], [If(ifthenStmt=[(Id(name='isA'), [], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])], elseStmt=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,303)) 
    def test_AST_304(self):
        input = """ Function: getArray
            Parameter: arr, size
            Body:

            EndBody.
            Function: main
            Body:
                getArray();
            EndBody.
            """
        expect = Program([FuncDecl(name=Id(name='getArray'), param=[VarDecl(variable=Id(name='arr'), varDimen=[], varInit=None), VarDecl(variable=Id(name='size'), varDimen=[], varInit=None)], body=([], [])), FuncDecl(name=Id(name='main'), param=[], body=([], [CallStmt(method=Id(name='getArray'), param=[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,304)) 
    def test_AST_305(self):
        input = """ Function: getArray
            Parameter: arr, size[4]
            Body:
                For (i = 0, i < size, 1) Do
                    arr[i] = read();
                EndFor.
                Return arr;
            EndBody.
            Function: main
            Body:
                Var: arr;
                arr = getArray();
            EndBody.
            """
        expect = Program([FuncDecl(name=Id(name='getArray'), param=[VarDecl(variable=Id(name='arr'), varDimen=[], varInit=None), VarDecl(variable=Id(name='size'), varDimen=[IntLiteral(value=4)], varInit=None)], body=([], [For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='size')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=ArrayCell(arr=Id(name='arr'), idx=[Id(name='i')]), rhs=CallStmt(method=Id(name='read'), param=[]))])), Return(expr=Id(name='arr'))])), FuncDecl(name=Id(name='main'), param=[], body=([VarDecl(variable=Id(name='arr'), varDimen=[], varInit=None)], [Assign(lhs=Id(name='arr'), rhs=CallStmt(method=Id(name='getArray'), param=[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,305)) 
    def test_AST_306(self):
        input = """ Function: getArrayOfEvenNum
            Parameter: arr, size
            Body:
                For (i = 0, i < size, 1) Do
                    tmp = read();
                    If tmp % 2 != 0 Then Continue; EndIf.
                    arr[i] = read();
                EndFor.
                Return arr;
            EndBody.
            Function: main
            Body:
                Var: arr;
                arr = getArrayOfEvenNum();
            EndBody.
            """
        expect = Program([FuncDecl(name=Id(name='getArrayOfEvenNum'), param=[VarDecl(variable=Id(name='arr'), varDimen=[], varInit=None), VarDecl(variable=Id(name='size'), varDimen=[], varInit=None)], body=([], [For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='size')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='tmp'), rhs=CallStmt(method=Id(name='read'), param=[])), If(ifthenStmt=[(BinaryOp(op='!=', left=BinaryOp(op='%', left=Id(name='tmp'), right=IntLiteral(value=2)), right=IntLiteral(value=0)), [], [Continue()])], elseStmt=([], [])), Assign(lhs=ArrayCell(arr=Id(name='arr'), idx=[Id(name='i')]), rhs=CallStmt(method=Id(name='read'), param=[]))])), Return(expr=Id(name='arr'))])), FuncDecl(name=Id(name='main'), param=[], body=([VarDecl(variable=Id(name='arr'), varDimen=[], varInit=None)], [Assign(lhs=Id(name='arr'), rhs=CallStmt(method=Id(name='getArrayOfEvenNum'), param=[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,306)) 
    def test_AST_307(self):
        input = """ Function : isPrime
            Parameter: n
            Body:
                For (i = 2, (n - 1) \ 2, 1) Do
                    If(n % i == 0) Then
                        Return False;
                    Else
                        Return True;
                    EndIf.
                EndFor.
            EndBody.
            Function: main
            Body:
                print(isPrime(4));
            EndBody.
            """
        expect = Program([FuncDecl(name=Id(name='isPrime'), param=[VarDecl(variable=Id(name='n'), varDimen=[], varInit=None)], body=([], [For(idx1=Id(name='i'), expr1=IntLiteral(value=2), expr2=BinaryOp(op='\\', left=BinaryOp(op='-', left=Id(name='n'), right=IntLiteral(value=1)), right=IntLiteral(value=2)), expr3=IntLiteral(value=1), loop=([], [If(ifthenStmt=[(BinaryOp(op='==', left=BinaryOp(op='%', left=Id(name='n'), right=Id(name='i')), right=IntLiteral(value=0)), [], [Return(expr=BooleanLiteral(value=True))])], elseStmt=([], [Return(expr=BooleanLiteral(value=True))]))]))])), FuncDecl(name=Id(name='main'), param=[], body=([], [CallStmt(method=Id(name='print'), param=[CallStmt(method=Id(name='isPrime'), param=[IntLiteral(value=4)])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,307)) 
    def test_AST_308(self):
        input = """ Var: name, surname;
                Function: main
                Body:
                    write("Nhap ten cua ban:");
                    readln(name);
                    write("Nhap ho cua ban:");
                    readln(surname);
                    writeln();
                    writeln();
                    writeln("Ten day du cua ban la : ",name," ",surname);
                    readln();
                EndBody.
            """
        expect = Program([VarDecl(variable=Id(name='name'), varDimen=[], varInit=None), VarDecl(variable=Id(name='surname'), varDimen=[], varInit=None), FuncDecl(name=Id(name='main'), param=[], body=([], [CallStmt(method=Id(name='write'), param=[StringLiteral(value='Nhap ten cua ban:')]), CallStmt(method=Id(name='readln'), param=[Id(name='name')]), CallStmt(method=Id(name='write'), param=[StringLiteral(value='Nhap ho cua ban:')]), CallStmt(method=Id(name='readln'), param=[Id(name='surname')]), CallStmt(method=Id(name='writeln'), param=[]), CallStmt(method=Id(name='writeln'), param=[]), CallStmt(method=Id(name='writeln'), param=[StringLiteral(value='Ten day du cua ban la : '), Id(name='name'), StringLiteral(value=' '), Id(name='surname')]), CallStmt(method=Id(name='readln'), param=[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,308)) 
    def test_AST_309(self):
        input = """ Var: age;
                Function: main
                Body:
                    write("Nhap tuoi cua ban:");
                    readln(age);
                    writeln();
                    writeln("Your age is: " + age);
                    readln();
                EndBody.
            """
        expect = Program([VarDecl(variable=Id(name='age'), varDimen=[], varInit=None), FuncDecl(name=Id(name='main'), param=[], body=([], [CallStmt(method=Id(name='write'), param=[StringLiteral(value='Nhap tuoi cua ban:')]), CallStmt(method=Id(name='readln'), param=[Id(name='age')]), CallStmt(method=Id(name='writeln'), param=[]), CallStmt(method=Id(name='writeln'), param=[BinaryOp(op='+', left=StringLiteral(value='Your age is: '), right=Id(name='age'))]), CallStmt(method=Id(name='readln'), param=[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,309)) 
    def test_AST_310(self):
        input = """ Function: multi
            Parameter: a,b
            Body:
                Return a*b;
            EndBody.
            """
        expect = Program([FuncDecl(name=Id(name='multi'), param=[VarDecl(variable=Id(name='a'), varDimen=[], varInit=None), VarDecl(variable=Id(name='b'), varDimen=[], varInit=None)], body=([], [Return(expr=BinaryOp(op='*', left=Id(name='a'), right=Id(name='b')))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,310)) 
    def test_AST_311(self):
        input = """ Function: multi
            Parameter: x, y
            Body:
                If x == 1 Then Return y;
                Else
                    Return y + (multi(x-1, y));
                EndIf.
            EndBody.
            """
        expect = Program([FuncDecl(name=Id(name='multi'), param=[VarDecl(variable=Id(name='x'), varDimen=[], varInit=None), VarDecl(variable=Id(name='y'), varDimen=[], varInit=None)], body=([], [If(ifthenStmt=[(BinaryOp(op='==', left=Id(name='x'), right=IntLiteral(value=1)), [], [Return(expr=Id(name='y'))])], elseStmt=([], [Return(expr=BinaryOp(op='+', left=Id(name='y'), right=CallStmt(method=Id(name='multi'), param=[BinaryOp(op='-', left=Id(name='x'), right=IntLiteral(value=1)), Id(name='y')])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,311)) 
    def test_AST_312(self):
        input = """ Function: multi
            Parameter: x, y
            Body:
                Var: ans = 2;
                While x > 0 Do
                    ans = ans + y;
                    x = x - 1;
                EndWhile.
            EndBody.
            """
        expect = Program([FuncDecl(name=Id(name='multi'), param=[VarDecl(variable=Id(name='x'), varDimen=[], varInit=None), VarDecl(variable=Id(name='y'), varDimen=[], varInit=None)], body=([VarDecl(variable=Id(name='ans'), varDimen=[], varInit=IntLiteral(value=2))], [While(exp=BinaryOp(op='>', left=Id(name='x'), right=IntLiteral(value=0)), sl=([], [Assign(lhs=Id(name='ans'), rhs=BinaryOp(op='+', left=Id(name='ans'), right=Id(name='y'))), Assign(lhs=Id(name='x'), rhs=BinaryOp(op='-', left=Id(name='x'), right=IntLiteral(value=1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,312)) 
    def test_AST_313(self):
        input = """ Function: multi
            Parameter: x, y
            Body:
                Var: ans = 0;
                Do
                    ans = ans + y;
                    x = x - 1;
                While x > 0
                EndDo.
            EndBody.
            """
        expect = Program([FuncDecl(name=Id(name='multi'), param=[VarDecl(variable=Id(name='x'), varDimen=[], varInit=None), VarDecl(variable=Id(name='y'), varDimen=[], varInit=None)], body=([VarDecl(variable=Id(name='ans'), varDimen=[], varInit=IntLiteral(value=0))], [Dowhile(sl=([], [Assign(lhs=Id(name='ans'), rhs=BinaryOp(op='+', left=Id(name='ans'), right=Id(name='y'))), Assign(lhs=Id(name='x'), rhs=BinaryOp(op='-', left=Id(name='x'), right=IntLiteral(value=1)))]), exp=BinaryOp(op='>', left=Id(name='x'), right=IntLiteral(value=0)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,313)) 
    def test_AST_314(self):
        input = """ Function: a
            Body:
                Var: http = "";
                http = require(http);
            EndBody.
            """
        expect = Program([FuncDecl(name=Id(name='a'), param=[], body=([VarDecl(variable=Id(name='http'), varDimen=[], varInit=StringLiteral(value=''))], [Assign(lhs=Id(name='http'), rhs=CallStmt(method=Id(name='require'), param=[Id(name='http')]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,314)) 
    def test_AST_315(self):
        input = """ Function: sum
            Parameter: n
            Body:
                Var: sum = 0;
                For (i = 0, i < n, 1) Do
                    sum = sum + i;
                EndFor.
                Return sum;
            EndBody.
            """
        expect = Program([FuncDecl(name=Id(name='sum'), param=[VarDecl(variable=Id(name='n'), varDimen=[], varInit=None)], body=([VarDecl(variable=Id(name='sum'), varDimen=[], varInit=IntLiteral(value=0))], [For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='n')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=Id(name='sum'), right=Id(name='i')))])), Return(expr=Id(name='sum'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,315)) 
    def test_AST_316(self):
        input = """ Function: product
            Parameter: n
            Body:
                Var: prod = 1.0;
                While n > 0 Do
                    prod = prod * n;
                    n = n - 1;
                EndWhile.
                Return prod;
            EndBody.
            """
        expect = Program([FuncDecl(name=Id(name='product'), param=[VarDecl(variable=Id(name='n'), varDimen=[], varInit=None)], body=([VarDecl(variable=Id(name='prod'), varDimen=[], varInit=FloatLiteral(value=1.0))], [While(exp=BinaryOp(op='>', left=Id(name='n'), right=IntLiteral(value=0)), sl=([], [Assign(lhs=Id(name='prod'), rhs=BinaryOp(op='*', left=Id(name='prod'), right=Id(name='n'))), Assign(lhs=Id(name='n'), rhs=BinaryOp(op='-', left=Id(name='n'), right=IntLiteral(value=1)))])), Return(expr=Id(name='prod'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,316)) 
    def test_AST_317(self):
        input = """ Function: sum
            Parameter: a, b
            Body:
                Return float_of_int(a) +. float_of_int(b);
            EndBody.
            """
        expect = Program([FuncDecl(name=Id(name='sum'), param=[VarDecl(variable=Id(name='a'), varDimen=[], varInit=None), VarDecl(variable=Id(name='b'), varDimen=[], varInit=None)], body=([], [Return(expr=BinaryOp(op='+.', left=CallStmt(method=Id(name='float_of_int'), param=[Id(name='a')]), right=CallStmt(method=Id(name='float_of_int'), param=[Id(name='b')])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,317)) 
    def test_AST_318(self):
        input = """ Function: sumArr
            Parameter:  arrA, arrB
            Body:
                Var: diffLen = 0, isA = False, smaller, sum;
                diffLen = len(arrA) - len(arrB);
                If diffLen > 0 Then 
                    isA = True; 
                    smaller = len(arrA);
                Else 
                    isA = False; 
                    smaller = len(arrB);
                EndIf.
                diffLen = abs(diffLen);
                For (i = 0, i < smaller, 1) Do
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
                For (i = smaller, i < smaller + diffLen, 1 + 1) Do
                    If isA Then 
                        sum = sum + arrB[i];
                    Else
                        sum = sum + arrA[i];
                    EndIf.
                EndFor.
            EndBody. 
            """
        expect = Program([FuncDecl(name=Id(name='sumArr'), param=[VarDecl(variable=Id(name='arrA'), varDimen=[], varInit=None), VarDecl(variable=Id(name='arrB'), varDimen=[], varInit=None)], body=([VarDecl(variable=Id(name='diffLen'), varDimen=[], varInit=IntLiteral(value=0)), VarDecl(variable=Id(name='isA'), varDimen=[], varInit=BooleanLiteral(value=True)), VarDecl(variable=Id(name='smaller'), varDimen=[], varInit=None), VarDecl(variable=Id(name='sum'), varDimen=[], varInit=None)], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), If(ifthenStmt=[(BinaryOp(op='>', left=Id(name='diffLen'), right=IntLiteral(value=0)), [], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]))])], elseStmt=([], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))])), Assign(lhs=Id(name='diffLen'), rhs=CallStmt(method=Id(name='abs'), param=[Id(name='diffLen')])), For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='smaller')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), For(idx1=Id(name='i'), expr1=Id(name='smaller'), expr2=BinaryOp(op='<', left=Id(name='i'), right=BinaryOp(op='+', left=Id(name='smaller'), right=Id(name='diffLen'))), expr3=BinaryOp(op='+', left=IntLiteral(value=1), right=IntLiteral(value=1)), loop=([], [If(ifthenStmt=[(Id(name='isA'), [], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])], elseStmt=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,318)) 
    def test_AST_319(self):
        input = """ Function: jasonMraz
        Body:
                    For (traiTimBenLe = (3-2) == 1+2*test(1), 3, func(1)[1] * 2) Do
                        barrr(myArr[2][3][4]);
                        diffLen = len(arrA) - len(arrB);
                    EndFor.
                
                    For (bar = c <. 4.5, foo(3) + bar(a[3]) =/= a[3][3][b[2][2][7]], func(3)) Do
                        string = "test function with string";
                        barrr(myArr[2][3][4]);
                    EndFor.
                
                Do
                    a[3 + foo(2)] = a[b[2][3]] + 4;
                    arr = getArrayOfEvenNum();
                    sum = sum + arrA[i] + arrB[i];
                While foo(thuanNgo) EndDo.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='jasonMraz'), param=[], body=([], [For(idx1=Id(name='traiTimBenLe'), expr1=BinaryOp(op='==', left=BinaryOp(op='-', left=IntLiteral(value=3), right=IntLiteral(value=2)), right=BinaryOp(op='+', left=IntLiteral(value=1), right=BinaryOp(op='*', left=IntLiteral(value=2), right=CallStmt(method=Id(name='test'), param=[IntLiteral(value=1)])))), expr2=IntLiteral(value=3), expr3=BinaryOp(op='*', left=ArrayCell(arr=CallStmt(method=Id(name='func'), param=[IntLiteral(value=1)]), idx=[IntLiteral(value=1)]), right=IntLiteral(value=2)), loop=([], [CallStmt(method=Id(name='barrr'), param=[ArrayCell(arr=Id(name='myArr'), idx=[IntLiteral(value=2), IntLiteral(value=3), IntLiteral(value=4)])]), Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')])))])), For(idx1=Id(name='bar'), expr1=BinaryOp(op='<.', left=Id(name='c'), right=FloatLiteral(value=4.5)), expr2=BinaryOp(op='=/=', left=BinaryOp(op='+', left=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), right=CallStmt(method=Id(name='bar'), param=[ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3)])])), right=ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3), IntLiteral(value=3), ArrayCell(arr=Id(name='b'), idx=[IntLiteral(value=2), IntLiteral(value=2), IntLiteral(value=7)])])), expr3=CallStmt(method=Id(name='func'), param=[IntLiteral(value=3)]), loop=([], [Assign(lhs=Id(name='string'), rhs=StringLiteral(value='test function with string')), CallStmt(method=Id(name='barrr'), param=[ArrayCell(arr=Id(name='myArr'), idx=[IntLiteral(value=2), IntLiteral(value=3), IntLiteral(value=4)])])])), Dowhile(sl=([], [Assign(lhs=ArrayCell(arr=Id(name='a'), idx=[BinaryOp(op='+', left=IntLiteral(value=3), right=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=2)]))]), rhs=BinaryOp(op='+', left=ArrayCell(arr=Id(name='a'), idx=[ArrayCell(arr=Id(name='b'), idx=[IntLiteral(value=2), IntLiteral(value=3)])]), right=IntLiteral(value=4))), Assign(lhs=Id(name='arr'), rhs=CallStmt(method=Id(name='getArrayOfEvenNum'), param=[])), Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))]), exp=CallStmt(method=Id(name='foo'), param=[Id(name='thuanNgo')]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,319)) 
    def test_AST_320(self):
        input = """ Function: a
            Body:
                print(hello);
            EndBody.
            """
        expect = Program([FuncDecl(name=Id(name='a'), param=[], body=([], [CallStmt(method=Id(name='print'), param=[Id(name='hello')])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,320)) 
    def test_AST_321(self):
        input = """ Function: sayBye
            Body:
            Var: isEnd = True;
            If isEnd && foo(2) Then
                    print("bye bye");
                EndIf.
            EndBody.
            """
        expect = Program([FuncDecl(name=Id(name='sayBye'), param=[], body=([VarDecl(variable=Id(name='isEnd'), varDimen=[], varInit=BooleanLiteral(value=True))], [If(ifthenStmt=[(BinaryOp(op='&&', left=Id(name='isEnd'), right=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=2)])), [], [CallStmt(method=Id(name='print'), param=[StringLiteral(value='bye bye')])])], elseStmt=([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,321)) 
    def test_AST_322(self):
        input = """ Function: sayBye
            Parameter: x, a[2][1]
            Body:
            Var: isEnd = True;
            x = x + 5 == True;
            If isEnd Then
                    print("bye bye");
                EndIf.
            EndBody.
            """
        expect = Program([FuncDecl(name=Id(name='sayBye'), param=[VarDecl(variable=Id(name='x'), varDimen=[], varInit=None), VarDecl(variable=Id(name='a'), varDimen=[IntLiteral(value=2), IntLiteral(value=1)], varInit=None)], body=([VarDecl(variable=Id(name='isEnd'), varDimen=[], varInit=BooleanLiteral(value=True))], [Assign(lhs=Id(name='x'), rhs=BinaryOp(op='==', left=BinaryOp(op='+', left=Id(name='x'), right=IntLiteral(value=5)), right=BooleanLiteral(value=True))), If(ifthenStmt=[(Id(name='isEnd'), [], [CallStmt(method=Id(name='print'), param=[StringLiteral(value='bye bye')])])], elseStmt=([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,322)) 

    def test_AST_323(self):
        input = """ Function: haAnhTuan123
        Body:
                    For (adamLevine = foo(thuanNgo), 1231 + -11 == False, func(3)) Do
                        hehe = (foo(3)[3*3-1][22] != xyA) <=. 3.234;
                        While a <= 4 Do
                    diffLen = len(arrA) - len(arrB);
                    For (i = 0, i < smaller, 1) Do
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
                    sum = sum + arrA[i] + arrB[i];
                EndWhile.
                    EndFor.
                
                    While a <= 4 Do
                        arr = getArrayOfEvenNum();
                        diffLen = len(arrA) - len(arrB);
                    EndWhile.
                
                Do
                    tmp = read();
                    sum = sum + arrA[i] + arrB[i];
                    diffLen = len(arrA) - len(arrB);
                While bar[1] EndDo.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='haAnhTuan123'), param=[], body=([], [For(idx1=Id(name='adamLevine'), expr1=CallStmt(method=Id(name='foo'), param=[Id(name='thuanNgo')]), expr2=BinaryOp(op='==', left=BinaryOp(op='+', left=IntLiteral(value=1231), right=UnaryOp(op='-', body=IntLiteral(value=11))), right=BooleanLiteral(value=True)), expr3=CallStmt(method=Id(name='func'), param=[IntLiteral(value=3)]), loop=([], [Assign(lhs=Id(name='hehe'), rhs=BinaryOp(op='<=.', left=BinaryOp(op='!=', left=ArrayCell(arr=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), idx=[BinaryOp(op='-', left=BinaryOp(op='*', left=IntLiteral(value=3), right=IntLiteral(value=3)), right=IntLiteral(value=1)), IntLiteral(value=22)]), right=Id(name='xyA')), right=FloatLiteral(value=3.234))), While(exp=BinaryOp(op='<=', left=Id(name='a'), right=IntLiteral(value=4)), sl=([], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='smaller')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))]))])), While(exp=BinaryOp(op='<=', left=Id(name='a'), right=IntLiteral(value=4)), sl=([], [Assign(lhs=Id(name='arr'), rhs=CallStmt(method=Id(name='getArrayOfEvenNum'), param=[])), Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')])))])), Dowhile(sl=([], [Assign(lhs=Id(name='tmp'), rhs=CallStmt(method=Id(name='read'), param=[])), Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')]))), Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')])))]), exp=ArrayCell(arr=Id(name='bar'), idx=[IntLiteral(value=1)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,323)) 
    
    def test_AST_324(self):
        input = """ Function: barz
        Body:
                    For (thanhToan = a <= 4, (3-2) == 1+2*test(1), func(3)) Do
                        string = "test function with string";
                        If tmp % 2 != 0 Then Continue; EndIf.
                    EndFor.
                
                Do
                    string = "test function with string";
                    hehe = (foo(3)[3*3-1][22] != xyA) <=. 3.234;
                    Return y + (multi(x-1, y));
                While 0xFFAA EndDo.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='barz'), param=[], body=([], [For(idx1=Id(name='thanhToan'), expr1=BinaryOp(op='<=', left=Id(name='a'), right=IntLiteral(value=4)), expr2=BinaryOp(op='==', left=BinaryOp(op='-', left=IntLiteral(value=3), right=IntLiteral(value=2)), right=BinaryOp(op='+', left=IntLiteral(value=1), right=BinaryOp(op='*', left=IntLiteral(value=2), right=CallStmt(method=Id(name='test'), param=[IntLiteral(value=1)])))), expr3=CallStmt(method=Id(name='func'), param=[IntLiteral(value=3)]), loop=([], [Assign(lhs=Id(name='string'), rhs=StringLiteral(value='test function with string')), If(ifthenStmt=[(BinaryOp(op='!=', left=BinaryOp(op='%', left=Id(name='tmp'), right=IntLiteral(value=2)), right=IntLiteral(value=0)), [], [Continue()])], elseStmt=([], []))])), Dowhile(sl=([], [Assign(lhs=Id(name='string'), rhs=StringLiteral(value='test function with string')), Assign(lhs=Id(name='hehe'), rhs=BinaryOp(op='<=.', left=BinaryOp(op='!=', left=ArrayCell(arr=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), idx=[BinaryOp(op='-', left=BinaryOp(op='*', left=IntLiteral(value=3), right=IntLiteral(value=3)), right=IntLiteral(value=1)), IntLiteral(value=22)]), right=Id(name='xyA')), right=FloatLiteral(value=3.234))), Return(expr=BinaryOp(op='+', left=Id(name='y'), right=CallStmt(method=Id(name='multi'), param=[BinaryOp(op='-', left=Id(name='x'), right=IntLiteral(value=1)), Id(name='y')])))]), exp=IntLiteral(value=65450))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,324)) 

    def test_AST_325(self):
        input = """ Function: anotherONe
            Body:
            EndBody.
            """
        expect = Program([FuncDecl(name=Id(name='anotherONe'), param=[], body=([], []))])
        self.assertTrue(TestAST.checkASTGen(input,expect,325)) 
    def test_AST_326(self):
        input = """ Function: nickyMjnaj
        Body:
                    For (seeSingShare = bar[1], 3520, 0xFFAA) Do
                        writeln("Ten day du cua ban la : ",name," ",surname);
                        a[3 + foo(2)] = a[b[2][3]] + 4;
                    EndFor.
                
                Do
                    barrr(myArr[2][3][4]);
                    Return (ax + by == 0);
                    If tmp % 2 != 0 Then Continue; EndIf.
                While foo(thuanNgo) EndDo.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='nickyMjnaj'), param=[], body=([], [For(idx1=Id(name='seeSingShare'), expr1=ArrayCell(arr=Id(name='bar'), idx=[IntLiteral(value=1)]), expr2=IntLiteral(value=3520), expr3=IntLiteral(value=65450), loop=([], [CallStmt(method=Id(name='writeln'), param=[StringLiteral(value='Ten day du cua ban la : '), Id(name='name'), StringLiteral(value=' '), Id(name='surname')]), Assign(lhs=ArrayCell(arr=Id(name='a'), idx=[BinaryOp(op='+', left=IntLiteral(value=3), right=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=2)]))]), rhs=BinaryOp(op='+', left=ArrayCell(arr=Id(name='a'), idx=[ArrayCell(arr=Id(name='b'), idx=[IntLiteral(value=2), IntLiteral(value=3)])]), right=IntLiteral(value=4)))])), Dowhile(sl=([], [CallStmt(method=Id(name='barrr'), param=[ArrayCell(arr=Id(name='myArr'), idx=[IntLiteral(value=2), IntLiteral(value=3), IntLiteral(value=4)])]), Return(expr=BinaryOp(op='==', left=BinaryOp(op='+', left=Id(name='ax'), right=Id(name='by')), right=IntLiteral(value=0))), If(ifthenStmt=[(BinaryOp(op='!=', left=BinaryOp(op='%', left=Id(name='tmp'), right=IntLiteral(value=2)), right=IntLiteral(value=0)), [], [Continue()])], elseStmt=([], []))]), exp=CallStmt(method=Id(name='foo'), param=[Id(name='thuanNgo')]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,326)) 

    def test_AST_327(self):
        input = """ Function: ids
        Body:
                    For (nickyMjnaj = 10e-11, func(3), func(3)) Do
                        diffLen = len(arrA) - len(arrB);
                        Return 1;
                    EndFor.
                
                    For (func1 = 3520, a <= 4, a[3+foo(2)]) Do
                        Return 1;
                        getArray();
                    EndFor.
                
                Do
                    a[3 + foo(2)] = a[b[2][3]] + 4;
                    Return 2;
                    While a <= 4 Do
                    diffLen = len(arrA) - len(arrB);
                    For (i = 0, i < smaller, 1) Do
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
                    sum = sum + arrA[i] + arrB[i];
                EndWhile.
                While 3 EndDo.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='ids'), param=[], body=([], [For(idx1=Id(name='nickyMjnaj'), expr1=FloatLiteral(value=1e-10), expr2=CallStmt(method=Id(name='func'), param=[IntLiteral(value=3)]), expr3=CallStmt(method=Id(name='func'), param=[IntLiteral(value=3)]), loop=([], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), Return(expr=IntLiteral(value=1))])), For(idx1=Id(name='func1'), expr1=IntLiteral(value=3520), expr2=BinaryOp(op='<=', left=Id(name='a'), right=IntLiteral(value=4)), expr3=ArrayCell(arr=Id(name='a'), idx=[BinaryOp(op='+', left=IntLiteral(value=3), right=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=2)]))]), loop=([], [Return(expr=IntLiteral(value=1)), CallStmt(method=Id(name='getArray'), param=[])])), Dowhile(sl=([], [Assign(lhs=ArrayCell(arr=Id(name='a'), idx=[BinaryOp(op='+', left=IntLiteral(value=3), right=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=2)]))]), rhs=BinaryOp(op='+', left=ArrayCell(arr=Id(name='a'), idx=[ArrayCell(arr=Id(name='b'), idx=[IntLiteral(value=2), IntLiteral(value=3)])]), right=IntLiteral(value=4))), Return(expr=IntLiteral(value=2)), While(exp=BinaryOp(op='<=', left=Id(name='a'), right=IntLiteral(value=4)), sl=([], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='smaller')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))]))]), exp=IntLiteral(value=3))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,327)) 

    def test_AST_328(self):
        input = """ Function: a
            Body:
                a = myArr[2][3][4];
            EndBody.
            """
        expect = Program([FuncDecl(name=Id(name='a'), param=[], body=([], [Assign(lhs=Id(name='a'), rhs=ArrayCell(arr=Id(name='myArr'), idx=[IntLiteral(value=2), IntLiteral(value=3), IntLiteral(value=4)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,328)) 
    def test_AST_329(self):
        input = """ Function: a
            Body:
                barrr(myArr[2][3][4]);
            EndBody.
            """
        expect = Program([FuncDecl(name=Id(name='a'), param=[], body=([], [CallStmt(method=Id(name='barrr'), param=[ArrayCell(arr=Id(name='myArr'), idx=[IntLiteral(value=2), IntLiteral(value=3), IntLiteral(value=4)])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,329)) 
    def test_AST_330(self):
        input = """ Function: sayBye
            Body:
            Var: isEnd = True;
            If isEnd Then
                    print("bye bye");
                EndIf.
            EndBody.
            """
        expect = Program([FuncDecl(name=Id(name='sayBye'), param=[], body=([VarDecl(variable=Id(name='isEnd'), varDimen=[], varInit=BooleanLiteral(value=True))], [If(ifthenStmt=[(Id(name='isEnd'), [], [CallStmt(method=Id(name='print'), param=[StringLiteral(value='bye bye')])])], elseStmt=([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,330)) 
    def test_AST_331(self):
        input = """ Function: adamLevine
        Body:
            If giacMoNgayxua == 100 Then
                saQe = foo(thuanNgo);
            EndIf.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='adamLevine'), param=[], body=([], [If(ifthenStmt=[(BinaryOp(op='==', left=Id(name='giacMoNgayxua'), right=IntLiteral(value=100)), [], [Assign(lhs=Id(name='saQe'), rhs=CallStmt(method=Id(name='foo'), param=[Id(name='thuanNgo')]))])], elseStmt=([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,331)) 
    def test_AST_332(self):
        input = """ Function: aHUhu
        Body:

                For (i = 0, i < smaller, 1) Do
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
                writeln("Ten day du cua ban la : ",name," ",surname);
                If (aHUhu - 10e-11) Then
                    diffLen = len(arrA) - len(arrB);
                Else
                    Return 1;
                    If tmp % 2 != 0 Then Continue; EndIf.
                EndIf.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='aHUhu'), param=[], body=([], [For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='smaller')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), CallStmt(method=Id(name='writeln'), param=[StringLiteral(value='Ten day du cua ban la : '), Id(name='name'), StringLiteral(value=' '), Id(name='surname')]), If(ifthenStmt=[(BinaryOp(op='-', left=Id(name='aHUhu'), right=FloatLiteral(value=1e-10)), [], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')])))])], elseStmt=([], [Return(expr=IntLiteral(value=1)), If(ifthenStmt=[(BinaryOp(op='!=', left=BinaryOp(op='%', left=Id(name='tmp'), right=IntLiteral(value=2)), right=IntLiteral(value=0)), [], [Continue()])], elseStmt=([], []))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,332)) 
    def test_AST_333(self):
        input = """ Function: cajoon
        Body:

                Return y + (multi(x-1, y));
                diffLen = len(arrA) - len(arrB);
                If (piano + c <. 4.5) Then
                    Return 1;
                Else
                    hehe = (foo(3)[3*3-1][22] != xyA) <=. 3.234;
                    tmp = read();
                EndIf.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='cajoon'), param=[], body=([], [Return(expr=BinaryOp(op='+', left=Id(name='y'), right=CallStmt(method=Id(name='multi'), param=[BinaryOp(op='-', left=Id(name='x'), right=IntLiteral(value=1)), Id(name='y')]))), Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), If(ifthenStmt=[(BinaryOp(op='<.', left=BinaryOp(op='+', left=Id(name='piano'), right=Id(name='c')), right=FloatLiteral(value=4.5)), [], [Return(expr=IntLiteral(value=1))])], elseStmt=([], [Assign(lhs=Id(name='hehe'), rhs=BinaryOp(op='<=.', left=BinaryOp(op='!=', left=ArrayCell(arr=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), idx=[BinaryOp(op='-', left=BinaryOp(op='*', left=IntLiteral(value=3), right=IntLiteral(value=3)), right=IntLiteral(value=1)), IntLiteral(value=22)]), right=Id(name='xyA')), right=FloatLiteral(value=3.234))), Assign(lhs=Id(name='tmp'), rhs=CallStmt(method=Id(name='read'), param=[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,333)) 
    def test_AST_334(self):
        input = """ Function: func1
        Body:

                arr = getArrayOfEvenNum();
                If tmp % 2 != 0 Then Continue; EndIf.
                If (seeSingShare + func(3)) Then
                    arr = getArrayOfEvenNum();
                Else
                                If diffLen > 0 Then 
                    isA = True; 
                    smaller = len(arrA);
                Else 
                    isA = False; 
                    smaller = len(arrB);
                EndIf.
                    diffLen = len(arrA) - len(arrB);
                EndIf.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='func1'), param=[], body=([], [Assign(lhs=Id(name='arr'), rhs=CallStmt(method=Id(name='getArrayOfEvenNum'), param=[])), If(ifthenStmt=[(BinaryOp(op='!=', left=BinaryOp(op='%', left=Id(name='tmp'), right=IntLiteral(value=2)), right=IntLiteral(value=0)), [], [Continue()])], elseStmt=([], [])), If(ifthenStmt=[(BinaryOp(op='+', left=Id(name='seeSingShare'), right=CallStmt(method=Id(name='func'), param=[IntLiteral(value=3)])), [], [Assign(lhs=Id(name='arr'), rhs=CallStmt(method=Id(name='getArrayOfEvenNum'), param=[]))])], elseStmt=([], [If(ifthenStmt=[(BinaryOp(op='>', left=Id(name='diffLen'), right=IntLiteral(value=0)), [], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]))])], elseStmt=([], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))])), Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,334)) 

    def test_AST_335(self):
        input = """ Function: hmmOkmsa
        Body:
                Do
                    writeln("Ten day du cua ban la : ",name," ",surname);
                    string = "test function with string";
                    arr = getArrayOfEvenNum();
                While x + 5 == True EndDo.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='hmmOkmsa'), param=[], body=([], [Dowhile(sl=([], [CallStmt(method=Id(name='writeln'), param=[StringLiteral(value='Ten day du cua ban la : '), Id(name='name'), StringLiteral(value=' '), Id(name='surname')]), Assign(lhs=Id(name='string'), rhs=StringLiteral(value='test function with string')), Assign(lhs=Id(name='arr'), rhs=CallStmt(method=Id(name='getArrayOfEvenNum'), param=[]))]), exp=BinaryOp(op='==', left=BinaryOp(op='+', left=Id(name='x'), right=IntLiteral(value=5)), right=BooleanLiteral(value=True)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,335)) 

    def test_AST_336(self):
        input = """ Function: g5R
        Body:
                sum = sum + arrA[i] + arrB[i];
                            If diffLen > 0 Then 
                    isA = True; 
                    smaller = len(arrA);
                Else 
                    isA = False; 
                    smaller = len(arrB);
                EndIf.
                If (nlgt \ 3520) Then
                    diffLen = len(arrA) - len(arrB);
                Else
                    Return y + (multi(x-1, y));
                    writeln("Ten day du cua ban la : ",name," ",surname);
                EndIf.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='g5R'), param=[], body=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')]))), If(ifthenStmt=[(BinaryOp(op='>', left=Id(name='diffLen'), right=IntLiteral(value=0)), [], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]))])], elseStmt=([], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))])), If(ifthenStmt=[(BinaryOp(op='\\', left=Id(name='nlgt'), right=IntLiteral(value=3520)), [], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')])))])], elseStmt=([], [Return(expr=BinaryOp(op='+', left=Id(name='y'), right=CallStmt(method=Id(name='multi'), param=[BinaryOp(op='-', left=Id(name='x'), right=IntLiteral(value=1)), Id(name='y')]))), CallStmt(method=Id(name='writeln'), param=[StringLiteral(value='Ten day du cua ban la : '), Id(name='name'), StringLiteral(value=' '), Id(name='surname')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,336)) 
    def test_AST_337(self):
        input = """ Function: nlgt
        Body:
                diffLen = len(arrA) - len(arrB);
                arr = getArrayOfEvenNum();
                If (cajoon + 3520) Then
                    barrr(myArr[2][3][4]);
                Else
                    tmp = read();
                    writeln("Ten day du cua ban la : ",name," ",surname);
                EndIf.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='nlgt'), param=[], body=([], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), Assign(lhs=Id(name='arr'), rhs=CallStmt(method=Id(name='getArrayOfEvenNum'), param=[])), If(ifthenStmt=[(BinaryOp(op='+', left=Id(name='cajoon'), right=IntLiteral(value=3520)), [], [CallStmt(method=Id(name='barrr'), param=[ArrayCell(arr=Id(name='myArr'), idx=[IntLiteral(value=2), IntLiteral(value=3), IntLiteral(value=4)])])])], elseStmt=([], [Assign(lhs=Id(name='tmp'), rhs=CallStmt(method=Id(name='read'), param=[])), CallStmt(method=Id(name='writeln'), param=[StringLiteral(value='Ten day du cua ban la : '), Id(name='name'), StringLiteral(value=' '), Id(name='surname')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,337)) 
    def test_AST_338(self):
        input = """ Function: seeSingShare
        Body:
                tmp = read();
                barrr(myArr[2][3][4]);
                If (giacMoNgayxua +. (3-2) == 1+2*test(1)) Then
                    Return 1;
                Else
                    diffLen = len(arrA) - len(arrB);
                    Return y + (multi(x-1, y));
                EndIf.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='seeSingShare'), param=[], body=([], [Assign(lhs=Id(name='tmp'), rhs=CallStmt(method=Id(name='read'), param=[])), CallStmt(method=Id(name='barrr'), param=[ArrayCell(arr=Id(name='myArr'), idx=[IntLiteral(value=2), IntLiteral(value=3), IntLiteral(value=4)])]), If(ifthenStmt=[(BinaryOp(op='==', left=BinaryOp(op='+.', left=Id(name='giacMoNgayxua'), right=BinaryOp(op='-', left=IntLiteral(value=3), right=IntLiteral(value=2))), right=BinaryOp(op='+', left=IntLiteral(value=1), right=BinaryOp(op='*', left=IntLiteral(value=2), right=CallStmt(method=Id(name='test'), param=[IntLiteral(value=1)])))), [], [Return(expr=IntLiteral(value=1))])], elseStmt=([], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), Return(expr=BinaryOp(op='+', left=Id(name='y'), right=CallStmt(method=Id(name='multi'), param=[BinaryOp(op='-', left=Id(name='x'), right=IntLiteral(value=1)), Id(name='y')])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,338)) 
    def test_AST_339(self):
        input = """ Function: brunoMraz
        Body:
                            If diffLen > 0 Then 
                    isA = True; 
                    smaller = len(arrA);
                Else 
                    isA = False; 
                    smaller = len(arrB);
                EndIf.
                If tmp % 2 != 0 Then Continue; EndIf.
                If (jasonMraz -. 1.2e-1) Then
                    sum = sum + arrA[i] + arrB[i];
                Else
                                For (i = 0, i < smaller, 1) Do
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
                    string = "test function with string";
                EndIf.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='brunoMraz'), param=[], body=([], [If(ifthenStmt=[(BinaryOp(op='>', left=Id(name='diffLen'), right=IntLiteral(value=0)), [], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]))])], elseStmt=([], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))])), If(ifthenStmt=[(BinaryOp(op='!=', left=BinaryOp(op='%', left=Id(name='tmp'), right=IntLiteral(value=2)), right=IntLiteral(value=0)), [], [Continue()])], elseStmt=([], [])), If(ifthenStmt=[(BinaryOp(op='-.', left=Id(name='jasonMraz'), right=FloatLiteral(value=0.12)), [], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])], elseStmt=([], [For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='smaller')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), Assign(lhs=Id(name='string'), rhs=StringLiteral(value='test function with string'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,339)) 
    def test_AST_340(self):
        input = """ Function: func1
        Body:
                            If diffLen > 0 Then 
                    isA = True; 
                    smaller = len(arrA);
                Else 
                    isA = False; 
                    smaller = len(arrB);
                EndIf.
                Return 1;
                If (cajoon \. (3-2) == 1+2*test(1)) Then
                    writeln("Ten day du cua ban la : ",name," ",surname);
                Else
                    Return 1;
                    barrr(myArr[2][3][4]);
                EndIf.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='func1'), param=[], body=([], [If(ifthenStmt=[(BinaryOp(op='>', left=Id(name='diffLen'), right=IntLiteral(value=0)), [], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]))])], elseStmt=([], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))])), Return(expr=IntLiteral(value=1)), If(ifthenStmt=[(BinaryOp(op='==', left=BinaryOp(op='\\.', left=Id(name='cajoon'), right=BinaryOp(op='-', left=IntLiteral(value=3), right=IntLiteral(value=2))), right=BinaryOp(op='+', left=IntLiteral(value=1), right=BinaryOp(op='*', left=IntLiteral(value=2), right=CallStmt(method=Id(name='test'), param=[IntLiteral(value=1)])))), [], [CallStmt(method=Id(name='writeln'), param=[StringLiteral(value='Ten day du cua ban la : '), Id(name='name'), StringLiteral(value=' '), Id(name='surname')])])], elseStmt=([], [Return(expr=IntLiteral(value=1)), CallStmt(method=Id(name='barrr'), param=[ArrayCell(arr=Id(name='myArr'), idx=[IntLiteral(value=2), IntLiteral(value=3), IntLiteral(value=4)])])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,340)) 
    def test_AST_341(self):
        input = """ Function: piano
        Body:
                sum = sum + arrA[i] + arrB[i];
                getArray();
                If (nguyenHa \ 3520 == 3520) Then
                    Return y + (multi(x-1, y));
                Else
                    diffLen = len(arrA) - len(arrB);
                    diffLen = len(arrA) - len(arrB);
                EndIf.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='piano'), param=[], body=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')]))), CallStmt(method=Id(name='getArray'), param=[]), If(ifthenStmt=[(BinaryOp(op='==', left=BinaryOp(op='\\', left=Id(name='nguyenHa'), right=IntLiteral(value=3520)), right=IntLiteral(value=3520)), [], [Return(expr=BinaryOp(op='+', left=Id(name='y'), right=CallStmt(method=Id(name='multi'), param=[BinaryOp(op='-', left=Id(name='x'), right=IntLiteral(value=1)), Id(name='y')])))])], elseStmt=([], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,341)) 
    def test_AST_342(self):
        input = """ Function: nguyenHa
        Body:
                            For (i = 0, i < smaller, 1) Do
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
                If (bangKieu1 || 3) != foo(a[3][2]) + xyz Then
                    writeln("Ten day du cua ban la : ",name," ",surname);
                Else
                    diffLen = len(arrA) - len(arrB);
                    getArray();
                    arr = getArrayOfEvenNum();
                EndIf.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='nguyenHa'), param=[], body=([], [For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='smaller')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), If(ifthenStmt=[(BinaryOp(op='!=', left=BinaryOp(op='||', left=Id(name='bangKieu1'), right=IntLiteral(value=3)), right=BinaryOp(op='+', left=CallStmt(method=Id(name='foo'), param=[ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3), IntLiteral(value=2)])]), right=Id(name='xyz'))), [], [CallStmt(method=Id(name='writeln'), param=[StringLiteral(value='Ten day du cua ban la : '), Id(name='name'), StringLiteral(value=' '), Id(name='surname')])])], elseStmt=([], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), CallStmt(method=Id(name='getArray'), param=[]), Assign(lhs=Id(name='arr'), rhs=CallStmt(method=Id(name='getArrayOfEvenNum'), param=[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,342)) 
    def test_AST_343(self):
        input = """ Function: traiTimBenLe
        Body:
                diffLen = len(arrA) - len(arrB);
                If (foo +. func(3)) != func(1)[1] * 2 Then
                    writeln("Ten day du cua ban la : ",name," ",surname);
                Else
                                For (i = 0, i < smaller, 1) Do
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
                    Return y + (multi(x-1, y));
                    Return 1;
                EndIf.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='traiTimBenLe'), param=[], body=([], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), If(ifthenStmt=[(BinaryOp(op='!=', left=BinaryOp(op='+.', left=Id(name='foo'), right=CallStmt(method=Id(name='func'), param=[IntLiteral(value=3)])), right=BinaryOp(op='*', left=ArrayCell(arr=CallStmt(method=Id(name='func'), param=[IntLiteral(value=1)]), idx=[IntLiteral(value=1)]), right=IntLiteral(value=2))), [], [CallStmt(method=Id(name='writeln'), param=[StringLiteral(value='Ten day du cua ban la : '), Id(name='name'), StringLiteral(value=' '), Id(name='surname')])])], elseStmt=([], [For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='smaller')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), Return(expr=BinaryOp(op='+', left=Id(name='y'), right=CallStmt(method=Id(name='multi'), param=[BinaryOp(op='-', left=Id(name='x'), right=IntLiteral(value=1)), Id(name='y')]))), Return(expr=IntLiteral(value=1))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,343)) 
    def test_AST_344(self):
        input = """ Function: bangKieu1
        Body:
                Return 1;
                If (aHUhu || 1.2e-1) != 3 Then
                    diffLen = len(arrA) - len(arrB);
                Else
                    hehe = (foo(3)[3*3-1][22] != xyA) <=. 3.234;
                    diffLen = len(arrA) - len(arrB);
                    barrr(myArr[2][3][4]);
                EndIf.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='bangKieu1'), param=[], body=([], [Return(expr=IntLiteral(value=1)), If(ifthenStmt=[(BinaryOp(op='!=', left=BinaryOp(op='||', left=Id(name='aHUhu'), right=FloatLiteral(value=0.12)), right=IntLiteral(value=3)), [], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')])))])], elseStmt=([], [Assign(lhs=Id(name='hehe'), rhs=BinaryOp(op='<=.', left=BinaryOp(op='!=', left=ArrayCell(arr=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), idx=[BinaryOp(op='-', left=BinaryOp(op='*', left=IntLiteral(value=3), right=IntLiteral(value=3)), right=IntLiteral(value=1)), IntLiteral(value=22)]), right=Id(name='xyA')), right=FloatLiteral(value=3.234))), Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), CallStmt(method=Id(name='barrr'), param=[ArrayCell(arr=Id(name='myArr'), idx=[IntLiteral(value=2), IntLiteral(value=3), IntLiteral(value=4)])])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,344)) 
    def test_AST_345(self):
        input = """ Function: khiCodonEmnhoai
        Body:
                hehe = (foo(3)[3*3-1][22] != xyA) <=. 3.234;
                If (seeSingShare + a[3+foo(2)]) > 10e-11 Then
                    If diffLen > 0 Then 
                    isA = True; 
                    smaller = len(arrA);
                Else 
                    isA = False; 
                    smaller = len(arrB);
                EndIf.
                Else
                    If tmp % 2 != 0 Then Continue; EndIf.
                    getArray();
                    writeln("Ten day du cua ban la : ",name," ",surname);
                EndIf.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='khiCodonEmnhoai'), param=[], body=([], [Assign(lhs=Id(name='hehe'), rhs=BinaryOp(op='<=.', left=BinaryOp(op='!=', left=ArrayCell(arr=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), idx=[BinaryOp(op='-', left=BinaryOp(op='*', left=IntLiteral(value=3), right=IntLiteral(value=3)), right=IntLiteral(value=1)), IntLiteral(value=22)]), right=Id(name='xyA')), right=FloatLiteral(value=3.234))), If(ifthenStmt=[(BinaryOp(op='>', left=BinaryOp(op='+', left=Id(name='seeSingShare'), right=ArrayCell(arr=Id(name='a'), idx=[BinaryOp(op='+', left=IntLiteral(value=3), right=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=2)]))])), right=FloatLiteral(value=1e-10)), [], [If(ifthenStmt=[(BinaryOp(op='>', left=Id(name='diffLen'), right=IntLiteral(value=0)), [], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]))])], elseStmt=([], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))]))])], elseStmt=([], [If(ifthenStmt=[(BinaryOp(op='!=', left=BinaryOp(op='%', left=Id(name='tmp'), right=IntLiteral(value=2)), right=IntLiteral(value=0)), [], [Continue()])], elseStmt=([], [])), CallStmt(method=Id(name='getArray'), param=[]), CallStmt(method=Id(name='writeln'), param=[StringLiteral(value='Ten day du cua ban la : '), Id(name='name'), StringLiteral(value=' '), Id(name='surname')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,345)) 
    def test_AST_346(self):
        input = """ Function: cajoon
        Body:
                While func(3) Do
                    If tmp % 2 != 0 Then Continue; EndIf.
                    arr = getArrayOfEvenNum();
                    tmp = read();
                EndWhile.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='cajoon'), param=[], body=([], [While(exp=CallStmt(method=Id(name='func'), param=[IntLiteral(value=3)]), sl=([], [If(ifthenStmt=[(BinaryOp(op='!=', left=BinaryOp(op='%', left=Id(name='tmp'), right=IntLiteral(value=2)), right=IntLiteral(value=0)), [], [Continue()])], elseStmt=([], [])), Assign(lhs=Id(name='arr'), rhs=CallStmt(method=Id(name='getArrayOfEvenNum'), param=[])), Assign(lhs=Id(name='tmp'), rhs=CallStmt(method=Id(name='read'), param=[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,346)) 
    def test_AST_347(self):
        input = """ Function: foo
        Body:
                While x + 5 == True Do
                    For (i = 0, i < smaller, 1) Do
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
                    tmp = read();
                    diffLen = len(arrA) - len(arrB);
                EndWhile.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='foo'), param=[], body=([], [While(exp=BinaryOp(op='==', left=BinaryOp(op='+', left=Id(name='x'), right=IntLiteral(value=5)), right=BooleanLiteral(value=True)), sl=([], [For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='smaller')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), Assign(lhs=Id(name='tmp'), rhs=CallStmt(method=Id(name='read'), param=[])), Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,347)) 
    def test_AST_348(self):
        input = """ Function: nickyMjnaj
        Body:
                While 1.2e-1 Do
                    string = "test function with string";
                    hehe = (foo(3)[3*3-1][22] != xyA) <=. 3.234;
                    diffLen = len(arrA) - len(arrB);
                EndWhile.
            
        EndBody.
        Function: foo
            Body:
            getArray();
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='nickyMjnaj'), param=[], body=([], [While(exp=FloatLiteral(value=0.12), sl=([], [Assign(lhs=Id(name='string'), rhs=StringLiteral(value='test function with string')), Assign(lhs=Id(name='hehe'), rhs=BinaryOp(op='<=.', left=BinaryOp(op='!=', left=ArrayCell(arr=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), idx=[BinaryOp(op='-', left=BinaryOp(op='*', left=IntLiteral(value=3), right=IntLiteral(value=3)), right=IntLiteral(value=1)), IntLiteral(value=22)]), right=Id(name='xyA')), right=FloatLiteral(value=3.234))), Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')])))]))])), FuncDecl(name=Id(name='foo'), param=[], body=([], [CallStmt(method=Id(name='getArray'), param=[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,348)) 
    def test_AST_349(self):
        input = """ Function: adamLevine
        Body:
                While 10e-11 Do
                    barrr(myArr[2][3][4]);
                    tmp = read();
                    For (i = 0, i < smaller, 1) Do
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
                EndWhile.
            
        EndBody.
        Function: jasonMraz
            Body:
            sum = sum + arrA[i] + arrB[i];
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='adamLevine'), param=[], body=([], [While(exp=FloatLiteral(value=1e-10), sl=([], [CallStmt(method=Id(name='barrr'), param=[ArrayCell(arr=Id(name='myArr'), idx=[IntLiteral(value=2), IntLiteral(value=3), IntLiteral(value=4)])]), Assign(lhs=Id(name='tmp'), rhs=CallStmt(method=Id(name='read'), param=[])), For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='smaller')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))]))]))])), FuncDecl(name=Id(name='jasonMraz'), param=[], body=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,349)) 
    def test_AST_350(self):
        input = """ Function: nlgt
        Body:
                While 10e-11 Do
                    If diffLen > 0 Then 
                    isA = True; 
                    smaller = len(arrA);
                Else 
                    isA = False; 
                    smaller = len(arrB);
                EndIf.
                    If tmp % 2 != 0 Then Continue; EndIf.
                    If tmp % 2 != 0 Then Continue; EndIf.
                EndWhile.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='nlgt'), param=[], body=([], [While(exp=FloatLiteral(value=1e-10), sl=([], [If(ifthenStmt=[(BinaryOp(op='>', left=Id(name='diffLen'), right=IntLiteral(value=0)), [], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]))])], elseStmt=([], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))])), If(ifthenStmt=[(BinaryOp(op='!=', left=BinaryOp(op='%', left=Id(name='tmp'), right=IntLiteral(value=2)), right=IntLiteral(value=0)), [], [Continue()])], elseStmt=([], [])), If(ifthenStmt=[(BinaryOp(op='!=', left=BinaryOp(op='%', left=Id(name='tmp'), right=IntLiteral(value=2)), right=IntLiteral(value=0)), [], [Continue()])], elseStmt=([], []))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,350)) 
    def test_AST_351(self):
        input = """ Function: bar
        Body:
                While func(3) Do
                    diffLen = len(arrA) - len(arrB);
                    hehe = (foo(3)[3*3-1][22] != xyA) <=. 3.234;
                    tmp = read();
                EndWhile.
            
        EndBody.
        Function: jasonMraz
            Body:
            diffLen = len(arrA) - len(arrB);
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='bar'), param=[], body=([], [While(exp=CallStmt(method=Id(name='func'), param=[IntLiteral(value=3)]), sl=([], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), Assign(lhs=Id(name='hehe'), rhs=BinaryOp(op='<=.', left=BinaryOp(op='!=', left=ArrayCell(arr=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), idx=[BinaryOp(op='-', left=BinaryOp(op='*', left=IntLiteral(value=3), right=IntLiteral(value=3)), right=IntLiteral(value=1)), IntLiteral(value=22)]), right=Id(name='xyA')), right=FloatLiteral(value=3.234))), Assign(lhs=Id(name='tmp'), rhs=CallStmt(method=Id(name='read'), param=[]))]))])), FuncDecl(name=Id(name='jasonMraz'), param=[], body=([], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,351)) 
    def test_AST_352(self):
        input = """ Function: khiCodonEmnhoai
        Body:
                While a <= 4 Do
                    Return 1;
                    getArray();
                    If diffLen > 0 Then 
                    isA = True; 
                    smaller = len(arrA);
                Else 
                    isA = False; 
                    smaller = len(arrB);
                EndIf.
                EndWhile.
            
        EndBody.
        Function: seeSingShare
            Body:
            Return y + (multi(x-1, y));
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='khiCodonEmnhoai'), param=[], body=([], [While(exp=BinaryOp(op='<=', left=Id(name='a'), right=IntLiteral(value=4)), sl=([], [Return(expr=IntLiteral(value=1)), CallStmt(method=Id(name='getArray'), param=[]), If(ifthenStmt=[(BinaryOp(op='>', left=Id(name='diffLen'), right=IntLiteral(value=0)), [], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]))])], elseStmt=([], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))]))]))])), FuncDecl(name=Id(name='seeSingShare'), param=[], body=([], [Return(expr=BinaryOp(op='+', left=Id(name='y'), right=CallStmt(method=Id(name='multi'), param=[BinaryOp(op='-', left=Id(name='x'), right=IntLiteral(value=1)), Id(name='y')])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,352)) 
    def test_AST_353(self):
        input = """ Var: ans;
    Function: func1
        Body:
                While c <. 4.5 Do
                    barrr(myArr[2][3][4]);
                    string = "test function with string";
                    sum = sum + arrA[i] + arrB[i];
                EndWhile.
            
        EndBody. """
        expect = Program([VarDecl(variable=Id(name='ans'), varDimen=[], varInit=None), FuncDecl(name=Id(name='func1'), param=[], body=([], [While(exp=BinaryOp(op='<.', left=Id(name='c'), right=FloatLiteral(value=4.5)), sl=([], [CallStmt(method=Id(name='barrr'), param=[ArrayCell(arr=Id(name='myArr'), idx=[IntLiteral(value=2), IntLiteral(value=3), IntLiteral(value=4)])]), Assign(lhs=Id(name='string'), rhs=StringLiteral(value='test function with string')), Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,353)) 
    def test_AST_354(self):
        input = """ Var: x=4;
    Function: bar
        Body:
                While c <. 4.5 Do
                    writeln("Ten day du cua ban la : ",name," ",surname);
                    writeln("Ten day du cua ban la : ",name," ",surname);
                    diffLen = len(arrA) - len(arrB);
                EndWhile.
            
        EndBody. """
        expect = Program([VarDecl(variable=Id(name='x'), varDimen=[], varInit=IntLiteral(value=4)), FuncDecl(name=Id(name='bar'), param=[], body=([], [While(exp=BinaryOp(op='<.', left=Id(name='c'), right=FloatLiteral(value=4.5)), sl=([], [CallStmt(method=Id(name='writeln'), param=[StringLiteral(value='Ten day du cua ban la : '), Id(name='name'), StringLiteral(value=' '), Id(name='surname')]), CallStmt(method=Id(name='writeln'), param=[StringLiteral(value='Ten day du cua ban la : '), Id(name='name'), StringLiteral(value=' '), Id(name='surname')]), Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,354)) 
    def test_AST_355(self):
        input = """ Var: x=4;
    Function: func1
        Body:
                While 3520 Do
                    barrr(myArr[2][3][4]);
                    If tmp % 2 != 0 Then Continue; EndIf.
                    tmp = read();
                EndWhile.
            
        EndBody.
        Function: func1
            Body:
            writeln("Ten day du cua ban la : ",name," ",surname);
        EndBody. """
        expect = Program([VarDecl(variable=Id(name='x'), varDimen=[], varInit=IntLiteral(value=4)), FuncDecl(name=Id(name='func1'), param=[], body=([], [While(exp=IntLiteral(value=3520), sl=([], [CallStmt(method=Id(name='barrr'), param=[ArrayCell(arr=Id(name='myArr'), idx=[IntLiteral(value=2), IntLiteral(value=3), IntLiteral(value=4)])]), If(ifthenStmt=[(BinaryOp(op='!=', left=BinaryOp(op='%', left=Id(name='tmp'), right=IntLiteral(value=2)), right=IntLiteral(value=0)), [], [Continue()])], elseStmt=([], [])), Assign(lhs=Id(name='tmp'), rhs=CallStmt(method=Id(name='read'), param=[]))]))])), FuncDecl(name=Id(name='func1'), param=[], body=([], [CallStmt(method=Id(name='writeln'), param=[StringLiteral(value='Ten day du cua ban la : '), Id(name='name'), StringLiteral(value=' '), Id(name='surname')])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,355)) 
    def test_AST_356(self):
        input = """ Var: ans;
    Function: bangKieu1
        Body:
                While bar[1] Do
                    Return 1;
                    Return 1;
                    If tmp % 2 != 0 Then Continue; EndIf.
                EndWhile.
            
        EndBody. """
        expect = Program([VarDecl(variable=Id(name='ans'), varDimen=[], varInit=None), FuncDecl(name=Id(name='bangKieu1'), param=[], body=([], [While(exp=ArrayCell(arr=Id(name='bar'), idx=[IntLiteral(value=1)]), sl=([], [Return(expr=IntLiteral(value=1)), Return(expr=IntLiteral(value=1)), If(ifthenStmt=[(BinaryOp(op='!=', left=BinaryOp(op='%', left=Id(name='tmp'), right=IntLiteral(value=2)), right=IntLiteral(value=0)), [], [Continue()])], elseStmt=([], []))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,356)) 
    def test_AST_357(self):
        input = """ Var: ans;
    Function: foo
        Body:
                While 3520 Do
                    For (i = 0, i < smaller, 1) Do
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
                    Return 1;
                    diffLen = len(arrA) - len(arrB);
                EndWhile.
            
                    string = "test function with string";
                    If traiTimBenLe != (3) Then
                        barrr(myArr[2][3][4]);
                    ElseIf jasonMraz <=. khiCodonEmnhoai Then
                        sum = sum + arrA[i] + arrB[i];
                    EndIf.
                
        EndBody. """
        expect = Program([VarDecl(variable=Id(name='ans'), varDimen=[], varInit=None), FuncDecl(name=Id(name='foo'), param=[], body=([], [While(exp=IntLiteral(value=3520), sl=([], [For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='smaller')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), Return(expr=IntLiteral(value=1)), Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')])))])), Assign(lhs=Id(name='string'), rhs=StringLiteral(value='test function with string')), If(ifthenStmt=[(BinaryOp(op='!=', left=Id(name='traiTimBenLe'), right=IntLiteral(value=3)), [], [CallStmt(method=Id(name='barrr'), param=[ArrayCell(arr=Id(name='myArr'), idx=[IntLiteral(value=2), IntLiteral(value=3), IntLiteral(value=4)])])]), (BinaryOp(op='<=.', left=Id(name='jasonMraz'), right=Id(name='khiCodonEmnhoai')), [], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])], elseStmt=([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,357)) 
    def test_AST_358(self):
        input = """ Var: x=4;
    Function: bar
        Body:
                While func(3) Do
                    getArray();
                    diffLen = len(arrA) - len(arrB);
                    tmp = read();
                EndWhile.
            
        EndBody. """
        expect = Program([VarDecl(variable=Id(name='x'), varDimen=[], varInit=IntLiteral(value=4)), FuncDecl(name=Id(name='bar'), param=[], body=([], [While(exp=CallStmt(method=Id(name='func'), param=[IntLiteral(value=3)]), sl=([], [CallStmt(method=Id(name='getArray'), param=[]), Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), Assign(lhs=Id(name='tmp'), rhs=CallStmt(method=Id(name='read'), param=[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,358)) 
    def test_AST_359(self):
        input = """ Var: x=4;
    Function: brunoMraz
        Body:
                While foo(a[3][2]) + xyz Do
                    getArray();
                    writeln("Ten day du cua ban la : ",name," ",surname);
                    writeln("Ten day du cua ban la : ",name," ",surname);
                EndWhile.
            
        EndBody. """
        expect = Program([VarDecl(variable=Id(name='x'), varDimen=[], varInit=IntLiteral(value=4)), FuncDecl(name=Id(name='brunoMraz'), param=[], body=([], [While(exp=BinaryOp(op='+', left=CallStmt(method=Id(name='foo'), param=[ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3), IntLiteral(value=2)])]), right=Id(name='xyz')), sl=([], [CallStmt(method=Id(name='getArray'), param=[]), CallStmt(method=Id(name='writeln'), param=[StringLiteral(value='Ten day du cua ban la : '), Id(name='name'), StringLiteral(value=' '), Id(name='surname')]), CallStmt(method=Id(name='writeln'), param=[StringLiteral(value='Ten day du cua ban la : '), Id(name='name'), StringLiteral(value=' '), Id(name='surname')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,359)) 
    def test_AST_360(self):
        input = """ Var: c, d[2][4];
    Function: jasonMraz
        Body:
                While a <= 4 Do
                    diffLen = len(arrA) - len(arrB);
                    For (i = 0, i < smaller, 1) Do
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
                    sum = sum + arrA[i] + arrB[i];
                EndWhile.
            
        EndBody. """
        expect = Program([VarDecl(variable=Id(name='c'), varDimen=[], varInit=None), VarDecl(variable=Id(name='d'), varDimen=[IntLiteral(value=2), IntLiteral(value=4)], varInit=None), FuncDecl(name=Id(name='jasonMraz'), param=[], body=([], [While(exp=BinaryOp(op='<=', left=Id(name='a'), right=IntLiteral(value=4)), sl=([], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='smaller')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,360)) 
    def test_AST_361(self):
        input = """ Var: x=4;
    Var: c, d[2][4];
    Function: bar
        Body:
                For (barz = 1.2e-1, func(1)[1] * 2, c <. 4.5) Do
                    If tmp % 2 != 0 Then Continue; EndIf.
                    diffLen = len(arrA) - len(arrB);
                EndFor.
            
                    While 3520 Do
                        arr = getArrayOfEvenNum();
                        hehe = (foo(3)[3*3-1][22] != xyA) <=. 3.234;
                    EndWhile.
                
        EndBody. """
        expect = Program([VarDecl(variable=Id(name='x'), varDimen=[], varInit=IntLiteral(value=4)), VarDecl(variable=Id(name='c'), varDimen=[], varInit=None), VarDecl(variable=Id(name='d'), varDimen=[IntLiteral(value=2), IntLiteral(value=4)], varInit=None), FuncDecl(name=Id(name='bar'), param=[], body=([], [For(idx1=Id(name='barz'), expr1=FloatLiteral(value=0.12), expr2=BinaryOp(op='*', left=ArrayCell(arr=CallStmt(method=Id(name='func'), param=[IntLiteral(value=1)]), idx=[IntLiteral(value=1)]), right=IntLiteral(value=2)), expr3=BinaryOp(op='<.', left=Id(name='c'), right=FloatLiteral(value=4.5)), loop=([], [If(ifthenStmt=[(BinaryOp(op='!=', left=BinaryOp(op='%', left=Id(name='tmp'), right=IntLiteral(value=2)), right=IntLiteral(value=0)), [], [Continue()])], elseStmt=([], [])), Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')])))])), While(exp=IntLiteral(value=3520), sl=([], [Assign(lhs=Id(name='arr'), rhs=CallStmt(method=Id(name='getArrayOfEvenNum'), param=[])), Assign(lhs=Id(name='hehe'), rhs=BinaryOp(op='<=.', left=BinaryOp(op='!=', left=ArrayCell(arr=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), idx=[BinaryOp(op='-', left=BinaryOp(op='*', left=IntLiteral(value=3), right=IntLiteral(value=3)), right=IntLiteral(value=1)), IntLiteral(value=22)]), right=Id(name='xyA')), right=FloatLiteral(value=3.234)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,361)) 
    def test_AST_362(self):
        input = """ Var: a[2];
    Var: ans;
    Function: biBe
        Body:
                For (saQe = 10e-11, a[3+foo(2)], a <= 4) Do
                    tmp = read();
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
            
        EndBody.
        Function: adamLevine
            Body:
            arr = getArrayOfEvenNum();
        EndBody. """
        expect = Program([VarDecl(variable=Id(name='a'), varDimen=[IntLiteral(value=2)], varInit=None), VarDecl(variable=Id(name='ans'), varDimen=[], varInit=None), FuncDecl(name=Id(name='biBe'), param=[], body=([], [For(idx1=Id(name='saQe'), expr1=FloatLiteral(value=1e-10), expr2=ArrayCell(arr=Id(name='a'), idx=[BinaryOp(op='+', left=IntLiteral(value=3), right=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=2)]))]), expr3=BinaryOp(op='<=', left=Id(name='a'), right=IntLiteral(value=4)), loop=([], [Assign(lhs=Id(name='tmp'), rhs=CallStmt(method=Id(name='read'), param=[])), Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))]))])), FuncDecl(name=Id(name='adamLevine'), param=[], body=([], [Assign(lhs=Id(name='arr'), rhs=CallStmt(method=Id(name='getArrayOfEvenNum'), param=[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,362)) 
    def test_AST_363(self):
        input = """ Var: a[2];
    Var:s, c, d[2][4];
    Function: giacMoNgayxua
        Body:
                For (ids = func(3), func(3), a <= 4) Do
                    x = (a+1 < 2) < 3;
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
            
                    diffLen = len(arrA) - len(arrB);
                    If hmmOkmsa <= (foo(thuanNgo)) Then
                        For (i = 0, i < smaller, 1) Do
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
                    ElseIf seeSingShare <=. func(1)[1] * 2 Then
                        hehe = (foo(3)[3*3-1][22] != xyA) <=. 3.234;
                    EndIf.
                
        EndBody. """
        expect = Program([VarDecl(variable=Id(name='a'), varDimen=[IntLiteral(value=2)], varInit=None), VarDecl(variable=Id(name='s'), varDimen=[], varInit=None), VarDecl(variable=Id(name='c'), varDimen=[], varInit=None), VarDecl(variable=Id(name='d'), varDimen=[IntLiteral(value=2), IntLiteral(value=4)], varInit=None), FuncDecl(name=Id(name='giacMoNgayxua'), param=[], body=([], [For(idx1=Id(name='ids'), expr1=CallStmt(method=Id(name='func'), param=[IntLiteral(value=3)]), expr2=CallStmt(method=Id(name='func'), param=[IntLiteral(value=3)]), expr3=BinaryOp(op='<=', left=Id(name='a'), right=IntLiteral(value=4)), loop=([], [Assign(lhs=Id(name='x'), rhs=BinaryOp(op='<', left=BinaryOp(op='<', left=BinaryOp(op='+', left=Id(name='a'), right=IntLiteral(value=1)), right=IntLiteral(value=2)), right=IntLiteral(value=3))), Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), If(ifthenStmt=[(BinaryOp(op='<=', left=Id(name='hmmOkmsa'), right=CallStmt(method=Id(name='foo'), param=[Id(name='thuanNgo')])), [], [For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='smaller')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))]))]), (BinaryOp(op='<=.', left=Id(name='seeSingShare'), right=BinaryOp(op='*', left=ArrayCell(arr=CallStmt(method=Id(name='func'), param=[IntLiteral(value=1)]), idx=[IntLiteral(value=1)]), right=IntLiteral(value=2))), [], [Assign(lhs=Id(name='hehe'), rhs=BinaryOp(op='<=.', left=BinaryOp(op='!=', left=ArrayCell(arr=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), idx=[BinaryOp(op='-', left=BinaryOp(op='*', left=IntLiteral(value=3), right=IntLiteral(value=3)), right=IntLiteral(value=1)), IntLiteral(value=22)]), right=Id(name='xyA')), right=FloatLiteral(value=3.234)))])], elseStmt=([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,363)) 
    def test_AST_364(self):
        input = """ Var: ans;
    Var: a[2];
    Function: seeSingShare
        Body:
                For (nickyMjnaj = func(3), a <= 4, bar[1]) Do
                    Return 1;
                    hehe = (foo(3)[3*3-1][22] != xyA) <=. 3.234;
                EndFor.
            
                    While (3-2) == 1+2*test(1) Do
                        diffLen = len(arrA) - len(arrB);
                        arr = getArrayOfEvenNum();
                    EndWhile.
                
                    diffLen = len(arrA) - len(arrB);
                    If conTho <= (foo(3) + bar(a[3]) =/= a[3][3][b[2][2][7]]) Then
                        sum = sum + arrA[i] + arrB[i];
                    ElseIf jasonMraz >= bar[1] Then
                        tmp = read();
                    EndIf.
                
        EndBody.
        Function: cajoon
            Body:
            sum = sum + arrA[i] + arrB[i];
        EndBody. """
        expect = Program([VarDecl(variable=Id(name='ans'), varDimen=[], varInit=None), VarDecl(variable=Id(name='a'), varDimen=[IntLiteral(value=2)], varInit=None), FuncDecl(name=Id(name='seeSingShare'), param=[], body=([], [For(idx1=Id(name='nickyMjnaj'), expr1=CallStmt(method=Id(name='func'), param=[IntLiteral(value=3)]), expr2=BinaryOp(op='<=', left=Id(name='a'), right=IntLiteral(value=4)), expr3=ArrayCell(arr=Id(name='bar'), idx=[IntLiteral(value=1)]), loop=([], [Return(expr=IntLiteral(value=1)), Assign(lhs=Id(name='hehe'), rhs=BinaryOp(op='<=.', left=BinaryOp(op='!=', left=ArrayCell(arr=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), idx=[BinaryOp(op='-', left=BinaryOp(op='*', left=IntLiteral(value=3), right=IntLiteral(value=3)), right=IntLiteral(value=1)), IntLiteral(value=22)]), right=Id(name='xyA')), right=FloatLiteral(value=3.234)))])), While(exp=BinaryOp(op='==', left=BinaryOp(op='-', left=IntLiteral(value=3), right=IntLiteral(value=2)), right=BinaryOp(op='+', left=IntLiteral(value=1), right=BinaryOp(op='*', left=IntLiteral(value=2), right=CallStmt(method=Id(name='test'), param=[IntLiteral(value=1)])))), sl=([], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), Assign(lhs=Id(name='arr'), rhs=CallStmt(method=Id(name='getArrayOfEvenNum'), param=[]))])), Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), If(ifthenStmt=[(BinaryOp(op='<=', left=Id(name='conTho'), right=BinaryOp(op='=/=', left=BinaryOp(op='+', left=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), right=CallStmt(method=Id(name='bar'), param=[ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3)])])), right=ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3), IntLiteral(value=3), ArrayCell(arr=Id(name='b'), idx=[IntLiteral(value=2), IntLiteral(value=2), IntLiteral(value=7)])]))), [], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))]), (BinaryOp(op='>=', left=Id(name='jasonMraz'), right=ArrayCell(arr=Id(name='bar'), idx=[IntLiteral(value=1)])), [], [Assign(lhs=Id(name='tmp'), rhs=CallStmt(method=Id(name='read'), param=[]))])], elseStmt=([], []))])), FuncDecl(name=Id(name='cajoon'), param=[], body=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,364)) 
    def test_AST_365(self):
        input = """ Var: ans;
    Var: x=4;
    Function: func1
        Body:
                For (foo = foo(3) + bar(a[3]) =/= a[3][3][b[2][2][7]], foo(a[3][2]) + xyz, a <= 4) Do
                    barrr(myArr[2][3][4]);
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
            
                    While func(3) Do
                        hehe = (foo(3)[3*3-1][22] != xyA) <=. 3.234;
                        sum = sum + arrA[i] + arrB[i];
                    EndWhile.
                
                    If tmp % 2 != 0 Then Continue; EndIf.
                    If func1 != ((3-2) == 1+2*test(1)) Then
                        getArray();
                    ElseIf barz =/= 3 Then
                        barrr(myArr[2][3][4]);
                    EndIf.
                
        EndBody. """
        expect = Program([VarDecl(variable=Id(name='ans'), varDimen=[], varInit=None), VarDecl(variable=Id(name='x'), varDimen=[], varInit=IntLiteral(value=4)), FuncDecl(name=Id(name='func1'), param=[], body=([], [For(idx1=Id(name='foo'), expr1=BinaryOp(op='=/=', left=BinaryOp(op='+', left=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), right=CallStmt(method=Id(name='bar'), param=[ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3)])])), right=ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3), IntLiteral(value=3), ArrayCell(arr=Id(name='b'), idx=[IntLiteral(value=2), IntLiteral(value=2), IntLiteral(value=7)])])), expr2=BinaryOp(op='+', left=CallStmt(method=Id(name='foo'), param=[ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3), IntLiteral(value=2)])]), right=Id(name='xyz')), expr3=BinaryOp(op='<=', left=Id(name='a'), right=IntLiteral(value=4)), loop=([], [CallStmt(method=Id(name='barrr'), param=[ArrayCell(arr=Id(name='myArr'), idx=[IntLiteral(value=2), IntLiteral(value=3), IntLiteral(value=4)])]), Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), While(exp=CallStmt(method=Id(name='func'), param=[IntLiteral(value=3)]), sl=([], [Assign(lhs=Id(name='hehe'), rhs=BinaryOp(op='<=.', left=BinaryOp(op='!=', left=ArrayCell(arr=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), idx=[BinaryOp(op='-', left=BinaryOp(op='*', left=IntLiteral(value=3), right=IntLiteral(value=3)), right=IntLiteral(value=1)), IntLiteral(value=22)]), right=Id(name='xyA')), right=FloatLiteral(value=3.234))), Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), If(ifthenStmt=[(BinaryOp(op='!=', left=BinaryOp(op='%', left=Id(name='tmp'), right=IntLiteral(value=2)), right=IntLiteral(value=0)), [], [Continue()])], elseStmt=([], [])), If(ifthenStmt=[(BinaryOp(op='!=', left=Id(name='func1'), right=BinaryOp(op='==', left=BinaryOp(op='-', left=IntLiteral(value=3), right=IntLiteral(value=2)), right=BinaryOp(op='+', left=IntLiteral(value=1), right=BinaryOp(op='*', left=IntLiteral(value=2), right=CallStmt(method=Id(name='test'), param=[IntLiteral(value=1)]))))), [], [CallStmt(method=Id(name='getArray'), param=[])]), (BinaryOp(op='=/=', left=Id(name='barz'), right=IntLiteral(value=3)), [], [CallStmt(method=Id(name='barrr'), param=[ArrayCell(arr=Id(name='myArr'), idx=[IntLiteral(value=2), IntLiteral(value=3), IntLiteral(value=4)])])])], elseStmt=([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,365)) 
    def test_AST_366(self):
        input = """ Var:s, c, d[2][4];
    Var: a[2];
    Function: biBe
        Body:
                For (aHUhu = 3, 3, (3-2) == 1+2*test(1)) Do
                    If diffLen > 0 Then 
                    isA = True; 
                    smaller = len(arrA);
                Else 
                    isA = False; 
                    smaller = len(arrB);
                EndIf.
                    a[2] =foo(3) + bar(a[3]) =/= a[3][3][b[2][2][7]];
                EndFor.
            
        EndBody. """
        expect = Program([VarDecl(variable=Id(name='s'), varDimen=[], varInit=None), VarDecl(variable=Id(name='c'), varDimen=[], varInit=None), VarDecl(variable=Id(name='d'), varDimen=[IntLiteral(value=2), IntLiteral(value=4)], varInit=None), VarDecl(variable=Id(name='a'), varDimen=[IntLiteral(value=2)], varInit=None), FuncDecl(name=Id(name='biBe'), param=[], body=([], [For(idx1=Id(name='aHUhu'), expr1=IntLiteral(value=3), expr2=IntLiteral(value=3), expr3=BinaryOp(op='==', left=BinaryOp(op='-', left=IntLiteral(value=3), right=IntLiteral(value=2)), right=BinaryOp(op='+', left=IntLiteral(value=1), right=BinaryOp(op='*', left=IntLiteral(value=2), right=CallStmt(method=Id(name='test'), param=[IntLiteral(value=1)])))), loop=([], [If(ifthenStmt=[(BinaryOp(op='>', left=Id(name='diffLen'), right=IntLiteral(value=0)), [], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]))])], elseStmt=([], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))])), Assign(lhs=ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=2)]), rhs=BinaryOp(op='=/=', left=BinaryOp(op='+', left=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), right=CallStmt(method=Id(name='bar'), param=[ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3)])])), right=ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3), IntLiteral(value=3), ArrayCell(arr=Id(name='b'), idx=[IntLiteral(value=2), IntLiteral(value=2), IntLiteral(value=7)])])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,366)) 
    def test_AST_367(self):
        input = """ Var:s, c, d[2][4];
    Var: ans;
    Function: khiCodonEmnhoai
        Body:
                For (caRot = func(3), a[3+foo(2)], 0xFFAA) Do
                    getArray();
                    sum = sum + arrA[i] + arrB[i];
                EndFor.

                    While foo(thuanNgo) Do
                        For (i = 0, i < smaller, 1) Do
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
                        getArray();
                    EndWhile.

        EndBody. """
        expect = Program([VarDecl(variable=Id(name='s'), varDimen=[], varInit=None), VarDecl(variable=Id(name='c'), varDimen=[], varInit=None), VarDecl(variable=Id(name='d'), varDimen=[IntLiteral(value=2), IntLiteral(value=4)], varInit=None), VarDecl(variable=Id(name='ans'), varDimen=[], varInit=None), FuncDecl(name=Id(name='khiCodonEmnhoai'), param=[], body=([], [For(idx1=Id(name='caRot'), expr1=CallStmt(method=Id(name='func'), param=[IntLiteral(value=3)]), expr2=ArrayCell(arr=Id(name='a'), idx=[BinaryOp(op='+', left=IntLiteral(value=3), right=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=2)]))]), expr3=IntLiteral(value=65450), loop=([], [CallStmt(method=Id(name='getArray'), param=[]), Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), While(exp=CallStmt(method=Id(name='foo'), param=[Id(name='thuanNgo')]), sl=([], [For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='smaller')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), CallStmt(method=Id(name='getArray'), param=[])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,367)) 
    def test_AST_368(self):
        input = """ Var:s, c, d[2][4];
    Var: ans;
    Function: giacMoNgayxua
        Body:
                For (foo = 1.2e-1, 1231 + -11 == False, 1231 + -11 == False) Do
                    For (i = 0, i < smaller, 1) Do
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
                    sum = sum + arrA[i] + arrB[i];
                EndFor.

                    While x + 5 == True Do
                        diffLen = len(arrA) - len(arrB);
                        string = "test function with string";
                    EndWhile.

                    a[2] =foo(3) + bar(a[3]) =/= a[3][3][b[2][2][7]];
                    If nickyMjnaj == (a[3+foo(2)]) Then
                        tmp = read();
                    ElseIf guitar <. ((3-2) == 1+2*test(1)) Then
                        While func(3) Do
                    getArray();
                    diffLen = len(arrA) - len(arrB);
                    tmp = read();
                EndWhile.
                    EndIf.

        EndBody. """
        expect = Program([VarDecl(variable=Id(name='s'), varDimen=[], varInit=None), VarDecl(variable=Id(name='c'), varDimen=[], varInit=None), VarDecl(variable=Id(name='d'), varDimen=[IntLiteral(value=2), IntLiteral(value=4)], varInit=None), VarDecl(variable=Id(name='ans'), varDimen=[], varInit=None), FuncDecl(name=Id(name='giacMoNgayxua'), param=[], body=([], [For(idx1=Id(name='foo'), expr1=FloatLiteral(value=0.12), expr2=BinaryOp(op='==', left=BinaryOp(op='+', left=IntLiteral(value=1231), right=UnaryOp(op='-', body=IntLiteral(value=11))), right=BooleanLiteral(value=True)), expr3=BinaryOp(op='==', left=BinaryOp(op='+', left=IntLiteral(value=1231), right=UnaryOp(op='-', body=IntLiteral(value=11))), right=BooleanLiteral(value=True)), loop=([], [For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='smaller')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), While(exp=BinaryOp(op='==', left=BinaryOp(op='+', left=Id(name='x'), right=IntLiteral(value=5)), right=BooleanLiteral(value=True)), sl=([], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), Assign(lhs=Id(name='string'), rhs=StringLiteral(value='test function with string'))])), Assign(lhs=ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=2)]), rhs=BinaryOp(op='=/=', left=BinaryOp(op='+', left=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), right=CallStmt(method=Id(name='bar'), param=[ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3)])])), right=ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3), IntLiteral(value=3), ArrayCell(arr=Id(name='b'), idx=[IntLiteral(value=2), IntLiteral(value=2), IntLiteral(value=7)])]))), If(ifthenStmt=[(BinaryOp(op='==', left=Id(name='nickyMjnaj'), right=ArrayCell(arr=Id(name='a'), idx=[BinaryOp(op='+', left=IntLiteral(value=3), right=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=2)]))])), [], [Assign(lhs=Id(name='tmp'), rhs=CallStmt(method=Id(name='read'), param=[]))]), (BinaryOp(op='<.', left=Id(name='guitar'), right=BinaryOp(op='==', left=BinaryOp(op='-', left=IntLiteral(value=3), right=IntLiteral(value=2)), right=BinaryOp(op='+', left=IntLiteral(value=1), right=BinaryOp(op='*', left=IntLiteral(value=2), right=CallStmt(method=Id(name='test'), param=[IntLiteral(value=1)]))))), [], [While(exp=CallStmt(method=Id(name='func'), param=[IntLiteral(value=3)]), sl=([], [CallStmt(method=Id(name='getArray'), param=[]), Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), Assign(lhs=Id(name='tmp'), rhs=CallStmt(method=Id(name='read'), param=[]))]))])], elseStmt=([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,368)) 

    def test_AST_370(self):
        input = """ Var:s, c, d[2][4];
    Var: ans;
    Function: aHUhu
        Body:
                For (caRot = 1.2e-1, x + 5 == True, foo(a[3][2]) + xyz) Do
                    If tmp % 2 != 0 Then Continue; EndIf.
                    If tmp % 2 != 0 Then Continue; EndIf.
                EndFor.
            
                    If diffLen > 0 Then 
                    isA = True; 
                    smaller = len(arrA);
                Else 
                    isA = False; 
                    smaller = len(arrB);
                EndIf.
                    If brunoMraz != (func(3)) Then
                        getArray();
                    ElseIf haAnhTuan123 != foo Then
                        If diffLen > 0 Then 
                    isA = True; 
                    smaller = len(arrA);
                Else 
                    isA = False; 
                    smaller = len(arrB);
                EndIf.
                    EndIf.
                
        EndBody. """
        expect = Program([VarDecl(variable=Id(name='s'), varDimen=[], varInit=None), VarDecl(variable=Id(name='c'), varDimen=[], varInit=None), VarDecl(variable=Id(name='d'), varDimen=[IntLiteral(value=2), IntLiteral(value=4)], varInit=None), VarDecl(variable=Id(name='ans'), varDimen=[], varInit=None), FuncDecl(name=Id(name='aHUhu'), param=[], body=([], [For(idx1=Id(name='caRot'), expr1=FloatLiteral(value=0.12), expr2=BinaryOp(op='==', left=BinaryOp(op='+', left=Id(name='x'), right=IntLiteral(value=5)), right=BooleanLiteral(value=True)), expr3=BinaryOp(op='+', left=CallStmt(method=Id(name='foo'), param=[ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3), IntLiteral(value=2)])]), right=Id(name='xyz')), loop=([], [If(ifthenStmt=[(BinaryOp(op='!=', left=BinaryOp(op='%', left=Id(name='tmp'), right=IntLiteral(value=2)), right=IntLiteral(value=0)), [], [Continue()])], elseStmt=([], [])), If(ifthenStmt=[(BinaryOp(op='!=', left=BinaryOp(op='%', left=Id(name='tmp'), right=IntLiteral(value=2)), right=IntLiteral(value=0)), [], [Continue()])], elseStmt=([], []))])), If(ifthenStmt=[(BinaryOp(op='>', left=Id(name='diffLen'), right=IntLiteral(value=0)), [], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]))])], elseStmt=([], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))])), If(ifthenStmt=[(BinaryOp(op='!=', left=Id(name='brunoMraz'), right=CallStmt(method=Id(name='func'), param=[IntLiteral(value=3)])), [], [CallStmt(method=Id(name='getArray'), param=[])]), (BinaryOp(op='!=', left=Id(name='haAnhTuan123'), right=Id(name='foo')), [], [If(ifthenStmt=[(BinaryOp(op='>', left=Id(name='diffLen'), right=IntLiteral(value=0)), [], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]))])], elseStmt=([], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))]))])], elseStmt=([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,370)) 
    def test_AST_371(self):
        input = """ Var: ans;
    Var: ans;
    Function: adamLevine
        Body:
                For (traiTimBenLe = 3520, 3, 0xFFAA) Do
                    diffLen = len(arrA) - len(arrB);
                    barrr(myArr[2][3][4]);
                EndFor.
            
        EndBody.
        Function: giacMoNgayxua
            Body:
            Return 1;
        EndBody. """
        expect = Program([VarDecl(variable=Id(name='ans'), varDimen=[], varInit=None), VarDecl(variable=Id(name='ans'), varDimen=[], varInit=None), FuncDecl(name=Id(name='adamLevine'), param=[], body=([], [For(idx1=Id(name='traiTimBenLe'), expr1=IntLiteral(value=3520), expr2=IntLiteral(value=3), expr3=IntLiteral(value=65450), loop=([], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), CallStmt(method=Id(name='barrr'), param=[ArrayCell(arr=Id(name='myArr'), idx=[IntLiteral(value=2), IntLiteral(value=3), IntLiteral(value=4)])])]))])), FuncDecl(name=Id(name='giacMoNgayxua'), param=[], body=([], [Return(expr=IntLiteral(value=1))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,371)) 
    def test_AST_372(self):
        input = """ Var: a[2];
    Var: a[2];
    Function: func1
        Body:
                For (brunoMraz = foo(a[3][2]) + xyz, foo(3) + bar(a[3]) =/= a[3][3][b[2][2][7]], foo(3) + bar(a[3]) =/= a[3][3][b[2][2][7]]) Do
                    getArray();
                    For (i = 0, i < smaller, 1) Do
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
                EndFor.
            
        EndBody.
        Function: brunoMraz
            Body:
            While a <= 4 Do
                    diffLen = len(arrA) - len(arrB);
                    For (i = 0, i < smaller, 1) Do
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
                    sum = sum + arrA[i] + arrB[i];
                EndWhile.
        EndBody. """
        expect = Program([VarDecl(variable=Id(name='a'), varDimen=[IntLiteral(value=2)], varInit=None), VarDecl(variable=Id(name='a'), varDimen=[IntLiteral(value=2)], varInit=None), FuncDecl(name=Id(name='func1'), param=[], body=([], [For(idx1=Id(name='brunoMraz'), expr1=BinaryOp(op='+', left=CallStmt(method=Id(name='foo'), param=[ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3), IntLiteral(value=2)])]), right=Id(name='xyz')), expr2=BinaryOp(op='=/=', left=BinaryOp(op='+', left=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), right=CallStmt(method=Id(name='bar'), param=[ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3)])])), right=ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3), IntLiteral(value=3), ArrayCell(arr=Id(name='b'), idx=[IntLiteral(value=2), IntLiteral(value=2), IntLiteral(value=7)])])), expr3=BinaryOp(op='=/=', left=BinaryOp(op='+', left=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), right=CallStmt(method=Id(name='bar'), param=[ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3)])])), right=ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3), IntLiteral(value=3), ArrayCell(arr=Id(name='b'), idx=[IntLiteral(value=2), IntLiteral(value=2), IntLiteral(value=7)])])), loop=([], [CallStmt(method=Id(name='getArray'), param=[]), For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='smaller')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))]))]))])), FuncDecl(name=Id(name='brunoMraz'), param=[], body=([], [While(exp=BinaryOp(op='<=', left=Id(name='a'), right=IntLiteral(value=4)), sl=([], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='smaller')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,372)) 
    def test_AST_373(self):
        input = """ Var:s, c, d[2][4];
    Var: ans;
    Function: caRot
        Body:
                For (biBe = 0xFFAA, bar[1], foo(thuanNgo)) Do
                    diffLen = len(arrA) - len(arrB);
                    getArray();
                EndFor.
            
        EndBody. """
        expect = Program([VarDecl(variable=Id(name='s'), varDimen=[], varInit=None), VarDecl(variable=Id(name='c'), varDimen=[], varInit=None), VarDecl(variable=Id(name='d'), varDimen=[IntLiteral(value=2), IntLiteral(value=4)], varInit=None), VarDecl(variable=Id(name='ans'), varDimen=[], varInit=None), FuncDecl(name=Id(name='caRot'), param=[], body=([], [For(idx1=Id(name='biBe'), expr1=IntLiteral(value=65450), expr2=ArrayCell(arr=Id(name='bar'), idx=[IntLiteral(value=1)]), expr3=CallStmt(method=Id(name='foo'), param=[Id(name='thuanNgo')]), loop=([], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), CallStmt(method=Id(name='getArray'), param=[])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,373)) 
    def test_AST_374(self):
        input = """ Var: ans;
    Var: x=4;
    Function: khiCodonEmnhoai
        Body:
                For (conTho = foo(3) + bar(a[3]) =/= a[3][3][b[2][2][7]], func(1)[1] * 2, func(3)) Do
                    If tmp % 2 != 0 Then Continue; EndIf.
                    If tmp % 2 != 0 Then Continue; EndIf.
                EndFor.
            
        EndBody. """
        expect = Program([VarDecl(variable=Id(name='ans'), varDimen=[], varInit=None), VarDecl(variable=Id(name='x'), varDimen=[], varInit=IntLiteral(value=4)), FuncDecl(name=Id(name='khiCodonEmnhoai'), param=[], body=([], [For(idx1=Id(name='conTho'), expr1=BinaryOp(op='=/=', left=BinaryOp(op='+', left=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), right=CallStmt(method=Id(name='bar'), param=[ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3)])])), right=ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3), IntLiteral(value=3), ArrayCell(arr=Id(name='b'), idx=[IntLiteral(value=2), IntLiteral(value=2), IntLiteral(value=7)])])), expr2=BinaryOp(op='*', left=ArrayCell(arr=CallStmt(method=Id(name='func'), param=[IntLiteral(value=1)]), idx=[IntLiteral(value=1)]), right=IntLiteral(value=2)), expr3=CallStmt(method=Id(name='func'), param=[IntLiteral(value=3)]), loop=([], [If(ifthenStmt=[(BinaryOp(op='!=', left=BinaryOp(op='%', left=Id(name='tmp'), right=IntLiteral(value=2)), right=IntLiteral(value=0)), [], [Continue()])], elseStmt=([], [])), If(ifthenStmt=[(BinaryOp(op='!=', left=BinaryOp(op='%', left=Id(name='tmp'), right=IntLiteral(value=2)), right=IntLiteral(value=0)), [], [Continue()])], elseStmt=([], []))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,374)) 
    def test_AST_375(self):
        input = """ Var: a[2];
    Var: ans;
    Function: cajoon
        Body:
                For (jasonMraz = foo(thuanNgo), foo(a[3][2]) + xyz, c <. 4.5) Do
                    x = a+1 < (2 < 3);
                    a[2] =foo(3) + bar(a[3]) =/= a[3][3][b[2][2][7]];
                EndFor.
            
        EndBody. """
        expect = Program([VarDecl(variable=Id(name='a'), varDimen=[IntLiteral(value=2)], varInit=None), VarDecl(variable=Id(name='ans'), varDimen=[], varInit=None), FuncDecl(name=Id(name='cajoon'), param=[], body=([], [For(idx1=Id(name='jasonMraz'), expr1=CallStmt(method=Id(name='foo'), param=[Id(name='thuanNgo')]), expr2=BinaryOp(op='+', left=CallStmt(method=Id(name='foo'), param=[ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3), IntLiteral(value=2)])]), right=Id(name='xyz')), expr3=BinaryOp(op='<.', left=Id(name='c'), right=FloatLiteral(value=4.5)), loop=([], [Assign(lhs=Id(name='x'), rhs=BinaryOp(op='<', left=BinaryOp(op='+', left=Id(name='a'), right=IntLiteral(value=1)), right=BinaryOp(op='<', left=IntLiteral(value=2), right=IntLiteral(value=3)))), Assign(lhs=ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=2)]), rhs=BinaryOp(op='=/=', left=BinaryOp(op='+', left=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), right=CallStmt(method=Id(name='bar'), param=[ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3)])])), right=ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3), IntLiteral(value=3), ArrayCell(arr=Id(name='b'), idx=[IntLiteral(value=2), IntLiteral(value=2), IntLiteral(value=7)])])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,375)) 
    def test_AST_376(self):
        input = """ Var: a[2];
    Var: a[2];
    Function: barz
        Body:
                For (seeSingShare = a[3+foo(2)], c <. 4.5, foo(3) + bar(a[3]) =/= a[3][3][b[2][2][7]]) Do
                    diffLen = len(arrA) - len(arrB);
                    arr = getArrayOfEvenNum();
                EndFor.
            
        EndBody.
        Function: nguyenHa
            Body:
            getArray();
        EndBody. """
        expect = Program([VarDecl(variable=Id(name='a'), varDimen=[IntLiteral(value=2)], varInit=None), VarDecl(variable=Id(name='a'), varDimen=[IntLiteral(value=2)], varInit=None), FuncDecl(name=Id(name='barz'), param=[], body=([], [For(idx1=Id(name='seeSingShare'), expr1=ArrayCell(arr=Id(name='a'), idx=[BinaryOp(op='+', left=IntLiteral(value=3), right=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=2)]))]), expr2=BinaryOp(op='<.', left=Id(name='c'), right=FloatLiteral(value=4.5)), expr3=BinaryOp(op='=/=', left=BinaryOp(op='+', left=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), right=CallStmt(method=Id(name='bar'), param=[ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3)])])), right=ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3), IntLiteral(value=3), ArrayCell(arr=Id(name='b'), idx=[IntLiteral(value=2), IntLiteral(value=2), IntLiteral(value=7)])])), loop=([], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), Assign(lhs=Id(name='arr'), rhs=CallStmt(method=Id(name='getArrayOfEvenNum'), param=[]))]))])), FuncDecl(name=Id(name='nguyenHa'), param=[], body=([], [CallStmt(method=Id(name='getArray'), param=[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,376)) 
    def test_AST_377(self):
        input = """ Var:s, c, d[2][4];
    Var: x=4;
    Function: foo
        Body:
                For (jasonMraz = bar[1], 0xFFAA, func(3)) Do
                    hehe = (foo(3)[3*3-1][22] != xyA) <=. 3.234;
                    Return y + (multi(x-1, y));
                EndFor.
            
        EndBody. """
        expect = Program([VarDecl(variable=Id(name='s'), varDimen=[], varInit=None), VarDecl(variable=Id(name='c'), varDimen=[], varInit=None), VarDecl(variable=Id(name='d'), varDimen=[IntLiteral(value=2), IntLiteral(value=4)], varInit=None), VarDecl(variable=Id(name='x'), varDimen=[], varInit=IntLiteral(value=4)), FuncDecl(name=Id(name='foo'), param=[], body=([], [For(idx1=Id(name='jasonMraz'), expr1=ArrayCell(arr=Id(name='bar'), idx=[IntLiteral(value=1)]), expr2=IntLiteral(value=65450), expr3=CallStmt(method=Id(name='func'), param=[IntLiteral(value=3)]), loop=([], [Assign(lhs=Id(name='hehe'), rhs=BinaryOp(op='<=.', left=BinaryOp(op='!=', left=ArrayCell(arr=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), idx=[BinaryOp(op='-', left=BinaryOp(op='*', left=IntLiteral(value=3), right=IntLiteral(value=3)), right=IntLiteral(value=1)), IntLiteral(value=22)]), right=Id(name='xyA')), right=FloatLiteral(value=3.234))), Return(expr=BinaryOp(op='+', left=Id(name='y'), right=CallStmt(method=Id(name='multi'), param=[BinaryOp(op='-', left=Id(name='x'), right=IntLiteral(value=1)), Id(name='y')])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,377)) 
    def test_AST_378(self):
        input = """ Var:s, c, d[2][4];
    Var:s, c, d[2][4];
    Function: nguyenHa
        Body:
                For (hmmOkmsa = a <= 4, 0xFFAA, func(1)[1] * 2) Do
                    While a <= 4 Do
                    diffLen = len(arrA) - len(arrB);
                    For (i = 0, i < smaller, 1) Do
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
                    sum = sum + arrA[i] + arrB[i];
                EndWhile.
                    For (i = 0, i < smaller, 1) Do
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
                EndFor.
            
        EndBody. """
        expect = Program([VarDecl(variable=Id(name='s'), varDimen=[], varInit=None), VarDecl(variable=Id(name='c'), varDimen=[], varInit=None), VarDecl(variable=Id(name='d'), varDimen=[IntLiteral(value=2), IntLiteral(value=4)], varInit=None), VarDecl(variable=Id(name='s'), varDimen=[], varInit=None), VarDecl(variable=Id(name='c'), varDimen=[], varInit=None), VarDecl(variable=Id(name='d'), varDimen=[IntLiteral(value=2), IntLiteral(value=4)], varInit=None), FuncDecl(name=Id(name='nguyenHa'), param=[], body=([], [For(idx1=Id(name='hmmOkmsa'), expr1=BinaryOp(op='<=', left=Id(name='a'), right=IntLiteral(value=4)), expr2=IntLiteral(value=65450), expr3=BinaryOp(op='*', left=ArrayCell(arr=CallStmt(method=Id(name='func'), param=[IntLiteral(value=1)]), idx=[IntLiteral(value=1)]), right=IntLiteral(value=2)), loop=([], [While(exp=BinaryOp(op='<=', left=Id(name='a'), right=IntLiteral(value=4)), sl=([], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='smaller')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='smaller')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,378)) 
    def test_AST_379(self):
        input = """ Var: ans;
    Var:s, c, d[2][4];
    Function: nguyenHa
        Body:
                For (nlgt = a <= 4, c <. 4.5, (3-2) == 1+2*test(1)) Do
                    sum = sum + arrA[i] + arrB[i];
                    Return y + (multi(x-1, y));
                EndFor.
            
                    While 3520 Do
                        arr = getArrayOfEvenNum();
                        writeln("Ten day du cua ban la : ",name," ",surname);
                    EndWhile.
                
        EndBody. """
        expect = Program([VarDecl(variable=Id(name='ans'), varDimen=[], varInit=None), VarDecl(variable=Id(name='s'), varDimen=[], varInit=None), VarDecl(variable=Id(name='c'), varDimen=[], varInit=None), VarDecl(variable=Id(name='d'), varDimen=[IntLiteral(value=2), IntLiteral(value=4)], varInit=None), FuncDecl(name=Id(name='nguyenHa'), param=[], body=([], [For(idx1=Id(name='nlgt'), expr1=BinaryOp(op='<=', left=Id(name='a'), right=IntLiteral(value=4)), expr2=BinaryOp(op='<.', left=Id(name='c'), right=FloatLiteral(value=4.5)), expr3=BinaryOp(op='==', left=BinaryOp(op='-', left=IntLiteral(value=3), right=IntLiteral(value=2)), right=BinaryOp(op='+', left=IntLiteral(value=1), right=BinaryOp(op='*', left=IntLiteral(value=2), right=CallStmt(method=Id(name='test'), param=[IntLiteral(value=1)])))), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')]))), Return(expr=BinaryOp(op='+', left=Id(name='y'), right=CallStmt(method=Id(name='multi'), param=[BinaryOp(op='-', left=Id(name='x'), right=IntLiteral(value=1)), Id(name='y')])))])), While(exp=IntLiteral(value=3520), sl=([], [Assign(lhs=Id(name='arr'), rhs=CallStmt(method=Id(name='getArrayOfEvenNum'), param=[])), CallStmt(method=Id(name='writeln'), param=[StringLiteral(value='Ten day du cua ban la : '), Id(name='name'), StringLiteral(value=' '), Id(name='surname')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,379)) 
    def test_AST_380(self):
        input = """ Var: a[2];
    Var: ans;
    Function: barz
        Body:
                For (cajoon = foo(3) + bar(a[3]) =/= a[3][3][b[2][2][7]], 1.2e-1, c <. 4.5) Do
                    Return 1;
                    If diffLen > 0 Then 
                    isA = True; 
                    smaller = len(arrA);
                Else 
                    isA = False; 
                    smaller = len(arrB);
                EndIf.
                EndFor.
            
        EndBody.
        Function: g5R
            Body:
            getArray();
        EndBody. """
        expect = Program([VarDecl(variable=Id(name='a'), varDimen=[IntLiteral(value=2)], varInit=None), VarDecl(variable=Id(name='ans'), varDimen=[], varInit=None), FuncDecl(name=Id(name='barz'), param=[], body=([], [For(idx1=Id(name='cajoon'), expr1=BinaryOp(op='=/=', left=BinaryOp(op='+', left=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), right=CallStmt(method=Id(name='bar'), param=[ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3)])])), right=ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3), IntLiteral(value=3), ArrayCell(arr=Id(name='b'), idx=[IntLiteral(value=2), IntLiteral(value=2), IntLiteral(value=7)])])), expr2=FloatLiteral(value=0.12), expr3=BinaryOp(op='<.', left=Id(name='c'), right=FloatLiteral(value=4.5)), loop=([], [Return(expr=IntLiteral(value=1)), If(ifthenStmt=[(BinaryOp(op='>', left=Id(name='diffLen'), right=IntLiteral(value=0)), [], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]))])], elseStmt=([], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))]))]))])), FuncDecl(name=Id(name='g5R'), param=[], body=([], [CallStmt(method=Id(name='getArray'), param=[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,380)) 
    def test_AST_381(self):
        input = """ Function: khiCodonEmnhoai
        Body:
                Do
                    string = "test function with string";
                    writeln("Ten day du cua ban la : ",name," ",surname);
                    isA = True;
                    smaller = len(arrA);
                While a <= 4 EndDo.
            
                    For (biBe = x + 5 == True, 1.2e-1, 1.2e-1) Do
                        arr = getArrayOfEvenNum();
                        x = a+1 < (2 < 3);
                    EndFor.
                
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='khiCodonEmnhoai'), param=[], body=([], [Dowhile(sl=([], [Assign(lhs=Id(name='string'), rhs=StringLiteral(value='test function with string')), CallStmt(method=Id(name='writeln'), param=[StringLiteral(value='Ten day du cua ban la : '), Id(name='name'), StringLiteral(value=' '), Id(name='surname')]), Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]))]), exp=BinaryOp(op='<=', left=Id(name='a'), right=IntLiteral(value=4))), For(idx1=Id(name='biBe'), expr1=BinaryOp(op='==', left=BinaryOp(op='+', left=Id(name='x'), right=IntLiteral(value=5)), right=BooleanLiteral(value=True)), expr2=FloatLiteral(value=0.12), expr3=FloatLiteral(value=0.12), loop=([], [Assign(lhs=Id(name='arr'), rhs=CallStmt(method=Id(name='getArrayOfEvenNum'), param=[])), Assign(lhs=Id(name='x'), rhs=BinaryOp(op='<', left=BinaryOp(op='+', left=Id(name='a'), right=IntLiteral(value=1)), right=BinaryOp(op='<', left=IntLiteral(value=2), right=IntLiteral(value=3))))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,381)) 
    def test_AST_382(self):
        input = """ Function: foo
        Body:
                Do
                    x = a+1 < (2 < 3);
                    a[3 + foo(2)] = a[b[2][3]] + 4;
                    sum = sum + arrA[i] + arrB[i];
                While foo(3) + bar(a[3]) =/= a[3][3][b[2][2][7]] EndDo.
            
                    For (seeSingShare = 3520, c <. 4.5, foo(3) + bar(a[3]) =/= a[3][3][b[2][2][7]]) Do
                        If tmp % 2 != 0 Then Continue; EndIf.
                        diffLen = len(arrA) - len(arrB);
                    EndFor.
                
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='foo'), param=[], body=([], [Dowhile(sl=([], [Assign(lhs=Id(name='x'), rhs=BinaryOp(op='<', left=BinaryOp(op='+', left=Id(name='a'), right=IntLiteral(value=1)), right=BinaryOp(op='<', left=IntLiteral(value=2), right=IntLiteral(value=3)))), Assign(lhs=ArrayCell(arr=Id(name='a'), idx=[BinaryOp(op='+', left=IntLiteral(value=3), right=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=2)]))]), rhs=BinaryOp(op='+', left=ArrayCell(arr=Id(name='a'), idx=[ArrayCell(arr=Id(name='b'), idx=[IntLiteral(value=2), IntLiteral(value=3)])]), right=IntLiteral(value=4))), Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))]), exp=BinaryOp(op='=/=', left=BinaryOp(op='+', left=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), right=CallStmt(method=Id(name='bar'), param=[ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3)])])), right=ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3), IntLiteral(value=3), ArrayCell(arr=Id(name='b'), idx=[IntLiteral(value=2), IntLiteral(value=2), IntLiteral(value=7)])]))), For(idx1=Id(name='seeSingShare'), expr1=IntLiteral(value=3520), expr2=BinaryOp(op='<.', left=Id(name='c'), right=FloatLiteral(value=4.5)), expr3=BinaryOp(op='=/=', left=BinaryOp(op='+', left=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), right=CallStmt(method=Id(name='bar'), param=[ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3)])])), right=ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3), IntLiteral(value=3), ArrayCell(arr=Id(name='b'), idx=[IntLiteral(value=2), IntLiteral(value=2), IntLiteral(value=7)])])), loop=([], [If(ifthenStmt=[(BinaryOp(op='!=', left=BinaryOp(op='%', left=Id(name='tmp'), right=IntLiteral(value=2)), right=IntLiteral(value=0)), [], [Continue()])], elseStmt=([], [])), Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,382)) 
    def test_AST_383(self):
        input = """ Function: haAnhTuan123
        Body:
                Do
                    a[3 + foo(2)] = a[b[2][3]] + 4;
                    Return 1;
                    Break;
                While 10e-11 EndDo.
            
                    For (aHUhu = bar[1], a[3+foo(2)], 3520) Do
                        While a <= 4 Do
                    diffLen = len(arrA) - len(arrB);
                    For (i = 0, i < smaller, 1) Do
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
                    sum = sum + arrA[i] + arrB[i];
                EndWhile.
                        Return 2;
                    EndFor.
                
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='haAnhTuan123'), param=[], body=([], [Dowhile(sl=([], [Assign(lhs=ArrayCell(arr=Id(name='a'), idx=[BinaryOp(op='+', left=IntLiteral(value=3), right=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=2)]))]), rhs=BinaryOp(op='+', left=ArrayCell(arr=Id(name='a'), idx=[ArrayCell(arr=Id(name='b'), idx=[IntLiteral(value=2), IntLiteral(value=3)])]), right=IntLiteral(value=4))), Return(expr=IntLiteral(value=1)), Break()]), exp=FloatLiteral(value=1e-10)), For(idx1=Id(name='aHUhu'), expr1=ArrayCell(arr=Id(name='bar'), idx=[IntLiteral(value=1)]), expr2=ArrayCell(arr=Id(name='a'), idx=[BinaryOp(op='+', left=IntLiteral(value=3), right=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=2)]))]), expr3=IntLiteral(value=3520), loop=([], [While(exp=BinaryOp(op='<=', left=Id(name='a'), right=IntLiteral(value=4)), sl=([], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='smaller')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), Return(expr=IntLiteral(value=2))]))]))])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,383)) 
    def test_AST_384(self):
        input = """ Function: bangKieu1
        Body:
                Do
                    sum = sum + arrA[i] + arrB[i];
                    hehe = (foo(3)[3*3-1][22] != xyA) <=. 3.234;
                    a[3 + foo(2)] = a[b[2][3]] + 4;
                While 3 EndDo.
            
                    For (seeSingShare = x + 5 == True, a <= 4, c <. 4.5) Do
                        a[3 + foo(2)] = a[b[2][3]] + 4;
                        Return;
                    EndFor.
                
                    While 10e-11 Do
                        getArray();
                        Return (ax + by == 0);
                    EndWhile.
                
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='bangKieu1'), param=[], body=([], [Dowhile(sl=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')]))), Assign(lhs=Id(name='hehe'), rhs=BinaryOp(op='<=.', left=BinaryOp(op='!=', left=ArrayCell(arr=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), idx=[BinaryOp(op='-', left=BinaryOp(op='*', left=IntLiteral(value=3), right=IntLiteral(value=3)), right=IntLiteral(value=1)), IntLiteral(value=22)]), right=Id(name='xyA')), right=FloatLiteral(value=3.234))), Assign(lhs=ArrayCell(arr=Id(name='a'), idx=[BinaryOp(op='+', left=IntLiteral(value=3), right=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=2)]))]), rhs=BinaryOp(op='+', left=ArrayCell(arr=Id(name='a'), idx=[ArrayCell(arr=Id(name='b'), idx=[IntLiteral(value=2), IntLiteral(value=3)])]), right=IntLiteral(value=4)))]), exp=IntLiteral(value=3)), For(idx1=Id(name='seeSingShare'), expr1=BinaryOp(op='==', left=BinaryOp(op='+', left=Id(name='x'), right=IntLiteral(value=5)), right=BooleanLiteral(value=True)), expr2=BinaryOp(op='<=', left=Id(name='a'), right=IntLiteral(value=4)), expr3=BinaryOp(op='<.', left=Id(name='c'), right=FloatLiteral(value=4.5)), loop=([], [Assign(lhs=ArrayCell(arr=Id(name='a'), idx=[BinaryOp(op='+', left=IntLiteral(value=3), right=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=2)]))]), rhs=BinaryOp(op='+', left=ArrayCell(arr=Id(name='a'), idx=[ArrayCell(arr=Id(name='b'), idx=[IntLiteral(value=2), IntLiteral(value=3)])]), right=IntLiteral(value=4))), Return(expr=None)])), While(exp=FloatLiteral(value=1e-10), sl=([], [CallStmt(method=Id(name='getArray'), param=[]), Return(expr=BinaryOp(op='==', left=BinaryOp(op='+', left=Id(name='ax'), right=Id(name='by')), right=IntLiteral(value=0)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,384)) 
    def test_AST_385(self):
        input = """ Function: adamLevine
        Body:
                Do
                    diffLen = len(arrA) - len(arrB);
                    getArray();
                    sum = sum + arrA[i] + arrB[i];
                While foo(a[3][2]) + xyz EndDo.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='adamLevine'), param=[], body=([], [Dowhile(sl=([], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), CallStmt(method=Id(name='getArray'), param=[]), Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))]), exp=BinaryOp(op='+', left=CallStmt(method=Id(name='foo'), param=[ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3), IntLiteral(value=2)])]), right=Id(name='xyz')))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,385)) 
    def test_AST_386(self):
        input = """ Function: hmmOkmsa
        Body:
                Do
                    For (i = 0, i < smaller, 1) Do
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
                    If diffLen > 0 Then 
                    isA = True; 
                    smaller = len(arrA);
                Else 
                    isA = False; 
                    smaller = len(arrB);
                EndIf.
                    Continue;
                While (3-2) == 1+2*test(1) EndDo.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='hmmOkmsa'), param=[], body=([], [Dowhile(sl=([], [For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='smaller')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), If(ifthenStmt=[(BinaryOp(op='>', left=Id(name='diffLen'), right=IntLiteral(value=0)), [], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]))])], elseStmt=([], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))])), Continue()]), exp=BinaryOp(op='==', left=BinaryOp(op='-', left=IntLiteral(value=3), right=IntLiteral(value=2)), right=BinaryOp(op='+', left=IntLiteral(value=1), right=BinaryOp(op='*', left=IntLiteral(value=2), right=CallStmt(method=Id(name='test'), param=[IntLiteral(value=1)])))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,386)) 
    def test_AST_387(self):
        input = """ Function: brunoMraz
        Body:
                Do
                    Break;
                    getArray();
                    Return 2;
                While c <. 4.5 EndDo.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='brunoMraz'), param=[], body=([], [Dowhile(sl=([], [Break(), CallStmt(method=Id(name='getArray'), param=[]), Return(expr=IntLiteral(value=2))]), exp=BinaryOp(op='<.', left=Id(name='c'), right=FloatLiteral(value=4.5)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,387)) 
    def test_AST_388(self):
        input = """ Function: bangKieu1
        Body:
                Do
                    hehe = (foo(3)[3*3-1][22] != xyA) <=. 3.234;
                    Return 1;
                    Return 1;
                While 3520 EndDo.
            
                    For (haAnhTuan123 = func(1)[1] * 2, foo(a[3][2]) + xyz, 1.2e-1) Do
                        If diffLen > 0 Then 
                    isA = True; 
                    smaller = len(arrA);
                Else 
                    isA = False; 
                    smaller = len(arrB);
                EndIf.
                        Return 1;
                    EndFor.
                
                    While 1231 + -11 == False Do
                        barrr(myArr[2][3][4]);
                        hehe = (foo(3)[3*3-1][22] != xyA) <=. 3.234;
                    EndWhile.
                
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='bangKieu1'), param=[], body=([], [Dowhile(sl=([], [Assign(lhs=Id(name='hehe'), rhs=BinaryOp(op='<=.', left=BinaryOp(op='!=', left=ArrayCell(arr=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), idx=[BinaryOp(op='-', left=BinaryOp(op='*', left=IntLiteral(value=3), right=IntLiteral(value=3)), right=IntLiteral(value=1)), IntLiteral(value=22)]), right=Id(name='xyA')), right=FloatLiteral(value=3.234))), Return(expr=IntLiteral(value=1)), Return(expr=IntLiteral(value=1))]), exp=IntLiteral(value=3520)), For(idx1=Id(name='haAnhTuan123'), expr1=BinaryOp(op='*', left=ArrayCell(arr=CallStmt(method=Id(name='func'), param=[IntLiteral(value=1)]), idx=[IntLiteral(value=1)]), right=IntLiteral(value=2)), expr2=BinaryOp(op='+', left=CallStmt(method=Id(name='foo'), param=[ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3), IntLiteral(value=2)])]), right=Id(name='xyz')), expr3=FloatLiteral(value=0.12), loop=([], [If(ifthenStmt=[(BinaryOp(op='>', left=Id(name='diffLen'), right=IntLiteral(value=0)), [], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]))])], elseStmt=([], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))])), Return(expr=IntLiteral(value=1))])), While(exp=BinaryOp(op='==', left=BinaryOp(op='+', left=IntLiteral(value=1231), right=UnaryOp(op='-', body=IntLiteral(value=11))), right=BooleanLiteral(value=True)), sl=([], [CallStmt(method=Id(name='barrr'), param=[ArrayCell(arr=Id(name='myArr'), idx=[IntLiteral(value=2), IntLiteral(value=3), IntLiteral(value=4)])]), Assign(lhs=Id(name='hehe'), rhs=BinaryOp(op='<=.', left=BinaryOp(op='!=', left=ArrayCell(arr=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), idx=[BinaryOp(op='-', left=BinaryOp(op='*', left=IntLiteral(value=3), right=IntLiteral(value=3)), right=IntLiteral(value=1)), IntLiteral(value=22)]), right=Id(name='xyA')), right=FloatLiteral(value=3.234)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,388)) 
    def test_AST_389(self):
        input = """ Function: hmmOkmsa
        Body:
                    For (cajoon = 1231 + -11 == False, 3, foo(3) + bar(a[3]) =/= a[3][3][b[2][2][7]]) Do
                        diffLen = len(arrA) - len(arrB);
                        sum = sum + arrA[i] + arrB[i];
                    EndFor.
                
                Do
                    tmp = read();
                    Return 2;
                    If diffLen > 0 Then 
                    isA = True; 
                    smaller = len(arrA);
                Else 
                    isA = False; 
                    smaller = len(arrB);
                EndIf.
                While a <= 4 EndDo.
            
                    For (adamLevine = c <. 4.5, c <. 4.5, 1.2e-1) Do
                        tmp = read();
                        If tmp % 2 != 0 Then Continue; EndIf.
                    EndFor.
                
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='hmmOkmsa'), param=[], body=([], [For(idx1=Id(name='cajoon'), expr1=BinaryOp(op='==', left=BinaryOp(op='+', left=IntLiteral(value=1231), right=UnaryOp(op='-', body=IntLiteral(value=11))), right=BooleanLiteral(value=True)), expr2=IntLiteral(value=3), expr3=BinaryOp(op='=/=', left=BinaryOp(op='+', left=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), right=CallStmt(method=Id(name='bar'), param=[ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3)])])), right=ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3), IntLiteral(value=3), ArrayCell(arr=Id(name='b'), idx=[IntLiteral(value=2), IntLiteral(value=2), IntLiteral(value=7)])])), loop=([], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), Dowhile(sl=([], [Assign(lhs=Id(name='tmp'), rhs=CallStmt(method=Id(name='read'), param=[])), Return(expr=IntLiteral(value=2)), If(ifthenStmt=[(BinaryOp(op='>', left=Id(name='diffLen'), right=IntLiteral(value=0)), [], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]))])], elseStmt=([], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))]))]), exp=BinaryOp(op='<=', left=Id(name='a'), right=IntLiteral(value=4))), For(idx1=Id(name='adamLevine'), expr1=BinaryOp(op='<.', left=Id(name='c'), right=FloatLiteral(value=4.5)), expr2=BinaryOp(op='<.', left=Id(name='c'), right=FloatLiteral(value=4.5)), expr3=FloatLiteral(value=0.12), loop=([], [Assign(lhs=Id(name='tmp'), rhs=CallStmt(method=Id(name='read'), param=[])), If(ifthenStmt=[(BinaryOp(op='!=', left=BinaryOp(op='%', left=Id(name='tmp'), right=IntLiteral(value=2)), right=IntLiteral(value=0)), [], [Continue()])], elseStmt=([], []))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,389)) 
    def test_AST_390(self):
        input = """ Function: hmmOkmsa
        Body:
                Do
                    Continue;
                    For (i = 0, i < smaller, 1) Do
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
                    While func(3) Do
                    getArray();
                    diffLen = len(arrA) - len(arrB);
                    tmp = read();
                EndWhile.
                While 3 EndDo.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='hmmOkmsa'), param=[], body=([], [Dowhile(sl=([], [Continue(), For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='smaller')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), While(exp=CallStmt(method=Id(name='func'), param=[IntLiteral(value=3)]), sl=([], [CallStmt(method=Id(name='getArray'), param=[]), Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), Assign(lhs=Id(name='tmp'), rhs=CallStmt(method=Id(name='read'), param=[]))]))]), exp=IntLiteral(value=3))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,390)) 
    def test_AST_391(self):
        input = """ Function: barz
        Body:
                    For (floRida = 1.2e-1, 1.2e-1, 3520) Do
                        arr = getArrayOfEvenNum();
                        Break;
                    EndFor.
                
                Do
                    x = a+1 < (2 < 3);
                    getArray();
                    writeln("Ten day du cua ban la : ",name," ",surname);
                While foo(3) + bar(a[3]) =/= a[3][3][b[2][2][7]] EndDo.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='barz'), param=[], body=([], [For(idx1=Id(name='floRida'), expr1=FloatLiteral(value=0.12), expr2=FloatLiteral(value=0.12), expr3=IntLiteral(value=3520), loop=([], [Assign(lhs=Id(name='arr'), rhs=CallStmt(method=Id(name='getArrayOfEvenNum'), param=[])), Break()])), Dowhile(sl=([], [Assign(lhs=Id(name='x'), rhs=BinaryOp(op='<', left=BinaryOp(op='+', left=Id(name='a'), right=IntLiteral(value=1)), right=BinaryOp(op='<', left=IntLiteral(value=2), right=IntLiteral(value=3)))), CallStmt(method=Id(name='getArray'), param=[]), CallStmt(method=Id(name='writeln'), param=[StringLiteral(value='Ten day du cua ban la : '), Id(name='name'), StringLiteral(value=' '), Id(name='surname')])]), exp=BinaryOp(op='=/=', left=BinaryOp(op='+', left=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), right=CallStmt(method=Id(name='bar'), param=[ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3)])])), right=ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3), IntLiteral(value=3), ArrayCell(arr=Id(name='b'), idx=[IntLiteral(value=2), IntLiteral(value=2), IntLiteral(value=7)])])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,391)) 
    def test_AST_392(self):
        input = """ Function: jasonMraz
        Body:
                Do
                    For (i = 0, i < smaller, 1) Do
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
                    For (i = 0, i < smaller, 1) Do
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
                    diffLen = len(arrA) - len(arrB);
                While c <. 4.5 EndDo.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='jasonMraz'), param=[], body=([], [Dowhile(sl=([], [For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='smaller')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='smaller')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')])))]), exp=BinaryOp(op='<.', left=Id(name='c'), right=FloatLiteral(value=4.5)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,392)) 
    def test_AST_393(self):
        input = """ Function: func1
        Body:
                    For (thanhToan = func(1)[1] * 2, c <. 4.5, 10e-11) Do
                        While func(3) Do
                    getArray();
                    diffLen = len(arrA) - len(arrB);
                    tmp = read();
                EndWhile.
                        sum = sum + arrA[i] + arrB[i];
                    EndFor.
                
                    For (func1 = c <. 4.5, 3, func(3)) Do
                        Return;
                        x = a+1 < (2 < 3);
                    EndFor.
                
                    While (3-2) == 1+2*test(1) Do
                        getArray();
                        a[3 + foo(2)] = a[b[2][3]] + 4;
                    EndWhile.
                
                Do
                    Return 2;
                    a[2] =foo(3) + bar(a[3]) =/= a[3][3][b[2][2][7]];
                    Return 1;
                While x + 5 == True EndDo.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='func1'), param=[], body=([], [For(idx1=Id(name='thanhToan'), expr1=BinaryOp(op='*', left=ArrayCell(arr=CallStmt(method=Id(name='func'), param=[IntLiteral(value=1)]), idx=[IntLiteral(value=1)]), right=IntLiteral(value=2)), expr2=BinaryOp(op='<.', left=Id(name='c'), right=FloatLiteral(value=4.5)), expr3=FloatLiteral(value=1e-10), loop=([], [While(exp=CallStmt(method=Id(name='func'), param=[IntLiteral(value=3)]), sl=([], [CallStmt(method=Id(name='getArray'), param=[]), Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), Assign(lhs=Id(name='tmp'), rhs=CallStmt(method=Id(name='read'), param=[]))])), Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), For(idx1=Id(name='func1'), expr1=BinaryOp(op='<.', left=Id(name='c'), right=FloatLiteral(value=4.5)), expr2=IntLiteral(value=3), expr3=CallStmt(method=Id(name='func'), param=[IntLiteral(value=3)]), loop=([], [Return(expr=None), Assign(lhs=Id(name='x'), rhs=BinaryOp(op='<', left=BinaryOp(op='+', left=Id(name='a'), right=IntLiteral(value=1)), right=BinaryOp(op='<', left=IntLiteral(value=2), right=IntLiteral(value=3))))])), While(exp=BinaryOp(op='==', left=BinaryOp(op='-', left=IntLiteral(value=3), right=IntLiteral(value=2)), right=BinaryOp(op='+', left=IntLiteral(value=1), right=BinaryOp(op='*', left=IntLiteral(value=2), right=CallStmt(method=Id(name='test'), param=[IntLiteral(value=1)])))), sl=([], [CallStmt(method=Id(name='getArray'), param=[]), Assign(lhs=ArrayCell(arr=Id(name='a'), idx=[BinaryOp(op='+', left=IntLiteral(value=3), right=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=2)]))]), rhs=BinaryOp(op='+', left=ArrayCell(arr=Id(name='a'), idx=[ArrayCell(arr=Id(name='b'), idx=[IntLiteral(value=2), IntLiteral(value=3)])]), right=IntLiteral(value=4)))])), Dowhile(sl=([], [Return(expr=IntLiteral(value=2)), Assign(lhs=ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=2)]), rhs=BinaryOp(op='=/=', left=BinaryOp(op='+', left=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), right=CallStmt(method=Id(name='bar'), param=[ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3)])])), right=ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3), IntLiteral(value=3), ArrayCell(arr=Id(name='b'), idx=[IntLiteral(value=2), IntLiteral(value=2), IntLiteral(value=7)])]))), Return(expr=IntLiteral(value=1))]), exp=BinaryOp(op='==', left=BinaryOp(op='+', left=Id(name='x'), right=IntLiteral(value=5)), right=BooleanLiteral(value=True)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,393)) 
    def test_AST_394(self):
        input = """ Function: traiTimBenLe
        Body:
                    While foo(a[3][2]) + xyz Do
                        arr = getArrayOfEvenNum();
                        If diffLen > 0 Then 
                    isA = True; 
                    smaller = len(arrA);
                Else 
                    isA = False; 
                    smaller = len(arrB);
                EndIf.
                    EndWhile.
                
                Do
                    sum = sum + arrA[i] + arrB[i];
                    If diffLen > 0 Then 
                    isA = True; 
                    smaller = len(arrA);
                Else 
                    isA = False; 
                    smaller = len(arrB);
                EndIf.
                    If tmp % 2 != 0 Then Continue; EndIf.
                While x + 5 == True EndDo.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='traiTimBenLe'), param=[], body=([], [While(exp=BinaryOp(op='+', left=CallStmt(method=Id(name='foo'), param=[ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3), IntLiteral(value=2)])]), right=Id(name='xyz')), sl=([], [Assign(lhs=Id(name='arr'), rhs=CallStmt(method=Id(name='getArrayOfEvenNum'), param=[])), If(ifthenStmt=[(BinaryOp(op='>', left=Id(name='diffLen'), right=IntLiteral(value=0)), [], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]))])], elseStmt=([], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))]))])), Dowhile(sl=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')]))), If(ifthenStmt=[(BinaryOp(op='>', left=Id(name='diffLen'), right=IntLiteral(value=0)), [], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]))])], elseStmt=([], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))])), If(ifthenStmt=[(BinaryOp(op='!=', left=BinaryOp(op='%', left=Id(name='tmp'), right=IntLiteral(value=2)), right=IntLiteral(value=0)), [], [Continue()])], elseStmt=([], []))]), exp=BinaryOp(op='==', left=BinaryOp(op='+', left=Id(name='x'), right=IntLiteral(value=5)), right=BooleanLiteral(value=True)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,394)) 
    def test_AST_395(self):
        input = """ Function: brunoMraz
        Body:
                    For (nickyMjnaj = 1231 + -11 == False, foo(a[3][2]) + xyz, a[3+foo(2)]) Do
                        Return;
                        diffLen = len(arrA) - len(arrB);
                    EndFor.
                
                Do
                    While func(3) Do
                    getArray();
                    diffLen = len(arrA) - len(arrB);
                    tmp = read();
                EndWhile.
                    x = a+1 < (2 < 3);
                    arr = getArrayOfEvenNum();
                While 3 EndDo.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='brunoMraz'), param=[], body=([], [For(idx1=Id(name='nickyMjnaj'), expr1=BinaryOp(op='==', left=BinaryOp(op='+', left=IntLiteral(value=1231), right=UnaryOp(op='-', body=IntLiteral(value=11))), right=BooleanLiteral(value=True)), expr2=BinaryOp(op='+', left=CallStmt(method=Id(name='foo'), param=[ArrayCell(arr=Id(name='a'), idx=[IntLiteral(value=3), IntLiteral(value=2)])]), right=Id(name='xyz')), expr3=ArrayCell(arr=Id(name='a'), idx=[BinaryOp(op='+', left=IntLiteral(value=3), right=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=2)]))]), loop=([], [Return(expr=None), Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')])))])), Dowhile(sl=([], [While(exp=CallStmt(method=Id(name='func'), param=[IntLiteral(value=3)]), sl=([], [CallStmt(method=Id(name='getArray'), param=[]), Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), Assign(lhs=Id(name='tmp'), rhs=CallStmt(method=Id(name='read'), param=[]))])), Assign(lhs=Id(name='x'), rhs=BinaryOp(op='<', left=BinaryOp(op='+', left=Id(name='a'), right=IntLiteral(value=1)), right=BinaryOp(op='<', left=IntLiteral(value=2), right=IntLiteral(value=3)))), Assign(lhs=Id(name='arr'), rhs=CallStmt(method=Id(name='getArrayOfEvenNum'), param=[]))]), exp=IntLiteral(value=3))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,395)) 
    def test_AST_396(self):
        input = """ Function: giacMoNgayxua
        Body:
                    For (caRot = bar[1], 1231 + -11 == False, a[3+foo(2)]) Do
                        x = a+1 < (2 < 3);
                        Break;
                    EndFor.
                
                Do
                    Break;
                    While a <= 4 Do
                    diffLen = len(arrA) - len(arrB);
                    For (i = 0, i < smaller, 1) Do
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
                    sum = sum + arrA[i] + arrB[i];
                EndWhile.
                    hehe = (foo(3)[3*3-1][22] != xyA) <=. 3.234;
                While func(1)[1] * 2 EndDo.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='giacMoNgayxua'), param=[], body=([], [For(idx1=Id(name='caRot'), expr1=ArrayCell(arr=Id(name='bar'), idx=[IntLiteral(value=1)]), expr2=BinaryOp(op='==', left=BinaryOp(op='+', left=IntLiteral(value=1231), right=UnaryOp(op='-', body=IntLiteral(value=11))), right=BooleanLiteral(value=True)), expr3=ArrayCell(arr=Id(name='a'), idx=[BinaryOp(op='+', left=IntLiteral(value=3), right=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=2)]))]), loop=([], [Assign(lhs=Id(name='x'), rhs=BinaryOp(op='<', left=BinaryOp(op='+', left=Id(name='a'), right=IntLiteral(value=1)), right=BinaryOp(op='<', left=IntLiteral(value=2), right=IntLiteral(value=3)))), Break()])), Dowhile(sl=([], [Break(), While(exp=BinaryOp(op='<=', left=Id(name='a'), right=IntLiteral(value=4)), sl=([], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='smaller')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), Assign(lhs=Id(name='hehe'), rhs=BinaryOp(op='<=.', left=BinaryOp(op='!=', left=ArrayCell(arr=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=3)]), idx=[BinaryOp(op='-', left=BinaryOp(op='*', left=IntLiteral(value=3), right=IntLiteral(value=3)), right=IntLiteral(value=1)), IntLiteral(value=22)]), right=Id(name='xyA')), right=FloatLiteral(value=3.234)))]), exp=BinaryOp(op='*', left=ArrayCell(arr=CallStmt(method=Id(name='func'), param=[IntLiteral(value=1)]), idx=[IntLiteral(value=1)]), right=IntLiteral(value=2)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,396)) 
    def test_AST_397(self):
        input = """ Function: caRot
        Body:
                    For (piano = func(3), x + 5 == True, func(1)[1] * 2) Do
                        sum = sum + arrA[i] + arrB[i];
                        string = "test function with string";
                    EndFor.
                
                Do
                    While a <= 4 Do
                    diffLen = len(arrA) - len(arrB);
                    For (i = 0, i < smaller, 1) Do
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
                    sum = sum + arrA[i] + arrB[i];
                EndWhile.
                    string = "test function with string";
                    barrr(myArr[2][3][4]);
                While a <= 4 EndDo.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='caRot'), param=[], body=([], [For(idx1=Id(name='piano'), expr1=CallStmt(method=Id(name='func'), param=[IntLiteral(value=3)]), expr2=BinaryOp(op='==', left=BinaryOp(op='+', left=Id(name='x'), right=IntLiteral(value=5)), right=BooleanLiteral(value=True)), expr3=BinaryOp(op='*', left=ArrayCell(arr=CallStmt(method=Id(name='func'), param=[IntLiteral(value=1)]), idx=[IntLiteral(value=1)]), right=IntLiteral(value=2)), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')]))), Assign(lhs=Id(name='string'), rhs=StringLiteral(value='test function with string'))])), Dowhile(sl=([], [While(exp=BinaryOp(op='<=', left=Id(name='a'), right=IntLiteral(value=4)), sl=([], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='smaller')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), Assign(lhs=Id(name='string'), rhs=StringLiteral(value='test function with string')), CallStmt(method=Id(name='barrr'), param=[ArrayCell(arr=Id(name='myArr'), idx=[IntLiteral(value=2), IntLiteral(value=3), IntLiteral(value=4)])])]), exp=BinaryOp(op='<=', left=Id(name='a'), right=IntLiteral(value=4)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,397)) 
    def test_AST_398(self):
        input = """ Function: bangKieu1
        Body:
                    For (ids = a[3+foo(2)], bar[1], (3-2) == 1+2*test(1)) Do
                        Return 2;
                        barrr(myArr[2][3][4]);
                    EndFor.
                
                    For (thanhToan = c <. 4.5, func(1)[1] * 2, c <. 4.5) Do
                        isA = True;
                    smaller = len(arrA);
                        barrr(myArr[2][3][4]);
                    EndFor.
                
                Do
                    Return 1;
                    isA = True;
                    smaller = len(arrA);
                    writeln("Ten day du cua ban la : ",name," ",surname);
                While bar[1] EndDo.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='bangKieu1'), param=[], body=([], [For(idx1=Id(name='ids'), expr1=ArrayCell(arr=Id(name='a'), idx=[BinaryOp(op='+', left=IntLiteral(value=3), right=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=2)]))]), expr2=ArrayCell(arr=Id(name='bar'), idx=[IntLiteral(value=1)]), expr3=BinaryOp(op='==', left=BinaryOp(op='-', left=IntLiteral(value=3), right=IntLiteral(value=2)), right=BinaryOp(op='+', left=IntLiteral(value=1), right=BinaryOp(op='*', left=IntLiteral(value=2), right=CallStmt(method=Id(name='test'), param=[IntLiteral(value=1)])))), loop=([], [Return(expr=IntLiteral(value=2)), CallStmt(method=Id(name='barrr'), param=[ArrayCell(arr=Id(name='myArr'), idx=[IntLiteral(value=2), IntLiteral(value=3), IntLiteral(value=4)])])])), For(idx1=Id(name='thanhToan'), expr1=BinaryOp(op='<.', left=Id(name='c'), right=FloatLiteral(value=4.5)), expr2=BinaryOp(op='*', left=ArrayCell(arr=CallStmt(method=Id(name='func'), param=[IntLiteral(value=1)]), idx=[IntLiteral(value=1)]), right=IntLiteral(value=2)), expr3=BinaryOp(op='<.', left=Id(name='c'), right=FloatLiteral(value=4.5)), loop=([], [Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrA')])), CallStmt(method=Id(name='barrr'), param=[ArrayCell(arr=Id(name='myArr'), idx=[IntLiteral(value=2), IntLiteral(value=3), IntLiteral(value=4)])])])), Dowhile(sl=([], [Return(expr=IntLiteral(value=1)), Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrA')])), CallStmt(method=Id(name='writeln'), param=[StringLiteral(value='Ten day du cua ban la : '), Id(name='name'), StringLiteral(value=' '), Id(name='surname')])]), exp=ArrayCell(arr=Id(name='bar'), idx=[IntLiteral(value=1)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,398)) 
    def test_AST_399(self):
        input = """ Function: ids
        Body:
                    For (khiCodonEmnhoai = a <= 4, 0xFFAA, 1231 + -11 == False) Do
                        sum = sum + arrA[i] + arrB[i];
                        sum = sum + arrA[i] + arrB[i];
                    EndFor.
                
                Do
                    barrr(myArr[2][3][4]);
                    isA = True;
                    smaller = len(arrA);
                    diffLen = len(arrA) - len(arrB);
                While a[3+foo(2)] EndDo.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='ids'), param=[], body=([], [For(idx1=Id(name='khiCodonEmnhoai'), expr1=BinaryOp(op='<=', left=Id(name='a'), right=IntLiteral(value=4)), expr2=IntLiteral(value=65450), expr3=BinaryOp(op='==', left=BinaryOp(op='+', left=IntLiteral(value=1231), right=UnaryOp(op='-', body=IntLiteral(value=11))), right=BooleanLiteral(value=True)), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')]))), Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), Dowhile(sl=([], [CallStmt(method=Id(name='barrr'), param=[ArrayCell(arr=Id(name='myArr'), idx=[IntLiteral(value=2), IntLiteral(value=3), IntLiteral(value=4)])]), Assign(lhs=Id(name='isA'), rhs=BooleanLiteral(value=True)), Assign(lhs=Id(name='smaller'), rhs=CallStmt(method=Id(name='len'), param=[Id(name='arrA')])), Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')])))]), exp=ArrayCell(arr=Id(name='a'), idx=[BinaryOp(op='+', left=IntLiteral(value=3), right=CallStmt(method=Id(name='foo'), param=[IntLiteral(value=2)]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,399)) 
    def test_AST_400(self):
        input = """ Function: biBe
        Body:
                    For (nlgt = foo(thuanNgo), bar[1], c <. 4.5) Do
                        If tmp % 2 != 0 Then Continue; EndIf.
                        sum = sum + arrA[i] + arrB[i];
                    EndFor.
                
                    For (haAnhTuan123 = (3-2) == 1+2*test(1), func(1)[1] * 2, func(1)[1] * 2) Do
                        Return 2;
                        While func(3) Do
                    getArray();
                    diffLen = len(arrA) - len(arrB);
                    tmp = read();
                EndWhile.
                    EndFor.
                
                Do
                    diffLen = len(arrA) - len(arrB);
                    While a <= 4 Do
                    diffLen = len(arrA) - len(arrB);
                    For (i = 0, i < smaller, 1) Do
                    sum = sum + arrA[i] + arrB[i];
                EndFor.
                    sum = sum + arrA[i] + arrB[i];
                EndWhile.
                    Break;
                While 3520 EndDo.
            
        EndBody. """
        expect = Program([FuncDecl(name=Id(name='biBe'), param=[], body=([], [For(idx1=Id(name='nlgt'), expr1=CallStmt(method=Id(name='foo'), param=[Id(name='thuanNgo')]), expr2=ArrayCell(arr=Id(name='bar'), idx=[IntLiteral(value=1)]), expr3=BinaryOp(op='<.', left=Id(name='c'), right=FloatLiteral(value=4.5)), loop=([], [If(ifthenStmt=[(BinaryOp(op='!=', left=BinaryOp(op='%', left=Id(name='tmp'), right=IntLiteral(value=2)), right=IntLiteral(value=0)), [], [Continue()])], elseStmt=([], [])), Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), For(idx1=Id(name='haAnhTuan123'), expr1=BinaryOp(op='==', left=BinaryOp(op='-', left=IntLiteral(value=3), right=IntLiteral(value=2)), right=BinaryOp(op='+', left=IntLiteral(value=1), right=BinaryOp(op='*', left=IntLiteral(value=2), right=CallStmt(method=Id(name='test'), param=[IntLiteral(value=1)])))), expr2=BinaryOp(op='*', left=ArrayCell(arr=CallStmt(method=Id(name='func'), param=[IntLiteral(value=1)]), idx=[IntLiteral(value=1)]), right=IntLiteral(value=2)), expr3=BinaryOp(op='*', left=ArrayCell(arr=CallStmt(method=Id(name='func'), param=[IntLiteral(value=1)]), idx=[IntLiteral(value=1)]), right=IntLiteral(value=2)), loop=([], [Return(expr=IntLiteral(value=2)), While(exp=CallStmt(method=Id(name='func'), param=[IntLiteral(value=3)]), sl=([], [CallStmt(method=Id(name='getArray'), param=[]), Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), Assign(lhs=Id(name='tmp'), rhs=CallStmt(method=Id(name='read'), param=[]))]))])), Dowhile(sl=([], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), While(exp=BinaryOp(op='<=', left=Id(name='a'), right=IntLiteral(value=4)), sl=([], [Assign(lhs=Id(name='diffLen'), rhs=BinaryOp(op='-', left=CallStmt(method=Id(name='len'), param=[Id(name='arrA')]), right=CallStmt(method=Id(name='len'), param=[Id(name='arrB')]))), For(idx1=Id(name='i'), expr1=IntLiteral(value=0), expr2=BinaryOp(op='<', left=Id(name='i'), right=Id(name='smaller')), expr3=IntLiteral(value=1), loop=([], [Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), Assign(lhs=Id(name='sum'), rhs=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='sum'), right=ArrayCell(arr=Id(name='arrA'), idx=[Id(name='i')])), right=ArrayCell(arr=Id(name='arrB'), idx=[Id(name='i')])))])), Break()]), exp=IntLiteral(value=3520))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,400)) 
