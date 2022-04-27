
"""
 * @author nhphung
"""
from ast import Global
from pyclbr import Function
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
# Le Duc Cam - 1952588

class CType:
    pass

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None,kind=None,scope=None,class_belong_to=None,method_belong_to=None):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.kind = kind
        self.scope = scope
        self.class_belong_to = class_belong_to
        self.method_belong_to = method_belong_to

class StaticChecker(BaseVisitor,Utils):

    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putIntLn",MType([IntType()],VoidType()))
    ]
            
    
    def __init__(self,ast):
        self.ast = ast

 
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    # c is a list of symbols 
    def visitProgram(self,ast:Program, c): 
        c=[]
        for x in ast.decl:
            self.visit(x,c) 
        return []

    def visitClassDecl(self, ast:ClassDecl, c):
            # Check Id of ClassDecl #
        ## pass symbol whose type is ClassType, kind, scope of Id
        self.visit(ast.classname, ([i for i in c if type(i.mtype) is CType],Class()))
        ## case not error occur -> append classname
        c.append(Symbol(ast.classname.name, CType(), None, Class(), Global(),None,None))
        # , ast.classname.name, None
        current_class = c[-1]
            # Check memlist of ClassDecl #
        for mem in ast.memlist:
            self.visit(mem, (c,current_class))
        return 

    def visitMethodDecl(self, ast:MethodDecl, c_currentclass):
        c,class_belong_to = c_currentclass
        name = self.visit(ast.name, (c, Method(),class_belong_to))
        mtype = None
        value = None  
        kind  = ast.kind
        if type(kind) is Static:
            scope = Global()
        else:
            scope = Class()
        c.append(Symbol(name, mtype, value, kind, scope,class_belong_to,None))
        # print(c[-1].name,c[-1].kind,c[-1].scope,c[-1].value)
        current_method = c[-1]
        for i in ast.param: # list of VarDecl
            self.visit(i,(c,Parameter(),class_belong_to,current_method))
        # self.visit(ast.body,class_belong_to,current_method)
        return

    def visitAttributeDecl(self, ast:AttributeDecl, c_currentclass):
        c,class_belong_to = c_currentclass
        if type(ast.decl) is VarDecl:
            name = self.visit(ast.decl.variable, (c, Attribute(),class_belong_to))
            mtype = ast.decl.varType
            value = ast.decl.varInit  
        elif type(ast.decl) is ConstDecl: 
            name  = self.visit(ast.decl.constant, (c, Attribute(),class_belong_to ))
            mtype = ast.decl.constType
            value = ast.decl.value
            
        kind  = ast.kind
        if type(kind) is Static:
            scope = Global()
        else:
            scope = Class()
        c.append(Symbol(name, mtype, value, kind, scope,class_belong_to,None))
        # print(c[-1].name,c[-1].kind,c[-1].scope,c[-1].value)
        return

    def visitId(self,ast:Id, c): 
        ## kind of Id stored in c[1]
        ## class_belong_to in c[2]
        ## method_belong_to in c[3]

        # print(c[0])
        for i in c[0]:
            if ast.name == i.name:  
                if len(c) <=2 :           # Redecl Class (Scope: Global)
                    raise Redeclared(c[1],ast.name)
                elif len(c) ==3 :         # Redecl Attribute, Method
                    class_belong_to = c[2]
                    if (i.class_belong_to is None):     # -> this is a a class
                        continue
                    elif (class_belong_to.name == i.class_belong_to.name): # in the same class
                        raise Redeclared(c[1],ast.name)
                    elif (class_belong_to.name != i.class_belong_to.name): # in the different class
                        if i.name[0] == "$" and ast.name[0]=="$":     # in 2 class but global
                            raise Redeclared(c[1],ast.name)
                elif len(c) == 4: # Redecl Var,Const,Param
                    class_belong_to = c[2]
                    method_belong_to = c[3]
                    if (i.class_belong_to is None) or (i.method_belong_to is None):     # -> this is a a class
                        continue
                    elif (class_belong_to.name == i.class_belong_to.name) and (method_belong_to.name == i.method_belong_to.name):
                        raise Redeclared(c[1],ast.name)
        if len(c)>=3:
            return ast.name
        return 

    def visitVarDecl(self, ast:VarDecl, c_kind_class_method):
        c = c_kind_class_method[0]
        class_belong_to = c_kind_class_method[2]
        method_belong_to = c_kind_class_method[3]
        if type(c_kind_class_method[2] is Parameter):
            kind = Parameter()
        else:
            kind = Variable()   
        name = self.visit(ast.variable, (c, kind,class_belong_to,method_belong_to))
        mtype = ast.varType
        value = ast.varInit  
        scope = Method()
        c.append(Symbol(name, mtype, value, kind, scope,class_belong_to,method_belong_to))
        return

    def visitConstDecl(self, ast:ConstDecl, c):
        pass
    
    def visitBlock(self,ast:Block, c): 
        pass

    def visitAssign(self,ast:Assign, c): 
        pass

    def visitIf(self,ast:If, c): 
        pass

    def visitFor(self,ast:For, c): 
        pass
    
    def visitCallStmt(self,ast:CallStmt, c): 
        pass

    def visitReturn(self,ast:Return, c): 
        pass

    def visitBreak(self,ast:Break, c): 
        pass

    def visitContinue(self,ast:Continue, c): 
        pass

    def visitBinaryOp(self,ast:BinaryOp, c): 
        pass

    def visitUnaryOp(self,ast:UnaryOp, c): 
        pass
    
    def visitNewExpr(self,ast:NewExpr, c): 
        pass

    def visitCallExpr(self, ast:CallExpr, c): 
        pass

    def visitFieldAccess(self,ast:FieldAccess, c): 
        pass

    def visitInstance(self,ast, c): 
        pass

    def visitStatic(self,ast, c): 
        pass

    def visitArrayType(self,ast, c): 
        return ArrayType()
    
    def visitClassType(self,ast, c): 
        return ClassType()
    
    def visitVoidType(self,ast, c): 
        return VoidType()

    def visitIntType(self,ast, c): 
        return IntType()
    
    def visitFloatType(self,ast, c): 
        return FloatType()
    
    def visitBoolType(self,ast, c): 
        return BoolType()
    
    def visitStringType(self,ast, c): 
        return StringType()
    

    def visitArrayLiteral(self,ast, c): 
        pass

    def visitIntLiteral(self,ast, c): 
        return IntType()

    def visitFloatLiteral(self,ast, c): 
        return FloatType()
    
    def visitStringLiteral(self,ast, c): 
        return StringType()
    
    def visitBooleanLiteral(self,ast, c): 
        return BoolType()
    
    def visitNullLiteral(self,ast, c): 
        pass

    def visitSelfLiteral(self,ast, c): 
        pass

    
        


    

