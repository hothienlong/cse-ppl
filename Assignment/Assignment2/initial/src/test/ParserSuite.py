import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    '''test array'''
    def test_203(self):
        input = """Var: a, b ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))    
    
    def test_204(self):
        input = """Var: a[2], b = 3 ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))  

    
    def test_205(self):
        input = """Var: a[3] = 2, b ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))  

    
    def test_206(self):
        input = """Var: a[] ;"""
        expect = "Error on line 1 col 7: ]"
        self.assertTrue(TestParser.checkParser(input,expect,206))  
    
    def test_207(self):
        input = """Var: a[2][5] = {1,2,3} ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))  


    def test_208(self):
        input = """Var: a[2] = {2,{3,3},True}, b = "String: '"who that'"" ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))  


    def test_209(self):
        input = """Var: a[2] = {}, b = 2;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))  


    def test_210(self):
        input = """Var: a[2] = {{1, 2, {4, 5}} ; """
        expect = "Error on line 1 col 28: ;"
        self.assertTrue(TestParser.checkParser(input,expect,210))      

    '''Test var_dec, exp'''
    def test_211(self):
        input = """Function: babe
                    Body:
                        i= foo((3+4), True == False);
                    EndBody.
                \n """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))                                          

    def test_212(self):
        input = """x =3;\n Var x =2;"""
        expect = "Error on line 1 col 0: x"
        self.assertTrue(TestParser.checkParser(input,expect,212))    
  
    def test_213(self):
        input = """ Function: locfuho
                        Body:
                            foo = fuho(thochinh[2], {2,3}, a && b) ;
                        EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))
    def test_214(self):
        input = """Function: borrow
                    Parameter: n
                    Body:
                        fuho(2) ;
                    EndBody.     
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    def test_215(self):
        input = "{2,4, 4}"
        expect = "Error on line 1 col 0: {"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test_216(self):
        input = """ Function: body
                        Body:
                            a[3] = arr[b[2][3]] + 4;
                        EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    def test_217(self):
        input = "Var: a = 2 ; Var: b[3][3] = {foo(0905)};" #{literal_list}
        expect = "Error on line 1 col 29: foo"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test_218(self):
        input = """Var: b = 001;"""
        expect = "Error on line 1 col 10: 0"
        self.assertTrue(TestParser.checkParser(input,expect,218))
    def test_219(self):
        input = """ Function: ham
                        Body:
                            array[3][3] = foo(2 + nested_exp(5) - 3, ((3)));
                        EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    def test_220(self):
        input = """Var: i,j,k=2;  f=5;""" #stmt phải nằm trong body
        expect = "Error on line 1 col 15: f"
        self.assertTrue(TestParser.checkParser(input,expect,220))
    def test_221(self):
        input = """Function: borrow
                    Parameter: n
                    Body:
                        a[3 + foo(2)] = a[b[2][3]] + 4;
                    EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    def test_222(self):
        input = """Var:;"""
        expect = "Error on line 1 col 4: ;"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    def test_223(self):
        input = """ Function: hamso
                        Body:
                            x = a[b[c[d]]];
                        EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))
    def test_224(self):
        input = """Var: a = foo(2+3);""" #khoi tao bang literal
        expect = "Error on line 1 col 9: foo"
        self.assertTrue(TestParser.checkParser(input,expect,224))
    def test_225(self):
        input = """ Function: func
                        Body:
                            a = (1+2)<4;
                            a = -1; 
                            b = -0XAF;
                            c = -1.e3;
                            a[3] = {"abc", True, -1.e5}; 
                            a[True] = False;
                        EndBody.
                """
        expect = "Error on line 7 col 49: -"
        self.assertTrue(TestParser.checkParser(input,expect,225))
    def test_226(self):
        input = """ Function: func
                        Body:
                            a = True == (False + True);
                        EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))
    def test_227(self):
        input = """**Var x: XD =))****"""
        expect = "name 'UnterminatedComment' is not defined"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    
    def test_228(self):
        input = """Function: fact
                    Parameter: n
                    Body:
                        f = func(2.2,3) ;
                        Var: r = 10., v;
                        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                    EndBody."""
        expect = "Error on line 5 col 24: Var"
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test_229(self):
        input = """ Var: x;
                    Function: fact
                    Parameter:  arr[], x
                    Body:
                        f = func(2.2,3) ;
                        Var: r = 10., v;
                        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                    EndBody."""
        expect = "Error on line 3 col 36: ]"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    def test_230(self):
        input = """ Var: x;
                    Function: fact
                    Parameter: 
                    Body:
                        f = func(2.2,3) ;
                        Var: r = 10., v;
                        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                    EndBody."""
        expect = "Error on line 4 col 20: Body"
        self.assertTrue(TestParser.checkParser(input,expect,230))

    def test_231(self):
        input = """ Body:
                        a;
                    EndBody.
                    Var x;"""
        expect = "Error on line 1 col 1: Body"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test_232(self):
        input = """ Var: x;
                    Function: fact
                    Parameter: p
                    Body:
                        If 2+3 *4 Then 
                            print();
                        ElseIf valueOfFoo(2) Then
                            printf();
                        Else 
                            boolean();
                            cout(hello);
                        EndIf.
                        For (i = 0, i < 10, 2) Do
                            writeln(i);
                        EndFor.
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_233(self):
        input = """ Var: x;
                    break;
                    Function: fact
                    Parameter: p
                    Body:
                        return bye;
                        print(arr[], plsss);
                        return 0;
                    EndBody."""
        expect = "Error on line 2 col 20: break"
        self.assertTrue(TestParser.checkParser(input,expect,233))

    def test_234(self):
        input = """ Var: x;
                    Function: fact
                    Parameter: p
                    Body:
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))
    
    def test_235(self):
        input = """ Var: x;
                    Function: fact
                    Parameter: p
                    Body:
                        Break;
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test_236(self):
        input = """ Var: x;
                    Function: fact
                    Body:
                        For(arr[] = 1, 1<2, 2)
                            print(arr);
                        EndFor.
                    EndBody."""
        expect = "Error on line 4 col 31: ["
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test_237(self):
        input = """ Var: x;
                    Function: fact
                    Body:
                        For(arr = 1, 1<2, 2) Do
                            print(arr_);
                        EndFor.
                        Continue;

                        If 1<2 Then a=2;
                        Else 
                        EndIf.
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))

    def test_238(self):
        input = """ Var: x;
                    Function: fact
                    Body:
                        While True Do 
                            x = new(2);
                        EndWhile.

                        Do 
                            print("Hello world");
                        While isStartLearningProgramCode(print("Hello world"))
                        EndDo.
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def test_239(self):
        input = """ Var: x;
                    Function: fact
                    Body:
                        Return bye;                    
                        Return 0;
                        print(arr[2], plsss);
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))
       
    def test_240(self):
        input = """ Var: x;
                    Function: fact
                        Parameter: n
                        Body:
                            If n == 0 Then
                                Return 1;
                            Else
                                Return n * fact (n - 1);
                            EndIf.
                        EndBody.

                    Function: main
                        Body:
                        x = 10;
                        fact (x);
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test_241(self):
        input = """Function: foo
                    Parameter: a[5], b
                    Body:
                        Var: i = 0;
                        While (i < 5) Do
                            a[i] = b +. 1.0;
                            i = i + 1;
                        EndWhile.
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))    

    def test_242(self):
        input = """Function: fail
                    Body:
                        While (i < 5) Do
                            a[fail(0, -0.2) && index[2]] = b +. 1.0;
                            a = {2,2};
                        EndWhile.
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))   

    def test_243(self):
        input = """Function: fail
                    Body:
                        str = "str1" + "str2";
                        arr = {2,4} \. {2.2,3,5} * "ac" + i;
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))   

    def test_244(self):
        input = """Function: fail
                    Body:
                        While (i < 5) Do
                            Var: a = 2;
                            a = 3;
                        EndWhile.
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244)) 

    def test_245(self):
        input = """Function: fail
                    Body:
                        If i < 5 Then 
                            a = 3;
                            Var: a = 2;
                        EndIf.
                    EndBody."""
        expect = "Error on line 5 col 28: Var" #khai báo sau
        self.assertTrue(TestParser.checkParser(input,expect,245)) 

    def test_246(self):
        input = """Function: fail
                    Body:
                        If i < 5 Then 
                            Var: dung = 2;
                            While (True) Do
                                error = 3;
                                Var: sai = 2;
                            EndWhile.    
                        EndIf.
                    EndBody."""
        expect = "Error on line 7 col 32: Var"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test_247(self):
        input = """Function: idk
                    Body:
                        arr[0x233] = arr[0o23] + arr[foo(12)];
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    
    def test_248(self):
        input = """Function: true
                    Body:
                        If 6 Then 
                        EndIf.
                        For(i=2, 2<3, 3) Do
                            a = 2;
                        EndFor.
                        Return ;
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))  

    def test_249(self):
        input = """Function: true
                    Body:
                        For(i=2, 2<3, 3) Do
                            If a == 2 Then
                                Break;
                                Continue;
                            EndIf.
                        EndFor.
                        Return ;
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))  

    def test_250(self):
        input = """Function: true
                    Body:
                        While True Do
                            print("Hw");
                        EndWhile.
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test_251(self):
        input = """Function: true
                    Body:
                        Var: a[True] = False;
                        a[True] = False;
                        Return ;
                    EndBody.               
                    """
        expect = "Error on line 3 col 31: True"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test_252(self):
        input = """Function: true
                    Body:
                        foo(2)[3] = 2;
                    EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))
    
    def test_253(self):
        input = """Function: true
                    Body:
                        True[3] = False;
                        a[b[c]][i] = 0;
                        (True + b*c && !3)[99] = {2};
                        5[3] = 3[5];
                    EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test_254(self):
        input = """Function: true
                    Body:
                        arr[3][3] = 4[3] + True[3] && !2;
                        arr = 2 + !{2,2} % "kokoko\ko";
                    EndBody.               
                    """
        expect = "kokoko\k"
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def test_255(self):
        input = """Function: true
                    Body:
                        b = a--3; ** a - (-3) **
                        p[3] = a--;
                        p = a!3*b;
                    EndBody.               
                    """
        expect = "Error on line 4 col 34: ;"
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test_256(self):
        input = """**
                    Function: true
                    Body:
                        b = a--3;
                        p[3] = a--;
                        p = a!3*b;
                    EndBody.   
                   **            
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test_257(self):
        input = """**
                    Function: true
                    Body:
                       b = a--3; ** a - (-3) **
                    EndBody.   
                   **            
                    """
        expect = "Error on line 4 col 36: a"
        self.assertTrue(TestParser.checkParser(input,expect,257))

    def test_258(self):
        input = """**
                    Function: true
                    Body:
                       b = a--3; ** Var: b = 3; **
                    EndBody.   
                   **            
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def test_259(self):
        input = """ Var: a, b = 2, c = -1;
                    Function: true
                    Body:
                       Var: b = 2+3;
                    EndBody.             
                    """
        expect = "Error on line 1 col 20: -"
        self.assertTrue(TestParser.checkParser(input,expect,259))

    def test_260(self):
        input = """**
                    Function: true
                    Body:
                       **
                        Function: hello
                            Body:
                                print("Hello world");
                            EndBody.
                        **
                    EndBody.             
                **"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test_261(self):
        input = """**
                    Function: true
                    Body:
                       **
                        Function: hello
                            Body:
                                print("Hom nay la mot ngay \nang dep");
                            EndBody.
                        **
                    EndBody.             
                **"""
        expect = "Hom nay la mot ngay "
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test_262(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_263(self):
        input = """Var: ko = "09051508";
                    Function: hello                    
                    Body:
                        Varr x = 2, y = 3;
                    EndBody.
                """
        expect = "Error on line 4 col 27: r"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_264(self):
        input = """Function: hello
                    Var: ko = "09051508";
                    Body:
                        Var x = 2, y = 3
                        ppl = p + p + l;
                    EndBody.
                """
        expect = "Error on line 2 col 20: Var"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test_265(self):
        input = """Function: BigFunc
                    Body:
                        Return "WE L O S S";
                    EndBody.
                """
        expect = "B"
        self.assertTrue(TestParser.checkParser(input,expect,265))

    def test_266(self):
        input = """Function: bigFunc
                    Body:
                        Return "WE L O S S";
                    EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test_267(self):
        input = """Function: bigFunc
                    **Body:**
                        cout<<"Where is my body?";
                        **This is my end body**
                    EndBody.
                """
        expect = "Error on line 3 col 24: cout"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test_268(self):
        input = """Function: bigFunc
                    Body:
                        printf("How are you? I'm Strong, and you?",me\n);
                    EndBody.
                """
        expect = "How are you? I'm"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test_269(self):
        input = """Function: bigFunc
                     Body:
                         Var: chao, mung, ngay, phu, nu, viet, nam = 20-11;
                         print("%s, %s, %s, %s, %s, %s, %d", chao, mung, ngay, phu, nu, viet, nam);
                     EndBody.
                 """
        expect = "Error on line 3 col 71: -"
        self.assertTrue(TestParser.checkParser(input, expect, 269))

    def test_270(self):
        input = """Function: bigFunc
                     Body:
                         con_30_test_case_nua_moi_xong = !hahahahahahaha;
                         ko = huhuhuhu;
                         saddddddddddddddd(buon - kozui);
                     EndBody.
                 """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 270))

    def test_271(self):
        input = """Function: baucu
                     Body:
                         t_r_u_m_p = "Make America Great Again";
                     EndBody.
                 """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test_272(self):
        input = """Function: trituenhantao
                     Body:
                         If exp Then
                             If pass_turing Then
                                 If fake_human_success Then
                                     print("I am AI");
                                 ElseIf confirm_captcha Then
                                     print("I not robot");
                                 Else
                                     print("Cach mang 4.0");
                                 EndIf.
                             EndIf.
                         EndIf.
                     EndBody.
                 """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    def test_273(self):
        input = """Function: elliot_edison
                     Body:
                         Var: some_times_I_dream_of_saving_the_world;
                         we_are_fsosiety = mR_roBOt;
                         dark_army = mrRoBot + "Tyrell is alive";
                         hello("Did you forgot who i am?");
                         "404 Not Found"
                         **What...?**
                         Hello. whiteRose_hacktime();
                     EndBody.
                 """
        expect = "H"
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    def test_274(self):
        input = """Function: bigFunc
                     Body:
                         Var: var = var(var[var]);

                         string = "break loop\n boom";
                     EndBody.<EOF>
                 """
        expect = "Error on line 3 col 36: var"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test_275(self):
        input = """Function: twice
                        Body:
                            eyes_wide_open = jIHYO(14\\10\\2020);
                            dahyun(i <3 *u);
                            jzMina([0000][0000]);
                        EndBody.
                    """
        expect = "Error on line 5 col 35: ["
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test_276(self):
        input = """
                  Function: funny
                  Parameter: this, is, a, chuahe
                  Body:
                      str = "string";
                      z = y + "one illegal string\\m";
                  EndBody.
                  Function: anotherFunction
                  Body:
                      tt = str * bkit(this, is, a, chuahe);
                  EndBody.
                  """
        expect = "one illegal string\m"
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test_277(self):
        input = """
                Var: x = 1.;
                Var: y = 2.;
                EndBody.
                """
        expect = "Error on line 4 col 16: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    def test_278(self):
        input = """
                Body:
                    Var: noparam = 0.;
                    Var: gaugau = 1.;
                EndBody.
                """
        expect = "Error on line 2 col 16: Body"
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    def test_279(self):
        input = """
                Function: noFun
                Parameter: loop
                    Body:
                        Do If 2=2 Then 4=0;
                            ElseIf 2=2 Then 4=4;
                            Else Return True;
                            EndIf.
                        While 2=/=2;
                        EndDo. 
                    EndBody.
                """
        expect = "Error on line 5 col 31: ="
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    def test_280(self):
        input = """
                Function: manymanysubcua
                Body:
                    x = --9--------1---------0.5;
                EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test_281(self):
        input = """
                Function: what
                    Body:
                        whatthe = arr[2](3) * brr(3)[122];
                    EndBody.
                """
        expect = "Error on line 4 col 40: ("
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test_282(self):
        input = """
                Function: integer
                Parameter: a,b,c
                    Body:
                        Var: a = 0x122;
                        Var: b = 0o157;
                        print(a+b);
                    EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test_283(self): #Only have sign - and -.
        input = """
                Function: unary_not__have_add_operator
                Body:
                    constant_la_literal_noi_chung = +3;
                EndBody.
                """
        expect = "Error on line 4 col 52: +"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test_284(self):
        input = """
                Function: whileEEE
                Body:
                    While () Do
                        tra = le;
                        goilagiday = tra + long;
                    EndWhile.
                EndBody.
                    """
        expect = "Error on line 4 col 20: While"
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test_285(self):
        input = """
                Function: whileEEE
                Body:
                    While (((((((((((5+2))))))))))) Do
                        Return 0;
                    EndWhile.
                EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    def test_286(self):
        input = """
                Function: whileEEE
                Body:
                    While (((((((((((5+2))))))))))) Do
                        variable = exp(2)[exp];
                        madao_minhbeo = (foo() + 2)[0];
                        out = (out(out(out())))[123];
                    EndWhile.
                EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test_287(self):
        input = """ Var: x = 0X92.22, e = 0x8e-6;
                    """
        expect = "Error on line 1 col 14: ."
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test_288(self):#lỗi index vế trái
        input = """Function: foo
                    Parameter: x
                        Body:
                            x = x + 1;
                            x + 1[2];
                    EndBody."""
        expect = "Error on line 5 col 30: +"
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def test_289(self):
        input = """Function: var_follow
                    Parameter: xyz[10]
                        Body:
                            var(xy[1]);
                            Return True;
                        EndBody.
                    Var: x = 1;"""
        expect = "Error on line 7 col 20: Var"
        self.assertTrue(TestParser.checkParser(input,expect,289))


    def test_290(self):
        input = """ While (2) Do
                        tra = le;
                        goilagiday = tra + long;
                    EndWhile."""
        expect = "Error on line 1 col 1: While"
        self.assertTrue(TestParser.checkParser(input,expect,290))


    def test_291(self):
        input = """False"""
        expect = "Error on line 1 col 0: False"
        self.assertTrue(TestParser.checkParser(input,expect,291))

    def test_292(self):
        input = """Var: x = 1;Function:fibonaci Parameter:x Body:Returnfibonaci(x-1)+fibonaci(x-2);EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))

    def test_293(self):
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,293))

    def test_294(self):
        input = """Function: lstSquare
                    Parameter: n
                    Body:
                        If(n == 0) Then
                            Return arr[null];
                        Return lstSquare(n-1) + a[n*2];
                    EndBody."""
        expect = "Error on line 7 col 20: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,294))

    def test_295(self):
        input = """ Function: myFunc
                        Body:
                            Return xmu2;
                        EndBody.

                    Function: highOrderSquare
                    Parameter: n
                        Body:
                            lstSquare = list[];
                            For(Var: i=1, i<=n, 1) Do
                                lstSquare.append(i);
                            EndFor.
                            Return list(map(myFunc, lstSquare));
                        EndBody.
                """
        expect = "Error on line 9 col 45: ]"
        self.assertTrue(TestParser.checkParser(input,expect,295))

    def test_296(self):
        input = """ Function: swap
                    Parameter: a,b
                        Body:
                            Var: temp = a; **gan literal ko co id**
                            a = b;
                            b = temp;
                        EndBody.
                """
        expect = "Error on line 4 col 40: a"
        self.assertTrue(TestParser.checkParser(input,expect,296))

    def test_297(self):
        input = """ Function: gcd
                    Parameter: n1, n2
                        Body:
                            If(n2 != 0) Then
                                Return gcd(n2, n1%n2);
                            Else
                                Return n1;
                            EndIf.
                        EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))

    def test_298(self):
        input = """ Function: fibonaci
                        Body:
                            Var: t1=0,t2=1;
                            For(i=1, i<=n, 1) Do
                                print(t1);
                                nextTerm = t1+t2;
                                t1 = t2;
                                t2 = nextTerm;
                            EndFor.
                        EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))

    def test_299(self):
        input = """ Function: khabanh
                        Body:
                            cungkhaduoi = "1000 dong code, cuoi cung cung duoc ngu:((";
                            wait();
                            vancon(mot,cau,a[o[kia][huhu]]);
                            conmetmoiconmetmoilam_me_a(23*h);
                        EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))

    def test_300(self):
        input = """ Function: endgame
                    Parameter: testcase_thu300
                        Body:
                            noooo = 20\\10 + cua + toi;
                            gucnga();
                            sleep();
                            zzzzzzzzzzzzz__________ = zzzzzzzzzzzzzzzzzzzz__________;
                            khokhokhokhokho()[khokhokho] = khokhokho;
                        EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,300))

    def test_301(self):
        input = """ Function: endgame
                    Parameter: testcase_thu300
                        Body:
                            a+b[2] = c;
                        EndBody.
                """
        expect = "Error on line 4 col 29: +"
        self.assertTrue(TestParser.checkParser(input,expect,301))
















