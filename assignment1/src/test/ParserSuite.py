import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    # def test0(self):
    #     input = """  Class first_class{ }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,200))

    # def test1(self):
    #     input = """  Class Program{ Val a:Int;}"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,201))
    
    # def test2(self):
    #     input = """  Class Program{
    #         main (){ }
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,202))

    # def test3(self):
    #     input = """ Class main {
    #         Var $num1 , num2 :  Int;
    #         Val num3 , $num4 : Float;
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,203))
    
    # def test4(self):
    #     input = """ Class main {
    #         Var $num1 , num2 :  Int = 2,3;
    #         Val num3 , $num4 : Float = 2. ,2.3;
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,204))
    
    # def test5(self):
    #     input = """ Class main {
    #         Val  true :  Boolean = True;
    #         Var false : Boolean = False;
    #         Val True : Boolean;
    #     }
    #     """
    #     expect = "Error on line 4 col 16: True"
    #     self.assertTrue(TestParser.test(input,expect,205))
    
    # def test6(self):
    #     input = """ Class main {
    #         Val  true :  Boolean = True;

    #     """
    #     expect = "Error on line 4 col 8: <EOF>"
    #     self.assertTrue(TestParser.test(input,expect,206))
    
    # def test7(self):
    #     input = """ Class Rectangle: Shape {
    #                 }
    #                 Class Program {
    #                 }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,207))
    
    # def test8(self):
    #     input = """ Class Rectangle: Shape {
    #                 };
    #                 Class Program {
    #                 }"""
    #     expect = "Error on line 2 col 21: ;"
    #     self.assertTrue(TestParser.test(input,expect,208))
    
    # def test9(self):
    #     input = """ Class Rectangle: Shape {
    #                 Class Program {
    #                 }"""
    #     expect = "Error on line 2 col 20: Class"
    #     self.assertTrue(TestParser.test(input,expect,209))
    
    # def test10(self):
    #     input = """ Class Rectangle: Shape {
    #                     function(){  }
    #                 }
    #                 Class Program {
    #                     doSomeThing(a:Int){ }
    #                 }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,210))
    
    # def test11(self):
    #     input = """ Class Rectangle: CC {
    #                     function(){ Return somthing; }
    #                 }
    #                 Class Program {
    #                     doSomeThing(a:Int){ a = 4+4; }
    #                 }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,211))

    # def test12(self):
    #     input = """ Class Rectangle: CC {
    #                     function(){ return wrongReturnKeyword; }
    #                 }
    #                 Class Program {
    #                     doSomeThing(a:Int){ a = 4+4; }
    #                 }"""
    #     expect = "Error on line 2 col 43: wrongReturnKeyword"
    #     self.assertTrue(TestParser.test(input,expect,212))

    # def test13(self):
    #     input = """ Class Rectangle: CC {
    #                     function(){ Return simpleExpresion; }
    #                 }
    #                 Class Program {
    #                     doSomeThing(a:Int){ 
    #                         a = 4+4; 
    #                         Return complexExpression * a + 5/6;
    #                     }
    #                 }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,213))

    # def test14(self):
    #     input = """ Class Rectangle: CC {
    #                     function(){ Return simpleExpresion; }
    #                 }
    #                 Class Program {
    #                     Var a,b : Int;
    #                     constructor( c:Int ){  
    #                         Self.a = Self.b = c;  
    #                     }
    #                 }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,214))
    
    # def test15(self):
    #     input = """ Class ProgramCC {
    #                     Var a,b : Int;
    #                     Constructor (){ 
    #                         Self.a = Self.b = 2 + 2;
    #                     }
    #                     Constructor( c:Int ){  
    #                         Self.a = Self.b = c;  
    #                     }
    #                 }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,215))
    
    # def test16(self):
    #     input = """ Class ProgramCC {
    #                     Var a,b : Int;
    #                     Constructor (){ 
    #                         Self.a = Self.b = 2 + 2;
    #                     }
    #                     Destructor( c:Int ){  
    #                         Self.a = Self.b = 0;  
    #                     }
    #                 }"""
    #     expect = "Error on line 6 col 36: c"
    #     self.assertTrue(TestParser.test(input,expect,216))
    
    # def test17(self):
    #     input = """ Class ProgramCC {
    #                     Var a,b : Int;
    #                     Constructor (){ 
    #                         Self.a = Self.b = 2 + 2;
    #                     }
    #                     Clear(){ 
    #                         Return notThing;
    #                     }
    #                     Destructor(){  
    #                         Self.callClear();  
    #                     }
    #                 }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,217))

    # def test18(self): 
    #     input = """ Class ProgramCC {
    #                     Var a,b : Int;
    #                     Clear(){ 
    #                         wrongClear(){ };
    #                         Return notThing;
    #                     }
    #                     Destructor(){  
    #                         Self.callClear();  
    #                     }
    #                 }"""
    #     expect = "Error on line 4 col 38: ("
    #     self.assertTrue(TestParser.test(input,expect,218))
    
    # def test19(self):  
    #     input = """ Class ProgramCC {
    #                     Var a,b : Int;
    #                     Clear(){ 
    #                         a=1------1+1--1;
    #                         Return notThing;
    #                     }
    #                     Destructor(){  
    #                         Self.callClear(3*3*3,3);  
    #                     }
    #                 }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,219))
    
    # def test20(self):
    #     input = """ Class Rectangle: Shape {
    #                     getArea() {
    #                         Val a : Shape = New Shape(3,4);  
    #                         b = c = d = e = 5 * 3 + 12 - 19 + 4;
    #                         Return Self.length * Self.width;
    #                     }
    #                     set(a,b:Float){
    #                         Self.length = a;
    #                         Self.width  = b;
    #                     }
    #                 }
    #             """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,220))

    # def test21(self): 
    #     input = """ Class A:  B {
    #                     set(a,b:Float){
    #                         Self.length = a;
    #                         Self.width  = b;
    #                         a.$foo();
    #                     }
    #                 }
    #             """
    #     expect = "Error on line 5 col 34: ("
    #     self.assertTrue(TestParser.test(input,expect,221))
    
    # def test22(self): 
    #     input = """ Class A:  B {
    #                     set(a,b:Float){
    #                         Self.length = a;
    #                         Self.width  = b;
    #                         a.foo();
    #                     }
    #                 }
    #             """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,222)) 
    
    
    
    # def test23(self):  # ??? Return New X().Y()
    #     input = """ Class Rec : Shape {
    #                     getArea() {
    #                         Return Self.length * Self.width;
    #                     }
    #                     func(){
    #                         Return New X(111111111111111111);
    #                     }
    #                 }
    #             """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,223))

    # def test24(self): 
    #     input = """ Class A:  B {
    #                     Var a: Array[Int,-1];
    #                 }
    #             """
    #     expect = "Error on line 2 col 41: -"
    #     self.assertTrue(TestParser.test(input,expect,224)) 
    
    # def test25(self): 
    #     input = """ Class A:  B {
    #                     Var a: Array[Int,0];
    #                 }
    #             """
    #     expect = "Error on line 2 col 41: 0"
    #     self.assertTrue(TestParser.test(input,expect,225)) 
    
    # def test26(self): 
    #     input = """ Class A:  B {
    #                     Var a: Array[Int,2];
    #                 }
    #             """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,226)) 

    # def test27(self):
    #     input = """ Class Rectangle: Shape {
    #                     getArea() {
    #                         Val a : New Shape(3,4);  
    #                         Return Self.length * Self.width;
    #                     }
    #                 }
    #             """
    #     expect = "Error on line 3 col 36: New"
    #     self.assertTrue(TestParser.test(input,expect,227))
    
    # def test28(self):
    #     input = """ Class Rectangle: Shape {
    #                     getArea() {
    #                         Val a,b : Shape ;
    #                         Return Self.length * Self.width;
    #                     }
    #                 }
    #             """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,228))
    
    # def test29(self):
    #     input = """ Class Rectangle: Shape {
    #                     getArea() {
    #                         Val a,b : Shape = New Shape(3,4), New Shape(2) ;
    #                         Return Self.length * Self.width;
    #                     }
    #                 }
    #             """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,229))
    
    # def test30(self):
    #     input = """ Class Rectangle: Shape {
    #                     getArea() {
    #                         Var $a,$s : Shape = New Shape(), New Shape(1) ;
    #                         Return Self.length * Self.width;
    #                     }
    #                 }
    #             """
    #     expect = "Error on line 3 col 32: $a"
    #     self.assertTrue(TestParser.test(input,expect,230))
    
    # def test31(self):
    #     input = """ Class main {
    #         Var $num1, $num2, $num3, $num4 :  Int;
    #         MyFunc(a,b : Int ; c : Float){
    #             Var num1, num2, num3, num4 :  Int = 123, 100 + 100,123 + 1299, 54 + 55;
    #             a[0] = Self.a; 
    #             If (2 > a[0] && (Self.num1 <= 1)) {
    #                a = 1;
    #             }
    #         }
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,231))
    
    # def test32(self):
    #     input = """ Class main {
    #         Var $num1, $num2, $num3, $num4 :  Float = 2. , 3.2 , 3e-4, .1e2;
    #         MyFunc(a,b : Int ; c : Float){
    #             Var num1, num2, num3, num4 :  Int = 123, 100 + 100,123 + 1299, 54 + 55;
    #             a[0] = Self.a; 
    #             If (2 > a[0] && (Self.num1 <= 1)) {
    #                a = 1;
    #             }
    #         }
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,232))

    # def test33(self):
    #     input = """  Class Arr{
    #         main (){
    #             Var a: Array[Array[Int,4],2] = Array(
    #                 Array(1,1), 
    #                 Array(2,7,3) 
    #             );
    #         }
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,233))

    # def test34(self):
    #     input = """  Class Arr{
    #         main (){
    #             Var a: Array[Array[Array[Int,1],2],2] = Array(
    #                 Array(Array(1), Array(1)),
    #                 Array(Array(1), Array(1))
    #             );
    #         }
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,234))
    
    # def test35(self):
    #     input = """  Class Arr{
    #         main (){
    #             Var a: Array[Array[Boolean,4],2] = Array(
    #                 Array(True,False), Array(True) 
    #             );
    #         }
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,235))
    
    # def test36(self):
    #     input = """  Class Arr{
    #         main (){
    #             Var a: Array[Array[String,4],2] = Array(
    #                 Array("a","b"), Array("c") 
    #             );
    #         }
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,236))
    
    # def test37(self):
    #     input = """  Class Arr{
    #         main (){
    #             Var a: Array[Array[Float,4],2] = Array(
    #                 Array(4.0,2.73), Array(.1e1) 
    #             );
    #         }
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,237))
    
    # def test38(self):
    #     input = """  Class Arr{
    #         main (){
    #             Var a : Shape = New Shape();
    #             a.width = 5;
    #         }
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,238))
    
    # def test39(self):
    #     input = """  Class Arr{
    #         main (){
    #             Var a : Shape = New Shape();
    #             a::$width = 5;
    #         }
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,239))
    
    # def test40(self):
    #     input = """  Class Arr{
    #         Var $a : Shape = New Shape();
    #         main (){
    #             b = $a::width ;
    #         }
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,240))



    # def test41(self):
    #     input = """Class Pro {
    #                 main() {
    #                     Var X,y,z : New Rec(1*2+1,5);
    #                 }
    #             }"""
    #     expect = "Error on line 3 col 36: New"
    #     self.assertTrue(TestParser.test(input,expect,241))
    
    # def test42(self):
    #     input = """Class Pro {
    #                 main() {
    #                     Var X,y : Rec =  New Rec(1*2+1,5), New Rec(1*2+1,5);
    #                 }
    #             }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,242))
    
    # def test43(self):
    #     input = """Class Pro {
    #                 main() {
    #                     Val X,y : Rec =  New Rec(1*2+1,5), New Rec(1*2+1,5);
    #                     X = New Y();
    #                 }
    #             }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,243))
    
    # def test44(self):
    #     input = """Class Pro {
    #                 main() {
    #                     Val X,y : Rec =  New Rec(1*2+1,5), New Rec(1*2+1,5);
    #                     A,s,d,F = New Y();
    #                 }
    #             }"""
    #     expect = "Error on line 4 col 25: ,"
    #     self.assertTrue(TestParser.test(input,expect,244))
    
    # def test45(self):
    #     input = """Class Pro {
    #                 main() {
    #                     Val X,y : Rec =  New Rec(1*2+1,5), New Rec(1*2+1,5);
    #                     A=s = New Y();
    #                 }
    #             }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,245))
    
    # def test46(self):
    #     input = """ Class Rectangle: Shape {
    #                     getArea() {
    #                         Var b : Array[Int,4];
    #                         a = b = 5*3 + 1-1+4;
    #                         b[1] = 1;
    #                         Return Self.length * Self.width;
    #                     }
    #                 }
    #             """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,246))
    
    # def test47(self):
    #     input = """ Class Rectangle: Shape {
    #                     getArea() {
    #                         Var a : Shape = New Shape(Array("string"), Array(1));
    #                         d[X] = 1;
    #                         Return a.length * Self.width;
    #                     }
    #                 }
    #             """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,247))
    
    # def test48(self):
    #     input = """ Class Rectangle: Shape {
    #                     getArea() {
    #                         Var a : Shape = New Shape(Array("string"), Array(1));
    #                         d[0X] = 1;
    #                         Return a.length * Self.width;
    #                     }
    #                 }
    #             """
    #     expect = "Error on line 4 col 31: X"
    #     self.assertTrue(TestParser.test(input,expect,248))
    
    # def test49(self):
    #     input = """ Class Rectangle: Shape {
    #                     getArea() {
    #                         Var a : Shape = New Shape(Array("string"), Array(1));
    #                         d[0X1] = 1;
    #                         Return a.length * Self.width;
    #                     }
    #                 }
    #             """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,249))
    
    # def test50(self):
    #     input = """ Class Rectangle: Shape {
    #                     getArea() {
    #                         Var a : Array[Array[Int,1],1] ;
    #                         d[0][1] = 1;
    #                         Return a.length * Self.width;
    #                     }
    #                 }
    #             """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,250))
    
    # def test51(self):
    #     input = """ Class Rectangle: Shape {
    #                     getArea() {
    #                         Var a : Array[Array[Int,1],1] ;
    #                         d[0][1][] = 1;
    #                         Return a.length * Self.width;
    #                     }
    #                 }
    #             """
    #     expect = "Error on line 4 col 36: ]"
    #     self.assertTrue(TestParser.test(input,expect,251))
    
    # def test52(self):
    #     input = """Class main {
    #         Var b: Array[Int, 273];
    #         Val n :Int = 0;
    #         Var $n1, $n2, $n3, $n4 :  Int = 123+123,11,22,33;
    #         MyFunc(a,b,c : Int ; d : Float){
    #            Var n1, n2, n3, n4 :  Int = 100 + 100,123 + 1299, 54 + 55,2;
    #            If (False && True && True){
    #                a = b;  
    #            }
    #            Elseif (True && False){
    #                a = b+4+5;
    #            }
    #            Elseif (2 && False || True){
    #                a = b+10;
    #             }
    #            Else{
    #                a = c = b+1*2;
    #                Foreach (i In 1 .. 273 By 3){
    #                     If(a >= (b+c) ){
    #                         Continue;
    #                     }
    #                     Elseif(a < (b+c) ){
    #                         a = b - 1; 
    #                         Break;
    #                     }
    #                     Else {
    #                         a = b * 2;
    #                         Return c*1/2+1+3;
    #                     }
    #                 } 
    #            }
    #         }
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,252))

    # def test53(self):
    #     input = """
    #     Class Shape {
    #         Val $numShape: Int = 0;
    #         $getNumShape() {
    #             Return $numShape;
    #         }
    #     }
    #     Class Test {
    #         main () {
    #             Out.printInt(Shape::$numShape);
    #             Var r,s : Float;
    #             s = r * r * 3.14;
    #             a[0] = s;
    #         }
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,253))
    
    # def test54(self):
    #     input = """
    #     Class Shape {
    #         Var $numShape: Int = 0;
    #         Val pi:Float = 3.14;
    #         $getNumShape() {
    #             Return $numShape;
    #         }
    #     }
    #     Class Test {
    #         main () {
    #             Var a : Shape = New Shape();
    #             Var r,s : Float;
    #             s = r * r * a.pi;
    #         }
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,254))
    
    # def test55(self):
    #     input = """
    #     Class Test {
    #         main () {
    #             Var a : Shape = New Shape();
    #             Var r,s : Float;
    #             s = r * r * a::$pi;
    #         }
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,255))
    
    # def test56(self):
    #     input = """Class S {
    #         Var S : String = "case normal";
    #         Constructor(){ }
    #         Constructor(a: String ; b : String){
    #             a = !True && !False;
    #             n = b;
    #         }
    #         Destructor(){ }

    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,256))
    
    # def test57(self):
    #     input = """Class S{
    #         Var S : String = "case 2 destructor";
    #         Constructor(){ }
    #         Destructor(){}
    #         Destructor(){ }
    #     }"""
    #     expect = "Error on line 5 col 12: Destructor"
    #     self.assertTrue(TestParser.test(input,expect,257))
    
    # def test58(self):
    #     input = """Class S{
    #         Var S : String = "case destructor has param";
    #         Constructor(){ }
    #         Destructor(a,b : Float){}
    #     }"""
    #     expect = "Error on line 4 col 23: a"
    #     self.assertTrue(TestParser.test(input,expect,258))
    
    # def test59(self):
    #     input = """Class S{
    #         Var S : String = "case 2 destructor";
    #         Constructor(){ }
    #         Destructor(){
    #             Destructor(){ }
    #         }
    #     }"""
    #     expect = "Error on line 5 col 16: Destructor"
    #     self.assertTrue(TestParser.test(input,expect,259))
    
    # def test60(self):
    #     input = """Class S{
    #         Var S : String = "case 2 destructor";
    #         Constructor(){
    #             Destructor(){  };
    #         }
    #         Destructor(){  }
    #     }"""
    #     expect = "Error on line 4 col 16: Destructor"
    #     self.assertTrue(TestParser.test(input,expect,260))
    
    # def test61(self):
    #     input = """Class S{
    #         Var S : String = "case 2 destructor";
    #         Constructor(){
    #             Constructor(){  };
    #         }
    #         Destructor(){  }
    #     }"""
    #     expect = "Error on line 4 col 16: Constructor"
    #     self.assertTrue(TestParser.test(input,expect,261))
    
    # def test62(self):
    #     input = """Class S{
    #         Var S : String = "case 2 destructor";
    #         Constructor(){ }
    #         Destructor(){ 
    #             Constructor(){  }
    #         }
    #     }"""
    #     expect = "Error on line 5 col 16: Constructor"
    #     self.assertTrue(TestParser.test(input,expect,262))
    
    # def test63(self):
    #     input = """
    #     Class S {
    #         func() {
    #             Foreach(i In 1 .. 100 By 1){
    #                 If(k % i == 1){
    #                     Break;
    #                 }
    #                 Else{
    #                     c = c + 1;
    #                 }
    #             }
    #             Return New X();
    #         }
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 263))
    
    # def test64(self):
    #     input = """Class S {
    #         func() {
    #             Foreach(i In 1 .. 100 By 1){
    #                 If(k+27 % i == 4){
    #                     Return New K (3,4);
    #                 }
    #                 Elseif (a > b) {
    #                     c += 1;
    #                 }
    #             }
    #         }
    #     }
    #     """
    #     expect = "Error on line 8 col 27: ="
    #     self.assertTrue(TestParser.test(input, expect, 264))
    
    # def test65(self):
    #     input = """Class S {
    #         func() {
    #             Foreach (ite In 1 .. 100 By 10){
    #                 If(k+27 % i == 4){
    #                     Return K.attr;
    #                 }
    #                 Elseif (a ==. b) {
    #                     c = c +. "hello";
    #                 }
    #             }
    #         }
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 265))
    
    # def test66(self):
    #     input = """Class S {
    #         func() {
    #             Foreach (ite In 1 .. 100 By 10){
    #                 If(k % 27 % i == 4 % 3){
    #                     Return K.attr;
    #                 }
    #             }
    #         }
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 266))
    
    # def test67(self):
    #     input = """Class S {
    #         func() {
    #             Foreach (ite In 1 .. 100 By 10){
    #                 If(("str") ==. a){
    #                     Return Null;
    #                 }
    #             }
    #         }
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 267))
    
    # def test68(self):
    #     input = """Class S {
    #         func() {
    #             Foreach (ite1 In 1 .. 100 By 10){
    #                Foreach (ite2 In 1 .. 100 By 11){
    #                    funcal(Null,3);
    #                 }
    #             }
    #         }
    #     }"""
    #     expect = "Error on line 5 col 29: ("
    #     self.assertTrue(TestParser.test(input, expect, 268))
    
    # def test69(self):
    #     input = """Class S {
    #         func() {
    #             Foreach (ite1 In 1 .. 100 By 10){
    #                Foreach (ite2 In 1 .. 100 By 11){
    #                    a.funcal(Null,3);
    #                 }
    #             }
    #         }
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 269))
    
    # def test70(self):
    #     input = """Class S {
    #         func() {
    #             Foreach (ite1 In 1 .. 100 By 10){
    #                Foreach (ite2 In 1 .. 100 By 11){
    #                    Break;
    #                    Break;
    #                 }
    #             }
    #         }
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 270))
    
    # def test71(self):
    #     input = """Class C {
    #             foo(){
    #                 Var a,b,c : Int;
    #                 a = x.Y();
    #                 b = 0B100011101;
    #                 c = 0x12AC001;
    #             } 
    #         }
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 271))
    
    # def test72(self):
    #     input = """Class C {
    #             foo(){
    #                 Var a,b,c : Int;
    #                 a = x.Y() * (-1.2e-10);
    #                 b = 0B100110101;
    #                 c = 0x12AC001;
    #             } 
    #         }
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 272))
    
    # def test73(self):
    #     input = """Class C {
    #             foo(){
    #                 Var a:Array[Int,3];
    #                 Val k :Int = 2;
    #                 a[k] = 5;
    #             } 
    #         }
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 273))
    
    # def test74(self):
    #     input = """Class C {
    #             foo(){
    #                 Var a:Array[Array[Int,4],4];
    #                 Foreach (i In 1 .. 100 By 10){
    #                     Foreach (j In 1 .. 100 By 11){
    #                         a[i][j] = i+j;
    #                     }
    #                 }
    #             } 
    #         }
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 274))
    
    # def test75(self):
    #     input = """Class C {
    #             foo(){
    #                 Var a:Array[Array[Int,4],4];
    #                 Foreach (i In 1 .. 100 By 10){
    #                     Foreach (j In 1 .. 100 By 11){
    #                         a[i+1][j] = i*j;
    #                     }
    #                 }
    #             } 
    #         }
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 275))
    
    # def test76(self):
    #     input = """Class C {
    #             foo(){
    #                 Var a,b:Array[Array[Int,4],4];
    #                 Foreach (i In 1 .. 100 By 10){
    #                         a[b[i]] = i;
    #                 }
    #             } 
    #         }
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 276))
    
    # def test77(self):
    #     input = """Class C {
    #             foo(){
    #                 Var a,b:Array[Array[Int,4],4];
    #                 a[b[4]+1] = a[0];
    #             } 
    #         }
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 277))
    
    # def test78(self): ## check coi co call truc tiep ham vay dc ko
    #     input = """Class S {
    #             foox(){
    #                 foo(1*2,"b"+."c","a"==."b");
    #             }
    #         }
    #     """
    #     expect = "Error on line 3 col 23: ("
    #     self.assertTrue(TestParser.test(input, expect, 278))
    
    # def test79(self): ## check coi co call truc tiep ham vay dc ko
    #     input = """Class S {
    #             foox(){
    #                 a = foo(1*2,"b"+."c","a"==."b");
    #             }
    #         }
    #     """
    #     expect = "Error on line 3 col 27: ("
    #     self.assertTrue(TestParser.test(input, expect, 279))
    
    # def test80(self): 
    #     input = """Class S: A, B,C {
    #             foo(){
    #                 Var s :String = "No multiple inheritance";
    #                 Return False;
    #             } 
    #         }
    #     """
    #     expect = "Error on line 1 col 10: ,"
    #     self.assertTrue(TestParser.test(input, expect, 280))
    
    # def test81(self): 
    #     input = """Class C: Cam {
    #             foo(){
    #                 If (True){
    #                     If (0==0 && (0!=1) || (1 < (2*(3+4))) || !(4)){
    #                         a=(5+ (4*8) + 10);
    #                         If (b == True){
    #                             If (True){
    #                                 If (True){
    #                                     b = False;
    #                                 }
    #                                 Else{
    #                                     If (True){
    #                                         b = False;
    #                                         Return True;
    #                                     }
    #                                 }
    #                             }
    #                         }  
    #                     }
    #                 }
    #                 Return False;
    #             } 
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 281))
    
    # def test82(self):
    #     input = """Class C{
    #             Constructor(r : Int = 1){
    #                 Self.r = r;
    #                 Self.area = (r*r);
    #             }
    #             foo(){
    #                 Var arr : Array[Array[Shape,4],5];
    #             }
    #         }
    #     """
    #     expect = "Error on line 2 col 36: ="
    #     self.assertTrue(TestParser.test(input, expect, 282))
    
    # def test83(self):
    #     input = """Class C{
    #             Constructor(ra : Int){
    #                 Self.ra = ra;
    #             }
    #             fox(){
    #                 Var arr : Array[Array[Shape,1],2];
    #                 Foreach (i In 0 .. (2*3)-1 By 1){
    #                     Foreach (j In 0 .. 2-2-1 ){
    #                         Var shape0 : Shape = New Shape(i);
    #                         arr[j][j] =  shape0;
    #                         If ((j == 4)){
    #                             Return "bruh";
    #                         }
    #                     }
    #                 }
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 283))     
    
    # def test84(self):
    #     input = """Class C{
    #             fox(){
    #                 Var arr : Array[Array[Shape,1],2];
    #                 Var x : Float = arr[1][2].area;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 284))  
    
    # def test85(self):
    #     input = """Class C{
    #             fox(){
    #                 Var arr : Array[Array[Shape,1],2];
    #                 Var x : Float = Array[1,2,3];
    #             }
    #         }
    #     """
    #     expect = "Error on line 4 col 41: ["
    #     self.assertTrue(TestParser.test(input, expect, 285))  
       
    # def test86(self):
    #     input = """Class Program{
    #             Main(){
    #             Var b : Int = 12;
    #             If( a * 1 + 2 == 9 ){
    #                 b = a = c = d = Self.pi ; 
    #                 Foreach (i In 1 .. 100 By 5){
    #                     a =  arr[1+2+3];
    #                     a = a::$getShape();
    #                     Continue;
    #                 }
    #             }
    #             Else{
    #                 a = a * 3 / 3 /3 /4 /4 + 5 -9; 
    #             }
    #         }
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 286)) 
    
    # def test87(self):
    #     input = """2 + 1 + a.fox()"""
    #     expect = "Error on line 1 col 0: 2"
    #     self.assertTrue(TestParser.test(input,expect,287))
    
    # def test88(self):
    #     input = """Class S {
    #             fox(){
    #                 a[c][d][k.foo()] = 1;
    #             }
    #             Var l,f : Int = 1 , 1 - 2;
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,288))
    
    # def test89(self):
    #     input = """Class S{
    #             fox(){
    #                 a[c[1]][d][k.foo()] = 1;
    #             }
    #             Var x,z : Int = 1 , 1 - 2;
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,289))
    
    # def test90(self):
    #     input = """Class S{
    #             fox(){
    #                 a[b[x]] = 1;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,290))
    
    # def test91(self):
    #     input = """Class S{
    #             fox(){
    #                 a[b[c[d[1]]]] = 1;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,291))
    
    # def test92(self):
    #     input = """Class S{
    #             fox(){
    #                 a[b[c[d[Self.wow]]]] = 1;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,292))
    
    # def test93(self):
    #     input = """Class S{
    #             fox(){
    #                 a[b[c[d[abc::$wow]]]] = 1;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,293))
    
    # def test94(self):
    #     input = """Class S{
    #             fox(){
    #                 a[b[c[d[abc::$wow]]]] = 1;
    #                 Var a : New X();
    #             }
    #         }
    #     """
    #     expect = "Error on line 4 col 28: New"
    #     self.assertTrue(TestParser.test(input,expect,294))
    
    # def test95(self):
    #     input = """Class A B{
    #             fox(){
    #                 a[b[c[d[abc::$wow]]]] = 1;
    #                 Var a : New X();
    #             }
    #         }
    #     """
    #     expect = "Error on line 1 col 8: B"
    #     self.assertTrue(TestParser.test(input,expect,295))
    
    # def test96(self):
    #     input = """Class A::B{
    #             fox(){
    #                 a[b[c[d[abc::$wow]]]] = 1;
    #                 Var a : New X();
    #             }
    #         }
    #     """
    #     expect = "Error on line 1 col 7: ::"
    #     self.assertTrue(TestParser.test(input,expect,296))
    
    # def test97(self):
    #     input = """Class A:B{
    #             fox(){
    #                 a[b[c[d[abc::$wow]]]] = 1;
    #                 Destructor(){ };
    #             }
    #         }
    #     """
    #     expect = "Error on line 4 col 20: Destructor"
    #     self.assertTrue(TestParser.test(input,expect,297))
    
    # def test98(self):
    #     input = """Class A:B{
    #             fox(){
    #                 Self.a = Self.b*Self.c-Self::$e+(Self.x - Self.Y());
    #                 Self.a = Self::$A();
    #                 Self::$b = Self.B();
    #                 Self.a = Self.$A;
    #             }
    #         }
    #     """
    #     expect = "Error on line 6 col 34: $A"
    #     self.assertTrue(TestParser.test(input,expect,298))
    
    def test99(self):
        input = """Class A:B{
                fox(){
                    Self.a = Self.A();
                    Self::$b = Self::$B();
                    Self.a.a.a(a,b);
                    a.a.a[0][1].func(a,b);
                    A.a.a.foo();
                (a.a[1][2][3]).foo();
                MotorBike::$ab.foo();
                (MotorBike::$a.a[1][2]).foo();
                    
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))
     
     