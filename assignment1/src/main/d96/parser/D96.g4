grammar D96;
// Student ID: 1952588 - Le Duc Cam
@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}
program : (class_decl)+ EOF;
				
					/* Parser - Recognizer */


	// class decleration
class_decl: CLASS identifier (COLON identifier)? LCB member_list* destructor? member_list* RCB ;
member_list: attribute_decl | method_decl | constructor  ;


	// attribute decleration
attribute_decl: attribute_decl_1 | attribute_decl_2;

attribute_decl_1: (VAL|VAR) identifier (COMMA identifier)* COLON data_types  SEMI; // var a,b : Int ; // var a: Array[Int, 5]; // non nullable		

attribute_decl_2: (VAL|VAR) attribute_testing SEMI;  // var a : float = 2.1*3.0; // var a,b :Int = 2,3;
attribute_testing : (identifier COLON data_types ASSIGN expr) | (identifier COMMA attribute_testing (COMMA expr));
 // a,b,c:int = 2*3 , 2,3;

	// method decleration
method_decl: identifier LP parameter_list? RP block_statement ;   // get (){} 
parameter_list: parameter (SEMI parameter)*  ;   // nullable
parameter: identifier (COMMA identifier)* COLON data_types; // set(a,b:Int ; b:Array[Int,5] ){}

constructor : CONSTRUCTOR LP (parameter_list)? RP block_statement; 
destructor  : DESTRUCTOR LP RP block_statement;

	// block of statements 
block_statement: LCB statement* RCB ; // nullable list of statement
statement:
	  var_const_decl_statement | assign_statement 
	| if_statement | for_statement | break_statement 
	| continue_statement | return_statement | method_invocate_statement;

var_const_decl_statement 	: var_const_decl_1 | var_const_decl_2; // name should not follow the dollar identifier 
assign_statement 			: expr (ASSIGN expr)+ SEMI;   // a = 5*4+3;
if_statement 				: IF LP  expr RP block_statement (ELSEIF LP expr RP block_statement)* (ELSE block_statement)? ;
for_statement 				: FOREACH LP ID IN expr DOUBLEDOT expr (BY expr)? RP block_statement;
break_statement 			: BREAK SEMI; // Break;
continue_statement 			: CONTINUE SEMI; // Continue;
return_statement 			: RETURN expr? SEMI; // Return expr ;
// method_invocate_statement	: instance_call | static_call ;
// instance_call:(expr_7) DOT ID LP (expr (COMMA expr)* )? RP SEMI ;
// static_call: (expr_8 ) STATIC_GLOBAL_DOT DOLLAR_ID LP (expr (COMMA expr)* )? RP SEMI;
method_invocate_statement	: instance_method_invocate | static_method_invocate ;
method_invocate_expression	: instance_method_invocate | static_method_invocate ;
instance_method_invocate : expr_7* DOT ID LP (expr (COMMA expr)* )? RP SEMI?;
static_method_invocate   : expr_8* STATIC_GLOBAL_DOT DOLLAR_ID LP (expr (COMMA expr)* )? RP SEMI?;
// (identifier | SELF)
attribute_access: instance_attribute_access | static_attribute_access ;
instance_attribute_access: expr DOT ID  ; // Shape.length   ( identifier | SELF | ((ID|DOLLAR_ID)index_id)) 
static_attribute_access	 : (identifier | SELF | ((ID|DOLLAR_ID)index_id)) STATIC_GLOBAL_DOT DOLLAR_ID; // Shape :: Y 

var_const_decl_1 : (VAR|VAL) ID (COMMA ID )* COLON data_types SEMI; // var a: Array[Int, 7];
var_const_decl_2 : (VAR|VAL) var_const_testing SEMI ;    // var a : float = 2.7*7.2; // var a,b :Int = 2,7;
var_const_testing: ((ID COLON data_types ASSIGN expr) | (ID COMMA var_const_testing (COMMA expr))); 


data_types: primitive_types | array_type | class_type;

primitive_types: INT_TYPE | FLOAT_TYPE | STRING_TYPE | BOOLEAN_TYPE; //var a: Int;
array_type: ARRAY LSB (primitive_types | array_type | class_type) COMMA NATURAL  RSB; //var a: Array[Int, 5];
class_type: ID;
class_new_object: NEW ID LP (expr (COMMA expr)* )? RP ;  //var a: Shape =  New Shape(5+2);


	// literal
literals: (NATURAL | INTEGER_LIERAL | FLOAT_LITERAL  | BOOLEAN_LITERAL | STRING_LITERAL ) ;

identifier: (ID | DOLLAR_ID );
index_id:  (LSB expr RSB)+; // $a[0]


expr   : expr_1 (STRING_CONCATE | STRING_COMPARE) expr_1 | expr_1 ; //binary, infix, none-associate
expr_1 : expr_2 (EQUAL | NOT_EQUAL | LESS_THAN | GREATER_THAN | LESS_THAN_EQUAL | GREATER_THAN_EQUAL ) expr_2 | expr_2; // binary, infix, none-associate
expr_2 : expr_2 (AND|OR) expr_3 | expr_3 ; 	// binary, infix, left-associate
expr_3 : expr_3 (ADD|SUB) expr_4 | expr_4 ; 	// binary, infix, left-associate
expr_4 : expr_4 (MUL|DIV|MOD) expr_5 | expr_5; 	// binary, infix, left-associate
expr_5 : NOT expr_5| expr_6; 	// unary, prefix, right-associate
expr_6 : SUB expr_6| expr_7; 	// unary, prefix, right-associate
expr_7 : expr_7 index_id | expr_8 ; 	// unary, posfix, left-associate
expr_8 : expr_8 DOT  expr_9 | expr_9; 	//binary, infix, left-associate
expr_9 : expr_10 STATIC_GLOBAL_DOT expr_10 | expr_10; //binary, infix, left-associate
expr_10: NEW expr_10   | expr_11 ; 	//unary, prefix, right-associate
expr_11: literals | method_invocate_expression  |SELF  |((ID|DOLLAR_ID)index_id) | indexed_array  |  NULL | class_new_object | identifier  |(LP expr RP) ; 		//|const | variable | data_returned; 
// check here  LP (expr (COMMA expr)*)* RP   

	// Ar( Ar( Ar() ) , Ar( Ar(1,2), Ar(2,3)  )   Ar(1,2,3) Ar( Ar( Ar(2),Ar(3) ) , Ar(1,2)) 
multi_dimensional_arrays: (indexed_array (COMMA indexed_array)*) | (ARRAY LP multi_dimensional_arrays (COMMA multi_dimensional_arrays)* RP )  ;
indexed_array : ARRAY LP expr (COMMA expr)* RP;




				/*  Lexers Declaration  */

	// Literal
BOOLEAN_LITERAL: TRUE | FALSE;
NATURAL: [1-9][0-9]*;
INTEGER_LIERAL :
	DECIMAL 		{self.text=self.text.replace("_","")}
	| OCTAL 		{self.text=self.text.replace("_","")}
	| HEXADECIMAL 	{self.text=self.text.replace("_","")}
	| BINARY 		{self.text=self.text.replace("_","")}
	;

DECIMAL     : [0] |  ([1-9] ( [0-9] | '_'[0-9] )* ) ;
BINARY      : [0][bB] ( ([1] ('_'[01] | [01])*) | [0] ); 
OCTAL       : [0] ( [1-7] ( [0-7] | ('_'[0-7]))* | [0]);
HEXADECIMAL : [0][xX] ( [1-9A-F]  ('_'[0-9A-F] | [0-9A-F])*  | [0]);


fragment INTEGER_PART: [0] | ( [1-9] ( '_'[0-9] | [0-9] )* )  ;
fragment EXPONENT_PART: [eE][-+]? [0-9]+;
fragment DECIMAL_PART: DOT [0-9]* ;

FLOAT_LITERAL   
 	:	INTEGER_PART  DECIMAL_PART EXPONENT_PART?  {self.text=self.text.replace("_","")}   	  
	|	INTEGER_PART?   DECIMAL_PART EXPONENT_PART {self.text=self.text.replace("_","")}      			
	|	INTEGER_PART DECIMAL_PART? EXPONENT_PART 	{self.text=self.text.replace("_","")}	
;

STRING_LITERAL   : DQUOTE ( (ESCCHAR | STRCHAR)*) DQUOTE {self.text=self.text[1:-1]}; // [1:-1]
fragment DQUOTE  : '"';
fragment STRCHAR : ~[\\'"];
fragment ESCCHAR : (('\\b')|('\\f')|('\\r')|('\\n')|('\\t')|('\\\'')|('\\\\')|('\'"')); // \b \f \r \n \t ' \\ '"
fragment ILLESC  : ('\\' ~[bfrnt\\']) | ('\'' ~["]);

	// Characters Set
WS: [ \t\b\r\n\f]+ -> skip; // skip spaces, tabs, newlines, form feed
 
	// Comments  -- check 
BLOCK_COMMENT: (('##' .*? '##') | ('##' ~['##']* )) -> skip ;
// non-greedy, stops after the first match , ex: /* ... */ is ok but /* */*/ isn't

	// Types: (have not modified)
INT_TYPE	: 'Int';
VOID_TYPE	: 'Void';
FLOAT_TYPE	: 'Float';
STRING_TYPE	: 'String';
BOOLEAN_TYPE: 'Boolean';

	// Keywords: 
RETURN  	: 'Return';
BREAK   	: 'Break';
CONTINUE	: 'Continue';
IF			: 'If';
ELSEIF  	: 'Elseif';
ELSE    	: 'Else';
FOREACH 	: 'Foreach';
TRUE		: 'True';
FALSE		: 'False';
ARRAY   	: 'Array';
IN      	: 'In';
NULL		: 'Null';
CLASS   	: 'Class';
VAL			: 'Val';
VAR			: 'Var';
CONSTRUCTOR : 'Constructor';
DESTRUCTOR  : 'Destructor';
NEW			: 'New';
BY			: 'By';
SELF        : 'Self';
// WRITELN     :'WriteLn';

	// Operators:
ADD			 		: '+';
SUB			 		: '-';
MUL			 		: '*';
DIV			 		: '/';
MOD		 	 		: '%';
NOT			 		: '!';
AND			 		: '&&';
OR			 		: '||';
EQUAL		 		: '==';
ASSIGN		 		: '=';
NOT_EQUAL	 		: '!=';
LESS_THAN     		: '<';
LESS_THAN_EQUAL		: '<=';
GREATER_THAN  		: '>';
GREATER_THAN_EQUAL  : '>=';
STRING_CONCATE		: '+.';
STRING_COMPARE		: '==.';
STATIC_GLOBAL_DOT 	: '::';

	// Seperators:
LP		 : '('; // Left Parenthesis
RP		 : ')'; // Right Parenthesis
LSB		 : '['; // Left Square Bracket
RSB		 : ']'; // Right Square Bracket
LCB		 : '{'; // Left Curly Bracket
RCB		 : '}'; // Right Curly Bracket
DOT		 : '.'; // dot
DOUBLEDOT: '..'; // dot dot
COMMA	 : ','; // comma
SEMI	 : ';'; // semicolon
COLON	 : ':'; // colon

	// Identifiers:  //  python use intepreter
ID:  [_A-Za-z][_A-Za-z0-9]*; // modified
DOLLAR_ID: [$] [_A-Za-z0-9]+; // $, letters, underscores, digits




				/*  Lexical Errors */

UNCLOSE_STRING	: DQUOTE (ESCCHAR | STRCHAR)* EOF {raise UncloseString(self.text[1:])};
ILLEGAL_ESCAPE	: DQUOTE ((ESCCHAR | STRCHAR)*? ILLESC ) {raise IllegalEscape(self.text[1:])};
ERROR_CHAR: .{raise ErrorToken(self.text)};
