import unittest
from TestUtils import TestChecker
from AST import *

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
        Class c{
            Var c:String;
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
            Val c:Float;
            cc(){ 
                Val c:Int;
                Val c:Float;
            }
        }
        """
        expect = "Redeclared Constant: c"
        self.assertTrue(TestChecker.test(input,expect,410))
    
    def test411(self):
        input = """
        Class c{
            Val c:Float;
            cc(){ 
                Val c:Int;
                { Val c:Float; }
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