import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_comment1(self):
        self.assertTrue(TestLexer.checkLexeme("""*""","*,<EOF>",1)) #* là operator
    def test_comment2(self):
        self.assertTrue(TestLexer.checkLexeme("""**a bc**abc""","abc,<EOF>",2))
    def test_comment3(self):    
        self.assertTrue(TestLexer.checkLexeme("""***1 23**""","<EOF>",3))
    def test_comment4(self):
        self.assertTrue(TestLexer.checkLexeme("""** c***""","*,<EOF>",4))
        '''test 5: 1 cmt, 2 id, 3 operator *'''
    def test_comment5(self):
        self.assertTrue(TestLexer.checkLexeme("""**2 dau sao**co**mga1*""","co,Unterminated Comment",5))



    def test_identifier1(self):
        self.assertTrue(TestLexer.checkLexeme("""writeln""","writeln,<EOF>",6))
    def test_identifier2(self):  
        self.assertTrue(TestLexer.checkLexeme("""Wri_teLn""","Error Token W",7))
    def test_identifier3(self):
        self.assertTrue(TestLexer.checkLexeme("""9writeln""","9,writeln,<EOF>",8)) #đã định nghĩa int
    def test_identifier4(self):
        self.assertTrue(TestLexer.checkLexeme("""l_e Write""","l_e,Error Token W",9))
    def test_identifier5(self):
        self.assertTrue(TestLexer.checkLexeme("""_test""","Error Token _",10))
    

    def test_keyword1(self):
        self.assertTrue(TestLexer.checkLexeme("""Body""","Body,<EOF>",11))
    def test_keyword2(self):
        self.assertTrue(TestLexer.checkLexeme("""End Do""","Error Token E",12))
    def test_keyword3(self):
        self.assertTrue(TestLexer.checkLexeme("""endDo""","endDo,<EOF>",13)) #ID    
    def test_keyword4(self):
        self.assertTrue(TestLexer.checkLexeme("""Break DoEndDo""","Break,Do,EndDo,<EOF>",14))  
    def test_keyword5(self):
        self.assertTrue(TestLexer.checkLexeme("""ElseIf IfElse""","ElseIf,If,Else,<EOF>",15)) #not Else



    def test_operator1(self):
        self.assertTrue(TestLexer.checkLexeme("""+.""","+.,<EOF>",16))
    def test_operator2(self):
        self.assertTrue(TestLexer.checkLexeme("""*.""","*.,<EOF>",17))
    def test_operator3(self):
        self.assertTrue(TestLexer.checkLexeme("""\\""","\,<EOF>",18))
    def test_operator4(self):
        self.assertTrue(TestLexer.checkLexeme("""+.+""","+.,+,<EOF>",19))
    def test_operator5(self):
        self.assertTrue(TestLexer.checkLexeme("""\\\\""","\,\,<EOF>",20))


    def test_separator1(self):
        self.assertTrue(TestLexer.checkLexeme("""()[""","(,),[,<EOF>",21)) 
    def test_separator2(self):
        self.assertTrue(TestLexer.checkLexeme("""*.""","*.,<EOF>",22)) #operator
    def test_separator3(self):
        self.assertTrue(TestLexer.checkLexeme("""** . **...""",".,.,.,<EOF>",23))
    def test_separator4(self):
        self.assertTrue(TestLexer.checkLexeme("""[abc]""","[,abc,],<EOF>",24))
    def test_separator5(self):
        self.assertTrue(TestLexer.checkLexeme("""{a+b==b+a}""","{,a,+,b,==,b,+,a,},<EOF>",25))

    def test_integer1(self):
        self.assertTrue(TestLexer.checkLexeme("""01""","0,1,<EOF>",26))
    def test_integer2(self):
        self.assertTrue(TestLexer.checkLexeme("""199""","199,<EOF>",27))
    def test_integer3(self):
        self.assertTrue(TestLexer.checkLexeme("""0xFF""","0xFF,<EOF>",28))
    def test_integer4(self):#đọc 0o770 nhảy qua lexer ws -> nhảy ngược lại sẽ kiểm tra lại từ đầu
        self.assertTrue(TestLexer.checkLexeme("""0o770X11""","0o770,Error Token X",29)) 
    def test_integer5(self):
        self.assertTrue(TestLexer.checkLexeme("""000x9""","0,0,0x9,<EOF>",30))
    def test_integer6(self):
        self.assertTrue(TestLexer.checkLexeme("""0X002""","0,Error Token X",31))
    def test_integer7(self):
        self.assertTrue(TestLexer.checkLexeme("""0X7fabc -- 45 !=""","0X7,fabc,-,-,45,!=,<EOF>",32))
    def test_integer8(self):
        self.assertTrue(TestLexer.checkLexeme("""12X92""","12,Error Token X",33))
    def test_integer9(self):
        self.assertTrue(TestLexer.checkLexeme("""X92""","Error Token X",34))
    def test_integer10(self):
        self.assertTrue(TestLexer.checkLexeme("""0X92,0x0000x12x10010xo101""","0X92,,,0,x0000x12x10010xo101,<EOF>",35))



    def test_float1(self):
        self.assertTrue(TestLexer.checkLexeme("""12.0e3""","12.0e3,<EOF>",36))
    def test_float2(self):
        self.assertTrue(TestLexer.checkLexeme("""12e+3""","12e+3,<EOF>",37))
    def test_float3(self):
        self.assertTrue(TestLexer.checkLexeme("""12.e5""","12.e5,<EOF>",38))
    def test_float4(self):
        self.assertTrue(TestLexer.checkLexeme(""".12e""",".,12,e,<EOF>",39))
    def test_float5(self):
        self.assertTrue(TestLexer.checkLexeme("""e""","e,<EOF>",40)) #run được nhưng là id      
    def test_float6(self):
        self.assertTrue(TestLexer.checkLexeme("""022.13""","022.13,<EOF>",41))
    def test_float7(self):
        self.assertTrue(TestLexer.checkLexeme("""12.e03""","12.e03,<EOF>",42))
    def test_float8(self):
        self.assertTrue(TestLexer.checkLexeme("""000.e0""","000.e0,<EOF>",43))
    def test_float9(self):
        self.assertTrue(TestLexer.checkLexeme(""".123""",".,123,<EOF>",44))
    def test_float10(self):
        self.assertTrue(TestLexer.checkLexeme("""1.000""","1.000,<EOF>",45))



    def test_whitespace1(self):
        """test whitespace"""
        self.assertTrue(TestLexer.checkLexeme(""" \n\t""", "<EOF>", 46))
    def test_whitespace2(self):
        self.assertTrue(TestLexer.checkLexeme("""\t""", "<EOF>", 47))
    def test_whitespace3(self):
        self.assertTrue(TestLexer.checkLexeme("""\n""", "<EOF>", 48))
    def test_whitespace4(self):
        self.assertTrue(TestLexer.checkLexeme(""" \t \n \r""", "<EOF>", 49))
    def test_whitespace5(self):
       self.assertTrue(TestLexer.checkLexeme("""long\ntra \t\r""", "long,tra,<EOF>", 50))



    def test_string1(self):#dùng ' hay \' cũng như nhau?
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string" ""","""This is a string,<EOF>""",51))
    def test_string2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Hello my friend: '"ok'"'"end?'"gb friend'" """,
                                            """Unclosed String: Hello my friend: '"ok'"'"end?'"gb friend'" """,52))
    def test_string3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Hello my friend: '"ok'"'"end?'"gb friend\\'" """,
                                                """Hello my friend: '"ok'"'"end?'"gb friend\\',<EOF>""",53))
    def test_string4(self):#lấy chuỗi càng dài càng tốt => Illegal ko phải tách token
        self.assertTrue(TestLexer.checkLexeme(""" "Whrere is my single: "Cate"" ""","""Whrere is my single: ,Error Token C""",54))
    def test_string5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is my single'" ""","""Unclosed String: This is my single'" """,55))
    #'là dấu nháy đơn(có thể kí tự đb), \' là chuỗi có nháy đơn thuần
    def test_string6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Hello my friend: '"ok'"c" ""","""Hello my friend: '"ok'"c,<EOF>""",56))
    def test_string7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Escape is ok:\\b\\f\\r\\n" ""","""Escape is ok:\\b\\f\\r\\n,<EOF>""",57)) #escape của py là \\ -> \ kết hợp b là ra escape của BKIT: \b
    def test_string8(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Escape is No ok:\b\f\r\n" ""","""Unclosed String: Escape is No ok:""",58)) #escape của py là \b -> sử dụng đúng mục đích py
    def test_string9(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Whrere is my single: "Cate"" ""","""Whrere is my single: ,Error Token C""",59))
    def test_string10(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is my \single'" ""","""Illegal Escape In String: This is my \s""",60))
    def test_string11(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\"" """,""",Unclosed String:  """,61))
    def test_string12(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\"\"""",""",Unclosed String: """,62))
    def test_string13(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Hello my friend: '\\"ok'"c ""","""Illegal Escape In String: Hello my friend: '\\""",63))
    def test_string14(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Escape'wrong" ""","""Illegal Escape In String: Escape'w""",64))
    def test_string15(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Backs\\lack" ""","""Illegal Escape In String: Backs\l""",65))
    def test_string16(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Backs\\\\lack" ""","""Backs\\\\lack,<EOF>""",66))
    def test_string17(self):
        self.assertTrue(TestLexer.checkLexeme(""" "helloFriend"hi e"a\nThis is a string" ""","""helloFriend,hi,e,Unclosed String: a""",67))
    def test_string18(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\'" ""","""\\',<EOF>""",68))
    def test_string19(self):
        self.assertTrue(TestLexer.checkLexeme(""" "" """,""",<EOF>""",69))
    def test_string20(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is an unclose string\n" """,
                                            """Unclosed String: This is an unclose string""",70))



    def test_array1(self):
        self.assertTrue(TestLexer.checkLexeme("""{"abc", 5}""","""{,abc,,,5,},<EOF>""",71))
    def test_array2(self):
        self.assertTrue(TestLexer.checkLexeme("""{True,False}""","""{,True,,,False,},<EOF>""",72))
    def test_array3(self):
        self.assertTrue(TestLexer.checkLexeme("""{1.3,4}""","""{,1.3,,,4,},<EOF>""",73))
    def test_array4(self):
        self.assertTrue(TestLexer.checkLexeme("""{{1,2,3},{2}}""","""{,{,1,,,2,,,3,},,,{,2,},},<EOF>""",74))
    def test_array5(self):
        self.assertTrue(TestLexer.checkLexeme("""{{1,2,3,{3}A""","""{,{,1,,,2,,,3,,,{,3,},Error Token A""",75))


    '''orther testcase'''
    def test_block_comment(self):
        self.assertTrue(TestLexer.checkLexeme("""** This is a\n* multi-line\n* comment.\n**""","<EOF>",76))
    def test_comment6(self):
        self.assertTrue(TestLexer.checkLexeme("""**Var x: XD =))****""","Unterminated Comment",77))

    def test_keyword6(self):
        self.assertTrue(TestLexer.checkLexeme("""= . =""", "=,.,=,<EOF>", 78))



    def test_float11(self):
        self.assertTrue(TestLexer.checkLexeme("""0X92.22""","0X92,.,22,<EOF>",79))
    def test_float12(self):
        self.assertTrue(TestLexer.checkLexeme("""0x8e-6""","0x8,e,-,6,<EOF>",80))



 

    def test_1(self):
        self.assertTrue(TestLexer.checkLexeme("""If(t!=22)\n Then:x++;""","""If,(,t,!=,22,),Then,:,x,+,+,;,<EOF>""",81))
    def test_2(self):
        self.assertTrue(TestLexer.checkLexeme("""ho \\t thien\\n long""","""ho,\,t,thien,\,n,long,<EOF>""",82))
    def test_3(self):
        self.assertTrue(TestLexer.checkLexeme("""Var: a[] ;""","""Var,:,a,[,],;,<EOF>""",83))
    def test_4(self):
        self.assertTrue(TestLexer.checkLexeme("""\\c298 p $#$%@"45a-*7e1""","""\,c298,p,Error Token $""",84))
    def test_5(self):
        self.assertTrue(TestLexer.checkLexeme("""thienlong460@gmail.com""","""thienlong460,Error Token @""",85))
    def test_6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Nam <EOF> mo" ""","""Nam <EOF> mo,<EOF>""",86))
    def test_7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Var": a[2] = {}, b = ;""","""Var,:,a,[,2,],=,{,},,,b,=,;,<EOF>""",87))
    def test_8(self):
        self.assertTrue(TestLexer.checkLexeme("""Function: borrow\nParameter: n\nBody:\nfuho(2) ;\nEndBody. """,
                                              """Function,:,borrow,Parameter,:,n,Body,:,fuho,(,2,),;,EndBody,.,<EOF>""",88))
    def test_9(self):
        self.assertTrue(TestLexer.checkLexeme("""array[3][3] = foo(2 + nested_exp(5) - 3, ((3)));""",
                                              """array,[,3,],[,3,],=,foo,(,2,+,nested_exp,(,5,),-,3,,,(,(,3,),),),;,<EOF>""",89))
    def test_10(self):
        self.assertTrue(TestLexer.checkLexeme(""" a = (1+2)<4;\ba = -1; \fb = -0XAF;\rc = -1.e3;""",
                                              """a,=,(,1,+,2,),<,4,;,Error Token \b""",90))
    def test_11(self):
        self.assertTrue(TestLexer.checkLexeme(""" a = (1+2)<4;\ba = -1; \fb = -0XAF;\rc = -1.e3;""",
                                              """a,=,(,1,+,2,),<,4,;,Error Token \b""",91))
    def test_12(self):
        self.assertTrue(TestLexer.checkLexeme("""Function: borrow
                                                    Parameter: n
                                                    Body:
                                                        fuho(2) ;
                                                    EndBody.""","""Function,:,borrow,Parameter,:,n,Body,:,fuho,(,2,),;,EndBody,.,<EOF>""",92))
    def test_13(self):
        self.assertTrue(TestLexer.checkLexeme("""Function: body
                                                    Body:
                                                        a[3] = arr[b[2][3]] + 4;
                                                    EndBody.""","""Function,:,body,Body,:,a,[,3,],=,arr,[,b,[,2,],[,3,],],+,4,;,EndBody,.,<EOF>""",93))
    def test_14(self):
        self.assertTrue(TestLexer.checkLexeme("""Var: a = 2 ; Var: b[3][3] = {foo(0905)};""","""Var,:,a,=,2,;,Var,:,b,[,3,],[,3,],=,{,foo,(,0,905,),},;,<EOF>""",94))
    def test_15(self):
        self.assertTrue(TestLexer.checkLexeme("""Var: b = 001;""","""Var,:,b,=,0,0,1,;,<EOF>""",95))
    def test_16(self):
        self.assertTrue(TestLexer.checkLexeme("""Function: hamso
                                                    Body:
                                                        x = a[b[c[d]]];
                                                    EndBody.""","""Function,:,hamso,Body,:,x,=,a,[,b,[,c,[,d,],],],;,EndBody,.,<EOF>""",96))

    def test_17(self):
        self.assertTrue(TestLexer.checkLexeme("""f = func(2.2,3) ;
                                                    Var: r = 10., v;
                                                    v = (4. \. 3.) *. 3.14 *. r *. r *. r;""",
                                                    """f,=,func,(,2.2,,,3,),;,Var,:,r,=,10.,,,v,;,v,=,(,4.,\.,3.,),*.,3.14,*.,r,*.,r,*.,r,;,<EOF>""",97))

    def test_18(self):
        self.assertTrue(TestLexer.checkLexeme("""Var: x;
                                                Function: fact
                                                Parameter:  arr[], x
                                                Body:""","""Var,:,x,;,Function,:,fact,Parameter,:,arr,[,],,,x,Body,:,<EOF>""",98))
    def test_19(self):
        self.assertTrue(TestLexer.checkLexeme("""Error on line 1 col 1: Body""","""Error Token E""",99))

    def test_boolean(self): #nên đặt mấy từ khóa lên trên tránh bị id cover
        self.assertTrue(TestLexer.checkLexeme("""tTruecc False""","tTruecc,False,<EOF>",100))


