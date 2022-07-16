import unittest
from TestUtils import TestAST
from AST import *

from main.bkit.utils.AST import CallExpr, IntLiteral, VarDecl

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var:x;"""
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_1(self):
        input = """Var: x,y;"""
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
        # Program([VarDecl(Id(x)),VarDecl(Id(y))])

    def test_2(self):
        input = """Var: x, y=3;"""
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
        # Program([VarDecl(Id(x)),VarDecl(Id(y),IntLiteral(3))])

    def test_3(self):
        input = """Var: a;
                    Var: b,c=2;"""
        expect = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],IntLiteral(2))])
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
        # Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c),IntLiteral(2))])

    def test_4(self):
        input = """Var: arr[2] = 2;"""
        expect = Program([VarDecl(Id("arr"),[2],IntLiteral(2))])
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
        # Program([VarDecl(Id(arr),[2],IntLiteral(2))])

    def test_5(self):
        input = """Var: arr[2][3] = {1,2,4};"""
        expect = Program([VarDecl(Id("arr"),[2,3],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(4)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
        # Program([VarDecl(Id(arr),[2,3],ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(4)))])


    def test_6(self):
        input = """Var: arr[2] = {{1,2},{3}};"""
        expect = Program([VarDecl(Id("arr"),[2],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]),ArrayLiteral([IntLiteral(3)])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
        # Program([VarDecl(Id(arr),[2],ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(2)),ArrayLiteral(IntLiteral(3))))])
        #thiếu ; cũng ra kết quả??

    def test_7(self):
        input = """Var: arr[2] = {{1,True},{"String",{10.2}}};"""
        expect = Program([VarDecl(Id("arr"),[2],ArrayLiteral([ArrayLiteral([IntLiteral(1),BooleanLiteral(True)]),ArrayLiteral([StringLiteral("String"),ArrayLiteral([FloatLiteral(10.2)])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
        # Program([VarDecl(Id(arr),[2],ArrayLiteral(ArrayLiteral(IntLiteral(1),BooleanLiteral(true)),ArrayLiteral(StringLiteral(String),ArrayLiteral(FloatLiteral(10.2)))))])
    
    def test_8(self):
        input = """Var: arr[2];"""
        expect = Program([VarDecl(Id("arr"),[2],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
        # Program([VarDecl(Id(arr),[2])])

    def test_9(self):
        input = """Var: arr[2], b = 2;
                    Var: aba[2] = {True, False};"""
        expect = Program([VarDecl(Id("arr"),[2],None),
                        VarDecl(Id("b"),[],IntLiteral(2)),
                        VarDecl(Id("aba"),[2],ArrayLiteral([BooleanLiteral(True),BooleanLiteral(False)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
        # Program([VarDecl(Id(arr),[2]),VarDecl(Id(b),IntLiteral(2)),VarDecl(Id(aba),[2],ArrayLiteral(BooleanLiteral(true),BooleanLiteral(true)))])


    def test_10(self):
        input = """Var: arr = False;"""
        expect = Program([VarDecl(Id("arr"),[],BooleanLiteral(False))])
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_11(self):
        input = """Var: str = "This is assiment 2";"""
        expect = Program([VarDecl(Id("str"),[],StringLiteral("This is assiment 2"))])
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_11(self):
        input = """Var: aba[3];"""
        expect = Program([VarDecl(Id("aba"),[3],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_13(self):
        input = """Var: a[2] = {2,{3,3},True}, b = "String: '"who that'"" ;"""
        expect = Program([VarDecl(Id("a"),[2],ArrayLiteral([IntLiteral(2),ArrayLiteral([IntLiteral(3),IntLiteral(3)]),BooleanLiteral(True)])),
                        VarDecl(Id("b"),[],StringLiteral("String: '\"who that'\""))])
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
        # Program([VarDecl(Id(a),[2],ArrayLiteral(IntLiteral(2),ArrayLiteral(IntLiteral(3),IntLiteral(3)),BooleanLiteral(true))),VarDecl(Id(b),StringLiteral(String: '"who that'"))])
    
    def test_14(self):
        input = """Var: a[2] = {}, b = 2;"""
        expect = Program([VarDecl(Id("a"),[2],ArrayLiteral([])),
                        VarDecl(Id("b"),[],IntLiteral(2))])
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
        # Program([VarDecl(Id(a),[2],ArrayLiteral()),VarDecl(Id(b),IntLiteral(2))])

    def test_15(self):
        input = """Var: a;
                    Function: name
                    Parameter: cha
                    Body:
                        a = 2;
                    EndBody."""
        expect = Program([VarDecl(Id("a"),[],None),FuncDecl(Id("name"),                         #name func
                                                [VarDecl(Id("cha"),[],None)],                   #param
                                                ([],                                            #vardec
                                                [Assign(Id("a"),IntLiteral(2))]                 #stmt
                                                ))])
        self.assertTrue(TestAST.checkASTGen(input,expect,315))
    #     # Program([VarDecl(Id(a)),FuncDecl(Id(name)[VarDecl(Id(cha))],([][Assign(Id(a),IntLiteral(2))]))])

    def test_16(self):
        input = """Var: a;
                    Function: name
                    Body:
                        ba = 1;
                    EndBody."""
        expect = Program([VarDecl(Id("a"),[],None),FuncDecl(Id("name"),
                                                    [],
                                                    ([],
                                                    [Assign(Id("ba"),IntLiteral(1))])
                                                    )])
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_17(self):
        input = """ Function: name
                    Parameter: cha
                    Body:
                        
                    EndBody."""
        expect = Program([FuncDecl(Id("name"),
                                [VarDecl(Id("cha"),[],None)],
                                ([],
                                [])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_18(self):
        input = """Function: name
                    Parameter: cha
                    Body:
                        a = 2 + 3;
                    EndBody."""
        expect = Program([FuncDecl(Id("name"),
                                [VarDecl(Id("cha"),[],None)],
                                ([],
                                [Assign(Id("a"),BinaryOp("+",IntLiteral(2),IntLiteral(3)))])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,318))



    def test_19(self):
        input = """Var: a;
                    Function: name
                    Parameter: cha
                    Body:
                        a = 2;
                    EndBody.

                    Function: namelui
                    Parameter: bunthitnuong
                    Body:
                        goiham = funcall();
                    EndBody."""
        expect = Program([VarDecl(Id("a"),[],None),FuncDecl(Id("name"),
                                                            [VarDecl(Id("cha"),[],None)],
                                                            ([],
                                                            [Assign(Id("a"),IntLiteral(2))])
                                                            ),
                                                    FuncDecl(Id("namelui"),
                                                            [VarDecl(Id("bunthitnuong"),[],None)],
                                                            ([],
                                                            [Assign(Id("goiham"),CallExpr(Id("funcall"),[]))])
                                                            )])
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
        # Program([VarDecl(Id(a)),FuncDecl(Id(name)
        #                               [VarDecl(Id(cha))],
        #                               ([]
        #                               [Assign(Id(a),IntLiteral(2))])),
        #                         FuncDecl(Id(namelui)
        #                               [VarDecl(Id(bunthitnuong))],
        #                               ([]
        #                               [Assign(Id(goiham),CallExpr(funcall,[]))])
        #                               )])


    def test_20(self):
        input = """ Function: namelui
                    Parameter: bunthitnuong
                    Body:
                        goiham = funcall();
                    EndBody."""
        expect = Program([FuncDecl(Id("namelui"),
                                [VarDecl(Id("bunthitnuong"),[],None)],
                                ([],
                                [Assign(Id("goiham"),CallExpr(Id("funcall"),[]))])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,320))


    def test_21(self):
        input = """ Function: noname
                    Parameter: nolife
                    Body:
                        funcall();
                    EndBody."""
        expect = Program([FuncDecl(Id("noname"),
                                [VarDecl(Id("nolife"),[],None)],
                                ([],
                                [CallStmt(Id("funcall"),[])])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,321))
        # Program([FuncDecl(Id(noname)[VarDecl(Id(nolife))],([][CallStmt(funcall,[])]))])


    def test_22(self):
        input = """Var: a;
                    Function: name
                    Parameter: cha
                    Body:
                        a = 2;
                    EndBody.

                    Function: namelui
                    Parameter: bunthitnuong
                    Body:
                        a = 3;
                    EndBody."""
        expect = Program([VarDecl(Id("a"),[],None),
                        FuncDecl(Id("name"),
                                [VarDecl(Id("cha"),[],None)],
                                ([],
                                [Assign(Id("a"),IntLiteral(2))])
                                ),
                        FuncDecl(Id("namelui"),
                                [VarDecl(Id("bunthitnuong"),[],None)],
                                ([],
                                [Assign(Id("a"),IntLiteral(3))])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,322))


    def test_23(self):
        input = """ Function: name
                    Parameter: cha
                    Body:
                        funcall();
                    EndBody."""
        expect = Program([FuncDecl(Id("name"),
                                [VarDecl(Id("cha"),[],None)],
                                ([],
                                [CallStmt(Id("funcall"),[])])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,323))


    def test_24(self):
        input = """ Function: name
                    Parameter: cha
                    Body:
                        foo(1) = foo(2) + foo(3);
                        b = {True,"string"} && a;
                    EndBody."""
        expect = Program([FuncDecl(Id("name"),
                                [VarDecl(Id("cha"),[],None)],
                                ([],
                                #list stmt
                                [Assign(CallExpr(Id("foo"),[IntLiteral(1)]),BinaryOp("+",CallExpr(Id("foo"),[IntLiteral(2)]),CallExpr(Id("foo"),[IntLiteral(3)]))),
                                Assign(Id("b"),BinaryOp("&&",ArrayLiteral([BooleanLiteral(True),StringLiteral("string")]),Id("a")))])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,324))


    def test_25(self):
        input = """ """
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_26(self):
        input = """Function: babe
                    Body:
                        i= foo((3+4), True == False);
                    EndBody.
                \n"""
        expect = Program([FuncDecl(Id("babe"),
                                    [],
                                    ([],
                                    [Assign(Id("i"),CallExpr(Id("foo"),[BinaryOp("+",IntLiteral(3),IntLiteral(4)),BinaryOp("==",BooleanLiteral(True),BooleanLiteral(False))]))])
                                    )])
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_27(self):
        input = """Function: hello               
                    Body:
                        Var: ko = "09051508";
                        Var x = 2;
                        ppl = p + p + l;
                    EndBody."""
        expect = Program([FuncDecl(Id("hello"),
                                [],
                                ([VarDecl(Id("ko"),[],StringLiteral("09051508")),
                                VarDecl(Id("x"),[],IntLiteral(2))],
                                [Assign(Id("ppl"),BinaryOp("+",BinaryOp("+",Id("p"),Id("p")),Id("l")))])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_28(self):
        input = """Function: locfuho
                        Body:
                            foo = fuho(thochinh[2], {2,3}, a && b) ;
                        EndBody."""
        expect = Program([FuncDecl(Id("locfuho"),
                                [],
                                ([],
                                [Assign(Id("foo"),CallExpr(Id("fuho"),[ArrayCell(Id("thochinh"),[IntLiteral(2)]),ArrayLiteral([IntLiteral(2),IntLiteral(3)]),BinaryOp("&&",Id("a"),Id("b"))]))])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_29(self):
        input = """Function: borrow
                    Parameter: n
                    Body:
                        fuho(2) ;
                    EndBody."""
        expect = Program([FuncDecl(Id("borrow"),
                                [VarDecl(Id("n"),[],None)],
                                ([],
                                [CallStmt(Id("fuho"),[IntLiteral(2)])])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_30(self):
        input = """ Function: body
                        Body:
                            a[3] = arr[b[2][3]] + 4;
                        EndBody."""
        expect = Program([FuncDecl(Id("body"),
                                [],
                                ([],
                                [Assign(ArrayCell(Id("a"),[IntLiteral(3)]),BinaryOp("+",ArrayCell(Id("arr"),[ArrayCell(Id("b"),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4)))])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_31(self):
        input = """Var: a = 2 ; Var: b[3][3] = {};"""
        expect = Program([VarDecl(Id("a"),[],IntLiteral(2)),
                        VarDecl(Id("b"),[3,3],ArrayLiteral([]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_32(self):
        input = """Function: ham
                        Body:
                            array[3][3] = foo(2 + nested_exp(5) - 3, ((3)));
                        EndBody."""
        expect = Program([FuncDecl(Id("ham"),
                                [],
                                ([],
                                [Assign(ArrayCell(Id("array"),[IntLiteral(3),IntLiteral(3)]),
                                                            CallExpr(Id("foo"),[BinaryOp("-",BinaryOp("+",IntLiteral(2),CallExpr(Id("nested_exp"),[IntLiteral(5)])),IntLiteral(3)),IntLiteral(3)]))])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_33(self):
        input = """Function: borrow
                    Parameter: n
                    Body:
                        a[3 + foo(2)] = a[b[2][3]] + 4;
                    EndBody."""
        expect = Program([FuncDecl(Id("borrow"),
                                [VarDecl(Id("n"),[],None)],
                                ([],
                                [Assign(ArrayCell(Id("a"),[BinaryOp("+",IntLiteral(3),CallExpr(Id("foo"),[IntLiteral(2)]))]),
                                        BinaryOp("+",ArrayCell(Id("a"),[ArrayCell(Id("b"),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4)))])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_34(self):
        input = """Function: hamso
                        Body:
                            x = a[b[c[d]]];
                        EndBody."""
        expect = Program([FuncDecl(Id("hamso"),
                                [],
                                ([],
                                [Assign(Id("x"),
                                        ArrayCell(Id("a"),[ArrayCell(Id("b"),[ArrayCell(Id("c"),[Id("d")])])]))])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_35(self):
        input = """Function: func
                        Body:
                            a = True == (False + True);
                        EndBody."""
        expect = Program([FuncDecl(Id("func"),
                                [],
                                ([],
                                [Assign(Id("a"),
                                        BinaryOp("==",BooleanLiteral(True),BinaryOp("+",BooleanLiteral(False),BooleanLiteral(True))))])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_36(self):
        input = """**Var x: XD =))**"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_37(self):
        input = """Function: fact
                    Parameter: n
                    Body:
                        Var: r = 10., v;
                        v =  3.14 *. (4. \. 3.) *. r *. r *. r;
                    EndBody."""
        expect = Program([FuncDecl(Id("fact"),
                                [VarDecl(Id("n"),[],None)],
                                ([VarDecl(Id("r"),[],FloatLiteral(10.0)),VarDecl(Id("v"),[],None)],
                                [Assign(Id("v"),
                                        BinaryOp("*.",BinaryOp("*.",BinaryOp("*.",BinaryOp("*.",FloatLiteral(3.14),BinaryOp("\.",FloatLiteral(4.0),FloatLiteral(3.0))),Id("r")),Id("r")),Id("r")))])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_38(self):
        input = """Function: fact
                    Parameter:  arr[2], x
                    Body:
                        f = func(2.2,3) ;
                    EndBody."""
        expect = Program([FuncDecl(Id("fact"),
                                [VarDecl(Id("arr"),[2],None),VarDecl(Id("x"),[],None)],
                                ([],
                                [Assign(Id("f"),
                                        CallExpr(Id("func"),[FloatLiteral(2.2),IntLiteral(3)]))])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_39(self):
        input = """Var: x;
                    Function: fact
                    Parameter: p
                    Body:
                    EndBody."""
        expect = Program([VarDecl(Id("x"),[],None),
                        FuncDecl(Id("fact"),
                                [VarDecl(Id("p"),[],None)],
                                ([],
                                [])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_40(self):
        input = """Function: fact
                    Parameter: p
                    Body:
                        a[fail(0, -0.2) && index[2]] = b +. 1.0;
                    EndBody."""
        expect = Program([FuncDecl(Id("fact"),
                                [VarDecl(Id("p"),[],None)],
                                ([],
                                [Assign(ArrayCell(Id("a"),[BinaryOp("&&",CallExpr(Id("fail"),[IntLiteral(0),UnaryOp("-",FloatLiteral(0.2))]),ArrayCell(Id("index"),[IntLiteral(2)]))]),
                                        BinaryOp("+.",Id("b"),FloatLiteral(1.0)))])
                                        )])
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_41(self):
        input = """Function: fail
                    Body:
                        str = "str1" + "str2";
                        arr = {2,4} \. {2.2,3,5} * "ac" + i;
                    EndBody."""
        expect = Program([FuncDecl(Id("fail"),
                                [],
                                ([],

                                [Assign(Id("str"),
                                        BinaryOp("+",StringLiteral("str1"),StringLiteral("str2"))),
                                Assign(Id("arr"),
                                        BinaryOp("+",BinaryOp("*",BinaryOp("\.",ArrayLiteral([IntLiteral(2),IntLiteral(4)]),ArrayLiteral([FloatLiteral(2.2),IntLiteral(3),IntLiteral(5)])),StringLiteral("ac")),Id("i")))])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_42(self):
        input = """Function: idk
                    Body:
                        arr[0x233] = arr[0o23] + arr[foo(12)];
                    EndBody."""
        expect = Program([FuncDecl(Id("idk"),
                                [],
                                ([],
                                [Assign(ArrayCell(Id("arr"),[IntLiteral(563)]),
                                        BinaryOp("+",ArrayCell(Id("arr"),[IntLiteral(19)]),ArrayCell(Id("arr"),[CallExpr(Id("foo"),[IntLiteral(12)])])))])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_43(self):
        input = """Function: true
                    Body:
                        foo(2)[3] = 2;
                    EndBody."""
        expect = Program([FuncDecl(Id("true"),
                                [],
                                ([],
                                [Assign(ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),[IntLiteral(3)]),
                                        IntLiteral(2))])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_44(self):
        input = """Function: true
                    Body:
                        (True + b*c && !3)[99] = {2};
                        5[3] = 3[5];
                    EndBody."""
        expect = Program([FuncDecl(Id("true"),
                                [],
                                ([],

                                [Assign(ArrayCell(BinaryOp("&&",BinaryOp("+",BooleanLiteral(True),BinaryOp("*",Id("b"),Id("c"))),UnaryOp("!",IntLiteral(3))),[IntLiteral(99)]),
                                        ArrayLiteral([IntLiteral(2)])),
                                Assign(ArrayCell(IntLiteral(5),[IntLiteral(3)]),ArrayCell(IntLiteral(3),[IntLiteral(5)]))])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_45(self):
        input = """Function: true
                    Body:
                        arr[3][3] = 4[3] + True[3] && !2;
                    EndBody."""
        expect = Program([FuncDecl(Id("true"),
                                [],
                                ([],
                                [Assign(ArrayCell(Id("arr"),[IntLiteral(3),IntLiteral(3)]),
                                        BinaryOp("&&",BinaryOp("+",ArrayCell(IntLiteral(4),[IntLiteral(3)]),ArrayCell(BooleanLiteral(True),[IntLiteral(3)])),UnaryOp("!",IntLiteral(2))))])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_46(self):
        input = """Function: true
                    Body:
                        b = a--3; ** a - (-3) **
                    EndBody."""
        expect = Program([FuncDecl(Id("true"),
                                [],
                                ([],
                                [Assign(Id("b"),
                                        BinaryOp("-",Id("a"),UnaryOp("-",IntLiteral(3))))])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_47(self):
        input = """**
                    Function: true
                    Body:
                        b = a--3;
                        p[3] = a--;
                        p = a!3*b;
                    EndBody.   
                   ** """
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_48(self):
        input = """**
                    Function: true
                    Body:
                       **
                        Function: hello
                            Body:
                                print("Hom nay la mot ngay \\nang dep");
                            EndBody.
                        **
                    EndBody.             
                **"""
        expect = Program([FuncDecl(Id("hello"),
                                [],
                                ([],
                                [CallStmt(Id("print"),[StringLiteral("Hom nay la mot ngay \\nang dep")])])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_49(self):
        input = """Function: hello
                        Body:
                            print("Hello world");
                        EndBody."""
        expect = Program([FuncDecl(Id("hello"),
                                [],
                                ([],
                                [CallStmt(Id("print"),
                                [StringLiteral("Hello world")])])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_50(self):
        input = """Function: baucu
                     Body:
                         t_r_u_m_p = "Make America Great Again";
                        b_i_d_e_n = t_r_u_m_p + 76;
                     EndBody."""
        expect = Program([FuncDecl(Id("baucu"),
                                [],
                                ([],

                                [Assign(Id("t_r_u_m_p"),
                                        StringLiteral("Make America Great Again")),
                                Assign(Id("b_i_d_e_n"),BinaryOp("+",Id("t_r_u_m_p"),IntLiteral(76)))])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_51(self):
        input = """Function: fact
                    Parameter: p
                    Body:
                        If 1 Then 
                            print();
                        EndIf.
                    EndBody."""
        exp1 = IntLiteral(1)
        lstVardec1 = []
        lstStmt1 = [CallStmt(Id("print"),[])]
        tup1 = (exp1,lstVardec1,lstStmt1)
        ifthenStmt = [tup1]
        # lstVardecElse = []
        # lstStmtElse = []
        tupElse = ([],[])
        elseStmt = (tupElse)
        expect = Program([FuncDecl(Id("fact"),
                                [VarDecl(Id("p"),[],None)],
                                ([],
                                [If(ifthenStmt,elseStmt)])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,351))
        # Program([FuncDecl(Id(fact),
        #                  [VarDecl(Id(p))],
        #                   ([],
        #                   [If(IntLiteral(1),[],[CallStmt(Id(print),[])])Else([],[])])
        #                   )])
        # Program([FuncDecl(Id(fact),
        #                  [VarDecl(Id(p))],
        #                   ([],
        #                  [If(IntLiteral(1),[],[CallStmt(Id(print),[])])])
        #                   )])


    def test_52(self):
        input = """Function: fact
                    Parameter: p
                    Body:
                        If 2+3 *4 Then 
                            print();
                        ElseIf valueOfFoo(2) Then
                            printf();
                        EndIf.
                    EndBody."""
        exp1 = BinaryOp("+",IntLiteral(2),BinaryOp("*",IntLiteral(3),IntLiteral(4)))
        lstVardec1 = []
        lstStmt1 = [CallStmt(Id("print"),[])]
        tup1 = (exp1,lstVardec1,lstStmt1)
        exp2 = CallExpr(Id("valueOfFoo"),[IntLiteral(2)])
        lstVardec2 = []
        lstStmt2 = [CallStmt(Id("printf"),[])]
        tup2 = (exp2,lstVardec2,lstStmt2)
        ifthenStmt = [tup1,tup2]
        # lstVardecElse = []
        # lstStmtElse = []
        tupElse = ([],[])
        elseStmt = (tupElse)
        expect = Program([FuncDecl(Id("fact"),
                                [VarDecl(Id("p"),[],None)],
                                ([],
                                [If(ifthenStmt,elseStmt)])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_53(self):
        input = """Function: fact
                    Parameter: p
                    Body:
                        If 2+3 *4 Then 
                            Var: x = 0;
                        ElseIf valueOfFoo(2) Then
                            printf();
                        Else 
                            boolean();
                            cout(hello);
                        EndIf.
                    EndBody."""
        exp1 = BinaryOp("+",IntLiteral(2),BinaryOp("*",IntLiteral(3),IntLiteral(4)))
        lstVardec1 = [VarDecl(Id("x"),[],IntLiteral(0))]
        lstStmt1 = []
        tup1 = (exp1,lstVardec1,lstStmt1)
        exp2 = CallExpr(Id("valueOfFoo"),[IntLiteral(2)])
        lstVardec2 = []
        lstStmt2 = [CallStmt(Id("printf"),[])]
        tup2 = (exp2,lstVardec2,lstStmt2)
        ifthenStmt = [tup1,tup2]
        lstVardecElse = []
        lstStmtElse = [CallStmt(Id("boolean"),[]),CallStmt(Id("cout"),[Id("hello")])]
        tupElse = (lstVardecElse,lstStmtElse)
        elseStmt = (tupElse)
        expect = Program([FuncDecl(Id("fact"),
                                [VarDecl(Id("p"),[],None)],
                                ([],
                                [If(ifthenStmt,elseStmt)])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_54(self):
        input = """ Function: fact
                        Parameter: n
                        Body:
                            If n == 0 Then
                                Return 1;
                            Else
                                Return n * fact (n - 1);
                            EndIf.
                        EndBody."""
        exp1 = BinaryOp("==",Id("n"),IntLiteral(0))
        lstVardec1 = []
        lstStmt1 = [Return(IntLiteral(1))]
        tup1 = (exp1,lstVardec1,lstStmt1)
        ifthenStmt = [tup1]
        lstVardecElse = []
        lstStmtElse = [Return(BinaryOp("*",Id("n"),CallExpr(Id("fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))]
        tupElse = (lstVardecElse,lstStmtElse)
        elseStmt = (tupElse)
        expect = Program([FuncDecl(Id("fact"),
                        [VarDecl(Id("n"), [], None)],
                        ([],
                        [If(ifthenStmt, elseStmt)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_55(self):
        input = """Function: true
                    Body:
                        If 6 Then 
                        EndIf.
                        Return ;
                    EndBody."""
        exp1 = IntLiteral(6)
        lstVardec1 = []
        lstStmt1 = []
        tup1 = (exp1,lstVardec1,lstStmt1)
        ifthenStmt = [tup1]
        # lstVardecElse = []
        # lstStmtElse = []
        tupElse = ([],[])
        elseStmt = (tupElse)
        expect = Program([FuncDecl(Id("true"),
                                [],
                                ([],
                                [If(ifthenStmt, elseStmt),
                                Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_56(self):
        input = """Function: true
                    Body:
                        If 10 Then 
                            Var: x = 2, y = 3;
                            ppl = p + p + l;
                        EndIf.
                        Return ;
                    EndBody"""
        exp1 = IntLiteral(10)
        lstVardec1 = [VarDecl(Id("x"),[],IntLiteral(2)),
                        VarDecl(Id("y"),[],IntLiteral(3))]
        lstStmt1 = [Assign(Id("ppl"),BinaryOp("+",BinaryOp("+",Id("p"),Id("p")),Id("l")))]
        tup1 = (exp1,lstVardec1,lstStmt1)
        ifthenStmt = [tup1]
        # lstVardecElse = []
        # lstStmtElse = []
        tupElse = ([],[])
        elseStmt = (tupElse)
        expect = Program([FuncDecl(Id("true"),
                                [],
                                ([],
                                [If(ifthenStmt, elseStmt),
                                Return(None)])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_57(self):
        input = """ Function: gcd
                    Parameter: n1, n2
                        Body:
                            If(n2 != 0) Then
                                Return gcd(n2, n1%n2);
                            Else
                                Return n1;
                            EndIf.
                        EndBody."""
        exp1 = BinaryOp("!=",Id("n2"),IntLiteral(0))
        lstVardec1 = []
        lstStmt1 = [Return(CallExpr(Id("gcd"),[Id("n2"),BinaryOp("%",Id("n1"),Id("n2"))]))]
        tup1 = (exp1,lstVardec1,lstStmt1)
        ifthenStmt = [tup1]
        lstVardecElse = []
        lstStmtElse = [Return(Id("n1"))]
        tupElse = (lstVardecElse,lstStmtElse)
        elseStmt = (tupElse)
        expect = Program([FuncDecl(Id("gcd"),
                                [VarDecl(Id("n1"),[],None),
                                VarDecl(Id("n2"),[],None)],
                                
                                ([],
                                [If(ifthenStmt, elseStmt)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_58(self):
        input = """Function: thankyou
                        Body:
                            If(man) Then print("Thank you man!");
                            ElseIf(sir) Then print("Thank you sir!");
                            EndIf.
                        EndBody."""
        exp1 = Id("man")
        lstVardec1 = []
        lstStmt1 = [CallStmt(Id("print"),[StringLiteral("Thank you man!")])]
        tup1 = (exp1,lstVardec1,lstStmt1)
        exp2 = Id("sir")
        lstVardec2 = []
        lstStmt2 = [CallStmt(Id("print"),[StringLiteral("Thank you sir!")])]
        tup2 = (exp2,lstVardec2,lstStmt2)
        ifthenStmt = [tup1,tup2]
        tupElse = ([],[])
        elseStmt = (tupElse)
        expect = Program([FuncDecl(Id("thankyou"),
                                [],
                                ([],
                                [If(ifthenStmt,elseStmt)])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_59(self):
        input = """Function: hello
                        Body:
                            If(covid19(trigger)) Then
                                print("Hello new world");
                            EndIf.
                        EndBody."""
        exp1 = CallExpr(Id("covid19"),[Id("trigger")])
        lstVardec1 = []
        lstStmt1 = [CallStmt(Id("print"),[StringLiteral("Hello new world")])]
        tup1 = (exp1,lstVardec1,lstStmt1)
        ifthenStmt = [tup1]
        tupElse = ([],[])
        elseStmt = (tupElse)
        expect = Program([FuncDecl(Id("hello"),
                                [],
                                ([],
                                [If(ifthenStmt,elseStmt)])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_60(self):
        input = """Function: hello
                        Body:
                            If exp1 Then
                                If exp2_1 Then
                                ElseIf exp2_2 Then
                                Else
                            EndIf.
                        EndBody."""
        exp1 = Id("exp1")
        lstVardec1 = []

        exp2_1 = Id("exp2_1")
        lstVardec2_1 = []
        lstStmt2_1 = []
        tup2_1 = (exp2_1,lstVardec2_1,lstStmt2_1)
        exp2_2 = Id("exp2_2")
        lstVardec2_2 = []
        lstStmt2_2 = []
        tup2_2 = (exp2_2,lstVardec2_2,lstStmt2_2)
        ifthenStmtInner = [tup2_1,tup2_2]
        lstVardecElseInner = []
        lstStmtElseInner = []
        tupElseInner = (lstVardecElseInner,lstStmtElseInner)
        elseStmtInner = (tupElseInner)
        mot_stmt_if__o_phia_trong = If(ifthenStmtInner,elseStmtInner)
        lstStmt1 = [mot_stmt_if__o_phia_trong]
        
        tup1 = (exp1,lstVardec1,lstStmt1)
        ifthenStmt = [tup1]
        tupElse = ([],[])
        elseStmt = (tupElse)
        expect = Program([FuncDecl(Id("hello"),
                                [],
                                ([],
                                [If(ifthenStmt,elseStmt)])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_61(self):
        input = """Function: fact
                    Parameter: p
                    Body:
                        Return bye;
                        print(arr[1], plsss);
                    EndBody."""
        expect = Program([FuncDecl(Id("fact"),
                                [VarDecl(Id("p"),[],None)],
                                ([],

                                [Return(Id("bye")),
                                CallStmt(Id("print"),[ArrayCell(Id("arr"),[IntLiteral(1)]),Id("plsss")])])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_62(self):
        input = """Function: true
                    Body:
                        Var: a[1] = False;
                        a[0] = False;
                        Return ;
                    EndBody."""
        expect = Program([FuncDecl(Id("true"),
                                [],
                                ([VarDecl(Id("a"),[1],BooleanLiteral(False))],

                                [Assign(ArrayCell(Id("a"),[IntLiteral(0)]),BooleanLiteral(False)),
                                Return(None)])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_63(self):
        input = """Function: bigFunc
                    Body:
                        Return "WE L O S S";
                    EndBody."""
        expect = Program([FuncDecl(Id("bigFunc"),
                                [],
                                ([],
                                [Return(StringLiteral("WE L O S S"))])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_64(self):
        input = """Function: manymanysubcua
                Body:
                    x = --9---1;
                    Return --x;
                EndBody."""
        expect = Program([FuncDecl(Id("manymanysubcua"),
                                [],
                                ([],
                                [Assign(Id("x"),
                                        BinaryOp("-",UnaryOp("-",UnaryOp("-",IntLiteral(9))),UnaryOp("-",UnaryOp("-",IntLiteral(1))))),
                                Return(UnaryOp("-",UnaryOp("-",Id("x"))))])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_65(self):
        input = """Function: fact
                    Body:
                        For(arr = 1, 1<2, 2) Do
                            print(arr_);
                        EndFor.
                        Continue;
                    EndBody."""
        lstVardec = []
        lstStmt = [CallStmt(Id("print"),[Id("arr_")])]
        loop = (lstVardec,lstStmt)
        expect = Program([FuncDecl(Id("fact"),
                                [],
                                ([],

                                [For(Id("arr"),IntLiteral(1),BinaryOp("<",IntLiteral(1),IntLiteral(2)),IntLiteral(2),loop),
                                Continue()])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_66(self):
        input = """Function: fact
                    Body:
                        While True Do 
                            x = new(2);
                        EndWhile.
                    EndBody."""
        lstVardec = []
        lstStmt = [Assign(Id("x"),CallExpr(Id("new"),[IntLiteral(2)]))]
        loop = (lstVardec,lstStmt)
        expect = Program([FuncDecl(Id("fact"),
                                [],
                                ([],
                                [While(BooleanLiteral(True),loop)])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_67(self):
        input = """Function: fact
                Body:
                    Do 
                        print("Hello world");
                        While isStartLearningProgramCode(print("Hello world"))
                    EndDo.
                EndBody."""
        lstVardec = []
        lstStmt = [CallStmt(Id("print"),[StringLiteral("Hello world")])]
        loop = (lstVardec,lstStmt)
        expect = Program([FuncDecl(Id("fact"),
                                [],
                                ([],
                                [Dowhile(loop,CallExpr(Id("isStartLearningProgramCode"),[CallExpr(Id("print"),[StringLiteral("Hello world")])]))])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_68(self):
        input = """Function: foo
                    Parameter: a[5], b
                    Body:
                        Var: i = 0;
                        While (i < 5) Do
                            a[i] = b +. 1.0;
                            i = i + 1;
                        EndWhile.
                    EndBody."""
        lstVardec = []
        lstStmt = [Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),
                    Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]
        loop = (lstVardec,lstStmt)
        expect = Program([FuncDecl(Id("foo"),
                        [VarDecl(Id("a"),[5],None),VarDecl(Id("b"),[],None)],
                        ([VarDecl(Id("i"),[],IntLiteral(0))],
                        
                        [While(BinaryOp("<",Id("i"),IntLiteral(5)),loop)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_69(self):
        input = """Function: fail
                    Body:
                        While (i < 5) Do
                            a[fail(0, -0.2) && index[2]] = b +. 1.0;
                            a = {2,2};
                        EndWhile.
                    EndBody."""
        lstVardec = []
        lstStmt = [Assign(ArrayCell(Id("a"),[BinaryOp("&&",CallExpr(Id("fail"),[IntLiteral(0),UnaryOp("-",FloatLiteral(0.2))]),ArrayCell(Id("index"),[IntLiteral(2)]))]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),
                    Assign(Id("a"),ArrayLiteral([IntLiteral(2),IntLiteral(2)]))]
        loop = (lstVardec,lstStmt)
        expect = Program([FuncDecl(Id("fail"),
                                [],
                                ([],
                                [While(BinaryOp("<",Id("i"),IntLiteral(5)),loop)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_70(self):
        input = """Function: fail
                    Body:
                        str = "str1" + "str2";
                        arr = {2,4} \. {2.2,3,5} * "ac" + i;
                    EndBody."""
        expect = Program([FuncDecl(Id("fail"),
                                [],
                                ([],
                                [Assign(Id("str"),BinaryOp("+",StringLiteral("str1"),StringLiteral("str2"))),
                                Assign(Id("arr"),BinaryOp("+",BinaryOp("*",BinaryOp("\.",ArrayLiteral([IntLiteral(2),IntLiteral(4)]),ArrayLiteral([FloatLiteral(2.2),IntLiteral(3),IntLiteral(5)])),StringLiteral("ac")),Id("i")))])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_71(self):
        input = """Function: true
                    Body:
                        If 6 Then 
                        EndIf.
                        For(i=2, 2<3, 3) Do
                            a = 2;
                        EndFor.
                        Return ;
                    EndBody."""
        exp1 = IntLiteral(6)
        lstVardec1 = []
        lstStmt1 = []
        tup1 = (exp1,lstVardec1,lstStmt1)
        ifthenStmt = [tup1]
        # lstVardecElse = []
        # lstStmtElse = []
        tupElse = ([],[])
        elseStmt = (tupElse)
        loop = ([],
                [Assign(Id("a"),IntLiteral(2))])
        expect = Program([FuncDecl(Id("true"),
                                [],
                                ([],
                                [If(ifthenStmt,elseStmt),
                                For(Id("i"), IntLiteral(2), BinaryOp("<",IntLiteral(2),IntLiteral(3)), IntLiteral(3), loop),
                                Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_72(self):
        input = """Function: true
                    Body:
                        While True Do
                            print("Hw");
                        EndWhile.
                    EndBody."""
        loop = ([],[CallStmt(Id("print"),[StringLiteral("Hw")])])

        expect = Program([FuncDecl(Id("true"),
                                [],
                                ([],
                                [While(BooleanLiteral(True),loop)])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_73(self):
        input = """Function: whileEEE
                Body:
                    While ((5+2)) Do
                        variable = exp(2)[exp];
                        madao_minhbeo = (foo() + 2)[0];
                        out = (out)[123];
                    EndWhile.
                EndBody."""
        loop = ([],
            [Assign(Id("variable"),ArrayCell(CallExpr(Id("exp"),[IntLiteral(2)]),[Id("exp")])),
            Assign(Id("madao_minhbeo"),ArrayCell(BinaryOp("+",CallExpr(Id("foo"),[]),IntLiteral(2)),[IntLiteral(0)])),
            Assign(Id("out"),ArrayCell(Id("out"),[IntLiteral(123)]))])
        expect = Program([FuncDecl(Id("whileEEE"),
                                [],
                                ([],
                                [While(BinaryOp("+",IntLiteral(5),IntLiteral(2)),loop)])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_74(self):
        input = """Var: x;
                    Function: fact
                    Parameter: p
                    Body:
                        Break;
                    EndBody."""
        expect = Program([VarDecl(Id("x"),[],None),
                        FuncDecl(Id("fact"),
                        [VarDecl(Id("p"),[],None)],
                        ([],
                        [Break()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_75(self):
        input = """Var: x;
                    Function: fact
                    Parameter: p
                    Body:
                        to_be();
                        Continue;
                        Continue;
                        Continue;
                        Continue;
                    EndBody."""
        expect = Program([VarDecl(Id("x"),[],None),
                        FuncDecl(Id("fact"),
                        [VarDecl(Id("p"),[],None)],
                        ([],
                        [CallStmt(Id("to_be"),[]),Continue(),Continue(),Continue(),Continue()])
                        )])
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_76(self):
        input = """Var: x;
                    Function: fact
                    Parameter: p
                    Body:
                        Var: x[3][5];
                    EndBody."""
        expect = Program([VarDecl(Id("x"),[],None),
                        FuncDecl(Id("fact"),
                        [VarDecl(Id("p"),[],None)],
                        ([VarDecl(Id("x"),[3,5],None)],
                        []))])
        self.assertTrue(TestAST.checkASTGen(input,expect,376))


    def test_77(self):
        input = """Var: n[3] = {0x14,0O6,4.e-2};
                Var: t = 0X7F;"""
        expect = Program([VarDecl(Id("n"),[3],ArrayLiteral([IntLiteral(0x14),IntLiteral(0O6),FloatLiteral(0.04)])),
                        VarDecl(Id("t"),[],IntLiteral(0x7f))])
        self.assertTrue(TestAST.checkASTGen(input,expect,377))


    def test_78(self):
        input = """Function: boolean
                        Body:
                            anhlam = 0 + {12,22,23};
                            emsi = 21;
                        EndBody."""
        expect = Program([FuncDecl(Id("boolean"),
                                [],
                                ([],
                                [Assign(Id("anhlam"),
                                    BinaryOp("+",IntLiteral(0),ArrayLiteral([IntLiteral(12),IntLiteral(22),IntLiteral(23)]))),
                                Assign(Id("emsi"),IntLiteral(21))])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,378))


    def test_79(self):
        input = """Var: n = 0x46;"""
        expect = Program([VarDecl(Id("n"),[],IntLiteral(70))])
        self.assertTrue(TestAST.checkASTGen(input,expect,379))


    def test_80(self):
        input = """Var: txt = 0o22, none = 0O41;"""
        expect = Program([VarDecl(Id("txt"),[],IntLiteral(0o22)),VarDecl(Id("none"),[],IntLiteral(0o41))])
        self.assertTrue(TestAST.checkASTGen(input,expect,380))


    def test_81(self):
        input = """Function: a
                        Body:
                            o = 9.7 + 0X66 - 3.e-6;
                            k = 999;
                            e = "feel" + "special";
                        EndBody."""
        expect = Program([FuncDecl(Id("a"),
                                [],
                                ([],
                                [Assign(Id("o"),
                                    BinaryOp("-",BinaryOp("+",FloatLiteral(9.7),IntLiteral(0X66)),FloatLiteral(3.e-6))),
                                Assign(Id("k"),
                                    IntLiteral(999)),Assign(Id("e"),BinaryOp("+",StringLiteral("feel"),StringLiteral("special")))])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,381))


    def test_82(self):
        input = """Function: tat
                        Body:
                            mom = 129 + llac(z,y);
                        EndBody."""
        expect = Program([FuncDecl(Id("tat"),
                                [],
                                ([],
                                [Assign(Id("mom"),
                                    BinaryOp("+",IntLiteral(129),CallExpr(Id("llac"),[Id("z"),Id("y")])))])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,382))


    def test_83(self):
        input = """Var:x = 2, y = "Long";"""
        expect = Program([VarDecl(Id("x"),[], IntLiteral(2)), VarDecl(Id("y"),[],StringLiteral("Long"))])
        self.assertTrue(TestAST.checkASTGen(input,expect,383))


    def test_84(self):
        input = """Function: ppl
                    Parameter: jz[0], hoomie[0]
                    Body:
                    Var: x = 911;
                    EndBody."""
        expect = Program([FuncDecl(Id("ppl"),
                                   [VarDecl(Id("jz"),[0],None), VarDecl(Id("hoomie"),[0],None)],
                                   ([VarDecl(Id("x"),[],IntLiteral(911))],
                                    [])
                                   )])
        self.assertTrue(TestAST.checkASTGen(input,expect,384))


    def test_85(self):
        input = """Function: lpp
                    Body:
                    If True Then print(False);
                    ElseIf False Then x = 1;
                    ElseIf x == 1 Then Return True;
                    Else x = 2;
                    EndIf.
                    EndBody."""
        expect = Program([FuncDecl(Id("lpp"),
                                   [],
                                   ([],
                                    [If([(BooleanLiteral(True),[], [CallStmt(Id("print"), [BooleanLiteral(False)])]),
                                        (BooleanLiteral(False),[], [Assign(Id("x"), IntLiteral(1))]),
                                        (BinaryOp("==", Id("x"), IntLiteral(1)),[], [Return(BooleanLiteral(True))])],
                                    ([], [Assign(Id("x"), IntLiteral(2))]))])
                                   )])
        self.assertTrue(TestAST.checkASTGen(input,expect,385))


    def test_86(self):
        input = """Function: lpp
                Body:
                    Do fee(3);
                    While deep =/= True
                    EndDo.
                EndBody."""
        expect = Program([FuncDecl(Id("lpp"),
                                   [],
                                   ([],
                                    [Dowhile(
                                    ([],
                                     [CallStmt(Id("fee"),[IntLiteral(3)])]),
                                      BinaryOp("=/=", Id("deep"), BooleanLiteral(True)))
                                    ])
                                   )])
        self.assertTrue(TestAST.checkASTGen(input,expect,386))


    def test_87(self):
        input = """Function: lpp
                Body:
                    Do 
                        x = a <. b;
                        x = a >. b;
                        x = a <=. b;
                        x = a >=. b;
                    While deep =/= True
                    EndDo.
                EndBody."""
        expect = Program([FuncDecl(Id("lpp"),
                                   [],
                                   ([],
                                    [Dowhile(
                                    ([],
                                     [Assign(Id("x"), BinaryOp("<.", Id("a"), Id("b"))),
                                      Assign(Id("x"), BinaryOp(">.", Id("a"), Id("b"))),
                                      Assign(Id("x"), BinaryOp("<=.", Id("a"), Id("b"))),
                                      Assign(Id("x"), BinaryOp(">=.", Id("a"), Id("b")))
                                     ]),
                                      BinaryOp("=/=", Id("deep"), BooleanLiteral(True)))
                                    ])
                                   )])
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_88(self):
        input = """Function: loser
            Parameter: xxx[1]
            Body:
                xxx = (1 + 2);
            EndBody"""
        expect = Program([FuncDecl(Id('loser'),
                        [VarDecl(Id('xxx'),[1],None)],
                        ([],
                        [Assign(Id('xxx'),BinaryOp('+',IntLiteral(1),IntLiteral(2)))])
                        )])
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_89(self):
        input = """Function: main
                    Body:
                        For (i=0,i<2,2) Do
                            cout(i);
                        EndFor.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),
                                    [],
                                    (
                                        [],
                                        [For(Id('i'),
                                                IntLiteral(0),
                                                BinaryOp('<',Id('i'),IntLiteral(2)),
                                                IntLiteral(2),
                                                ([],
                                                [CallStmt(Id('cout'),[Id('i')])])
                                            )
                                        ]
                                    )
                                )
                            ])
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_90(self):
        input = """Function: main
                    Body:
                        While True Do
                            dosth();
                        EndWhile.
                    EndBody."""
        expect = Program(
                        [FuncDecl
                            (
                                Id('main'),
                                [],
                                (
                                    [],[
                                        While(BooleanLiteral(True),
                                        (
                                            [],
                                            [CallStmt(Id('dosth'),[])]
                                        )
                                        )
                                        ]
                                    )
                            )
                        ]
                    )
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_91(self):
        input = """Var: x32_1 = 0o11122233;"""
        expect = Program([VarDecl(Id('x32_1'),[],IntLiteral(0o11122233))])
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_92(self):
        input = """Var: x32_1 = "anh cung ko la";"""
        expect = Program([VarDecl(Id("x32_1"),[],StringLiteral("anh cung ko la"))])
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_93(self):
        input = """Function: main
                    Body:
                    **
                        nocaption(10101010 - -. 8888888);
                    **
                    EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_94(self):
        input = """Function: main
                    Body:
                        x = anh != (cung_khong == con_la *. nhac_si || mong_mo); 
                    EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("x"),BinaryOp("!=",Id("anh"),BinaryOp("==",Id("cung_khong"),BinaryOp("||",BinaryOp("*.",Id("con_la"),Id("nhac_si")),Id("mong_mo")))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_95(self):
        input = """Function: main
                    Body:
                        Var: r;
                        r = anh;
                        anh = khong_con(la(nhac_si[mong_mo]))[10];
                    EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("r"),[],None)],[Assign(Id("r"),Id("anh")),Assign(Id("anh"),ArrayCell(CallExpr(Id("khong_con"),[CallExpr(Id("la"),[ArrayCell(Id("nhac_si"),[Id("mong_mo")])])]),[IntLiteral(10)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_96(self):
        input = """Function: main
                    Body:
                        Return;
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[Return(expr = None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_97(self):
        input = """Function: main
                    Body:
                        a = 12E3;
                        true = True;
                    EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),FloatLiteral(12000.0)),Assign(Id("true"),BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_98(self):
        input = """Function: main
                    Body:
                        arr[3][5] = 2;
                    EndBody."""
        expect = Program([FuncDecl(Id("main"),
                                [],
                                ([],
                                [Assign(ArrayCell(Id("arr"),[IntLiteral(3),IntLiteral(5)]),IntLiteral(2))])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_99(self):
        input = """Function: integer
                    Parameter: a,b,c
                        Body:
                            Var: a = 0x122;
                            Var: b = 0o157;
                            print(a+b);
                        EndBody."""
        expect = Program([FuncDecl(Id("integer"),
                                [VarDecl(Id("a"),[],None),
                                VarDecl(Id("b"),[],None),
                                VarDecl(Id("c"),[],None)],
                                ([VarDecl(Id("a"),[],IntLiteral(290)),
                                VarDecl(Id("b"),[],IntLiteral(111))],
                                [CallStmt(Id("print"),[BinaryOp("+",Id("a"),Id("b"))])])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,399))

    def test_100(self):
        input = """Function: whileEEE
                    Body:
                        While (((((((((((5+2))))))))))) Do
                            Return 0;
                        EndWhile.
                    EndBody."""
        loop = [],[Return(IntLiteral(0))]
        expect = Program([FuncDecl(Id("whileEEE"),
                                [],
                                ([],
                                [While(BinaryOp("+",IntLiteral(5),IntLiteral(2)),loop)])
                                )])
        self.assertTrue(TestAST.checkASTGen(input,expect,400))
        


