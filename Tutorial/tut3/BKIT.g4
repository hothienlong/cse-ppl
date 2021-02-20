grammar BKIT;
// 1814771
@lexer::header {
from lexererr import *
}
options{
	language=Python3;
}
program: declaration* EOF;
declaration
    :   variable_declaration SM
    |   function_declaration
    |   statement SM
    ;
statement
    :   assignment
    |   call
    |   return_
    ;
variable_declaration
    :   type_  listid ;
type_: INT|FLOAT;
listid
    :   ID CM listid
    |   ID 
    ;
function_declaration
    :   type_ ID LP list_parameter RP LB body RB;
list_parameter
    :   variable_declaration (SM variable_declaration)*
    ;
body
    :   variable_declaration SM body
    |   statement SM body
    | 
    ;
assignment
    :   ID EQ expression
    ;
expression
    :   <assoc=left> expression (MUL|DIV) expression
    |   nonexpression SUB nonexpression
    |   <assoc=right> expression ADD expression
    |   operand
    ;
nonexpression
    :   <assoc=left> nonexpression (MUL|DIV) nonexpression
    |   <assoc=right> nonexpression ADD nonexpression
    |   operand
    ;
operand
    :   INTLIT 
    |   FLOATLIT
    |   ID
    |   call
    |   sub_expression
    ;
call
    :   ID LP list_expression RP
    ;
list_expression
    :   expression (CM expression)*
    ;
sub_expression
    :   LP expression RP
    ;
return_
    :   RETURN  expression
    ;
INT: 'int';
FLOAT: 'float';
RETURN: 'return';
LB: '{';
RB: '}';
SM: ';';
CM: ',';
EQ: '=';
LP: '(';
RP: ')';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
ID: [a-z][a-zA-Z_0-9]*;
WS : [ \t\r\n\f]+ -> skip ;
fragment DIGIT : [1-9][0-9]* | '0';
INTLIT
    :   DIGIT 
    ;

FLOATLIT
    :   DIGIT '.' [0-9]*
    |   DIGIT? '.' [0-9]+
    ;
