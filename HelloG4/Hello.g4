// Define a grammar called Hello
grammar Hello;

ID : [a-z]+ ;             // match lower-case identifiers
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
start  : 'hello' ID+ ;         // match keyword hello followed by an identifier