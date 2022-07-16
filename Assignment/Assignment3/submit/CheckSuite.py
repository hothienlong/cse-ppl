from main.bkit.utils.AST import BinaryOp, Dowhile, IntLiteral
from main.bkit.checker.StaticError import Function, Identifier, NoEntryPoint, TypeCannotBeInferred, TypeMismatchInExpression, TypeMismatchInStatement, Undeclared
import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    def test_Redeclared1(self):
        input = """Var: x = 2; Var: x = 3;"""
        expect = str(Redeclared(Variable(), "x"))
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_Redeclared2(self):
        input = """Var: x; Var: y; Var: x = 1;"""
        expect = str(Redeclared(Variable(), "x"))
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_Redeclared3(self):
        input = """Var: arr[3][5]; Var: arr = 4;"""
        expect = str(Redeclared(Variable(), "arr"))
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_Redeclared4(self):
        input = """ Var: arr[2][3] = {{2,3,4},{4,5,6}};
                    Var: array[2] = {"string","string2"}; 
                    **Var: list[0] = {};**
                    Var: arr;"""
        expect = str(Redeclared(Variable(), "arr"))
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_Redeclared5(self):
        input = """Var: bun = True; Var: bun[2] = {2};"""
        expect = str(Redeclared(Variable(), "bun"))
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_Redeclared6(self):
        input = """Var: c, d = 6, e, f, c;"""
        expect = str(Redeclared(Variable(), "c"))
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_Redeclared7(self):
        input = """Var: f = "strong"; Var: f = 3;"""
        expect = str(Redeclared(Variable(), "f"))
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_Redeclared8(self):
        input = """ Var: x;
                    Function: x
                    Parameter: main
                    Body: 
                        Var: y;
                    EndBody."""
        expect = str(Redeclared(Function(), "x"))
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_Redeclared9(self):
        input = """ Var: x = 2;
                    Function: main
                    Body: 
                        Var: x = 3;
                        Var: y = 4;
                        Var: y;
                    EndBody."""
        expect = str(Redeclared(Variable(), "y"))
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_Redeclared10(self):
        input = """ Var: x = 2;
                    Function: main
                    Parameter: x,y,a,a
                    Body: 
                        Var: x = 3;
                        Var: zzz = 4;
                        Var: zzz;
                    EndBody."""
        expect = str(Redeclared(Parameter(), "a"))
        self.assertTrue(TestChecker.test(input,expect,410))


    def test_Redeclared11(self):
        input = """ Var: x;
                    Function: main
                    Body:
                        While True Do 
                            Var: z = 2;
                            Var: z = 3;
                        EndWhile.
                    EndBody."""
        expect = str(Redeclared(Variable(), "z"))
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_Redeclared12(self):
        input = """ Var: x;
                    Function: main
                    Body:
                        While True Do 
                            Var: z = 2;
                            While True Do
                                Var: z = 3;
                                Var: ppl = 9;
                                Var: ppl[9];
                            EndWhile.
                        EndWhile.
                    EndBody."""
        expect = str(Redeclared(Variable(), "ppl"))
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_Redeclared13(self):
        input = """ Var: x;
                    Function: main
                    Parameter: p
                    Body:
                    EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_Redeclared14(self):
        input = """ Var: x;
                    Function: main
                    Body:
                        Var: arr;
                        For(arr = 1, 1<2, 2) Do
                            Var: x1;
                            Var: x2 = 3;
                        EndFor.

                        For(arr = 1, 1<2, 2) Do
                            Var: nut = "Nut for december forever";
                            Var: x2 = 4;
                            Var: nut;
                        EndFor.

                    EndBody."""
        expect = str(Redeclared(Variable(), "nut"))
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_Redeclared15(self):
        input = """ Var: x;
                    Function: main
                    Parameter: arr;
                    Body:
                        Var: fact = "what the fact?";
                        For(arr = 1, 1<2, 2) Do
                            Var: x1;
                            Var: x2 = 3;
                        EndFor.
                    EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_Redeclared16(self):
        input = """ **Var: x;**
                    Function: fact
                    Body:
                        Var: foo = "what the foo?";
                        Var: foo;
                        For(arr = 1, 1<2, 2) Do
                            Var: x1;
                            Var: x2 = 3;
                        EndFor.
                    EndBody.

                    Function: fact
                    Body:
                        Var: foo = "what the foo?";
                        For(arr = 1, 1<2, 2) Do
                            Var: x1;
                            Var: x2 = 3;
                        EndFor.
                    EndBody."""
        expect = str(Redeclared(Function(), "fact"))
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_Redeclared17(self):
        input = """ Function: main
                    Parameter: old
                    Body:
                        Var: old;
                        While (i < 5) Do
                            Var: a = 2;
                            a = 3;
                        EndWhile.
                    EndBody."""
        expect = str(Redeclared(Variable(), "old"))
        self.assertTrue(TestChecker.test(input,expect,417))


    def test_Redeclared18(self):
        input = """
                Function: main
                Body:
                    foo();
                EndBody.
                Function: foo
                Body:
                    Var: x = 5;
                    Var: y = 6;
                    Var: z = True;
                    If z Then 
                        Var: z = 0;
                        Var: t = 7;
                        z = 5;
                        t = 6;
                    Else
                        Var: z = 1;
                        Var: t = 9;
                        Var: t = 6;
                        z = 6;
                        t = 7;
                    EndIf.
                EndBody."""
        expect = str(Redeclared(Variable(), "t"))
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_Redeclared19(self):
        input = """ Var: x = 2;
                    Function: main
                    Parameter: arr[2], arr
                    Body: 
                        Var: arr = 3;
                        If i < 5 Then 
                            Var: x = 2;
                        EndIf.
                    EndBody."""
        expect = str(Redeclared(Parameter(), "arr"))
        self.assertTrue(TestChecker.test(input,expect,419))
    

    def test_420(self):
            input = """ Function: main
                        Body:
                            foo()[0] = 1;
                            **Var: arr;
                            arr[1] = 1;**
                        EndBody.
                        
                        Function: foo
                        Body:
                            Return 0;
                        EndBody."""
            expect = str(TypeCannotBeInferred(ArrayCell(CallExpr(Id("foo"),[]),[IntLiteral(0)])))
            self.assertTrue(TestChecker.test(input,expect,420))

    def test_Undeclared1(self):
        input = """ Var: x = 2;
                    Function: main
                    Parameter: y
                    Body: 
                        y = 3;
                        x = 4;
                        z = 5;
                    EndBody."""
        expect = str(Undeclared(Identifier(), "z"))
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_Undeclared2(self):
        input = """ Var: x = 2;
                    Function: main
                    Parameter: y
                    Body: 
                        Var: x = 3;
                        Var: i;
                        If i < 5 Then 
                            Var: arr = 2;
                        EndIf.
                        x = 4;
                        arr = 3.5;
                    EndBody."""
        expect = str(Undeclared(Identifier(), "arr"))
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_Undeclared3(self):
        input = """ Var: x = 2;
                    Function: main
                    Parameter: y
                    Body: 
                        Var: x = 3;
                        y = 4;
                        x = 2 + main(3)*ppl;
                    EndBody."""
        expect = str(Undeclared(Identifier(), "ppl"))
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_Undeclared4(self):
        input = """ Var: x = 2;
                    Function: main
                    Parameter: y
                    Body: 
                        Var: x = 3;
                        x = -y + z;
                    EndBody."""
        expect = str(Undeclared(Identifier(), "z"))
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_Undeclared5(self):
        input = """ Var: x = 2;
                    Function: main
                    Parameter: c 
                    Body: 
                        Var: y[2];
                        Var: x = 3;
                        y[2] = x + main(f);
                    EndBody."""
        expect = str(Undeclared(Identifier(), "f"))
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_Undeclared6(self):
        input = """ Var: x = 2;
                    Var: y = 3;
                    Function: main
                    Parameter: y
                    Body: 
                        x = 1;
                        d = 2;
                        b = 3;
                    EndBody."""
        expect = str(Undeclared(Identifier(), "d"))
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_Undeclared7(self):
        input = """ Var: x = 2;
                    Function: foo
                    Parameter: cse 
                    Body: 
                        Var: y[2];
                        Return y;
                    EndBody.
                    
                    Function: main
                    Parameter: c 
                    Body: 
                        Var: y[2];
                        Var: x = 3;
                        foo(4)[2] = x + main(2+4);
                        fee(4)[2] = x + main(2+4);
                    EndBody."""
        expect = str(Undeclared(Function(), "fee"))
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_Undeclared8(self):
        input = """ Var: x = 2;
                    Function: main
                    Body: 
                        foo();
                    EndBody.
                    
                    Function: foo
                    Body: 
                    EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_Undeclared9(self):
        input = """ Function: main
                    Parameter: x, y, z[4][4]
                    Body:
                        Var: s;
                        x();
                    EndBody."""
        expect = str(Undeclared(Function(),"x"))
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_Undeclared10(self):
        input = """Function: main
                    Parameter: x, y, n[4][4]
                    Body:
                        Var: s, t, v;
                        s = read();
                        t = 2;
                        t = int_of_float(5.1);
                        v = 5.0;
                        v = float_to_int(t);
                    EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_TypeMismatch1(self):
        input = """ Var: x = 2;
                    Function: main
                    Body: 
                        x = 4.2;
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"),FloatLiteral(4.2))))
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_TypeMismatch2(self):
        input = """ Var: x = 2;
                    Function: main
                    Body: 
                        Var: x = 3.3;
                        Var: i;
                        x = 4.5;         
                         If i < 5 Then 
                             Var: arr = 2;
                             arr = True;
                         EndIf.        
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("arr"),BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_TypeMismatch3(self):
        input = """ Var: x = 2;
                    Function: main
                    Body: 
                        Var: d = 3;
                        Var: i;
                        If i > 3 Then 
                            Var: x = 2;
                        EndIf.
                        d = x && d;
                    EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("&&",Id("x"),Id("d"))))
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_TypeMismatch4(self):
        input = """ Var: x = 2.0;
                    Function: main
                    Body: 
                        Var: d = 3;
                        Var: i;
                        If i < 5 Then 
                            Var: x = 2;
                        EndIf.
                        d = x + d;
                    EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("x"),Id("d"))))
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_TypeMismatch5(self):
        input = """ Var: x = 2;
                    Function: main
                    Body: 
                        Var: x = 2;
                        Var: y = 2.3
                        x = x *. y;
                    EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("*.",Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_TypeMismatch6(self):
        input = """ Var: x = 2;
                    Function: main
                    Parameter: y
                    Body: 
                        Var: x = 3;
                        Var: z = 5;
                        Var: str = "string";
                        str = x + z;
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("str"),BinaryOp("+",Id("x"),Id("z")))))
        self.assertTrue(TestChecker.test(input,expect,436))

    # làm tiếp tới 10
    def test_TypeMismatch7(self):
        input = """ Var: x;
                    Function: main
                    Parameter: x
                    Body: 
                        foo(2);
                        foo(2.2);
                    EndBody.
                                        
                    Function: foo
                    Parameter: y
                    Body: 
                        Var: jz;
                        Var: jz;
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[FloatLiteral(2.2)])))
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_TypeMismatch8(self):
        input = """ Function: main
                    Parameter: y
                    Body: 
                        **Var: a;
                        a = y;**

                        **Var: b;
                        b = main(10);**
                        **Var: b;
                        main(2);
                        b = main(2);**
                        **Var: b;
                        y = main(3) + 3;
                        b = main(3);**

                        **Var: c;
                        c = {1,2};**
                        Var: c;
                        Var: arr[2][3];
                        c = arr;

                        **Var: d;
                        d = 2 + main(2);**
                        
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("c"),Id("arr"))))
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_TypeMismatch9(self):
        input = """ Function: main
                    Parameter: y
                    Body: 
                        **Var: a[2][3];
                        a = y;**
                        **Var: a[2][3];
                        a = main(2);**

                        **Var: b[2][3];
                        main(2);
                        b = main(2);**

                        **Var: c[2] = {2,4};
                        Var: d[2];
                        c = d;**
                        **Var: c[2] = {2,4};
                        Var: d[2] = {2.3,4.2};
                        c = d;**
                        **Var: c[2], d[2];
                        c = d;**
                        
                        Var: c[2], d[2] = {True,True};
                        d = main(10);
                        c = main(11);

                        **Var: d[2];
                        Var: e = 2;
                        d = e;**
                        
                    EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_TypeMismatch10(self):
        input = """ Function: main
                    Parameter: y
                    Body: 
                        **Var: a = 2, b = 2.0;
                        a = main(2);
                        b = main(2);**  

                        Var: b = 2;
                        main(2);
                        b = main(2);

                        **Var: c = 2;
                        c = {{1,2},{2,3}};**

                        **Var: d = 2, e = 3.3;
                        e = main(2);
                        d = main(2);**
                        
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("b"),CallExpr(Id("main"),[IntLiteral(2)]))))
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_441(self):
        input = """ Function: main
                    Parameter: y
                    Body: 
                        Var: a;
                        a = y;
                    EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("a"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,441))
    
    def test_442(self):
        input = """ Function: main
                    Parameter: y
                    Body: 
                        Var: b;
                        b = main(10);            
                    EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("b"),CallExpr(Id("main"),[IntLiteral(10)]))))
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_443(self):
        input = """ Function: main
                    Parameter: y
                    Body: 
                        Var: b;
                        main(2);
                        b = main(2);                   
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("b"),CallExpr(Id("main"),[IntLiteral(2)]))))
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_444(self):
        input = """ Function: main
                    Parameter: y
                    Body: 
                        Var: b;
                        y = main(3) + 3;
                        b = main(3);               
                    EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_445(self):
        input = """ Function: main
                    Parameter: y
                    Body: 
                        Var: c;
                        c = {1,2};
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("c"),ArrayLiteral([IntLiteral(1),IntLiteral(2)]))))
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_446(self):
        input = """ Function: main
                    Parameter: y
                    Body: 
                        Var: c;
                        Var: arr[2][3];
                        c = arr;
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("c"),Id("arr"))))
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_447(self):
        input = """ Function: main
                    Parameter: y
                    Body: 
                        Var: d;
                        d = 2 + main(2);
                    EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_448(self):
        input = """ Function: main
                    Parameter: y
                    Body: 
                        Var: a[2][3];
                        a = y;
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("a"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_449(self):
        input = """ Function: main
                    Parameter: y
                    Body: 
                        Var: a[2][3];
                        a = main(2);
                    EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_450(self):
        input = """ Function: main
                    Parameter: y
                    Body: 
                        Var: b[2][3];
                        main(2);
                        b = main(2);
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("b"),CallExpr(Id("main"),[IntLiteral(2)]))))
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_InferType1(self):
        input = """ Function: main
                    Body: 
                        Var: x;
                        Var: t;
                        Var: i;
                        x = 3;
                        If i < 5 Then 
                            Var: x;
                            x = 3.0;
                            t = x;
                        EndIf.
                        x = t;
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"),Id("t"))))
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_InferType2(self):
        input = """ Function: main
                    Body: 
                        Var: x;
                        Var: t;
                        x = 3;
                        t = x;
                        t = True;
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("t"),BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_InferType3(self):
        input = """ Function: main
                    Body: 
                        Var: x;
                        Var: t;
                        x = t;
                    EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("x"),Id("t"))))
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_InferType4(self):
        input = """ Function: main
                    Body: 
                        Var: x[4];
                        Var: t = 3;
                        x = t;
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"),Id("t"))))
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_InferType5(self):
        input = """ Function: main
                    Body: 
                        Var: x[4];
                        Var: t[4] = {2,3,4,5};
                        x = t;
                    EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_InferType6(self):
        input = """ Function: main
                    Body: 
                        Var: x;
                        Var: t = 3;
                        x = t + x;
                    EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_InferType7(self):
        input = """ Function: main
                    Body: 
                        Var: x;
                        Var: t;
                        x = t + x;
                        x = x +. t;
                    EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("+.",Id("x"),Id("t"))))
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_InferType8(self):
        input = """ Function: main
                    Parameter: x
                    Body: 
                        Var: t = 3;
                        t = x && 2;
                    EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("&&",Id("x"),IntLiteral(2))))
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_InferType9(self):
        input = """ Function: main
                    Parameter: x
                    Body: 
                        Var: t = 3;
                        Var: z;
                        z = x && z;
                        t = -x;
                    EndBody."""
        expect = str(TypeMismatchInExpression(UnaryOp("-",Id("x"))))
        self.assertTrue(TestChecker.test(input,expect,459))


    def test_InferType10(self):
        input = """ """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_InferType11(self):
        input = """ Var: x;
                    Function: foo
                    Parameter: x
                    Body: 
                        x = 2.0;
                    EndBody.
                                        
                    Function: main
                    Body: 
                        x = 3;
                        foo(x);
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[Id("x")])))
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_InferType12(self):
        input = """ Var: x;
                    Function: main
                    Parameter: y,z
                    Body: 
                        main(3,x);
                    EndBody."""
        expect = str(TypeCannotBeInferred(CallStmt(Id("main"),[IntLiteral(3),Id("x")])))
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_InferType13(self):
        input = """ Function: main
                    Parameter: x
                    Body:
                        Var: t = 2.0; 
                        main(3);
                        x = t;
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"),Id("t"))))
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_InferType14(self):
        input = """ Function: main
                    Parameter: x
                    Body: 
                        Var: t = 3;
                        main(1,3,4);
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[IntLiteral(1),IntLiteral(3),IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_InferType15(self):
        input = """ Function: main
                    Parameter: x
                    Body: 
                        Var: t = 3;
                        x = 4;
                        main(3.4);
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[FloatLiteral(3.4)])))
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_InferType16(self):
        input = """ Function: main
                    Parameter: x,y
                    Body: 
                        Var: t = 3;
                        Var: z = 2;
                        main(t,z);
                        main(2.3,3.4);
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[FloatLiteral(2.3),FloatLiteral(3.4)])))
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_InferType17(self):
        input = """ Function: main
                    Parameter: x,y
                    Body: 
                        Var: t = 3;
                        Var: z = 2;
                        main(t,z);
                        main(x,y);
                    EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_InferType18(self):
        input = """ Function: main
                    Parameter: x,y
                    Body: 
                        Var: t;
                        Var: z;
                        main(t+t,z+.z);
                        main(2.2,1);
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[FloatLiteral(2.2),IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_InferType19(self):
        input = """Function: main
                    Parameter: m
                    Body:
                        m = m + 1;
                        main("str");
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[StringLiteral("str")])))
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_InferType20(self):
        input = """Function: main
                    Body:
                        Var: m;
                        float_of_int(string_of_int(m));
                    EndBody."""
        expect = str(Undeclared(Function(),"float_of_int"))
        self.assertTrue(TestChecker.test(input,expect,470))


    def test_InferType21(self):
        input = """ Function: main
                    Body:
                        Var: x;
                        Var: i;
                        x = 3;
                         If i < 5 Then 
                             Var: y;
                             Var: x;
                             Var: y;
                         EndIf.
                    EndBody."""
        expect = str(Redeclared(Variable(),"y"))
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_InferType22(self):
        input = """ Function: main
                    Body:
                        Var: x;
                        x();
                    EndBody."""
        expect = str(Undeclared(Function(),"x"))
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_InferType23(self):
        input = """ Var: x;
                    Function: main
                    Parameter: y
                    Body:
                        main(3);
                        main(x);
                        x = 0.0;
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"),FloatLiteral(0.0))))
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_InferType24(self):
        input = """ Var: x;
                    Function: main
                    Parameter: y,z
                    Body:
                        If True Then
                            z = 0.0;
                        EndIf.
                        main(3,x);
                        main(x,0.0);
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[Id("x"),FloatLiteral(0.0)])))
        self.assertTrue(TestChecker.test(input,expect,474))


    def test_InferType25(self):
        input = """ Var: x;
                    Function: main
                    Body: 
                        x();
                    EndBody."""
        expect = str(Undeclared(Function(),"x"))
        self.assertTrue(TestChecker.test(input,expect,475))


    def test_InferType26(self):
        input = """ Var: x;
                    Function: main
                    Body: 
                        x = 2;
                        x();
                    EndBody."""
        expect = str(Undeclared(Function(),"x"))
        self.assertTrue(TestChecker.test(input,expect,476))


    def test_InferType27(self):
        input = """ Var: x;
                    Function: main
                    Parameter: main
                    Body: 
                        main(main + 2);
                    EndBody."""
        expect = str(Undeclared(Function(),"main"))
        self.assertTrue(TestChecker.test(input,expect,477))
    

    def test_InferType28(self):
        input = """ Function: foo
                    Parameter: x
                    Body: 
                    EndBody.

                    Function: main
                    Body: 
                        Var: t;
                        Var: z = 10;
                        foo(2.2);
                        t = foo(3.3);
                        z = foo(1.0);
                        foo(2);
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("t"),CallExpr(Id("foo"),[FloatLiteral(3.3)]))))
        self.assertTrue(TestChecker.test(input,expect,478))


    def test_InferType29(self):
        input = """ Function: foo
                    Parameter: x
                    Body: 
                        
                    EndBody.

                    Function: main
                    Body: 
                        Var: t;
                        Var: f;
                        t = 2 + foo(2);
                        f = 3.1 +. foo(3);
                    EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("+.",FloatLiteral(3.1),CallExpr(Id("foo"),[IntLiteral(3)]))))
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_80(self):
            input = """
                    Function: main
                    Parameter: x, y
                    Body:
                        x = x +. (y + x);
                    EndBody."""
            expect = str(TypeMismatchInExpression(BinaryOp("+",Id("y"),Id("x"))))
            self.assertTrue(TestChecker.test(input,expect,480))

    def test81(self):
        input = """ Function: foo
                    Parameter: x
                    Body: 
                        
                    EndBody.

                    Function: main
                    Body: 
                        Var: t = 2;
                        Var: f;
                        **t = foo(2);**
                        t = 2 + foo(2);
                        f = 3.1 +. foo(3,4);
                    EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[IntLiteral(3),IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_82(self):
        input = """ Function: foo
                    Parameter: x
                    Body: 
                    EndBody.

                    Function: main
                    Body: 
                        Var: t = 2;
                        t = foo(2);
                    EndBody.
                    
                    Function: fee
                    Body: 
                        Var: n;
                        n = foo(3);
                    EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_83(self):
        input = """ Function: foo
                    Parameter: x
                    Body: 
                    EndBody.

                    Function: main
                    Body: 
                        Var: t;
                        t = foo(2);
                    EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("t"),CallExpr(Id("foo"),[IntLiteral(2)]))))
        self.assertTrue(TestChecker.test(input,expect,483))


    def test_84(self):
        input = """ Function : printf
                    Parameter : x
                    Body:
                    EndBody.

                    Function: m
                    Body:
                        Var : value = 12345;
                    EndBody.

                    Function: main
                    Parameter : x, y
                    Body: 
                        printf(m); 
                    EndBody."""
        expect = str(Undeclared(Identifier(),"m"))
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_85(self):
            input = """ Function: main 
                        Body: 
                            Var: a = 1, x; 
                            a = foo(x); 
                        EndBody. 

                        Function: foo 
                        Parameter: z
                        Body: 
                        EndBody."""
            expect = str(TypeCannotBeInferred(Assign(Id("a"),CallExpr(Id("foo"),[Id("x")]))))
            self.assertTrue(TestChecker.test(input,expect,485))

    def test_86(self):
        input = """
        Function: main
        Parameter: x
        Body:
            main(main(5));
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[CallExpr(Id("main"),[IntLiteral(5)])])))
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_87(self):
            input = """ Var: x;
                        Function: main
                        Body:
                            Var: a;
                            If x Then a=2;
                            Else 
                            EndIf.
                            x = a;
                        EndBody. """
            expect = str(TypeMismatchInStatement(Assign(Id("x"),Id("a"))))
            self.assertTrue(TestChecker.test(input,expect,487))

    def test_88(self):
            input = """ Var: x;
                        Function: main
                        Body:
                            Var: a;
                            If x Then a=2;
                            Else 
                            EndIf.
                            
                            If 1 Then x = False;
                            EndIf.
                        EndBody. """
            exp1 = IntLiteral(1)
            lstVardec1 = []
            lstStmt1 = [Assign(Id("x"),BooleanLiteral(False))]
            tup1 = (exp1,lstVardec1,lstStmt1)
            ifthenStmt = [tup1]
            # lstVardecElse = []
            # lstStmtElse = []
            tupElse = ([],[])
            elseStmt = (tupElse)
            expect = str(TypeMismatchInStatement(If(ifthenStmt,elseStmt)))
            self.assertTrue(TestChecker.test(input,expect,488))
            # If(IntLiteral(1),[],[Assign(Id(x),BooleanLiteral(false))])Else([],[])

    def test_89(self):
            exp1 = IntLiteral(1)
            lstVardec1 = []
            lstStmt1 = [CallStmt(Id("print"),[])]
            tup1 = (exp1,lstVardec1,lstStmt1)
            ifthenStmt = [tup1]
            # lstVardecElse = []
            # lstStmtElse = []
            tupElse = ([],[])
            elseStmt = (tupElse)
            input = """Function: main
                    Parameter: p
                    Body:
                        If 1 Then 
                            print();
                        EndIf.
                    EndBody."""

            expect = str(TypeMismatchInStatement(If(ifthenStmt,elseStmt)))
            self.assertTrue(TestChecker.test(input,expect,489))

    def test_90(self): #tham so la ham
            input = """ Function: main
                        Parameter: x, y
                        Body:
                            Var: z;
                            z = main(1, main(x, True));
                        EndBody."""
            expect = str(TypeCannotBeInferred(Assign(Id("z"),CallExpr(Id("main"),[IntLiteral(1),CallExpr(Id("main"),[Id("x"),BooleanLiteral(True)])]))))
            self.assertTrue(TestChecker.test(input,expect,490))


    def test_91(self):
            input = """ Function: main
                        Parameter: p
                        Body:
                            Var: x;
                            If p Then 
                                x = True;
                            ElseIf True Then
                                p = 2;
                            EndIf.
                        EndBody."""
            expect = str(TypeMismatchInStatement(Assign(Id("p"),IntLiteral(2))))
            self.assertTrue(TestChecker.test(input,expect,491))

    def test_92(self):
            input = """ Function: main
                        Parameter: p
                        Body:
                            Var: x;
                            If main(2) Then 
                                x = True;
                            ElseIf True Then
                                p = main(2);
                            EndIf.

                            **Var: arr[2][3];
                            If arr Then 
                                x = True;
                            EndIf.**
                        EndBody."""
            expect = str(TypeMismatchInStatement(Assign(Id("p"),CallExpr(Id("main"),[IntLiteral(2)]))))
            self.assertTrue(TestChecker.test(input,expect,492))

    def test_93(self):
            input = """ Function: main
                        Parameter: p
                        Body:
                            Var: x[2];
                            x[p] = 4;
                            x[p][p] = True;
                        EndBody."""
            expect = str(TypeMismatchInExpression(ArrayCell(Id("x"),[Id("p"),Id("p")])))
            self.assertTrue(TestChecker.test(input,expect,493))

    def test_94(self):
            input = """ Function: main
                        Body:
                            Var: arr;
                            Var: exp2;
                            Var: exp3;
                            For(arr = main(), exp2, exp3) Do
                                exp2 = exp3 + main();
                            EndFor.
                        EndBody."""
            expect = str(TypeMismatchInStatement(Assign(Id("exp2"),BinaryOp("+",Id("exp3"),CallExpr(Id("main"),[])))))
            self.assertTrue(TestChecker.test(input,expect,494))

    def test_95(self):
            input = """ Function: main
                        Body:
                            Do 
                                printf("Hello world");
                                While printf("Hello world")
                            EndDo.
                        EndBody.
                        
                        Function: printf
                        Parameter: string
                        Body:
                        EndBody."""
            exp = CallExpr(Id("printf"),[StringLiteral("Hello world")])
            lstVarDecl = []
            lstStmt = [CallStmt(Id("printf"),[StringLiteral("Hello world")])]
            tup = (lstVarDecl,lstStmt)
            expect = str(TypeMismatchInStatement(Dowhile(tup,exp)))
            self.assertTrue(TestChecker.test(input,expect,495))
            # Dowhile([],[CallStmt(Id(print),[StringLiteral(Hello world)])],CallExpr(Id(print),[StringLiteral(Hello world)]))

    def test_96(self):
            input = """ Function: main
                        Parameter: n
                        Body:
                            If n == 0 Then
                                Return 1;
                            Else
                                Return main(n - 1);
                            EndIf.

                            main(n);

                        EndBody."""
            expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[Id("n")])))
            self.assertTrue(TestChecker.test(input,expect,496))

    def test_97(self):
            input = """ Function: main
                        Body:
                            Var: x;

                            main();
                            Return foo();
                            Return x;
                        EndBody.
                        
                        Function: foo
                        Body:
                        EndBody."""
            expect = str(TypeMismatchInStatement(Return(Id("x"))))
            self.assertTrue(TestChecker.test(input,expect,497))

    def test_98(self):
            input = """ Function: main
                        Body:
                            Var: x = 2.3;
                            Var: arg;
                            float_to_int(int_of_float(x));
                            arg = printStrLn(arg);
                        EndBody.
                        
                        Function: foo
                        Body:
                        EndBody."""
            expect = str(TypeMismatchInStatement(CallStmt(Id("float_to_int"),[CallExpr(Id("int_of_float"),[Id("x")])])))
            self.assertTrue(TestChecker.test(input,expect,498))

    def test_99(self):
        input = """
        Var: array[1][2];
        Var: a = 0.5;
        Function: main  
        Body:
            array = {1,2};         
            foo();
            
        EndBody.

        Function: foo
        Body:
            Var: n;
        EndBody.
            
        """
        expect = str(TypeMismatchInStatement(Assign(Id("array"),ArrayLiteral([IntLiteral(1),IntLiteral(2)]))))
        self.assertTrue(TestChecker.test(input,expect,499))

    def test_100(self):
        input = """
        
        Var: a = 0.5;
        Function: main  
        Body:
            ss();
        EndBody.

        Function: ss
        Body:
            Var: n;
            If n == 0 Then
                Var: a;
            Else
                Var: a;
            EndIf.
        EndBody.
            
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,500))

