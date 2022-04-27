import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
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
            c(Var c,c : Int){ }
        }
        """
        expect = "Redeclared Parameter: c"
        self.assertTrue(TestChecker.test(input,expect,406))
    
    def test407(self):
        input = """
        Class A{
            c(c,d : Int;   e:Float){ }
        }
        Class c{
            c( c:Int){ }
        }
        """
        expect = "[]"
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