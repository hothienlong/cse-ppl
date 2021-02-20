grammar BKIT;
//1812869
//chép toàn bộ vào phần đầu file
@lexer::header {
from lexererr import *
}

//chép toàn bộ vào phần thân file
@lexer::members {
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
}

options{
	language=Python3;
}


// ..........................................................................................................\\
// ..............................................PARSER.......................................................\\
// ..........................................................................................................\\
program: var_dec*  func_dec* EOF;

//-----variable declare
var_dec: VAR COLON var_list SEMI;

var_list: variable (COMMA variable)* ;

variable: non_initial | initial ;

non_initial: var_primitive | var_array ;

// var_type: var_primitive | var_array ;
var_primitive: IDENTIFIER ;

var_array: IDENTIFIER ('[' INTEGER_LITERAL ']')+ ;

initial:  var_primitive ASSIGN literal 
        | var_array ASSIGN literal 
        ;

//-----literal
literal
    : INTEGER_LITERAL
    | FLOAT_LITERAL
    | boolean_literal
    | STRING_LITERAL
    | array_literal
    ;

boolean_literal: TRUE | FALSE ;

array_literal: '{' (literal (',' literal)*)? '}' ;

//-----function declare
func_dec: FUNCTION COLON IDENTIFIER 
        (PARAMETER COLON var_list)? 
        BODY COLON list_stmt ENDBODY '.'
        ;


// ..............................................STATEMENT...................................................\\
list_vardec: var_dec* ;
list_stmt: list_vardec stmt* ;

stmt: assign_stmt
    | if_stmt
    | for_stmt
    | while_stmt 
    | do_while_stmt
    | break_stmt
    | continue_stmt
    | call_stmt
    | return_stmt
    ;


assign_stmt: var_primitive ASSIGN exp SEMI
           | index_exp ASSIGN exp  SEMI
           ;


if_stmt: IF exp THEN list_stmt
        (ELSEIF exp THEN list_stmt)*
        (ELSE list_stmt)?
        ENDIF DOT
        ;

for_stmt: FOR LP var_primitive ASSIGN exp COMMA exp COMMA exp RP DO
                list_stmt
          ENDFOR '.'
          ;

while_stmt: WHILE exp DO list_stmt ENDWHILE '.' ;

do_while_stmt: DO list_stmt WHILE exp ENDDO '.' ;

break_stmt: BREAK SEMI ;

continue_stmt: CONTINUE SEMI ;

call_stmt: func_call_exp SEMI ;

return_stmt: RETURN exp? SEMI ;




// ..............................................EXPRESSION..................................................\\
//exp là các biểu thức cho toán tử bên vế phải phép ASSIGN
//Array ko có operator -> ko có trong exp
exp: relational_exp ;

relational_exp
    : logical_binary_exp EQUAL logical_binary_exp  //True EQUAL True
    | logical_binary_exp NOT_EQUAL logical_binary_exp
    | logical_binary_exp LESS_THAN logical_binary_exp
    | logical_binary_exp GREATER_THAN logical_binary_exp
    | logical_binary_exp LESS_EQUAL logical_binary_exp
    | logical_binary_exp GREATER_EQUAL logical_binary_exp
    | logical_binary_exp NOT_EQUAL_FLOAT logical_binary_exp
    | logical_binary_exp LESS_THAN_FLOAT logical_binary_exp
    | logical_binary_exp LESS_EQUAL_FLOAT logical_binary_exp
    | logical_binary_exp GREATER_THAN_FLOAT logical_binary_exp
    | logical_binary_exp GREATER_EQUAL_FLOAT logical_binary_exp
    | logical_binary_exp
    ;

logical_binary_exp
    : logical_binary_exp AND adding_exp
    | logical_binary_exp OR adding_exp
    | adding_exp
    ;

adding_exp
    : adding_exp ADD_INT multiplying_exp  //nhân chia trước cộng trừ sau
    | adding_exp ADD_FLOAT multiplying_exp
    | adding_exp SUB_INT multiplying_exp
    | adding_exp SUB_FLOAT multiplying_exp
    | multiplying_exp
    ;

multiplying_exp
    : multiplying_exp MUL_INT logical_unary_exp
    | multiplying_exp MUL_FLOAT logical_unary_exp
    | multiplying_exp DIV_INT logical_unary_exp
    | multiplying_exp DIV_FLOAT logical_unary_exp
    | multiplying_exp INT_REMAINDER logical_unary_exp
    | logical_unary_exp
    ;

logical_unary_exp
    : NOT logical_unary_exp
    | sign_exp
    ;

sign_exp
    : SUB_INT sign_exp 
    | SUB_FLOAT sign_exp  
    | index_exp
    ;

//index và func phải gọi exp vì end_exp phải có '('exp')'
index_exp
    : operand ('[' exp ']')+ //muốn gọi biểu thức ko ()
    | operand
    ;
    //thay biểu thức 1 thành exp [exp]+ 
    //=> bị adding [exp], tức là 3+2[2] ko có dấu ngoặc
    //=>operand [exp]+


operand
    : IDENTIFIER
    | literal
    | func_call_exp
    | '(' exp ')' //exp này phải đc ưu tiên tính trước nên có () (biểu thức trong biểu thức: a=exp=>2-exp=>2-(3+4))
    ;


func_call_exp
    : IDENTIFIER '(' (exp (COMMA exp)*)? ')' 
    ;

// ..........................................................................................................\\
// ..............................................LEXER.......................................................\\
// ..........................................................................................................\\
/***************Keyword BKIT***************/
// KEYWORD
BODY: 'Body' ;
BREAK: 'Break' ;
CONTINUE: 'Continue' ;
DO: 'Do' ;
ELSE: 'Else' ;
ELSEIF: 'ElseIf' ;
ENDBODY: 'EndBody' ;
ENDIF: 'EndIf' ;
ENDFOR: 'EndFor' ;
ENDWHILE: 'EndWhile' ;
FOR: 'For' ;
FUNCTION: 'Function' ;
IF: 'If' ;
PARAMETER: 'Parameter' ;
RETURN: 'Return' ;
THEN: 'Then' ;
VAR: 'Var' ;
WHILE: 'While' ;
TRUE: 'True' ;
FALSE: 'False' ;
ENDDO: 'EndDo' ;



/***************Operator BKIT***************/
//-----standard operator 
ASSIGN: '=' ;
ADD_INT: '+' ;
ADD_FLOAT: '+.' ;
SUB_INT: '-' ;
SUB_FLOAT: '-.' ;
MUL_INT: '*' ;
MUL_FLOAT: '*.' ;
DIV_INT: '\\' ;
DIV_FLOAT: '\\.' ;
INT_REMAINDER: '%' ;

//-----boolean operator
NOT: '!' ;
AND: '&&' ;
OR: '||' ;

//-----relational operator
EQUAL: '==' ;
NOT_EQUAL: '!=' ;
LESS_THAN: '<' ;
GREATER_THAN: '>' ;
LESS_EQUAL: '<=' ;
GREATER_EQUAL: '>=' ;
NOT_EQUAL_FLOAT: '=/=' ;
LESS_THAN_FLOAT: '<.' ;
GREATER_THAN_FLOAT: '>.' ;
LESS_EQUAL_FLOAT: '<=.' ;
GREATER_EQUAL_FLOAT: '>=.' ;


/***************Separator BKIT***************/              
// SEPARATOR: ('(' | ')' | '[' | ']' | ':' | '.' | ',' | ';' | '{' | '}') ;
LP: '(' ;
RP: ')' ;
LSB: '[' ;
LRB: ']' ;
COLON: ':' ;
DOT: '.' ;
COMMA: ',' ;
SEMI: ';' ;
LB: '{' ;
RB: '}' ;


/***************Literal BKIT***************/ 

//-----integer 
fragment DEC: '0' | [1-9][0-9]* ;
fragment HEX: '0'[xX] [1-9A-F] [0-9A-F]* ;
fragment OCT: '0'[oO] [1-7] [0-7]* ;
INTEGER_LITERAL: DEC | HEX | OCT ;


//-----float//1.23e-4 (integer=1, decimal=.23, exponent=e-4)
fragment DIGIT: [0-9] ;
fragment EXPONENT: [eE] [+-]? DIGIT+ ;
FLOAT_LITERAL: ((DIGIT+ '.' DIGIT*)  EXPONENT?)
        | (DIGIT+  EXPONENT) ;
    





/***************String BKIT***************///đang tới trường hợp ko " trong string
fragment ESCAPE_SEQUENCES: ESCAPE_SEQUENCES_BACKSLASH | ESCAPE_SEQUENCES_SINGLEQUOTE ;//hợp lệ
fragment ESCAPE_SEQUENCES_BACKSLASH: '\\' [bfrnt'\\] ;
fragment ESCAPE_SEQUENCES_SINGLEQUOTE: ['] ["] ;
fragment POSTFIX_ESCAPE_SEQUENCES_BACKSLASH: [bfrnt'\\] ;
fragment POSTFIX_ESCAPE_SEQUENCES_SINGLEQUOTE: ["] ;
fragment NOT_POSTFIX_ESCAPE_SEQUENCES_BACKSLASH: ~[bfrnt'\\] ;
fragment NOT_POSTFIX_ESCAPE_SEQUENCES_SINGLEQUOTE: ~["] ;
fragment STRING_CHAR: ~["'\b\f\r\n\\] | ESCAPE_SEQUENCES ;
//có ' phải có " theo sau ko sẽ illegal vì có thể đứng trước " của string, ' đứng một mình là \'
STRING_LITERAL: '"' STRING_CHAR* '"' //
{
    #cắt từ 1->length-2
    self.text = self.text[1:-1]
};

UNCLOSE_STRING: '"' STRING_CHAR* (['\b\f\r\n\\] | EOF) //(ESCAPE_SEQUENCES | ~["'\\])*
{
    imposible = ["'",'\b','\f','\r','\n','\\']
    if(self.text[-1] in imposible): #EOF?
        raise UncloseString(self.text[1:-1])
    else:
        raise UncloseString(self.text[1:])
} ;//đã là string thì mới illegal in string

ILLEGAL_ESCAPE: '"' STRING_CHAR* (([\\] NOT_POSTFIX_ESCAPE_SEQUENCES_BACKSLASH?) | (['] NOT_POSTFIX_ESCAPE_SEQUENCES_SINGLEQUOTE?)) .*? '"'
{
		for x in range(len(self.text)):
			if self.text[x] == '\\':
	  			if (self.text[x+1] == 'b') or (self.text[x+1] == 'f') or (self.text[x+1] == 'r'):
				    continue
	  			elif (self.text[x+1] == 'n') or (self.text[x+1] == 't') or (self.text[x+1] == '\'') or (self.text[x+1] == '\\'):
				    continue
	  			elif (x+2)==(len(self.text)):
				    x=x-1
				    break
	  			else:
				    break
			elif self.text[x] == '\'':
	  			if(self.text[x+1] == '"'):
	  			    continue 
	  			elif (x+2)==(len(self.text)):
				    x=x-1
				    break
	  			else:
				    break                                      
		raise IllegalEscape(self.text[1:x+2])
} ;  //kết thúc bằng '



/***************Comment BKIT***************/
COMMENT: UNTERMINATED_COMMENT '**' -> skip;// .*? matches anything until the first **
UNTERMINATED_COMMENT: '**' .*?;


/*********Unmatch các trường hợp trên**********/
/***************Identifier BKIT***************/
fragment LETTER: [a-zA-Z] ;
IDENTIFIER:  [a-z](LETTER |'_' | [0-9])* ;

WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: .;

