grammar BKIT;

@lexer::header {
from lexererr import *
}

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

program     : (var_dec | func_dec)* EOF ; 

var_dec     : TYPE id_list SM ;

func_dec    : TYPE ID param_dec func_body ;
param_dec   : LP (TYPE id_list (SM TYPE id_list)*)? RP ;
func_body   : LB (var_dec | stmt)* RB ;

stmt        : (assign_stmt | call_stmt | return_stmt) SM;
assign_stmt : ID EQ exp0 ;
call_stmt   : ID LP (exp0 (CM exp0)*)? RP ;
return_stmt : RETURN exp0 ;

exp0        : exp1 ADD exp0 | exp1 ;
exp1        : exp2 SUB exp2 | exp2 ;
exp2        : exp2 (MUL | DIV) exp3 | exp3 ;
exp3        : LP exp0 RP | INTLIT | FLOATIT | ID | call_stmt ;

TYPE        : INT | FLOAT ;

INT         : 'int' ;
FLOAT       : 'float' ;
RETURN      : 'return' ;

ID          : [_a-zA-Z][_a-zA-Z0-9]* ;
id_list     : ID (CM ID)* ;
INTLIT      : [1-9][0-9]* | '0' ;
FLOATIT     : INTLIT ('.'[0-9]+)? ([eE][-+]? [0-9]+)? ;
 
LB          : '{' ;
RB          : '}' ;
LP          : '(' ;
RP          : ')' ;

SM          : ';' ;
CM          : ',' ;

EQ          : '=' ;

ADD         : '+' ;
SUB         : '-' ;
MUL         : '*' ;
DIV         : '/' ;

WS          : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines



ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;