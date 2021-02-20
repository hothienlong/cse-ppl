lexer grammar BKIT;

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

//mục đích là tách các token phân biệt ra->xác định bn token, chưa cần phân loại
// program  : ;//luật cho parser

fragment LETTER: [a-z] ;
fragment DIGIT: [0-9] ;
fragment EXPONENT: '-'? [0-9]+ ;




// ID: LETTER (LETTER | DIGIT)*;

// REAL: [0-9]+ (('.' [0-9]*) | ([eE] '-'? [0-9]+) | ('.' [0-9]* [eE] '-'? [0-9]+)) ;

// REAL: ((DIGIT+ '.' DIGIT*) | (DIGIT* '.' DIGIT+)  ('E' EXPONENT)?)
//  | (DIGIT+ 'E' EXPONENT) ;

// ID: [a-z] [a-z0-9]* ;

// STRING: '\''  (~[']|('\'' '\''))*  '\'' ;

// SEMI: ';' ;

// COLON: ':' ;

// // UPPER: [A-Z] ;

// STRING: ['] (~['] | [']['])* ['] ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;

// //chuyển mode định nghĩa string
// LQUOTE : '\'' -> more, mode(STR) ;
// mode STR;
// STRING : '\'' -> mode(DEFAULT_MODE) ; // token we want parser to see
// TEXT : . -> more ; // collect more text for string
