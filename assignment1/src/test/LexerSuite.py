import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_lower_uper(self):
        self.assertTrue(TestLexer.test("aAaA bBbB", "aAaA,bBbB,<EOF>", 100))

    def test_identifier1(self):
        self.assertTrue(TestLexer.test("id1 id2 id3 literal something","id1,id2,id3,literal,something,<EOF>",101))

    def test_identifier2(self):
        self.assertTrue(TestLexer.test("_id1 i_d2 __id3  abc_1_1_2 abc_2_4_33__4 cc6cc9_6969","_id1,i_d2,__id3,abc_1_1_2,abc_2_4_33__4,cc6cc9_6969,<EOF>",102))

    def test_identifier3(self):
        self.assertTrue(TestLexer.test("ID1 ID2ID2ID2 ID_3id3 id4ID4","ID1,ID2ID2ID2,ID_3id3,id4ID4,<EOF>",103))

    def test_identifier4(self):
        self.assertTrue(TestLexer.test("_____","_____,<EOF>",104)) 
    
    def test_identifier5(self):
        self.assertTrue(TestLexer.test("$staticFunction $staticVar","$staticFunction,$staticVar,<EOF>",105))  
    
    def test_identifier6(self):
        self.assertTrue(TestLexer.test("$_____id1 $id_2_ID2__Id2","$_____id1,$id_2_ID2__Id2,<EOF>",106))
    
    def test_identifier7(self):
        self.assertTrue(TestLexer.test("$dfa_sdf $$aaaaaa","$dfa_sdf,Error Token $",107)) 

    def test_identifier8(self):
        self.assertTrue(TestLexer.test("$6969_6969","$6969_6969,<EOF>",108)) 

    def test_identifier9(self):
        self.assertTrue(TestLexer.test("$_____ $5 $27_cc","$_____,$5,$27_cc,<EOF>",109)) 
    
    def test_identifier10(self):
        self.assertTrue(TestLexer.test("$a?","$a,Error Token ?",110)) 

    def test_separator(self):
        self.assertTrue(TestLexer.test("() [] . , ; : {}","(,),[,],.,,,;,:,{,},<EOF>",111))
   
    def test_octal1(self):
        self.assertTrue(TestLexer.test("001","00,1,<EOF>",112))

    def test_octal2(self):
        self.assertTrue(TestLexer.test("0123456789","01234567,89,<EOF>",113))
    
    def test_octal3(self):
        self.assertTrue(TestLexer.test("00000012345678999","00,00,00,12345678999,<EOF>",114))

    def test_octal4(self):
        self.assertTrue(TestLexer.test("0123__456__789","0123,__456__789,<EOF>",115))
    
    def test_octal5(self):
        self.assertTrue(TestLexer.test("01_23_456_78_9","01234567,89,<EOF>",116))
    
    def test_binary1(self):
        self.assertTrue(TestLexer.test("0b0 0B0 0b00 0b01 0b0012","0b0,0B0,0b0,0,0b0,1,0b0,012,<EOF>",117))

    def test_binary2(self):
        self.assertTrue(TestLexer.test("0b10101 0b03","0b10101,0b0,3,<EOF>",118))

    def test_binary3(self):
        self.assertTrue(TestLexer.test("0b111_00_111 0b1_1_1_1_1","0b11100111,0b11111,<EOF>",119))
    
    def test_binary4(self):
        self.assertTrue(TestLexer.test("0b_1110101","0,b_1110101,<EOF>",120))

    def test_binary5(self):
        self.assertTrue(TestLexer.test("0b1_00_0_000_0_0_0_","0b1000000000,_,<EOF>",121)) 

    def test_hexa_decimal1(self):
        self.assertTrue(TestLexer.test("0x111111 0X12345","0x111111,0X12345,<EOF>",122))    

    def test_hexa_decimal2(self):
        self.assertTrue(TestLexer.test("0xAbCd 0xFFff","0xA,bCd,0xFF,ff,<EOF>",123))
    
    def test_hexa_decimal3(self):
        self.assertTrue(TestLexer.test("0x0 0X01 0xABCD00000","0x0,0X0,1,0xABCD00000,<EOF>",124))      

    def test_hexa_decimal4(self):
        self.assertTrue(TestLexer.test("0xA_B_C_D1_2_3_4_5_6_7_8_9 0xA_BC_D00_000","0xABCD123456789,0xABCD00000,<EOF>",125))      

    def test_hexa_decimal5(self):
        self.assertTrue(TestLexer.test("0xABC123JKL","0xABC123,JKL,<EOF>",126)) 

    def test_decimal1(self):
        self.assertTrue(TestLexer.test("0 1 2 3 4 5 6 7 8 9 10 11","0,1,2,3,4,5,6,7,8,9,10,11,<EOF>",127)) 

    def test_decimal2(self):
        self.assertTrue(TestLexer.test("123 789 10000","123,789,10000,<EOF>",128))

    def test_decimal3(self):
        self.assertTrue(TestLexer.test("123_456_78_9 9_8_7_6_5_4_3_2_1","123456789,987654321,<EOF>",129))     

    def test_decimal4(self):
        self.assertTrue(TestLexer.test("_12_3_456_789_","_12_3_456_789_,<EOF>",130)) 

    def test_decimal5(self):
        self.assertTrue(TestLexer.test("123_456__78910","123456,__78910,<EOF>",131)) 

    def test_boolean(self):
        self.assertTrue(TestLexer.test("True False TRUE FaLse true","True,False,TRUE,FaLse,true,<EOF>",132)) #first 2 is bool the rest is id

    def test_float_1(self):
        self.assertTrue(TestLexer.test("0.2732001  273.273","0.2732001,273.273,<EOF>",133))
    
    def test_float_2(self):
        self.assertTrue(TestLexer.test("0.1 0.01  0.001 0.0001","0.1,0.01,0.001,0.0001,<EOF>",134))

    def test_float_3(self):
        self.assertTrue(TestLexer.test("000000.000","00,00,00,.,00,0,<EOF>",135))

    def test_float_4(self):
        self.assertTrue(TestLexer.test("273.000 1. 0.","273.000,1.,0.,<EOF>",136))

    def test_float_5(self):
        self.assertTrue(TestLexer.test(".7_3_7 .735 ",".,737,.,735,<EOF>",137))

    def test_float_6(self):
        self.assertTrue(TestLexer.test(".1e5 .1e+6 .0e-9 ",".1e5,.1e+6,.0e-9,<EOF>",138))

    def test_float_7(self):
        self.assertTrue(TestLexer.test(".2e10 .0002e+1 .20001E-27",".2e10,.0002e+1,.20001E-27,<EOF>",139))

    def test_float_8(self):
        self.assertTrue(TestLexer.test("123_456.e7  1_2_3_4_5.12e-99 1_0.001e-100","123456.e7,12345.12e-99,10.001e-100,<EOF>",140))

    def test_float_9(self):
        self.assertTrue(TestLexer.test("1_2_3.e","123.,e,<EOF>",141))

    def test_float_10(self):
        self.assertTrue(TestLexer.test("0_1_2_3.e","0,_1_2_3,.,e,<EOF>",142))
    
    def test_float_11(self):
        self.assertTrue(TestLexer.test(".E00b52 1_234.567_789e246_357", ".E00,b52,1234.567,_789e246_357,<EOF>", 143))
    
    def test_float_12(self):
        self.assertTrue(TestLexer.test(".e000X01ABCD", ".e000,X01ABCD,<EOF>", 144))
    
    def test_float13(self):
        self.assertTrue(TestLexer.test(".123e-45 .001E5",".123e-45,.001E5,<EOF>",145))
  
    def test_float14(self):
        self.assertTrue(TestLexer.test("1_2_3_4.e567 123e456", "1234.e567,123e456,<EOF>", 146))
    
    def test_float15(self):
        self.assertTrue(TestLexer.test("1_2_3_4.e5_6_7 1__2e3", "1234.e5,_6_7,1,__2e3,<EOF>", 147))

    def test_string_1(self):
        self.assertTrue(TestLexer.test("\"\"", ",<EOF>", 148))

    def test_string_2(self):
        self.assertTrue(TestLexer.test("\"normal string\"", "normal string,<EOF>", 149))

    def test_string_3(self):
        self.assertTrue(TestLexer.test("\" string with a space at head\"", " string with a space at head,<EOF>", 150))

    def test_string_4(self):
        self.assertTrue(TestLexer.test("\"cam say : if I ?\"\"", "cam say : if I ?,Unclosed String: ", 151))

    def test_string_5(self):
        self.assertTrue(TestLexer.test("\"he asked me : '\"Where is the book ?!?!'\" \"", "he asked me : '\"Where is the book ?!?!'\" ,<EOF>", 152))

    def test_string_6(self):
        self.assertTrue(TestLexer.test("\"string with escpape char : \\b \\f \\r \\n \\t \\\\ \\'\"", "string with escpape char : \\b \\f \\r \\n \\t \\\\ \\',<EOF>", 153))

    def test_string_7(self):
        self.assertTrue(TestLexer.test("\"some more escpape char: \\b \\f \\r \\n \\t \\\\ \\'\"", "some more escpape char: \\b \\f \\r \\n \\t \\\\ \\',<EOF>", 154))

    def test_string_8(self):
        self.assertTrue(TestLexer.test("\"\\n \\' newline infront\"", "\\n \\' newline infront,<EOF>", 155))

    def test_string_9(self):
        self.assertTrue(TestLexer.test("\"'\" some thing here\\n \\n \\t'\" some thing here\"", "'\" some thing here\\n \\n \\t'\" some thing here,<EOF>", 156))

    def test_string_10(self):
        self.assertTrue(TestLexer.test("\"1st string\" \"2nd string \\t \\n\" \"3rd string \\t\\n\\b \"", "1st string,2nd string \\t \\n,3rd string \\t\\n\\b ,<EOF>", 157))
    
    def test_string_11(self):
        self.assertTrue(TestLexer.test("\"....???!!!!!+-/*&^%$#@\" ", "....???!!!!!+-/*&^%$#@,<EOF>", 158))

    def test_string12(self):
        self.assertTrue(TestLexer.test("\"cau ca co con cho can cacao \"", "cau ca co con cho can cacao ,<EOF>", 159))
    
    def test_string13(self):
        self.assertTrue(TestLexer.test("\"", "Unclosed String: ", 160))

    def test_string14(self):
        self.assertTrue(TestLexer.test("\"\\n \\t", "Unclosed String: \\n \\t", 161))

    def test_string15(self):
        self.assertTrue(TestLexer.test("\"This '\" string '\" is \"  \"unclosed","This '\" string '\" is ,Unclosed String: unclosed", 162))

    def test_string16(self):
        self.assertTrue(TestLexer.test("\" not close '\" '\" \\b\\b\\b\\b", "Unclosed String:  not close '\" '\" \\b\\b\\b\\b", 163))

    def test_operator1(self):
        self.assertTrue(TestLexer.test("||||::&&", "||,||,::,&&,<EOF>", 164))    

    def test_operator2(self):
        self.assertTrue(TestLexer.test("!===!!=", "!=,==,!,!=,<EOF>", 165)) 

    def test_operator3(self):
        self.assertTrue(TestLexer.test("!=!!!!=", "!=,!,!,!,!=,<EOF>", 166)) 

    def test_operator4(self):
        self.assertTrue(TestLexer.test("+ - * / % ++", "+,-,*,/,%,+,+,<EOF>", 167)) 

    def test_operator5(self):
        self.assertTrue(TestLexer.test("=== != > >= < <=", "==,=,!=,>,>=,<,<=,<EOF>", 168)) 

    def test_operator6(self):
        self.assertTrue(TestLexer.test("+..==.", "+.,.,==.,<EOF>", 169))

    def test_operator7(self):
        self.assertTrue(TestLexer.test("&&&", "&&,Error Token &", 170))

    def test_operator8(self):
        self.assertTrue(TestLexer.test("-273", "-,273,<EOF>", 171))   

    def test_operator9(self):
        self.assertTrue(TestLexer.test("-01239xASDFGH", "-,0123,9,xASDFGH,<EOF>", 172))

    def test_operator10(self):
        self.assertTrue(TestLexer.test("## block_comment_here ##", "<EOF>", 173))

    def test_operator11(self):
        self.assertTrue(TestLexer.test("## block_end", "<EOF>", 174))
    
    def test_operator12(self):
        self.assertTrue(TestLexer.test("####abc##", "abc,<EOF>", 175))
    
    def test_operator13(self):
        self.assertTrue(TestLexer.test("...", "..,.,<EOF>", 176))
    
    def test_operator14(self):
        self.assertTrue(TestLexer.test("######", "<EOF>", 177))
    
    def test_operator15(self):
        self.assertTrue(TestLexer.test("##.#.#.#", "Error Token #", 178))

    def test_operator16(self):
        self.assertTrue(TestLexer.test(":::", "::,:,<EOF>", 179))
    
    def test_operator17(self):
        self.assertTrue(TestLexer.test("?", "Error Token ?", 180))
    
    def test_type1(self):
        self.assertTrue(TestLexer.test("Int INT int", "Int,INT,int,<EOF>", 181))
    
    def test_type2(self):
        self.assertTrue(TestLexer.test("Float FLOAT float", "Float,FLOAT,float,<EOF>", 182))
    
    def test_type3(self):
        self.assertTrue(TestLexer.test("String STRING string", "String,STRING,string,<EOF>", 183))
    
    def test_type4(self):
        self.assertTrue(TestLexer.test("Boolean BOOLEAN boolean", "Boolean,BOOLEAN,boolean,<EOF>", 184))
    
    def test_type5(self):
        self.assertTrue(TestLexer.test("Float a = 2.73", "Float,a,=,2.73,<EOF>", 185))
    
    def test_keyword1(self):
        self.assertTrue(TestLexer.test("If Elseif Else", "If,Elseif,Else,<EOF>", 186))

    def test_keyword2(self):
        self.assertTrue(TestLexer.test("Foreach Break Continue In", "Foreach,Break,Continue,In,<EOF>", 187))

    def test_keyword3(self):
        self.assertTrue(TestLexer.test("Return Array New ", "Return,Array,New,<EOF>", 188))

    def test_keyword4(self):
        self.assertTrue(TestLexer.test("Class Val Var Self Null", "Class,Val,Var,Self,Null,<EOF>", 189))
    
    def test_keyword5(self):
        self.assertTrue(TestLexer.test("Constructor Destructor By", "Constructor,Destructor,By,<EOF>", 190))

    def test_everything1(self):
        self.assertTrue(TestLexer.test("Var a :Int", "Var,a,:,Int,<EOF>", 191))
    
    def test_everything2(self):
        self.assertTrue(TestLexer.test("Val b,c :String", "Val,b,,,c,:,String,<EOF>", 192))
    
    def test_illegal_escape0(self):
        self.assertTrue(TestLexer.test(" \"abc\\n\\abc\" ", "Illegal Escape In String: abc\\n\\a", 193))
    
    def test_illegal_escape1(self):
        self.assertTrue(TestLexer.test("\"\\\\\!\"", "Illegal Escape In String: \\\\\!", 194))
    
    def test_illegal_escape2(self):
        self.assertTrue(TestLexer.test("\"test EscSeq \\c  \'\"something here \'\" \"", "Illegal Escape In String: test EscSeq \\c", 195))
    
    def test_illegal_escape3(self):
        self.assertTrue(TestLexer.test("\"\\asdfghjkl\"", "Illegal Escape In String: \\a", 196))
    
    def test_illegal_escape4(self):
        self.assertTrue(TestLexer.test("\"\\\\ backslash \\\\ \\\' single quote \\z\"", "Illegal Escape In String: \\\\ backslash \\\\ \\\' single quote \\z", 197))
    
    def test_illegal_esc_5(self):
        self.assertTrue(TestLexer.test("\"Hey: '\" What\\'up? \\n \\n \\t \\j '\" \"", "Illegal Escape In String: Hey: '\" What\\'up? \\n \\n \\t \\j", 198))
    
    def test_illegal_esc_6(self):
        self.assertTrue(TestLexer.test("\"Wowy + '\" \\t \\b Karik '\" \\r \\=", "Illegal Escape In String: Wowy + '\" \\t \\b Karik '\" \\r \\=", 199))
    
    
    