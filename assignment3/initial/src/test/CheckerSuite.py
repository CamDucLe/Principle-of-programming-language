import unittest
from TestUtils import TestChecker
from AST import *
# Le Duc Cam - 1952588 #

class CheckerSuite(unittest.TestCase):
    ### Redeclared ###
    def test400(self):
        input = """
            Class l{ }
            Class d{ }
            Class c{ }
            Class z{ }
            Class c{ }
        """
        expect = "Redeclared Class: c"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test401(self):
        input = """
        Class cam{
            Var cam:Int;
            Var cc :Int;
            Var cam:Float;
        }
        """
        expect = "Redeclared Attribute: cam"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test402(self):
        input = """
        Class cc{
            Var cam:Int;
            Val cam :Int;
        }
        """
        expect = "Redeclared Attribute: cam"
        self.assertTrue(TestChecker.test(input,expect,402))
    
    def test403(self):
        input = """
        Class cam{
            Var cam:Int;
            Var duc,le :Int;
        }
        Class camcam{ Var $cam:Int;}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test404(self):
        input = """
        Class A{ Var $A:Int; }
        Class B{ Val $A:Int; }
        """
        expect = "Redeclared Attribute: $A"
        self.assertTrue(TestChecker.test(input,expect,404))
    
    def test405(self):
        input = """
        Class cc{
            cc(){ }
            cam(){ }
        }
        Class cam{ 
            cam(){ }
            cam(){ }
        }
        """
        expect = "Redeclared Method: cam"
        self.assertTrue(TestChecker.test(input,expect,405))
    
    def test406(self):
        input = """
        Class c{
            c( c,c : Int){ }
        }
        """
        expect = "Redeclared Parameter: c"
        self.assertTrue(TestChecker.test(input,expect,406))
    
    def test407(self):
        input = """
        Class A{
            $x(c,d : Int;   e:Float){ }
        }
        Class c{
            c( c:Int){ }
            Val $x:Int;
        }
        """
        expect = "Redeclared Attribute: $x"
        self.assertTrue(TestChecker.test(input,expect,407))
    
    def test408(self):
        input = """
        Class A{
            c(c : Int){ }
        }
        Class c{
            c( c:Int; c:Float){ }
        }
        """
        expect = "Redeclared Parameter: c"
        self.assertTrue(TestChecker.test(input,expect,408))
    
    def test409(self):
        input = """
        Class c0{
            Var c1:String;
            cc(c : Int){ 
                Var c:Float;
            }
        }
        """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,409))
    
    def test410(self):
        input = """
        Class c{
            Val c:Float=27;
            cc(){ 
                Val c:Int=27;
                Val c:Float=27;
            }
        }
        """
        expect = "Redeclared Constant: c"
        self.assertTrue(TestChecker.test(input,expect,410))
    
    def test411(self):
        input = """
        Class c{
            Val c:Float = 27;
            cc(){ 
                Val c:Int= 27;
                { Val c:Float = 27; }
            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,411))
    
    ### Undeclared ###
    def test412(self):
        input = """
        Class b{
            Var c:Int;
        }
        Class c{
            c(){ 
                c = 4;
            }
        }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,412))
    
    def test413(self):
        input = """
        Class c{
            c2(){ 
                { Var c: Int;}
                c = 4;
            }
        }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test414(self):
        input = """
        Class c{
            c2(){ 
                Var a :Float;
                { Var c: Int;}
                c[3] = a; 
            }
        }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test415(self):
        input = """
        Class c{
            c2(){ 
                { Var c: Int;}
                Self.c = 4;
            }
        }
        """
        expect = "Undeclared Attribute: c"
        self.assertTrue(TestChecker.test(input,expect,415))
    
    def test416(self):
        input = """
        Class c0{ }
        Class c{
            c2(){ 
                Var cc: c0; 
                { Var t: Int;}
                cc.t = 4;
            }
        }
        """
        expect = "Undeclared Attribute: t"
        self.assertTrue(TestChecker.test(input,expect,416))
    
    def test417(self):
        input = """
        Class c0{ 
            Var t:Int;
        }
        Class c{
            c2(){ 
                Var cc: c0; 
                cc.t = 4;
            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,417))
    
    def test418(self): ##? check cai test nay coi raise cai gi (undec class hay id)
        input = """
        Class c{
            c2(){ 
                Var a :Float;
                { Var c: Int;}
                CC.b = a; 
            }
        }
        """
        expect = "Undeclared Class: CC"
        self.assertTrue(TestChecker.test(input,expect,418))
    
    def test419(self):
        input = """
        Class c{
            c2(){ 
                Val a :CC;
            }
        }
        """
        expect = "Undeclared Class: CC"
        self.assertTrue(TestChecker.test(input,expect,419))
    
    def test420(self):
        input = """
        Class c{
            Var a: CC;
            c(){  }
        }
        """
        expect = "Undeclared Class: CC"
        self.assertTrue(TestChecker.test(input,expect,420))
    
    def test421(self):
        input = """
        Class c{
            c(){  
                Var CC:Int;
                Self.CC();
            }
        }
        """
        expect = "Undeclared Method: CC"
        self.assertTrue(TestChecker.test(input,expect,421))
    
    def test422(self):
        input = """
        Class b{ }
        Class c{
            c(){  
                Var obj:b;
                obj.CC();
            }
        }
        """
        expect = "Undeclared Method: CC"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test423(self):
        input = """
        Class b { }
        Class c:d{ }
        """
        expect = "Undeclared Class: d"
        self.assertTrue(TestChecker.test(input,expect,423))

    ### Cannot Assign To Constant ###
    def test424(self):
        input = """
        Class c{
            m(){  
                Val a:Int = 2;
                { a = 7; }
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(a),IntLit(7))"
        self.assertTrue(TestChecker.test(input,expect,424))
    
    def test425(self):
        input = """
        Class c{
            Val a:Int = 5;
            m(){  
                Self.a = 10;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Self(),Id(a)),IntLit(10))"
        self.assertTrue(TestChecker.test(input,expect,425))
    
    def test426(self):
        input = """
        Class B{ 
            Val a:Int = 27;
        }
        Class c{
            m(){  
                Var b:B;
                b.a = 10;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Id(b),Id(a)),IntLit(10))"
        self.assertTrue(TestChecker.test(input,expect,426))
    
    def test427(self):
        input = """
        Class c{
            m(){  
                Val b:Array[Int, 2] = Array(1,2);
                b[5] = 10;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(ArrayCell(Id(b),[IntLit(5)]),IntLit(10))"
        self.assertTrue(TestChecker.test(input,expect,427))
    
    def test428(self):
        input = """
        Class c1{
            Val x:Array[Int, 1]= Array(7,2);
        }
        Class c2{
            m(){  
                Var c2:c1;
                c2.x[0] = 10;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(ArrayCell(FieldAccess(Id(c2),Id(x)),[IntLit(0)]),IntLit(10))"
        self.assertTrue(TestChecker.test(input,expect,428))
    
    def test429(self):
        input = """
        Class c{
            Val x:Array[Int, 1] = Array(0);
            m(){  
                Self.x[0] = 27;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(ArrayCell(FieldAccess(Self(),Id(x)),[IntLit(0)]),IntLit(27))"
        self.assertTrue(TestChecker.test(input,expect,429))

    ## Type Mismatch In Statement ###
    def test430(self):
        input = """
        Class B{
            Var b:Float;
        }
        Class C{
            testIf(){  
                Var a:Int =5 ;
                Var obj:B;
                If (obj.b>=a){ }
            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,430))
    
    def test431(self):
        input = """
        Class C{
            Var b:String;
            testIf(){  
                Var a:Int =5 ;
                If (Self.b==a){ }
            }
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(==,FieldAccess(Self(),Id(b)),Id(a)),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,431))
    
    def test432(self):
        input = """
        Class C{
            testIf(){  
                Var a:Int =0 ;
                Foreach (a In  1 .. 5 By 1){
                    Var b: Float;
                    If (a == b){ }
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(==,Id(a),Id(b)),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test433(self):
        input = """
        Class C{
            Var i :Int;
            testIf(){  
                Var a:Float =0 ;
                If( 5 > Self.i){
                    Var b:Int;
                    If(Self.i==b){  }
                    If(a==.b){  }
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(==.,Id(a),Id(b)),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,433))
    
    def test434(self):
        input = """
        Class C{
            Var i :Int;
            testFor(a:Float; b:Int; s:String;i:Int){  
                Foreach (i In  1 .. 5 By 1){
                    If( b >= Self.i){  
                        Var j:Int;
                        Foreach (j In 1 .. 4){
                            If(a == j){ } 
                        }
                    }
                    If(s==."str"){  }
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(==,Id(a),Id(j)),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,434))
    
    def test435(self):
        input = """
        Class A{
            Var x: Float;
            Var k:String;
        }
        Class C{
            Var i :Int;
            Var obj : A;
            testAssign(x:Int;y:Boolean){  
                Var obj2 : A;
                Self.obj.x = 5.5;
                x = Self.i;
                y = obj2.k;
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(y),FieldAccess(Id(obj2),Id(k)))" 
        self.assertTrue(TestChecker.test(input,expect,435))
    
    def test436(self): 
        input = """
        Class A{
            Var x: Float;
        }
        Class C{
            Var obj : A;
            testAssign(x:Int;y:Boolean){  
                Var i :Int;
                Self.obj.x = i ;
            }
        }
        """
        expect = "[]" 
        self.assertTrue(TestChecker.test(input,expect,436))

    def test437(self):
        input = """
        Class C{
            testAssign(x:Int;y:Boolean){  
                Var c1 : Array[Float,5];
                Var c2 : Array[Int,5];
                c1[4] = 5;
                c2[0] = c1[4];
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(c2),[IntLit(0)]),ArrayCell(Id(c1),[IntLit(4)]))" 
        self.assertTrue(TestChecker.test(input,expect,437))
    
    def test438(self):
        input = """
        Class A{
            Var  x : Array[Float,5];
        }
        Class C{
            Var obj : A;
            Var  k : Array[Float,5];
            testAssign(x:Int;y:Boolean){  
                Var cc : Array[String,5];
                Self.obj.x[0] = Self.k[2] ;
                Self.obj.x[0] = x ;
                cc[2] = Self.obj.x[0] ;
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(cc),[IntLit(2)]),ArrayCell(FieldAccess(FieldAccess(Self(),Id(obj)),Id(x)),[IntLit(0)]))" 
        self.assertTrue(TestChecker.test(input,expect,438))
    
    def test439(self):
        input = """
        Class A{
            Var  x : Array[Int,5];
        }
        Class C{
            Var obj : A;
            Var  k : Array[Float,5];
            testAssign(x:Array[Int,5];y:Boolean){  
                Var cc: Array[String,5];
                Self.k = Self.obj.x ;
                cc = x ;
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(cc),Id(x))" 
        self.assertTrue(TestChecker.test(input,expect,439))
    
    def test440(self):
        input = """
        Class C{
            Var  k : Array[Float,5];
            testAssign(x:Array[Int,5];y:Boolean){  
                Var cc: Array[Float,6];
                Self.k = x;
                cc = Self.k ;
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(cc),FieldAccess(Self(),Id(k)))" 
        self.assertTrue(TestChecker.test(input,expect,440))
    
    def test441(self): 
        input = """
        Class A{
            func(){ }
        }
        Class C{
            Var  obj : Int;
            f(){ }
            testAssign(x:Array[Int,5];y:Boolean){  
                Self.obj.func();
            }
        }
        """
        expect = "Type Mismatch In Statement: Call(FieldAccess(Self(),Id(obj)),Id(func),[])" 
        self.assertTrue(TestChecker.test(input,expect,441))
    
    def test442(self): 
        input = """
        Class A{
            func(){ }
        }
        Class C{
            Var  obj : A;
            f(){ }
            test(x:Array[Int,5];f:Boolean){  
                Self.obj.f();
            }
        }
        """
        expect = "Undeclared Method: f" 
        self.assertTrue(TestChecker.test(input,expect,442))
    
    def test443(self): 
        input = """
        Class A{
            func(){ }
        }
        Class C{
            f(){ }
            test(x:Array[Int,5];f:Boolean){  
                Var  obj : String;
                obj.func();
            }
        }
        """
        expect = "Type Mismatch In Expression: FieldAccess(Id(obj),Id(func))" 
        self.assertTrue(TestChecker.test(input,expect,443))

    def test446(self):
        input = """
        Class a{ }
        Class C{
            fun(){
                Var d,e: Int = 6,9;
                Var z:a;
                Val j,k,l:Int=1,2,3;
                Val str:String = "str";
                Val c1:Float = 99;
                Var c2:Float = 98;
                Var i: Int = "str";
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(i),IntType,StringLit(str))" 
        self.assertTrue(TestChecker.test(input,expect,446))
    
    def test447(self): 
        input = """
        Class a{ }
        Class C{
            Var x: Array[Float,5] = Array(11.2);
            Val y: Array[Float,5] = Array(11.1,12.6);
            Var z: Int = 5;
            Var b: Float = 5; 
            Val l: String = "STR";
            Val r: Boolean = 27.3;
        }
        """
        expect = "Type Mismatch In Constant Declaration: AttributeDecl(Instance,ConstDecl(Id(r),BoolType,FloatLit(27.3)))" 
        self.assertTrue(TestChecker.test(input,expect,447))

        ##### Type Mismatch In Exp ###

    def test444(self): 
        input = """
        Class A{
            Var a : Array[Int,5];
        }
        Class B{
            func(){
                Var obj :A;
                Var k:Float;
                Val d:Int = 5;
                k = d ;
                k = obj.a[1] ;
                obj.a[1.1] = d;
            }
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(FieldAccess(Id(obj),Id(a)),[FloatLit(1.1)])" 
        self.assertTrue(TestChecker.test(input,expect,444))
    
    
    def test445(self): 
        input = """
        Class C{
            func(){
                Var a:Array[Int,5];
                Var k:Float;
                k = a[4][6.6];
            }
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),[IntLit(4),FloatLit(6.6)])" 
        self.assertTrue(TestChecker.test(input,expect,445))
    
    def test448(self):  
        input = """
        Class C{
            Val b:Float = 55; 
            fun(){  
                Var a: Float = 55;
                a = "asd" + 4.3;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,StringLit(asd),FloatLit(4.3))" 
        self.assertTrue(TestChecker.test(input,expect,448))
    
    def test449(self):  
        input = """
        Class C{
            Var b:Float = 55; 
            fun(){  
                Var a: Int = 55;
                Self.b = a % 4.4;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(a),FloatLit(4.4))" 
        self.assertTrue(TestChecker.test(input,expect,449))
    
    def test450(self):  
        input = """
        Class C{
            Var b:String = "asd"; 
            fun(){  
                Var a: Int = 55;
                Self.b = Self.b +. "tail";
                Var s :String;
                s = "head" + a;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,StringLit(head),Id(a))" 
        self.assertTrue(TestChecker.test(input,expect,450))
    
    def test451(self):  
        input = """
        Class C{
            Var b:Boolean = True; 
            fun(){  
                Var a: Boolean;
                a = !Self.b ;
                Self.b = !True; 
                a = !(!5) ;
            }
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,IntLit(5))" 
        self.assertTrue(TestChecker.test(input,expect,451))
    
    def test452(self):  
        input = """
        Class C{
            Var b:Boolean = True; 
            fun(){  
                Var a: Int;
                Var k :Float;
                Val f :Float = 5;
                k = 5 + (f+2.3);
                a = 5+(!6);
            }
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,IntLit(6))" 
        self.assertTrue(TestChecker.test(input,expect,452))
    
    def test453(self):  
        input = """
        Class A{
            Var att:Int = 5;
            func(){ }
        }
        Class C{
            f(){ }
            Var  obj : Int;
            test(x:Array[Int,5];f:Boolean){
                Var o :A;  
                x[1] = o.att;
                x[1] = Self.obj.att;
            }
        }
        """
        expect = "Type Mismatch In Expression: FieldAccess(FieldAccess(Self(),Id(obj)),Id(att))" 
        self.assertTrue(TestChecker.test(input,expect,453))
    
    def test454(self):  
        input = """
        Class A{
            func(){ 
                Return 5;
            }
        }
        Class C{
            f(){ }
            Var  obj : Int;
            test(x:Array[Int,5];f:Boolean){
                Var o :Int;
                Var k :Float;  
                x[1] = o.func();
               
            }
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(o),Id(func),[])" 
        self.assertTrue(TestChecker.test(input,expect,454))
    
    def test455(self):  
        input = """
        Class A{
            func(){ 
                Return 5;
            }
        }
        Class C{
            f(){ }
            Var  obj : Int;
            Var obj2: A;
            test(x:Array[Int,5]){
                Var k :Float;  
                k = Self.obj2.func();
                k = Self.obj.func();
            }
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(FieldAccess(Self(),Id(obj)),Id(func),[])" 
        self.assertTrue(TestChecker.test(input,expect,455))
    
    def test456(self):  
        input = """
        Class A{
            func(){ 
                Return 27;
            }
        }
        Class C{
            f(){ }
            Var  obj : Int;
            test(x:Array[Int,5]){
                Var k :Float;  
                k = Self.obj.func();
            }
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(FieldAccess(Self(),Id(obj)),Id(func),[])" 
        self.assertTrue(TestChecker.test(input,expect,456))

    def test457(self):  
        input = """
        Class A{
            func(){ 
                Return 5;
            }
        }
        Class C{
            f(){ }
            Var  obj : A;
            test(x:Array[Int,5]){
                Var k :Float;  
                k = Self.obj.func(x,z);
            }
        }
        """
        expect = "Undeclared Identifier: z" 
        self.assertTrue(TestChecker.test(input,expect,457))
    
    def test458(self):  
        input = """
        Class C{
            Var f: Float = 5.5;
            f(){  }
        }
        """
        expect = "[]" 
        self.assertTrue(TestChecker.test(input,expect,458))
    
    def test459(self):  
        input = """
        Class C{
            func(){ }
            f(){
                Self.func(x);
            }
        }
        """
        expect = "Undeclared Identifier: x" 
        self.assertTrue(TestChecker.test(input,expect,459))
    
    def test460(self):  
        input = """
        Class A{
            foo(x:Float){ 
                Return 5;
            }
        }
        Class C{
            func(x:Int){ }
            f(){
                Var obj:A;
                Var f:Float;
                Var i:Int;
                Val s:String ="str";
                obj.foo(f);
                obj.foo(i);
                obj.foo(s);
            }
        }
        """
        expect = "Type Mismatch In Statement: Call(Id(obj),Id(foo),[Id(s)])" 
        self.assertTrue(TestChecker.test(input,expect,460))
    
    def test461(self):  
        input = """
        Class A{
            foo(x:Float){ 
                Return 5;
            }
        }
        Class C{
            func(x:Int){ }
            f(){
                Var obj:A;
                Var f:Float;
                Var i:Int = 5;
                Val s:String = "str";
                f = obj.foo(f);
                f = obj.foo(i);
                f = obj.foo(s);
            }
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(obj),Id(foo),[Id(s)])" 
        self.assertTrue(TestChecker.test(input,expect,461))
    
    #### Type Mismatch In Constant ####
        
    def test462(self):  
        input = """
        Class C{
            func(x:Int){ 
                Val k:Int = "asd";
            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(k),IntType,StringLit(asd))" 
        self.assertTrue(TestChecker.test(input,expect,462))
    
    def test463(self):  
        input = """
        Class A { }
        Class C{
            func(x:Int){ 
                Val k:A = 5;
            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(k),ClassType(Id(A)),IntLit(5))" 
        self.assertTrue(TestChecker.test(input,expect,463))
    
    def test464(self):  
        input = """
        Class A { }
        Class C{
            func(x:Int){ 
                Val z:Boolean = True;
                Val m:String = "asd";
                Val l: String = 5.5; 
            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(l),StringType,FloatLit(5.5))" 
        self.assertTrue(TestChecker.test(input,expect,464))
    
    def test465(self):  
        input = """
        Class A { }
        Class C{
            func(x:Int){ 
                Var z:Boolean = True;
                Var c :Int = 4;
                z = ! False;
                z = ! (x+c);
            }
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,BinaryOp(+,Id(x),Id(c)))" 
        self.assertTrue(TestChecker.test(input,expect,465))

    ## MustInLoop ###

    def test466(self):  
        input = """
        Class A { }
        Class C{
            func(x:Int){ 
                Var i:Int;
                Foreach (i In 1 .. 5 By 2){
                    {Break;}
                    If ( 5 == i  ){
                        If ( True == False ){
                            Break;
                        }
                        Break;
                    }
                    Break;
                }
                {Break;}
            }
        }
        """
        expect = "Break Not In Loop" 
        self.assertTrue(TestChecker.test(input,expect,466))
    
    def test467(self):  
        input = """
        Class A { }
        Class C{
            func(x:Int){ 
                Var i:Int ;
                Foreach (i In 1 .. 5 By 2){
                    {Continue;}
                    If ( 5 == i  ){
                        
                        Continue;
                    }
                    Continue;
                }
                If ( True == False ){
                    Continue;
                }
            }
        }
        """
        expect = "Continue Not In Loop" 
        self.assertTrue(TestChecker.test(input,expect,467))
    
    def test468(self):  
        input = """
        Class A { }
        Class C{
            func(v:Int){
                Break; 
            }
        }
        """
        expect = "Break Not In Loop" 
        self.assertTrue(TestChecker.test(input,expect,468))
    
    def test469(self):  
        input = """
        Class A { }
        Class C{
            func(v:Int){
                Continue; 
            }
        }
        """
        expect = "Continue Not In Loop" 
        self.assertTrue(TestChecker.test(input,expect,469))
    
    ##  Illegal Constant Expression ###
    def test470(self):  
        input = """
        Class A { }
        Class C{
            func(v:Int){
                Val a : Int;
            }
        }
        """
        expect = "Illegal Constant Expression: None" 
        self.assertTrue(TestChecker.test(input,expect,470))
    
    def test471(self):  
        input = """
        Class A { }
        Class C{
            func(v:Int){
                Var b:Int = 5;
                Val k:Int = 5;
                Val a : Float = b;
            }
        }
        """
        expect = "Illegal Constant Expression: Id(b)" 
        self.assertTrue(TestChecker.test(input,expect,471))

    def test472(self):  
        input = """
        Class C{
            Var b:Int = 5;
            func(v:Int){
                Val a : Float = b;
            }
        }
        """
        expect = "Undeclared Identifier: b" 
        self.assertTrue(TestChecker.test(input,expect,472))
    
    def test473(self):  
        input = """
        Class C{
            Var b:Int = 5;
            func(v:Int){
                Val a : Float = Self.b;
            }
        }
        """
        expect = "Illegal Constant Expression: FieldAccess(Self(),Id(b))" 
        self.assertTrue(TestChecker.test(input,expect,473))
    
    def test474(self):  
        input = """
        Class C{
            Var b:Int = 5;
            func(v:Int){
                Val a : Float = Self.b + 5;
            }
        }
        """
        expect = "Illegal Constant Expression: BinaryOp(+,FieldAccess(Self(),Id(b)),IntLit(5))" 
        self.assertTrue(TestChecker.test(input,expect,474))
    
    def test475(self):  
        input = """
        Class C{
            Val b:Int = 5;
            func(v:Int){
                Val a : Float = Self.b + 5;
            }
        }
        """
        expect = "[]" 
        self.assertTrue(TestChecker.test(input,expect,475))
    
    def test476(self):  
        input = """
        Class C{
            Val b:Int = 5;
            func(v:Int){
                Val c: Float = 5;
                Val a : Float = c + Self.b ;
            }
        }
        """
        expect = "[]" 
        self.assertTrue(TestChecker.test(input,expect,476))
    
    def test477(self):  
        input = """
        Class C{
            func(v:Int){
                Var c: Array[Int,5] = Array(1,2,3);
                Val a : Array[Int,5] = c ;
            }
        }
        """
        expect = "Illegal Constant Expression: Id(c)" 
        self.assertTrue(TestChecker.test(input,expect,477))
    
    # check tiep Illegal Constant Expression cho Array

    ## Illegal Array Literal  ###

    def test478(self):  
        input = """
        Class C{
            func(v:Int){
                Val c: Array[Int,5] = Array(1,"asd",3);
                Val a : Array[Int,5] = c ;
            }
        }
        """
        expect = "Illegal Array Literal: [IntLit(1),StringLit(asd),IntLit(3)]" 
        self.assertTrue(TestChecker.test(input,expect,478))
    
    def test479(self):  
        input = """
        Class C{
            func(v:Int){
                Val c: Array[Int,5] = Array(1,True,3);
                Val a : Array[Int,5] = c ;
            }
        }
        """
        expect = "Illegal Array Literal: [IntLit(1),BooleanLit(True),IntLit(3)]" 
        self.assertTrue(TestChecker.test(input,expect,479))
   
    def test480(self):  
        input = """
        Class C{
            func(v:Int){
                Var c: Array[Int,5] = Array(1,True,3);
            }
        }
        """
        expect = "Illegal Array Literal: [IntLit(1),BooleanLit(True),IntLit(3)]" 
        self.assertTrue(TestChecker.test(input,expect,480))
    
    def test481(self):  
        input = """
        Class C{
            func(v:Int){
                Var c: Array[Int,5] = Array(False,True);
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(c),ArrayType(5,IntType),[BooleanLit(False),BooleanLit(True)])" 
        self.assertTrue(TestChecker.test(input,expect,481))
    
    def test482(self):  
        input = """
        Class A{ }
        Class C{
            func(v:Int){
                Var b:A;
                Var c: Array[Boolean,5] = Array(False,True);
            }
        }
        """
        expect = "[]" 
        self.assertTrue(TestChecker.test(input,expect,482))
    
    def test483(self):  
        input = """
        Class A { }
        Class C{
            Val a : Int;
            func(v:Int){ }
        }
        """
        expect = "Illegal Constant Expression: None" 
        self.assertTrue(TestChecker.test(input,expect,483))
    
    def test484(self):  
        input = """
        Class A { }
        Class C{
            Val arr:Array[Int,4] = Array("a",2);
            Val d:A;
            Val c:Boolean = ! True;
            Val b:Int = 5 + 5;
            func(v:Int){ }
        }
        """
        expect = "Illegal Array Literal: [StringLit(a),IntLit(2)]" 
        self.assertTrue(TestChecker.test(input,expect,484))
    
    def test485(self):  
        input = """
        Class A { }
        Class C{
            Val arr:Array[Int,4] = Array(1,2);
            Val d:A;
            Val c:Boolean = ! True;
            Val b:Float = 5 + 5;
            Val a : Int = Self.b + 5.5;
            func(v:Int){ }
        }
        """
        expect = "Type Mismatch In Constant Declaration: AttributeDecl(Instance,ConstDecl(Id(a),IntType,BinaryOp(+,FieldAccess(Self(),Id(b)),FloatLit(5.5))))" 
        self.assertTrue(TestChecker.test(input,expect,485))
    
    def test486(self):  
        input = """
        Class A { }
        Class C{
            Var arr:Array[Int,4] = Array(1,2);
            Var d:A;
            Var c:Boolean = ! True;
            Var b:Float = 5 + 5;
            Var a : Int = Self.b + 5.5;
            func(v:Int){ }
        }
        """
        expect = "Type Mismatch In Statement: AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,FieldAccess(Self(),Id(b)),FloatLit(5.5))))" 
        self.assertTrue(TestChecker.test(input,expect,486))
    
    def test487(self):  
        input = """
        Class A { }
        Class C{
            Var arr:Array[Int,4] ;
            Var d:A;
            Var c:Boolean;
            Var b:Float ;
            Var a : Float = Self.b + 5.5;
            func(v:Int){ }
        }
        """
        expect = "[]" 
        self.assertTrue(TestChecker.test(input,expect,487))

    # ### Illegal Member Access ###

    def test488(self):  
        input = """
        Class A { 
            Var $i:Int;
        }
        Class C{
            func(v:Int){ 
                Var b:Int;
                Var obj:A;
                b = obj::$i;
            }
        }
        """
        expect = "Illegal Member Access: FieldAccess(Id(obj),Id($i))" 
        self.assertTrue(TestChecker.test(input,expect,488))
    
    def test489(self):  
        input = """
        Class A { 
            Var i:Int;
        }
        Class C{
            Var obj:A; 
            func(v:Int){ 
                Var b:Int;
                b = A.i;
            }
        }
        """
        expect = "Illegal Member Access: FieldAccess(Id(A),Id(i))" 
        self.assertTrue(TestChecker.test(input,expect,489))
    
    def test490(self):  
        input = """
        Class B { 
            Var $i:Int;
        }
        Class C{
            Var obj:B; 
            func(v:Int){ 
                Var b:Int;
                b = A::$i;
            }
        }
        """
        expect = "Undeclared Class: A" 
        self.assertTrue(TestChecker.test(input,expect,490))
    
    def test491(self):  
        input = """
        Class B { 
            Var $i:Int;
            Val b:Int = 5;
        }
        Class C{
            Var obj:B; 
            func(v:Int){ 
                v = obj.i;
            }
        }
        """
        expect = "Undeclared Identifier: obj" 
        self.assertTrue(TestChecker.test(input,expect,491))
    
    ### No Entry Point ### 

    def test492(self):  
        input = """
        Class Program { 
            main( ) { 
                
            }
        }
        """
        expect = "[]" 
        self.assertTrue(TestChecker.test(input,expect,492))
    
    def test493(self):  
        input = """
        Class Program { 
            Var a:Int;
            Var main:Int=Self.a;
            main(x:Int ) { }
        }
        """
        expect = "No Entry Point" 
        self.assertTrue(TestChecker.test(input,expect,493))
    
    def test494(self):  
        input = """
        Class Program { 
            fun( ) { }
        }
        """
        expect = "No Entry Point" 
        self.assertTrue(TestChecker.test(input,expect,494))
    
    def test495(self):  
        input = """
        Class Program { 
            main( ) { 
                Return 1;
            }
        }
        """
        expect = "No Entry Point" 
        self.assertTrue(TestChecker.test(input,expect,495))
    
    def test496(self):  
        input = """
        Class Program { 
            main( ) { 
                If (True == False){
                    Return;
                }
            }
        }
        """
        expect = "[]" 
        self.assertTrue(TestChecker.test(input,expect,496))
    
    def test497(self):  
        input = """
        
        Class Animal { 
            Var b:Int;
            Constructor(x:Float){ }
        }
        Class Dog{
            Var c:Int;
            Val d:Animal = New Animal (Self.c) ;
            Val d2:Animal = New Animal ("str") ;
            f(){            }
        }
        """
        expect = "Type Mismatch In Expression: NewExpr(Id(Animal),[StringLit(str)])" 
        self.assertTrue(TestChecker.test(input,expect,497))
    
    def test498(self):  
        input = """
        
        Class Animal { 
            Var b:Int;
            Constructor(x:Int){

            }
        }
        Class Dog{
            f(){
                Val d:Animal = New Animal () ;
            }
        }
        """
        expect = "Type Mismatch In Expression: NewExpr(Id(Animal),[])" 
        self.assertTrue(TestChecker.test(input,expect,498))
    
    def test499(self):  
        input = """
        Class Animal { 
            Var b:Int;
            Constructor(x:Int){  }
        }
        Class Dog{
            f(){
                Var x,y:Int;
                Val d:Animal = New Animal (x,y) ;
            }
        }
        """
        expect = "Type Mismatch In Expression: NewExpr(Id(Animal),[Id(x),Id(y)])" 
        self.assertTrue(TestChecker.test(input,expect,499))

    # test on Bkel #
    
#     def test500(self):  
#         input = Program([
#         ClassDecl(
#             Id("Program"),
#             [
#                 MethodDecl(
#                     Static(),
#                     Id("main"),
#                     [],
#                     Block([])
#                 ),
#                 AttributeDecl(
#                     Instance(),
#                     VarDecl(
#                         Id("myVar"),
#                         StringType(),
#                         StringLiteral("Hello World")
#                     )
#                 ),
#                 AttributeDecl(
#                     Instance(),
#                     VarDecl(
#                         Id("myVar"),
#                         IntType()
#                     )
#                 )
#             ]
#         )
#     ]
# )
#         expect = "Redeclared Attribute: myVar" 
#         self.assertTrue(TestChecker.test(input,expect,500))
    