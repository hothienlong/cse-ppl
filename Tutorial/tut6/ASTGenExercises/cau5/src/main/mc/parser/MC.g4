grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

program: vardecl+ EOF;

vardecl: mctype manyvar ;

mctype: INTTYPE | FLOATTYPE ;

manyvar: var (COMMA var)* ;

var: ID (LSB INTLIT RSB)? ;


FLOATTYPE: 'float'  ;

INTTYPE: 'int';

ID: [a-z]+;
 
COMMA: ',' ;

INTLIT: [0-9]+ ;

LSB : '[';

RSB : ']';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;