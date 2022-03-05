import unittest
from TestUtils import TestAST
from AST import *
# Le Duc Cam - 1952588
class ASTGenSuite(unittest.TestCase):
    def test_class_decl0(self):
        input = """Class Test { }"""
        expect = "Program([ClassDecl(Id(Test),[])])"
        self.assertTrue(TestAST.test(input,expect,300))

    def test_class_decl1(self):
        input = """
        Class Program{ 
            main(){ }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,301))

    def test_class_decl2(self):
        input = """Class Test : Cam { }"""
        expect = "Program([ClassDecl(Id(Test),Id(Cam),[])])"
        self.assertTrue(TestAST.test(input,expect,302))
    
    def test_class_decl3(self):
        input = """ Class Test1{ }
                    Class Test2{ }
                    Class $Test3{} """
        expect = "Program([ClassDecl(Id(Test1),[]),ClassDecl(Id(Test2),[]),ClassDecl(Id($Test3),[])])"
        self.assertTrue(TestAST.test(input,expect,303))

    def test_class_decl4(self):
        input = """
        Class Test1{ 
        }
        Class Test2 : Cam{ }
        """
        expect = "Program([ClassDecl(Id(Test1),[]),ClassDecl(Id(Test2),Id(Cam),[])])"
        self.assertTrue(TestAST.test(input,expect,304))
    
    def test_class_decl5(self):
        input = """
        Class $Test1{ 
        }
        Class $Test2 : Cam{ }
        """
        expect = "Program([ClassDecl(Id($Test1),[]),ClassDecl(Id($Test2),Id(Cam),[])])"
        self.assertTrue(TestAST.test(input,expect,305))


    def test_method_decl1(self):
        input = """
        Class Test{
            Constructor(){ }
            Destructor(){ }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,306))

    def test_method_decl2(self):
        input = """
        Class Test{
            instance_method(){ }
            $static_method(){ }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(instance_method),Instance,[],Block([])),MethodDecl(Id($static_method),Static,[],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,307))
    


    def test_method_decl3(self):
        input = """
        Class Test{
            Constructor(a,b : Int){ 
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,308))

    def test_method_decl4(self):
        input = """
        Class Test{
            Cam(a,b : Int;c:Float){ 
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(Cam),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,309))

    def test_method_decl5(self):
        input = """
        Class Test{
            Cam(a:Int;b:Float;c,d:String;e,f,g:Boolean){ 
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(Cam),Instance,[param(Id(a),IntType),param(Id(b),FloatType),param(Id(c),StringType),param(Id(d),StringType),param(Id(e),BoolType),param(Id(f),BoolType),param(Id(g),BoolType)],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,310))

    def test_method_decl6(self):
        input = """
        Class $Test{
            $Cam(a,b,c : Int; d:Int;e,f:Int){    }
        }
        """
        expect = "Program([ClassDecl(Id($Test),[MethodDecl(Id($Cam),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),IntType),param(Id(e),IntType),param(Id(f),IntType)],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,311))

    def test_attribute_decl1(self):
        input = """
        Class Test {
            Val a,b,c:Int;
        }
        """
        expect = 'Program([ClassDecl(Id(Test),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,None)),AttributeDecl(Instance,ConstDecl(Id(b),IntType,None)),AttributeDecl(Instance,ConstDecl(Id(c),IntType,None))])])'
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_attribute_decl2(self):
        input = """
        Class Test {
            Val a,$b:Int;
        }
        """
        expect = 'Program([ClassDecl(Id(Test),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,None)),AttributeDecl(Static,ConstDecl(Id($b),IntType,None))])])'
        self.assertTrue(TestAST.test(input, expect, 313))
    
    def test_attribute_decl3(self):
        input = """
        Class Test {
            Var a,$b:Float;
        }
        """
        expect = 'Program([ClassDecl(Id(Test),[AttributeDecl(Instance,VarDecl(Id(a),FloatType)),AttributeDecl(Static,VarDecl(Id($b),FloatType))])])'
        self.assertTrue(TestAST.test(input, expect, 314))
    
    def test_attribute_decl4(self):
        input = """
        Class Test {
            Var a,$b:Float ;
            Val a,$b:Float;
        }
        """
        expect = 'Program([ClassDecl(Id(Test),[AttributeDecl(Instance,VarDecl(Id(a),FloatType)),AttributeDecl(Static,VarDecl(Id($b),FloatType)),AttributeDecl(Instance,ConstDecl(Id(a),FloatType,None)),AttributeDecl(Static,ConstDecl(Id($b),FloatType,None))])])'
        self.assertTrue(TestAST.test(input, expect, 315))
    
    def test_attribute_decl5(self):
        input = """
        Class Test{
            Var a,$b :Int = 0x12,2+3;
        }
        """
        expect = "Program([ClassDecl(Id(Test),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(18))),AttributeDecl(Static,VarDecl(Id($b),IntType,BinaryOp(+,IntLit(2),IntLit(3))))])])"
        self.assertTrue(TestAST.test(input,expect,316))
    
    def test_attribute_decl6(self):
        input = """
        Class Test{
            Val a,$b :Int = 0b11,2*7;
        }
        """
        expect = "Program([ClassDecl(Id(Test),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(3))),AttributeDecl(Static,ConstDecl(Id($b),IntType,BinaryOp(*,IntLit(2),IntLit(7))))])])"
        self.assertTrue(TestAST.test(input,expect,317))
    
    def test_attribute_decl7(self):
        input = """
        Class Test{
            Var a:Array[Boolean,5] = Array(1,1,1,1,0);
            Destructor(){ }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,BoolType),[IntLit(1),IntLit(1),IntLit(1),IntLit(1),IntLit(0)])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,318))
    
    def test_attribute_decl8(self):
        input = """
        Class Test{
            Var a : ClassType = New ClassType(2,7);
            Constructor() { }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(ClassType)),NewExpr(Id(ClassType),[IntLit(2),IntLit(7)]))),MethodDecl(Id(Constructor),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,319))

    def test_var_const_decl1(self):
        input = """
        Class Test{
            Var a : ClassType = New ClassType();
            Constructor() { 
                Var b,c:Int;
                Val d:Float;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(ClassType)),NewExpr(Id(ClassType),[]))),MethodDecl(Id(Constructor),Instance,[],Block([VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),ConstDecl(Id(d),FloatType,None)]))])])"
        self.assertTrue(TestAST.test(input,expect,320))
    
    def test_var_const_decl2(self):
        input = """
        Class Test{
            Var a : ClassType = New ClassType();
            Constructor() { 
                Var b,c:Boolean;
                Val d:Float;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(ClassType)),NewExpr(Id(ClassType),[]))),MethodDecl(Id(Constructor),Instance,[],Block([VarDecl(Id(b),BoolType),VarDecl(Id(c),BoolType),ConstDecl(Id(d),FloatType,None)]))])])"
        self.assertTrue(TestAST.test(input,expect,321))
   
    def test_var_const_decl3(self):
        input = """
        Class Test{
            Constructor() { 
                Var b,c:Boolean = 1,0;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(Constructor),Instance,[],Block([VarDecl(Id(b),BoolType,IntLit(1)),VarDecl(Id(c),BoolType,IntLit(0))]))])])"
        self.assertTrue(TestAST.test(input,expect,322))
    
    def test_var_const_decl4(self):
        input = """
        Class Test{
            method1() { 
                Var b:String = "string";
            }
            $method2(){
                Val c:Int = 0b11 + 01;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(method1),Instance,[],Block([VarDecl(Id(b),StringType,StringLit(string))])),MethodDecl(Id($method2),Static,[],Block([ConstDecl(Id(c),IntType,BinaryOp(+,IntLit(3),IntLit(1)))]))])])"
        self.assertTrue(TestAST.test(input,expect,323))
    
    def test_stmt1(self):
        input = """
        Class Test{
            Constructor() { 
                a=1;
                Self.a=2-7;
                ClassA.a = ClassA::$b = d = 27 ;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(Id(a),IntLit(1)),AssignStmt(FieldAccess(Self(),Id(a)),BinaryOp(-,IntLit(2),IntLit(7))),AssignStmt(AssignStmt(AssignStmt(FieldAccess(Id(ClassA),Id(a)),FieldAccess(Id(ClassA),Id($b))),Id(d)),IntLit(27))]))])])"
        self.assertTrue(TestAST.test(input,expect,324))
    
    def test_stmt2(self):
        input = """
        Class Test{
            Constructor() { 
                a[0][1][2]=1;
                Self.a=a[1];
                ClassA.a[0] = ClassA::$b[1] = 27 ;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(0),IntLit(1),IntLit(2)]),IntLit(1)),AssignStmt(FieldAccess(Self(),Id(a)),ArrayCell(Id(a),[IntLit(1)])),AssignStmt(AssignStmt(ArrayCell(FieldAccess(Id(ClassA),Id(a)),[IntLit(0)]),ArrayCell(FieldAccess(Id(ClassA),Id($b)),[IntLit(1)])),IntLit(27))]))])])"
        self.assertTrue(TestAST.test(input,expect,325))
    
    def test_stmt3(self):
        input = """
        Class Test{
            Constructor() { 
                a[0][1][2]= !b || c;
                d[1].e = g[1] && ("h" ==. "i");
            }
        }
        """

        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(0),IntLit(1),IntLit(2)]),BinaryOp(||,UnaryOp(!,Id(b)),Id(c))),AssignStmt(FieldAccess(ArrayCell(Id(d),[IntLit(1)]),Id(e)),BinaryOp(&&,ArrayCell(Id(g),[IntLit(1)]),BinaryOp(==.,StringLit(h),StringLit(i))))]))])])"
        self.assertTrue(TestAST.test(input,expect,326))
    
    def test_stmt4(self):
        input = """
        Class Test{
            Constructor() { 
                a[5%3-1][1+2]= b/c;
                $d[1*2*7].e = ("h" +. "i");
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(ArrayCell(Id(a),[BinaryOp(-,BinaryOp(%,IntLit(5),IntLit(3)),IntLit(1)),BinaryOp(+,IntLit(1),IntLit(2))]),BinaryOp(/,Id(b),Id(c))),AssignStmt(FieldAccess(ArrayCell(Id($d),[BinaryOp(*,BinaryOp(*,IntLit(1),IntLit(2)),IntLit(7))]),Id(e)),BinaryOp(+.,StringLit(h),StringLit(i)))]))])])"
        self.assertTrue(TestAST.test(input,expect,327))
    
    def test_stmt5(self):
        input = """
        Class Test{
            Destructor() { 
                Foreach (i In 1 .. 100 By 2) {
                    i = Array(1,2,3);
                }
                Foreach (x In 3 .. 27 ) {
                    x = Array("a","b");
                }   
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(Destructor),Instance,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([AssignStmt(Id(i),[IntLit(1),IntLit(2),IntLit(3)])])]),For(Id(x),IntLit(3),IntLit(27),IntLit(1),Block([AssignStmt(Id(x),[StringLit(a),StringLit(b)])])])]))])])"
        self.assertTrue(TestAST.test(input,expect,328))
    
    def test_stmt6(self):
        input = """
        Class Test{
            testForLoop() { 
                Foreach (i In 1 .. 100 By 2) {
                    Foreach (x In 3 .. 27 ) {
                        x = Array(0B11,0X11);
                    }   
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(testForLoop),Instance,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([For(Id(x),IntLit(3),IntLit(27),IntLit(1),Block([AssignStmt(Id(x),[IntLit(3),IntLit(17)])])])])])]))])])"
        self.assertTrue(TestAST.test(input,expect,329))
    
    def test_stmt7(self):
        input = """
        Class Test{
            $testForLoop() { 
                Foreach (i In 1 .. 100 By 2) {
                    Break;
                    Continue; a=b;
                    Return;
                }
                Return exprs;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id($testForLoop),Static,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([Break,Continue,AssignStmt(Id(a),Id(b)),Return()])]),Return(Id(exprs))]))])])"
        self.assertTrue(TestAST.test(input,expect,330))
    
    def test_stmt8(self):
        input = """
        Class Test{
            $testMethodInvocate() { 
                Foreach (i In -5 .. 100 By 5) {
                    class.func1(27,"cam",True);
                    Self.func2();
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id($testMethodInvocate),Static,[],Block([For(Id(i),UnaryOp(-,IntLit(5)),IntLit(100),IntLit(5),Block([Call(Id(class),Id(func1),[IntLit(27),StringLit(cam),BooleanLit(True)]),Call(Self(),Id(func2),[])])])]))])])"
        self.assertTrue(TestAST.test(input,expect,331))
    
    def test_stmt9(self):
        input = """
        Class Test{
            $testMethodInvocate() { 
                Foreach (i In -5 .. 100 By 5) {
                    i = class.func1(27,"cam",True);
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id($testMethodInvocate),Static,[],Block([For(Id(i),UnaryOp(-,IntLit(5)),IntLit(100),IntLit(5),Block([AssignStmt(Id(i),CallExpr(Id(class),Id(func1),[IntLit(27),StringLit(cam),BooleanLit(True)]))])])]))])])"
        self.assertTrue(TestAST.test(input,expect,332))
    
    def test_stmt10(self):
        input = """
        Class Test{
            testIf() { 
                If(a>b){ }
                
                If (a<b){ } 
                Else { }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(testIf),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([])),If(BinaryOp(<,Id(a),Id(b)),Block([]),Block([]))]))])])"
        self.assertTrue(TestAST.test(input,expect,333))
    
    def test_stmt11(self):
        input = """
        Class Test{
            testIf() {     
                If (a>=b){ }
                Elseif (a==b){ }
                Elseif (a!=b) { }
                Elseif ( a<=b){ }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(testIf),Instance,[],Block([If(BinaryOp(>=,Id(a),Id(b)),Block([]),If(BinaryOp(==,Id(a),Id(b)),Block([]),If(BinaryOp(!=,Id(a),Id(b)),Block([]),If(BinaryOp(<=,Id(a),Id(b)),Block([])))))]))])])"
        self.assertTrue(TestAST.test(input,expect,334))
    
    def test_stmt12(self):
        input = """
        Class Test{
            testIff() {     
                If (a>b){ }
                Elseif (a<b){ }
                Elseif (a==b) { }
                Else { }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(testIff),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([]),If(BinaryOp(<,Id(a),Id(b)),Block([]),If(BinaryOp(==,Id(a),Id(b)),Block([]),Block([]))))]))])])"
        self.assertTrue(TestAST.test(input,expect,335))
    
    def test_stmt13(self):
        input = """
        Class Test{
            testIf() {     
                If(a>b){
                    c = Array(Array(1,2),Array(3,4));
                }
                If (a<b){ 
                    c = 2+7;
                } 
                Else { 
                    c = 2/7;
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(testIf),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(c),[[IntLit(1),IntLit(2)],[IntLit(3),IntLit(4)]])])),If(BinaryOp(<,Id(a),Id(b)),Block([AssignStmt(Id(c),BinaryOp(+,IntLit(2),IntLit(7)))]),Block([AssignStmt(Id(c),BinaryOp(/,IntLit(2),IntLit(7)))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,336))
    
    def test_stmt14(self):
        input = """
        Class Test{
            testIf() {     
                If(a>b){
                    c = d = 2;
                    d = 5%7;
                    e = 4-3;
                }
                If (a<b){ 
                    c = 2+7;
                    c = -2;
                } 
                Else { 
                    c = -2/7;
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(testIf),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(AssignStmt(Id(c),Id(d)),IntLit(2)),AssignStmt(Id(d),BinaryOp(%,IntLit(5),IntLit(7))),AssignStmt(Id(e),BinaryOp(-,IntLit(4),IntLit(3)))])),If(BinaryOp(<,Id(a),Id(b)),Block([AssignStmt(Id(c),BinaryOp(+,IntLit(2),IntLit(7))),AssignStmt(Id(c),UnaryOp(-,IntLit(2)))]),Block([AssignStmt(Id(c),BinaryOp(/,UnaryOp(-,IntLit(2)),IntLit(7)))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,337))
    
    def test_stmt15(self):
        input = """
        Class Test{
            test() {     
                If(a>b){
                    Var a :Int = 5%7; 
                    e = 4-3;
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(test),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([VarDecl(Id(a),IntType,BinaryOp(%,IntLit(5),IntLit(7))),AssignStmt(Id(e),BinaryOp(-,IntLit(4),IntLit(3)))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,338))
    
    def test_stmt16(self):
        input = """
        Class Test{
            Var $b,c:Int;
            test() {     
                Val a :Int = 5%7; 
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[AttributeDecl(Static,VarDecl(Id($b),IntType)),AttributeDecl(Instance,VarDecl(Id(c),IntType)),MethodDecl(Id(test),Instance,[],Block([ConstDecl(Id(a),IntType,BinaryOp(%,IntLit(5),IntLit(7)))]))])])"
        self.assertTrue(TestAST.test(input,expect,339))
    
    def test_stmt17(self):
        input = """
        Class Test{
            test() {     
                Val a :Int ; 
                Var b,c:Bool = False,True;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(test),Instance,[],Block([ConstDecl(Id(a),IntType,None),VarDecl(Id(b),ClassType(Id(Bool)),BooleanLit(False)),VarDecl(Id(c),ClassType(Id(Bool)),BooleanLit(True))]))])])"
        self.assertTrue(TestAST.test(input,expect,340))
    
    def test_stmt18(self):
        input = """
        Class Test{
            test(a,b:String) {     
                If ( a+b > c){
                    If ( d*e > -a[0]){
                        Return;
                    }
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(test),Instance,[param(Id(a),StringType),param(Id(b),StringType)],Block([If(BinaryOp(>,BinaryOp(+,Id(a),Id(b)),Id(c)),Block([If(BinaryOp(>,BinaryOp(*,Id(d),Id(e)),UnaryOp(-,ArrayCell(Id(a),[IntLit(0)]))),Block([Return()]))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,341))
    
    def test_stmt19(self):
        input = """
        Class Test{
            test() {     
                Val a : Float = Null;
                Var a : ClassX = Null; 
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(test),Instance,[],Block([ConstDecl(Id(a),FloatType,NullLiteral()),VarDecl(Id(a),ClassType(Id(ClassX)),NullLiteral())]))])])"
        self.assertTrue(TestAST.test(input,expect,342))
    
    def test_stmt20(self):
        input = """
        Class Test{
            test() {     
                Val a : ClassX;
                Var a : ClassX = New ClassX(); 
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(test),Instance,[],Block([ConstDecl(Id(a),ClassType(Id(ClassX)),None),VarDecl(Id(a),ClassType(Id(ClassX)),NewExpr(Id(ClassX),[]))]))])])"
        self.assertTrue(TestAST.test(input,expect,343))
    
    
    def test_stmt21(self):
        input = """
        Class Test{
            test() {     
                If ( a+ b.member  > classx.fun() ){
                    
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(test),Instance,[],Block([If(BinaryOp(>,BinaryOp(+,Id(a),FieldAccess(Id(b),Id(member))),CallExpr(Id(classx),Id(fun),[])),Block([]))]))])])"
        self.assertTrue(TestAST.test(input,expect,344))
    
    def test_stmt22(self):
        input = """
        Class Test{
            main() {     
                If ( a+ b.member  > classx::$fun() ){
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],Block([If(BinaryOp(>,BinaryOp(+,Id(a),FieldAccess(Id(b),Id(member))),CallExpr(Id(classx),Id($fun),[])),Block([]))]))])])"
        self.assertTrue(TestAST.test(input,expect,345))
    
    def test_stmt23(self):
        input = """
        Class Test{
            main() {     
                If ( d*classz::$f > 1){ }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],Block([If(BinaryOp(>,BinaryOp(*,Id(d),FieldAccess(Id(classz),Id($f))),IntLit(1)),Block([]))]))])])"
        self.assertTrue(TestAST.test(input,expect,346))
    
    def test_stmt24(self):
        input = """
        Class Test{
            main() {     
                Self.main(ClassX.func(1));
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],Block([Call(Self(),Id(main),[CallExpr(Id(ClassX),Id(func),[IntLit(1)])])]))])])"
        self.assertTrue(TestAST.test(input,expect,347))
    
    def test_stmt25(self):
        input = """
        Class Test{
            main() {     
                Self.main(ClassX.func(1)+ClassY::$var);
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],Block([Call(Self(),Id(main),[BinaryOp(+,CallExpr(Id(ClassX),Id(func),[IntLit(1)]),FieldAccess(Id(ClassY),Id($var)))])]))])])"
        self.assertTrue(TestAST.test(input,expect,348))

    def test_stmt26(self):
        input = """
        Class Test{
            main() {     
                Self.m(ClassX.func(Self.a)+ClassY::$var(a||True));
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],Block([Call(Self(),Id(m),[BinaryOp(+,CallExpr(Id(ClassX),Id(func),[FieldAccess(Self(),Id(a))]),CallExpr(Id(ClassY),Id($var),[BinaryOp(||,Id(a),BooleanLit(True))]))])]))])])"
        self.assertTrue(TestAST.test(input,expect,349))
    
    def test_stmt27(self):
        input = """
        Class Test{
            main() {     
                Foreach (i In Self.a( b.c( d.e() ) ) .. x::$y By 5 ){
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],Block([For(Id(i),CallExpr(Self(),Id(a),[CallExpr(Id(b),Id(c),[CallExpr(Id(d),Id(e),[])])]),FieldAccess(Id(x),Id($y)),IntLit(5),Block([])])]))])])"
        self.assertTrue(TestAST.test(input,expect,350))
    
    def test_stmt28(self):
        input = """
        Class Test{
            main() {     
                uh = Self.main(Self.func(1)+ClassY::$var);
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(uh),CallExpr(Self(),Id(main),[BinaryOp(+,CallExpr(Self(),Id(func),[IntLit(1)]),FieldAccess(Id(ClassY),Id($var)))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,351))
    
    def test52(self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;
            $getNumOfShape() {
                Return $numOfShape;
            }
        }
        Class Rectangle: Shape {
            getArea() {
                Return Self.length * Self.width;
            }
        }

        """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(Id($numOfShape))]))]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"
        self.assertTrue(TestAST.test(input,expect,352))
    
    def test53(self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;
            $getNumOfShape() {
                Return $numOfShape;
            }
        }
        Class Program {
            main() {
                Out.printInt(Shape::$numOfShape);
            }
        }
        """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(Id($numOfShape))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))])]))])])"
        self.assertTrue(TestAST.test(input,expect,353))

    def test54(self):
        input = """Class Program {
            main() {
                Self.b.method(2*3);
                ClassX::$b.method(param);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(FieldAccess(Self(),Id(b)),Id(method),[BinaryOp(*,IntLit(2),IntLit(3))]),Call(FieldAccess(Id(ClassX),Id($b)),Id(method),[Id(param)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 354))
    
    def test55(self):
        input = """Class Program {
            main() {
                Self.method(Self.b);
                ClassX::$b.method(ClassY::$e);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Self(),Id(method),[FieldAccess(Self(),Id(b))]),Call(FieldAccess(Id(ClassX),Id($b)),Id(method),[FieldAccess(Id(ClassY),Id($e))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 355))
    
    def test56(self):
        input = """Class Program {
            Var y:ClassX;
            Val $y:ClassY;
            Val y:ClassZ=Null;
            main() {
                Var x:ClassY;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(y),ClassType(Id(ClassX)),NullLiteral())),AttributeDecl(Static,ConstDecl(Id($y),ClassType(Id(ClassY)),None)),AttributeDecl(Instance,ConstDecl(Id(y),ClassType(Id(ClassZ)),NullLiteral())),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(x),ClassType(Id(ClassY)),NullLiteral())]))])])"
        self.assertTrue(TestAST.test(input, expect, 356))
    
    def test57(self):
        input = """Class Program {
            Var y:Array[ClassX,5];
            main() {
                Var y:Array[ClassX,5];
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(y),ArrayType(5,ClassType(Id(ClassX))))),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(y),ArrayType(5,ClassType(Id(ClassX))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 357))
    
    def test58(self):
        input = """Class Program {
            main() {
                Self.Call(classY::$a[1][2],classX.a[5]);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Self(),Id(Call),[ArrayCell(FieldAccess(Id(classY),Id($a)),[IntLit(1),IntLit(2)]),ArrayCell(FieldAccess(Id(classX),Id(a)),[IntLit(5)])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 358))
    
    def test59(self):
        input = """Class Program1 {
            main() {
                id = Self.Call().text;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program1),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(id),FieldAccess(CallExpr(Self(),Id(Call),[]),Id(text)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 359))

    def test60(self):
        input = """Class Program1 {
            main() {
                id = Self.Call(ClassX::$y().t);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program1),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(id),CallExpr(Self(),Id(Call),[FieldAccess(CallExpr(Id(ClassX),Id($y),[]),Id(t))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 360))
    
    def test61(self):
        input = """Class Program1 {
            main() {
                classZ.Call(ClassX::$y().t).text();
            }
        }"""
        expect = "Program([ClassDecl(Id(Program1),[MethodDecl(Id(main),Instance,[],Block([Call(CallExpr(Id(classZ),Id(Call),[FieldAccess(CallExpr(Id(ClassX),Id($y),[]),Id(t))]),Id(text),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 361))
    
    def test62(self):
        input = """Class Program1 {
            main() {
                id = classZ.Call().text();
            }
        }"""
        expect = "Program([ClassDecl(Id(Program1),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(id),CallExpr(CallExpr(Id(classZ),Id(Call),[]),Id(text),[]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 362))


    def test63(self):
        input = """Class Program {
            Main() {
                Return;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(Main),Instance,[],Block([Return()]))])])"
        self.assertTrue(TestAST.test(input, expect, 363))
    
    def test64(self):
        input = """Class program {
            main() {
                Return;
            }
        }"""
        expect = "Program([ClassDecl(Id(program),[MethodDecl(Id(main),Instance,[],Block([Return()]))])])"
        self.assertTrue(TestAST.test(input, expect, 364))

    def test65(self):
        input = """Class Program {
            main() {
                Return;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Return()]))])])"
        self.assertTrue(TestAST.test(input, expect, 365))
    
    def test66(self):
        input = """Class Program {
            main() {
                Return;
            }
            main(a:Int){ }
            $main(){ }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Return()])),MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([])),MethodDecl(Id($main),Static,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 366))

    def test67(self):
        input = """Class Program {
            main() {
                Return;
            }
            main(b:Int){ }
            main(){ }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Return()])),MethodDecl(Id(main),Instance,[param(Id(b),IntType)],Block([])),MethodDecl(Id(main),Static,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 367))
    
    def test68(self):
        input = """Class Program {
            main() {
                (a[1]).func();
                a[1] = 1;
                Out.println(a.a[1]);
                Return;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(ArrayCell(Id(a),[IntLit(1)]),Id(func),[]),AssignStmt(ArrayCell(Id(a),[IntLit(1)]),IntLit(1)),Call(Id(Out),Id(println),[ArrayCell(FieldAccess(Id(a),Id(a)),[IntLit(1)])]),Return()]))])])"
        self.assertTrue(TestAST.test(input, expect, 368))
    
    def test69(self):
        input = """
        Class Program {
            main_a () {
                Self.b.c.a(b,3,c,2*5);
                (classA.a[1][2][3]).foo(2,b);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main_a),Instance,[],Block([Call(FieldAccess(FieldAccess(Self(),Id(b)),Id(c)),Id(a),[Id(b),IntLit(3),Id(c),BinaryOp(*,IntLit(2),IntLit(5))]),Call(ArrayCell(FieldAccess(Id(classA),Id(a)),[IntLit(1),IntLit(2),IntLit(3)]),Id(foo),[IntLit(2),Id(b)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 369))

    def test70(self):
        input = """
        Class Program {
            main_a () {
                classA.a[1][2][3].foo(2/c,b);
                MotorBike::$ab.foo();
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main_a),Instance,[],Block([Call(ArrayCell(FieldAccess(Id(classA),Id(a)),[IntLit(1),IntLit(2),IntLit(3)]),Id(foo),[BinaryOp(/,IntLit(2),Id(c)),Id(b)]),Call(FieldAccess(Id(MotorBike),Id($ab)),Id(foo),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 370))
    
    def test71(self):
        input = """Class C{
            Var _9c2, $_: l_;
            foo(){
                Val a,b:ClassX;
            }
        }"""
        expect = "Program([ClassDecl(Id(C),[AttributeDecl(Instance,VarDecl(Id(_9c2),ClassType(Id(l_)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(l_)),NullLiteral())),MethodDecl(Id(foo),Instance,[],Block([ConstDecl(Id(a),ClassType(Id(ClassX)),None),ConstDecl(Id(b),ClassType(Id(ClassX)),None)]))])])"
        self.assertTrue(TestAST.test(input, expect, 371))
    
    def test72(self):
        input = """
        Class Program {
            main_a () {
                MotorBike::$ab.foo(b+2,c-2);
                (MotorBike::$a.a[1][2]).foo(27);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main_a),Instance,[],Block([Call(FieldAccess(Id(MotorBike),Id($ab)),Id(foo),[BinaryOp(+,Id(b),IntLit(2)),BinaryOp(-,Id(c),IntLit(2))]),Call(ArrayCell(FieldAccess(FieldAccess(Id(MotorBike),Id($a)),Id(a)),[IntLit(1),IntLit(2)]),Id(foo),[IntLit(27)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 372))
    
    def test73(self):
        input = """
        Class Program {
            main_a () {
                ClassX.vl(cam);
                ClassY::$a(27);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main_a),Instance,[],Block([Call(Id(ClassX),Id(vl),[Id(cam)]),Call(Id(ClassY),Id($a),[IntLit(27)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 373))
    
    def test74(self):
        input = """
        Class Program {
            main_a () {
                a.b::$c(cam);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main_a),Instance,[],Block([Call(FieldAccess(Id(a),Id(b)),Id($c),[Id(cam)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 374))
 
    def test75(self):
        input = """
        Class Program {
            main_a () {
                a::$b.c(cam);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main_a),Instance,[],Block([Call(FieldAccess(Id(a),Id($b)),Id(c),[Id(cam)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 375))
 

    def test76(self):
        input = """
        Class Program {
            main () {
                uh = Self.a.b.c.d;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(uh),FieldAccess(FieldAccess(FieldAccess(FieldAccess(Self(),Id(a)),Id(b)),Id(c)),Id(d)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 376))

    def test77(self):
        input = """
        Class Program {
            main_a () {
                uh = u.h;
                oh = o::$h;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main_a),Instance,[],Block([AssignStmt(Id(uh),FieldAccess(Id(u),Id(h))),AssignStmt(Id(oh),FieldAccess(Id(o),Id($h)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 377))
    
    def test78(self):
        input = """Class C {
                foo(){
                    Var a,b:Array[Array[Int,4],4];
                    a[b[4]+1] = a[0];
                } 
            }
            """
        expect = "Program([ClassDecl(Id(C),[MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),ArrayType(4,ArrayType(4,IntType))),VarDecl(Id(b),ArrayType(4,ArrayType(4,IntType))),AssignStmt(ArrayCell(Id(a),[BinaryOp(+,ArrayCell(Id(b),[IntLit(4)]),IntLit(1))]),ArrayCell(Id(a),[IntLit(0)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 378))
    
    def test79(self):
        input = """Class A:B{
                fox(){
                    a.a.a[0][1].func(a,b);
                    (a.a[1][2][3]).foo();
                    (MotorBike::$a.a[1][2]).foo();        
                }
            }
        """
        expect = "Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(fox),Instance,[],Block([Call(ArrayCell(FieldAccess(FieldAccess(Id(a),Id(a)),Id(a)),[IntLit(0),IntLit(1)]),Id(func),[Id(a),Id(b)]),Call(ArrayCell(FieldAccess(Id(a),Id(a)),[IntLit(1),IntLit(2),IntLit(3)]),Id(foo),[]),Call(ArrayCell(FieldAccess(FieldAccess(Id(MotorBike),Id($a)),Id(a)),[IntLit(1),IntLit(2)]),Id(foo),[])]))])])"
        self.assertTrue(TestAST.test(input,expect,379))
    
    def test80(self): 
        input = """Class S {
                foox(){
                    a.foo(1*2,("b"+."c")+."a","a"==."b");
                }
            }
        """
        expect = "Program([ClassDecl(Id(S),[MethodDecl(Id(foox),Instance,[],Block([Call(Id(a),Id(foo),[BinaryOp(*,IntLit(1),IntLit(2)),BinaryOp(+.,BinaryOp(+.,StringLit(b),StringLit(c)),StringLit(a)),BinaryOp(==.,StringLit(a),StringLit(b))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 380))
    
    def test81(self): 
        input = """Class S {
                foox(){
                    a = Self.foo(1*2,"a"+.("b" >=0));
                }
            }
        """
        expect = "Program([ClassDecl(Id(S),[MethodDecl(Id(foox),Instance,[],Block([AssignStmt(Id(a),CallExpr(Self(),Id(foo),[BinaryOp(*,IntLit(1),IntLit(2)),BinaryOp(+.,StringLit(a),BinaryOp(>=,StringLit(b),IntLit(0)))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 381))
    
    def test82(self): 
        input = """Class S: A{
                foo(){
                    class.a(a&&b||(!c));
                    Return False;
                } 
            }
        """
        expect = "Program([ClassDecl(Id(S),Id(A),[MethodDecl(Id(foo),Instance,[],Block([Call(Id(class),Id(a),[BinaryOp(||,BinaryOp(&&,Id(a),Id(b)),UnaryOp(!,Id(c)))]),Return(BooleanLit(False))]))])])"
        self.assertTrue(TestAST.test(input, expect, 382))
    
    def test83(self): 
        input = """
        Class C: Cam {
            foo(){
                If (True){
                    If (0==0 && (0!=1) || (1 < (2*(3+4))) || !(4)){
                        If(a[0]>= 2+2){ }        
                    }
                }
                Return False;
            } 
        }
        """
        expect = "Program([ClassDecl(Id(C),Id(Cam),[MethodDecl(Id(foo),Instance,[],Block([If(BooleanLit(True),Block([If(BinaryOp(==,IntLit(0),BinaryOp(||,BinaryOp(||,BinaryOp(&&,IntLit(0),BinaryOp(!=,IntLit(0),IntLit(1))),BinaryOp(<,IntLit(1),BinaryOp(*,IntLit(2),BinaryOp(+,IntLit(3),IntLit(4))))),UnaryOp(!,IntLit(4)))),Block([If(BinaryOp(>=,ArrayCell(Id(a),[IntLit(0)]),BinaryOp(+,IntLit(2),IntLit(2))),Block([]))]))])),Return(BooleanLit(False))]))])])"
        self.assertTrue(TestAST.test(input, expect, 383))
    
    def test84(self):
        input = """Class C{
                foo(){
                    Var arr : Array[Array[Shape,4],5];
                }
            }
        """
        expect = "Program([ClassDecl(Id(C),[MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(arr),ArrayType(5,ArrayType(4,ClassType(Id(Shape)))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 384))
    
    def test85(self):
        input = """
        Class C{
                fox(){
                    Foreach (i In 0 .. arr[j][j] By 1){
                        Foreach (j In 0 .. 2-2-1 ){
                            If ((j == 4)){
                                 Var shape0 : Shape = New Shape(i);
                            }
                        }
                    }
                }
        }
        """
        expect = "Program([ClassDecl(Id(C),[MethodDecl(Id(fox),Instance,[],Block([For(Id(i),IntLit(0),ArrayCell(Id(arr),[Id(j),Id(j)]),IntLit(1),Block([For(Id(j),IntLit(0),BinaryOp(-,BinaryOp(-,IntLit(2),IntLit(2)),IntLit(1)),IntLit(1),Block([If(BinaryOp(==,Id(j),IntLit(4)),Block([VarDecl(Id(shape0),ClassType(Id(Shape)),NewExpr(Id(Shape),[Id(i)]))]))])])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 385))     
    
    def test86(self):
        input = """
        Class C{
                fox(){
                    Var x : Float = arr[1][2].area;
                    Var x : Shit = New Shit(classX::$func(),Self.a);
                }
        }
        """
        expect = "Program([ClassDecl(Id(C),[MethodDecl(Id(fox),Instance,[],Block([VarDecl(Id(x),FloatType,FieldAccess(ArrayCell(Id(arr),[IntLit(1),IntLit(2)]),Id(area))),VarDecl(Id(x),ClassType(Id(Shit)),NewExpr(Id(Shit),[CallExpr(Id(classX),Id($func),[]),FieldAccess(Self(),Id(a))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 386))  
    
        
    def test87(self):
        input = """Class Program{
                main(){
                If( a * 1 + 2 == 9 ){
                    b = a = arr[1+2+3] = Self.pi ; 
                }
                Else{
                    a = a * 3 / 27/ 2001  + 0B11; 
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(==,BinaryOp(+,BinaryOp(*,Id(a),IntLit(1)),IntLit(2)),IntLit(9)),Block([AssignStmt(AssignStmt(AssignStmt(Id(b),Id(a)),ArrayCell(Id(arr),[BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3))])),FieldAccess(Self(),Id(pi)))]),Block([AssignStmt(Id(a),BinaryOp(+,BinaryOp(/,BinaryOp(/,BinaryOp(*,Id(a),IntLit(3)),IntLit(27)),IntLit(2001)),IntLit(3)))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 387)) 
    

    def test88(self):
        input = """Class S {
                fox(){
                    a[c][d][k.foo()] = 1;
                }
                Var l,f : Int = 1 , 1 - 012;
            }
        """
        expect = "Program([ClassDecl(Id(S),[MethodDecl(Id(fox),Instance,[],Block([AssignStmt(ArrayCell(Id(a),[Id(c),Id(d),CallExpr(Id(k),Id(foo),[])]),IntLit(1))])),AttributeDecl(Instance,VarDecl(Id(l),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(f),IntType,BinaryOp(-,IntLit(1),IntLit(10))))])])"
        self.assertTrue(TestAST.test(input,expect,388))
    
    def test89(self):
        input = """
        Class Lap{
                Var $laptops: Array[Boolean, 100];
                $Refresh(){
                    Foreach(i In (ElectricalDevice::$numOfDevices*100)/100 + 1 .. 100-100+35%34 By -1){
                        (laptops[i]).refresh();
                    }
                }
                start(){
                    Laptop::$nothing();
                    Return useBattery;
                }
                stop(){
                    Self.nothing();
                    Return -useBattery;
                }
        }
        """
        expect = "Program([ClassDecl(Id(Lap),[AttributeDecl(Static,VarDecl(Id($laptops),ArrayType(100,BoolType))),MethodDecl(Id($Refresh),Static,[],Block([For(Id(i),BinaryOp(+,BinaryOp(/,BinaryOp(*,FieldAccess(Id(ElectricalDevice),Id($numOfDevices)),IntLit(100)),IntLit(100)),IntLit(1)),BinaryOp(+,BinaryOp(-,IntLit(100),IntLit(100)),BinaryOp(%,IntLit(35),IntLit(34))),UnaryOp(-,IntLit(1)),Block([Call(ArrayCell(Id(laptops),[Id(i)]),Id(refresh),[])])])])),MethodDecl(Id(start),Instance,[],Block([Call(Id(Laptop),Id($nothing),[]),Return(Id(useBattery))])),MethodDecl(Id(stop),Instance,[],Block([Call(Self(),Id(nothing),[]),Return(UnaryOp(-,Id(useBattery)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 389))
            
    def test90(self):
        input = """
        Class Laptop:Electrical{
                Constructor(weight: Float; useBat:Boolean){
                    Self.weight = weight/100;
                    Self.useBattery = useBat;
                    ElectricalDevice::$devices[ElectricalDevice::$numOfDevices] = Self;
                    Laptop::$laptops[ElectricalDevice::$numOfDevices] = Self;
                    ElectricalDevice::$numOfDevices = ElectricalDevice::$numOfDevices+1;
                }
        }
        """
        expect = "Program([ClassDecl(Id(Laptop),Id(Electrical),[MethodDecl(Id(Constructor),Instance,[param(Id(weight),FloatType),param(Id(useBat),BoolType)],Block([AssignStmt(FieldAccess(Self(),Id(weight)),BinaryOp(/,Id(weight),IntLit(100))),AssignStmt(FieldAccess(Self(),Id(useBattery)),Id(useBat)),AssignStmt(ArrayCell(FieldAccess(Id(ElectricalDevice),Id($devices)),[FieldAccess(Id(ElectricalDevice),Id($numOfDevices))]),Self()),AssignStmt(ArrayCell(FieldAccess(Id(Laptop),Id($laptops)),[FieldAccess(Id(ElectricalDevice),Id($numOfDevices))]),Self()),AssignStmt(FieldAccess(Id(ElectricalDevice),Id($numOfDevices)),BinaryOp(+,FieldAccess(Id(ElectricalDevice),Id($numOfDevices)),IntLit(1)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 390))
    
    def test91(self):
        input = """
        Class Cam{
                addStud(newStu: Student){
                    class::$studentList[Classroom::$numOfStudents] = newStu;
                } 
            }
        """
        expect = "Program([ClassDecl(Id(Cam),[MethodDecl(Id(addStud),Instance,[param(Id(newStu),ClassType(Id(Student)))],Block([AssignStmt(ArrayCell(FieldAccess(Id(class),Id($studentList)),[FieldAccess(Id(Classroom),Id($numOfStudents))]),Id(newStu))]))])])"
        self.assertTrue(TestAST.test(input, expect, 391))
    
    def test92(self):
        input = """
        Class Program{
                main(){
                    Self.print("wow");   
                }
                print(s:String){
                    Return s+."wow";    
                }
                Constructor(){
                    class::$studs = classroom::$studs + 1;
                }
                Destructor(){
                    class::$studs = 0;
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Self(),Id(print),[StringLit(wow)])])),MethodDecl(Id(print),Instance,[param(Id(s),StringType)],Block([Return(BinaryOp(+.,Id(s),StringLit(wow)))])),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Id(class),Id($studs)),BinaryOp(+,FieldAccess(Id(classroom),Id($studs)),IntLit(1)))])),MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(FieldAccess(Id(class),Id($studs)),IntLit(0))]))])])"
        self.assertTrue(TestAST.test(input, expect, 392))
    
    def test93(self):
        input = """
        Class Program{
                main(){
                    Self.print("wow");
                    { 
                        Return New classX((Self.b[1]).a);
                        Return New classY((Self.b[1]).fun());
                    } { }  
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Self(),Id(print),[StringLit(wow)]),Block([Return(NewExpr(Id(classX),[FieldAccess(ArrayCell(FieldAccess(Self(),Id(b)),[IntLit(1)]),Id(a))])),Return(NewExpr(Id(classY),[CallExpr(ArrayCell(FieldAccess(Self(),Id(b)),[IntLit(1)]),Id(fun),[])]))]),Block([])]))])])"
        self.assertTrue(TestAST.test(input, expect, 393))
    
    def test94(self):
        input = """Class P {
            mama() {
                Val cam : ClassAC = Null;
                a = New X(1 + 1, a - 3 * b, 10 / 7 + d);
                a.a = 10;
                a.b = -100.00 + a.foo();
                a.a.b[1] = Array(1, 2, 3);
                Self.print(a.a);
            }
        }"""
        expect = "Program([ClassDecl(Id(P),[MethodDecl(Id(mama),Instance,[],Block([ConstDecl(Id(cam),ClassType(Id(ClassAC)),NullLiteral()),AssignStmt(Id(a),NewExpr(Id(X),[BinaryOp(+,IntLit(1),IntLit(1)),BinaryOp(-,Id(a),BinaryOp(*,IntLit(3),Id(b))),BinaryOp(+,BinaryOp(/,IntLit(10),IntLit(7)),Id(d))])),AssignStmt(FieldAccess(Id(a),Id(a)),IntLit(10)),AssignStmt(FieldAccess(Id(a),Id(b)),BinaryOp(+,UnaryOp(-,FloatLit(100.0)),CallExpr(Id(a),Id(foo),[]))),AssignStmt(ArrayCell(FieldAccess(FieldAccess(Id(a),Id(a)),Id(b)),[IntLit(1)]),[IntLit(1),IntLit(2),IntLit(3)]),Call(Self(),Id(print),[FieldAccess(Id(a),Id(a))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 394))
    
    def test95(self):
        input = """Class P {
            mama() {
                a = b[1]::$b2.fun();
                a = a1.a2.a3.fun(P.p1.p2);
                a = (a1::$a2.a3)::$a4;
            }
        }"""
        expect = "Program([ClassDecl(Id(P),[MethodDecl(Id(mama),Instance,[],Block([AssignStmt(Id(a),CallExpr(FieldAccess(ArrayCell(Id(b),[IntLit(1)]),Id($b2)),Id(fun),[])),AssignStmt(Id(a),CallExpr(FieldAccess(FieldAccess(Id(a1),Id(a2)),Id(a3)),Id(fun),[FieldAccess(FieldAccess(Id(P),Id(p1)),Id(p2))])),AssignStmt(Id(a),FieldAccess(FieldAccess(FieldAccess(Id(a1),Id($a2)),Id(a3)),Id($a4)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 395))
    
    def test96(self):
        input = """Class P {
            mama() {
                If (True){ 
                    {
                        a1::$a2.a[3][4] = Array(Array(2,7),Array(0,3));
                        b =( b1.fun().b2.fun())::$fun2();
                    }
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(P),[MethodDecl(Id(mama),Instance,[],Block([If(BooleanLit(True),Block([Block([AssignStmt(ArrayCell(FieldAccess(FieldAccess(Id(a1),Id($a2)),Id(a)),[IntLit(3),IntLit(4)]),[[IntLit(2),IntLit(7)],[IntLit(0),IntLit(3)]]),AssignStmt(Id(b),CallExpr(CallExpr(FieldAccess(CallExpr(Id(b1),Id(fun),[]),Id(b2)),Id(fun),[]),Id($fun2),[]))])]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 396))

    def test97(self):
        input = """
        Class P {
            cam() {
                Foreach (ite In New Y(1, 2, 3) .. Self.fox().a.bar() By MotherBoard::$cap.foo()) {
                    Self.print(cam);
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(P),[MethodDecl(Id(cam),Instance,[],Block([For(Id(ite),NewExpr(Id(Y),[IntLit(1),IntLit(2),IntLit(3)]),CallExpr(FieldAccess(CallExpr(Self(),Id(fox),[]),Id(a)),Id(bar),[]),CallExpr(FieldAccess(Id(MotherBoard),Id($cap)),Id(foo),[]),Block([Call(Self(),Id(print),[Id(cam)])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 397))
    
    def test98(self):
        input = """Class C {
                foo(){
                    a = x.Y(0b11*9);
                    b = 0B10 + 012;
                    If (this != Null) {
                        sys.out.print(node.data +. " cam");
                    }
                } 
            }
            """
        expect = "Program([ClassDecl(Id(C),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(a),CallExpr(Id(x),Id(Y),[BinaryOp(*,IntLit(3),IntLit(9))])),AssignStmt(Id(b),BinaryOp(+,IntLit(2),IntLit(10))),If(BinaryOp(!=,Id(this),NullLiteral()),Block([Call(FieldAccess(Id(sys),Id(out)),Id(print),[BinaryOp(+.,FieldAccess(Id(node),Id(data)),StringLit( cam))])]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 398))
    
    def test99(self):
        input = """Class C {
                fox(){
                    Var a : Int = a.b.c.d(C.fox());
                    a = x.Y() * (-1.2e4);
                    b = 0B100110101;
                    c = 0x12AC001;
                    well.print(done);
                } 
            }
            """
        expect = "Program([ClassDecl(Id(C),[MethodDecl(Id(fox),Instance,[],Block([VarDecl(Id(a),IntType,CallExpr(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(d),[CallExpr(Id(C),Id(fox),[])])),AssignStmt(Id(a),BinaryOp(*,CallExpr(Id(x),Id(Y),[]),UnaryOp(-,FloatLit(12000.0)))),AssignStmt(Id(b),IntLit(309)),AssignStmt(Id(c),IntLit(19578881)),Call(Id(well),Id(print),[Id(done)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 399))
    
    # def test100(self):
    #     input = """Class Program {
    #             main(){
    #                 Return 1;
    #             } 
    #             main(){
    #                 If (True){
    #                     Return 1;
    #                 }
    #             } 
    #             main(){
    #                 Return ;
    #             } 
    #             main(){
    #             } 
    #         }
    #         """
    #     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[],Block([Return(IntLit(1))])),MethodDecl(Id(main),Instance,[],Block([If(BooleanLit(True),Block([Return(IntLit(1))]))])),MethodDecl(Id(main),Static,[],Block([Return()])),MethodDecl(Id(main),Static,[],Block([]))])])"
    #     self.assertTrue(TestAST.test(input, expect, 400))
   
    
    

