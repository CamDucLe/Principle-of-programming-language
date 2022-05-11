"""
 * @author nhphung
"""
from ast import Global
from AST import * 
from Visitor import *
from StaticError import *
# Le Duc Cam - 1952588 #

class CType:
    pass
class ForScope:
    pass

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None,kind=None,scope=None,class_belong_to=None,method_belong_to=None,block_number=None,class_refer=None,sub_type=None,arr_size = None,param_list=[]):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.kind = kind
        self.scope = scope
        self.class_belong_to = class_belong_to
        self.method_belong_to = method_belong_to
        self.block_number = block_number
        self.class_refer = class_refer
        self.sub_type = sub_type
        self.arr_size = arr_size
        self.param_list = param_list

class StaticChecker(BaseVisitor):

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

    no_entry_flag = False
    main_flag = False
    number_of_return = 0
    def visitClassDecl(self, ast:ClassDecl, c):
            # Check Id of ClassDecl #
        ## pass symbol whose type is ClassType, kind, scope of Id
        self.visit(ast.classname, ([i for i in c if type(i.mtype) is CType],Class(),'check_redeclared'))
        ## case not error occur -> append classname
        c.append(Symbol(ast.classname.name, CType(), None, Class(), Global(),None,None,None))
        program_flag = False
        if ast.classname.name == "Program" and ast.parentname is None:
            program_flag = True

        current_class = c[-1]
            # Check memlist of ClassDecl #
        if program_flag == True:
            for mem in ast.memlist:            
                if type(mem) is MethodDecl and mem.name.name == "main":
                    if len(mem.param) == 0:
                        self.main_flag = True
                        break
        if program_flag==True and self.main_flag==True:
            self.no_entry_flag = True
        elif program_flag==True and self.main_flag==False:
            raise NoEntryPoint()
        
        
        for mem in ast.memlist:
            self.visit(mem, (c,current_class))
        
        if type(ast.parentname) is Id:
            self.visit(ast.parentname,(c,Class(),'check_undeclared_cl'))  

        if self.no_entry_flag == True and self.number_of_return!=0:       
            raise NoEntryPoint()
        constructor_flag = False
        for mem in ast.memlist:            
            if type(mem) is MethodDecl and mem.name.name == "Constructor":
                constructor_flag = True
        if constructor_flag == False:
            self.visit(MethodDecl(Instance(),Id('Constructor'),[],Block([])),(c,current_class))
        self.number_of_return = 0
        self.main_flag = False

        return 

    def visitMethodDecl(self, ast:MethodDecl, c_currentclass):
        c,class_belong_to = c_currentclass
        mtype = None
        name = self.visit(ast.name, (c, Method(),class_belong_to,mtype,'check_redeclared'))
        value = None  
        kind  = Method()
        if type(ast.kind) is Static:
            scope = Global()
        else:
            scope = Class()
        class_refer = class_belong_to
        param_list = []
        c.append(Symbol(name, mtype, value, kind, scope,class_belong_to,None,None,class_refer,None,None,param_list))
        current_method = c[-1]
        block_number = 0
        for i in ast.param: # list of VarDecl
            self.visit(i,(c,Parameter(),class_belong_to,current_method,block_number))
            param_list.append((i.variable,i.varType))
        for i in c:
            if i.name == ast.name.name and i.class_belong_to == class_belong_to and type(i.kind) is Method:
                i.param_list = param_list
                current_method = i
                break

        self.visit(ast.body,(c,class_belong_to,current_method,block_number))
        return

    def visitAttributeDecl(self, ast:AttributeDecl, c_currentclass):
        c,class_belong_to = c_currentclass
        sub_type = None
        arr_size = None
        if type(ast.decl) is VarDecl:
            mtype = ast.decl.varType
            name = self.visit(ast.decl.variable, (c, Attribute(),class_belong_to,mtype,'check_redeclared'))
            if type(ast.decl.varType) is ArrayType:
                sub_type = ast.decl.varType.eleType
                arr_size = ast.decl.varType.size
            value = ast.decl.varInit  
            kind = Variable()
            
            type_value = None
            if ast.decl.varInit is not None:
                if type(ast.decl.varInit) is BinaryOp:
                    if type(ast.decl.varInit.left) is Id:
                        raise Undeclared(Identifier(),ast.decl.varInit.left.name)
                    elif type(ast.decl.varInit.left) is ArrayCell:
                        if type(ast.decl.varInit.left.arr) is Id:
                            raise Undeclared(Identifier(),ast.decl.varInit.left.arr.name)
                    if type(ast.decl.varInit.right) is Id:
                        raise Undeclared(Identifier(),ast.decl.varInit.right.name)
                    elif type(ast.decl.varInit.right) is ArrayCell:
                        if type(ast.decl.varInit.right.arr) is Id:
                            raise Undeclared(Identifier(),ast.decl.varInit.right.arr.name)
                    type_value = self.visit(ast.decl.varInit,(c,class_belong_to,None,None))
                elif type(ast.decl.varInit) is UnaryOp:
                    if type(ast.decl.varInit.body) is Id:
                        raise Undeclared(Identifier(),ast.decl.varInit.body.name)
                    elif type(ast.decl.varInit.body) is ArrayCell:
                        if type(ast.decl.varInit.body.arr) is Id:
                            raise Undeclared(Identifier(),ast.decl.varInit.body.arr.name)
                    type_value = self.visit(ast.decl.varInit,(c,class_belong_to,None,None))
                elif type(ast.decl.varInit) is Id:
                    raise Undeclared(Identifier(),ast.decl.varInit.name)
                elif type(ast.decl.varInit) is FieldAccess:   
                    self.visit(ast.decl.varInit.fieldname, (c,Attribute(),class_belong_to,None,'check_undeclared_at'))
                    for i in c: 
                        if ast.decl.varInit.fieldname.name == i.name and i.class_belong_to == class_belong_to and type(i.scope) in [Class,Global] and type(i.kind) is Variable:
                            type_value = i.mtype
                            break                
                elif type(ast.decl.varInit) in [IntLiteral,StringLiteral,FloatLiteral,BooleanLiteral]:
                    type_value = self.visit(ast.decl.varInit,c) 
                elif type(ast.decl.varInit) is NewExpr:
                    flag_class_name = True
                    for i in c:
                        if ast.decl.varInit.classname.name == i.name and type(i.kind) is Class:
                            flag_class_name = False
                            break
                    if flag_class_name == True:
                        raise Undeclared(Class(),ast.decl.varInit.classname.name)  
                    param_list_constructor = []
                    param_list_newexpr = []
                    for i in c:
                        if i.name =="Constructor" and ast.decl.varInit.classname.name == i.class_belong_to.name and type(i.kind) is Method:
                            param_list_constructor = i.param_list
                            break
                    param_list_newexpr = ast.decl.varInit.param
                    type_list_constructor = []
                    type_list_newexpr = []
                    for i in param_list_newexpr:
                        if type(i) is Id:
                            raise TypeMismatchInExpression(ast.decl.varInit)
                        elif type(i) is ArrayCell:
                            if type(i.arr) is ArrayCell:
                                raise TypeMismatchInExpression(ast.decl.varInit)
                        elif type(i) is FieldAccess:
                            tmp_class_refer =  self.visit(i,(c,class_belong_to,None,None,None))
                            type_list_newexpr.append(self.visit(i.fieldname,(c,class_belong_to,None,None,tmp_class_refer,'check_type')))
                        elif type(i) in [IntLiteral,FloatLiteral,BooleanLiteral,StringLiteral]:    
                            type_list_newexpr.append(self.visit(i,(c,class_belong_to,None,None,None,'check_type')))
                    for i in param_list_constructor:
                        type_list_constructor.append(i[1])
                    if len(type_list_newexpr) != len(type_list_constructor):
                        raise TypeMismatchInExpression(ast.decl.varInit)
                    else:
                        for i in range(len(type_list_newexpr)):
                            if type(type_list_constructor[i]) != type(type_list_newexpr[i]):
                                if type(type_list_constructor[i]) is FloatType and type(type_list_newexpr[i]) is IntType:
                                    continue
                                else:
                                    raise TypeMismatchInExpression(ast.decl.varInit)
                    type_value = ClassType(Id('s'))
                elif type(ast.decl.varInit) is NullLiteral:
                    xyz=27
                elif type(ast.decl.varInit) is ArrayCell:
                    if type(ast.decl.varInit.arr) is not FieldAccess:
                        raise TypeMismatchInExpression(ast.decl.varInit)
                    else: 
                        tmp_class_refer = self.visit(ast.decl.varInit.arr,(c,class_belong_to,None,None))
                        type_value = self.visit(ast.decl.varInit.arr.fieldname,(c,class_belong_to,None,None,tmp_class_refer,"check_type"))
                        type_value = type_value.eleType
                        self.visit(ast.decl.varInit.arr.fieldname,(c,Attribute(),class_belong_to,tmp_class_refer,'check_undeclared_at'))
                        for i in range(len(ast.decl.varInit.idx)):
                            type_idx = None
                            if type(ast.decl.varInit.idx[i]) is Id:
                                raise TypeMismatchInExpression(ast.decl.varInit)
                            elif type(ast.decl.varInit.idx[i]) is FieldAccess:
                                tmp_class_refer2 = self.visit(ast.decl.varInit.idx[i],(c,class_belong_to,None,None))
                                type_idx = self.visit(ast.decl.varInit.idx[i].fieldname,(c,class_belong_to,None,None,tmp_class_refer2,'check_type'))
                            elif type(ast.decl.varInit.idx[i]) in [IntLiteral,FloatLiteral,BooleanLiteral,StringLiteral]:
                                type_idx = self.visit(ast.decl.varInit.idx[i],c)
                
                            if type(type_idx) is not IntType:
                                raise TypeMismatchInExpression(ast.decl.varInit)

                elif type(mtype) is ArrayType:
                    if type(ast.decl.varInit) is not ArrayLiteral:
                        raise TypeMismatchInStatement(ast)    
                    else:       ### ast value is ArrayLiteral
                        if len(ast.decl.varInit.value) > arr_size:
                            raise TypeMismatchInStatement(ast)
                        tmp_type = None
                        tmp_type = self.visit(ast.decl.varInit.value[0],c)
                        for i in ast.decl.varInit.value:
                            if  type(self.visit(i,c)) != type(tmp_type):
                                raise IllegalArrayLiteral(ast.decl.varInit)
                        sub_type = mtype.eleType
                        if type(sub_type) is FloatType and type(tmp_type) is IntType:
                            xyz =27  
                        elif type(tmp_type) != type(sub_type):
                            raise TypeMismatchInStatement(ast)    
                        type_value = mtype       
                if type(type_value) !=  type(mtype):
                    if type(type_value) is IntType and type(mtype) is FloatType:
                        xyz=27
                    elif type(ast.decl.varInit) is NullLiteral and type(mtype) is ClassType:
                        xyz=27
                    else:
                        raise TypeMismatchInStatement(ast)

        elif type(ast.decl) is ConstDecl: 
            mtype = ast.decl.constType
            name  = self.visit(ast.decl.constant, (c, Attribute(),class_belong_to,mtype ,'check_redeclared'))
            if type(ast.decl.constType) is ArrayType:
                sub_type = ast.decl.constType.eleType
                arr_size = ast.decl.constType.size
            value = ast.decl.value
            kind = Constant()
            self.const_decl = True
            ####
            if ast.decl.value is None and type(mtype) is not ClassType:
                raise IllegalConstantExpression(None) 
            type_value = None
            if ast.decl.value is not None:
                if type(ast.decl.value) is BinaryOp:
                    if type(ast.decl.value.left) is Id:
                        raise Undeclared(Identifier(),ast.decl.value.left.name)
                    elif type(ast.decl.value.left) is ArrayCell:
                        if type(ast.decl.value.left.arr) is Id:
                            raise Undeclared(Identifier(),ast.decl.value.left.arr.name)
                    if type(ast.decl.value.right) is Id:
                        raise Undeclared(Identifier(),ast.decl.value.right.name)
                    elif type(ast.decl.value.right) is ArrayCell:
                        if type(ast.decl.value.right.arr) is Id:
                            raise Undeclared(Identifier(),ast.decl.value.right.arr.name)
                    type_value = self.visit(ast.decl.value,(c,class_belong_to,None,None))
                    if self.const_flag == True or self.const_flag_2 == True:
                        raise IllegalConstantExpression(ast.decl.value) 
                elif type(ast.decl.value) is UnaryOp:
                    if type(ast.decl.value.body) is Id:
                        raise Undeclared(Identifier(),ast.decl.value.body.name)
                    elif type(ast.decl.value.body) is ArrayCell:
                        if type(ast.decl.value.body.arr) is Id:
                            raise Undeclared(Identifier(),ast.decl.value.body.arr.name)
                    type_value = self.visit(ast.decl.value,(c,class_belong_to,None,None))
                    if self.const_flag == True or self.const_flag_2 == True:
                        raise IllegalConstantExpression(ast.decl.value) 
                elif type(ast.decl.value) is Id:
                    raise Undeclared(Identifier(),ast.decl.value.name)
                elif type(ast.decl.value) is FieldAccess:   
                    self.visit(ast.decl.value.fieldname, (c,Attribute(),class_belong_to,None,'check_undeclared_at'))
                    for i in c: 
                        if ast.decl.value.fieldname.name == i.name and i.class_belong_to == class_belong_to and type(i.scope) in [Class,Global] and type(i.kind) is Constant:
                            self.const_flag= False
                            type_value = i.mtype
                            break
                        else: self.const_flag = True
                    
                    if self.const_flag == True or self.const_flag_2 == True:
                        raise IllegalConstantExpression(ast.value)          
                elif type(ast.decl.value) in [IntLiteral,StringLiteral,FloatLiteral,BooleanLiteral]:
                    type_value = self.visit(ast.decl.value,c) 
                elif type(ast.decl.value) is NewExpr:
                    flag_class_name = True
                    for i in c:
                        if ast.decl.value.classname.name == i.name and type(i.kind) is Class:
                            flag_class_name = False
                            break
                    if flag_class_name == True:
                        raise Undeclared(Class(),ast.decl.value.classname.name)  
                    param_list_constructor = []
                    param_list_newexpr = []
                    for i in c:
                        if i.name =="Constructor" and ast.decl.value.classname.name == i.class_belong_to.name and type(i.kind) is Method:
                            param_list_constructor = i.param_list
                            break
                    param_list_newexpr = ast.decl.value.param
                    type_list_constructor = []
                    type_list_newexpr = []
                    for i in param_list_newexpr:
                        if type(i) is Id:
                            raise TypeMismatchInExpression(ast.decl.value)
                        elif type(i) is ArrayCell:
                            if type(i.arr) is Id:
                                raise TypeMismatchInExpression(ast.decl.value)
                        elif type(i) is FieldAccess:
                            tmp_class_refer =  self.visit(i,(c,class_belong_to,None,None,None))
                            type_list_newexpr.append(self.visit(i.fieldname,(c,class_belong_to,None,None,tmp_class_refer,'check_type')))
                        elif type(i) in [IntLiteral,FloatLiteral,BooleanLiteral,StringLiteral]:    
                            type_list_newexpr.append(self.visit(i,(c,class_belong_to,None,None,None,'check_type')))
                    for i in param_list_constructor:
                        type_list_constructor.append(i[1])
                    if len(type_list_newexpr) != len(type_list_constructor):
                        raise TypeMismatchInExpression(ast.decl.value)
                    else:
                        for i in range(len(type_list_newexpr)):
                            if type(type_list_constructor[i]) != type(type_list_newexpr[i]):
                                if type(type_list_constructor[i]) is FloatType and type(type_list_newexpr[i]) is IntType:
                                    continue
                                else:
                                    raise TypeMismatchInExpression(ast.decl.value)
                    type_value = ClassType(Id('s'))
                elif type(ast.decl.value) is NullLiteral:
                    xyz=27
                elif type(ast.decl.value) is ArrayCell:
                    if type(ast.decl.value.arr) is not FieldAccess:
                        raise TypeMismatchInExpression(ast.decl.value)
                    else: 
                        tmp_class_refer = self.visit(ast.decl.value.arr,(c,class_belong_to,None,None))
                        type_value = self.visit(ast.decl.value.arr.fieldname,(c,class_belong_to,None,None,tmp_class_refer,"check_type"))
                        type_value = type_value.eleType
                        self.visit(ast.decl.value.arr.fieldname,(c,Attribute(),class_belong_to,tmp_class_refer,'check_undeclared_at'))
                        for i in range(len(ast.decl.value.idx)):
                            type_idx = None
                            if type(ast.decl.value.idx[i]) is Id:
                                raise TypeMismatchInExpression(ast.decl.value)
                            elif type(ast.decl.value.idx[i]) is FieldAccess:
                                tmp_class_refer2 = self.visit(ast.decl.value.idx[i],(c,class_belong_to,None,None))
                                type_idx = self.visit(ast.decl.value.idx[i].fieldname,(c,class_belong_to,None,None,tmp_class_refer2,'check_type'))
                            elif type(ast.decl.value.idx[i]) in [IntLiteral,FloatLiteral,BooleanLiteral,StringLiteral]:
                                type_idx = self.visit(ast.decl.value.idx[i],c)
                
                            if type(type_idx) is not IntType:
                                raise TypeMismatchInExpression(ast.decl.value)
                elif type(mtype) is ArrayType:
                    if type(ast.decl.value) is not ArrayLiteral:
                        raise TypeMismatchInConstant(ast)    
                    else:       ### ast value is ArrayLiteral
                        if len(ast.decl.value.value) > arr_size:
                            raise TypeMismatchInStatement(ast)
                        tmp_type = None
                        tmp_type = self.visit(ast.decl.value.value[0],c)
                        for i in ast.decl.value.value:
                            if  type(self.visit(i,c)) != type(tmp_type):
                                raise IllegalArrayLiteral(ast.decl.value)
                        sub_type = mtype.eleType
                        if type(sub_type) is FloatType and type(tmp_type) is IntType:
                            xyz =27  
                        elif type(tmp_type) != type(sub_type):
                            raise TypeMismatchInConstant(ast)    
                        type_value = mtype       
                if type(type_value) !=  type(mtype):
                    if type(type_value) is IntType and type(mtype) is FloatType:
                        xyz=27
                    elif type(ast.decl.value) is NullLiteral and type(mtype) is ClassType:
                        xyz=27
                    else:
                        raise TypeMismatchInConstant(ast)
                self.const_decl = False

        class_refer = None
        if str(mtype)[0:9] == 'ClassType':
            self.visit(mtype.classname,(c,Class(),'check_undeclared_cl'))
            for i in c:
                if i.name == mtype.classname.name and type(i.kind) is Class:
                    class_refer = i
                    break
        else:
            class_refer = class_belong_to
        
        if type(ast.kind) is Static:
            scope = Global()
        else:
            scope = Class()
        c.append(Symbol(name, mtype, value, kind, scope,class_belong_to,None,None,class_refer,sub_type,arr_size))
        return

    def visitBlock(self,ast:Block, c_class_method_block):
        c,class_belong_to,method_belong_to,block_number = c_class_method_block
        for inst in ast.inst:
            if type(inst) is VarDecl:
                self.visit(inst,(c,Variable(),class_belong_to,method_belong_to,block_number) )
            elif type(inst) is ConstDecl:
                self.visit(inst,(c,Constant(),class_belong_to,method_belong_to,block_number) )
            elif type(inst) is Block:
                self.visit(inst, (c,class_belong_to,method_belong_to,block_number+1))
            elif type(inst) is Assign:
                self.visit(inst,(c,class_belong_to,method_belong_to,block_number))
            elif type(inst) is CallStmt:
                self.visit(inst,(c,class_belong_to,method_belong_to,block_number))
            elif type(inst) is If:
                self.visit(inst,(c,class_belong_to,method_belong_to,block_number))
            elif type(inst) is For:
                self.visit(inst,(c,class_belong_to,method_belong_to,block_number))
            elif type(inst) is Return:
                self.number_of_return +=1
                self.visit(inst,(c,class_belong_to,method_belong_to,block_number))
            elif type(inst) is Continue:
                self.visit(inst,(c,class_belong_to,method_belong_to,block_number))
            elif type(inst) is Break:
                self.visit(inst,(c,class_belong_to,method_belong_to,block_number))
        return 

    def visitId(self,ast:Id, c): 
        ## list of symbol       in c[0]
        ## kind of Id stored    in c[1]
        ## class_belong_to      in c[2]
        ## method_belong_to     in c[3]
        ## block_number         in c[4]
        ## stmt                 in c[5]
        ## check                in c[-1]
        if c[-1] == 'check_type': # len(c) = 6
            class_belong_to = c[1]
            method_belong_to= c[2]
            block_number    = c[3]
            class_refer     = c[4]
            type_return     = None
            for i in c[0]:
                if ast.name == i.name:
                    if class_refer is None: # case var/const decl and case attribute of a class
                        if i.class_belong_to == class_belong_to and i.method_belong_to == method_belong_to and i.block_number <= block_number:
                            type_return =  i.mtype
                        elif i.class_belong_to == class_belong_to and type(i.scope) is Class:
                            type_return =  i.mtype
                    else:                  # case:   obj.att
                        if (i.class_belong_to == class_refer) and (type(i.scope) is Class) and (i.mtype is not None):
                            type_return = i.mtype
            return type_return

        if c[-1] == 'check_cannot_assign_to_constant':  # len(c) == 7
            class_belong_to = c[1]
            method_belong_to= c[2]
            block_number    = c[3]
            class_refer     = c[4]
            stmt = c[5]
           
            for i in c[0]:
                # same class, same method, block_number >= i.block_number
                if class_refer is None:
                    if (i.name == ast.name):
                        if ( i.class_belong_to == class_belong_to) and (i.method_belong_to == method_belong_to) and (i.block_number <= block_number): 
                            if type(i.kind) is Constant:
                                raise CannotAssignToConstant(stmt)
                        elif (i.class_belong_to == class_belong_to) and (type(i.scope) is Class):
                            if type(i.kind) is Constant:
                                raise CannotAssignToConstant(stmt)
                else:
                    if (i.name == ast.name):   
                        if (type(i.scope) is Class) and (type(i.kind) is Constant) and (class_refer.name == i.class_belong_to.name):
                            raise CannotAssignToConstant(stmt)
            return

        if c[-1] in ['check_undeclared_cl']:    ## len(c)==3
            if ast.name not in [ i.name for i in c[0]]:    # not decleared on the list of symbol
                raise Undeclared(c[1],ast.name)
        elif c[-1] in ['check_undeclared_id']: ## len(c)==6
            class_belong_to = c[2]
            method_belong_to= c[3]
            block_number    = c[4]
            if ast.name not in [ i.name for i in c[0]]:    # not decleared on the list of symbol
                raise Undeclared(c[1],ast.name)
            else:     # ast.name == i.name                  # declared but in different scope 
                for i in c[0]:
                    # same class, same method, block_number >= i.block_number
                    if (i.name == ast.name and i.class_belong_to == class_belong_to) and (i.method_belong_to == method_belong_to) and (i.block_number <= block_number): 
                        return i.mtype
                raise Undeclared(c[1],ast.name)
        elif c[-1] in ['check_undeclared_at','check_undeclared_me']:    ## len(c)==5
            class_belong_to = c[2]
            class_refer = c[3]
            if ast.name not in [ i.name for i in c[0]]:    # not decleared on the list of symbol
                raise Undeclared(c[1],ast.name)
            else:     # ast.name == i.name                  # declared but in different scope 
                for i in c[0]:
                    if (i.name == ast.name):
                        if class_refer is None or class_refer == class_belong_to: 
                            if (i.class_belong_to == class_belong_to and type(i.scope) in [Class,Global]): # same class
                                return i.mtype
                        else:
                            if i.class_refer == class_refer:
                                return i.mtype
                raise Undeclared(c[1],ast.name)

        if c[-1] == 'check_redeclared':
            for i in c[0]:
                if ast.name == i.name:
                   
                    if len(c) <= 3 :           # Redecl Class (Scope: Global)
                        raise Redeclared(c[1],ast.name)
                    elif len(c) == 5 :         # Redecl Attribute, Method
                        class_belong_to = c[2]
                        mtype = c[3]
                        if (i.class_belong_to is None):     # -> this is a a class
                            continue
                        elif class_belong_to.name == i.class_belong_to.name : # in the same class
                            if (mtype is None) and i.mtype is None:#  check method trung` method  
                                raise Redeclared(c[1],ast.name)
                            elif (mtype is not None) and i.mtype is not None:#  check attribute trung` attribute ? 
                                raise Redeclared(c[1],ast.name)
                            
                        
                        elif (class_belong_to.name != i.class_belong_to.name): # in the different class
                            if i.name[0] == "$" and ast.name[0]=="$":     # in 2 class but global
                                raise Redeclared(c[1],ast.name)
                    elif len(c) == 6: # Redecl Var,Const,Param
                        class_belong_to = c[2]
                        method_belong_to = c[3]
                        block_number = c[4]
                        if (i.class_belong_to is None) or (i.method_belong_to is None):     # -> this is a a class
                            continue
                        elif (class_belong_to.name == i.class_belong_to.name) and (method_belong_to.name == i.method_belong_to.name) and (block_number == i.block_number):
                            raise Redeclared(c[1],ast.name)
            if len(c)>=4:
                return ast.name

        return Id

    def visitVarDecl(self, ast:VarDecl, c_kind_class_method_block):
        c = c_kind_class_method_block[0]
        class_belong_to = c_kind_class_method_block[2]
        method_belong_to = c_kind_class_method_block[3]
        block_number = c_kind_class_method_block[4]
        sub_type = None
        arr_size = None
        if type(c_kind_class_method_block[1]) is Parameter:
            kind = Parameter()
        else:
            kind = Variable()   
        name = self.visit(ast.variable, (c, kind,class_belong_to,method_belong_to,block_number,'check_redeclared'))
        mtype = ast.varType
        if type(ast.varType) is ArrayType:
            sub_type = ast.varType.eleType
            arr_size = ast.varType.size
        class_refer = None
        if str(mtype)[0:9] == 'ClassType':
            self.visit(mtype.classname,(c,Class(),'check_undeclared_cl'))
            for i in c:
                if i.name == mtype.classname.name and type(i.kind) is Class:
                    class_refer = i
                    break
        else:
            class_refer = class_belong_to
        value = ast.varInit  
        scope = Method()
        
        if ast.varInit is not None:
            type_value = None
            if type(ast.varInit) in [BinaryOp,UnaryOp]:
                type_value = self.visit(ast.varInit,(c,class_belong_to,method_belong_to,block_number))
            elif type(ast.varInit) is Id:
                self.visit(ast.varInit, (c,Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id'))
                type_value = self.visit(ast.varInit, (c,class_belong_to,method_belong_to,block_number,None,'check_type'))
            elif type(ast.varInit) is FieldAccess:   
                if (ast.varInit) is not SelfLiteral:
                    self.visit(ast.varInit.obj, (c,Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id'))
                type_value = self.visit(ast.varInit.fieldname, (c,class_belong_to,method_belong_to,block_number,None,'check_type'))
            elif type(ast.varInit) in [IntLiteral,StringLiteral,FloatLiteral,BooleanLiteral]:
                type_value = self.visit(ast.varInit,c) 
            elif type(ast.varInit) is NewExpr:
                flag_class_name = True
                for i in c:
                    if ast.varInit.classname.name == i.name and type(i.kind) is Class:
                        flag_class_name = False
                        break
                if flag_class_name == True:
                    raise Undeclared(Class(),ast.varInit.classname.name)  
                param_list_constructor = []
                param_list_newexpr = []
                for i in c:
                    if i.name =="Constructor" and ast.varInit.classname.name == i.class_belong_to.name and type(i.kind) is Method:
                        param_list_constructor = i.param_list
                        break
                param_list_newexpr = ast.varInit.param
                type_list_constructor = []
                type_list_newexpr = []
                for i in param_list_newexpr:
                    type_list_newexpr.append(self.visit(i,(c,class_belong_to,method_belong_to,block_number,None,'check_type')))
                for i in param_list_constructor:
                    type_list_constructor.append(i[1])
                if len(type_list_newexpr) != len(type_list_constructor):
                    raise TypeMismatchInExpression(ast.varInit)
                else:
                    for i in range(len(type_list_newexpr)):
                        if type(type_list_constructor[i]) != type(type_list_newexpr[i]):
                            if type(type_list_constructor[i]) is FloatType and type(type_list_newexpr[i]) is IntType:
                                    continue
                            else:
                                raise TypeMismatchInExpression(ast.varInit)
                type_value = ClassType(Id('s'))        
            elif type(self.visit(value,c)) is NullLiteral:
                xyz=27
            elif type(ast.varInit) is ArrayCell:
                self.visit(ast.varInit.arr,(c,Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id'))    
                for i in range(len(ast.varInit.idx)):
                    type_idx = None
                    if type(ast.varInit.idx[i]) is Id:
                        self.visit(ast.varInit.idx[i],(c,Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id'))    
                        type_idx = self.visit(ast.varInit.idx[i],(c,class_belong_to,method_belong_to,block_number,None,'check_type'))
                    elif type(ast.varInit.idx[i]) is FieldAccess:
                        tmp_class_refer = self.visit(ast.varInit.idx[i],(c,class_belong_to,method_belong_to,block_number))
                        type_idx = self.visit(ast.varInit.idx[i].fieldname,(c,class_belong_to,method_belong_to,block_number,tmp_class_refer,'check_type'))
                    elif type(ast.varInit.idx[i]) in [IntLiteral,FloatLiteral,BooleanLiteral,StringLiteral]:
                        type_idx = self.visit(ast.varInit.idx[i],c)
                
                    if type(type_idx) is not IntType:
                        raise TypeMismatchInExpression(ast.varInit)
                type_value = self.visit(ast.varInit.arr,(c,class_belong_to,method_belong_to,block_number,None,'check_type'))
                type_value = type_value.eleType
            elif type(mtype) is ArrayType:
                if type(ast.varInit) is not ArrayLiteral:
                    raise TypeMismatchInStatement(ast)    
                else:       ### ast varInit is ArrayLiteral
                    if len(ast.varInit.value) > arr_size:
                        raise TypeMismatchInStatement(ast)
                    tmp_type = None
                    tmp_type = self.visit(ast.varInit.value[0],c)
                    for i in ast.varInit.value:
                        if  type(self.visit(i,c)) != type(tmp_type):
                            raise IllegalArrayLiteral(ast.varInit)
                    type_value = mtype
                    sub_type = mtype.eleType
                    for i in ast.varInit.value:
                        if type(sub_type) is FloatType and type(self.visit(i,c)) is IntType:
                            continue  
                        elif type(self.visit(i,c)) != type(sub_type):
                            raise TypeMismatchInStatement(ast)    
                    type_value = mtype
            if type(type_value) !=  type(mtype):
                if type(type_value) is IntType and type(mtype) is FloatType:
                    xyz=27
                elif type(ast.varInit) is NullLiteral and type(mtype) is ClassType:
                    xyz=27
                else:
                    raise TypeMismatchInStatement(ast)
        
        c.append(Symbol(name, mtype, value, kind, scope,class_belong_to,method_belong_to,block_number,class_refer,sub_type,arr_size))
        return
    
    const_flag = False
    const_flag_2 = False
    const_decl = False
    def visitConstDecl(self, ast:ConstDecl, c_kind_class_method_block):
        c = c_kind_class_method_block[0]
        class_belong_to = c_kind_class_method_block[2]
        method_belong_to = c_kind_class_method_block[3]
        block_number = c_kind_class_method_block[4]
        kind = c_kind_class_method_block[1] 
        sub_type = None
        arr_size =None
        self.const_decl = True
        name = self.visit(ast.constant, (c, kind,class_belong_to,method_belong_to,block_number,'check_redeclared'))
        mtype = ast.constType
        if type(ast.constType) is ArrayType:
            sub_type = ast.constType.eleType
            arr_size = ast.constType.size
        if str(mtype)[0:9] == 'ClassType':
            self.visit(mtype.classname,(c,Class(),'check_undeclared_cl'))
            for i in c:
                if i.name == mtype.classname.name and type(i.kind) is Class:
                    class_refer = i
                    break
        else:
            class_refer = class_belong_to
        value = ast.value  
        scope = Method()
        c.append(Symbol(name, mtype, value, kind, scope,class_belong_to,method_belong_to,block_number,class_refer,sub_type,arr_size))
               
        if ast.value is None and type(mtype) is not ClassType:
            raise IllegalConstantExpression(None) 
        type_value = None
        if ast.value is not None:
            if type(ast.value) in [BinaryOp,UnaryOp]:
                type_value = self.visit(ast.value,(c,class_belong_to,method_belong_to,block_number))
                if self.const_flag == True or self.const_flag_2 == True:
                    raise IllegalConstantExpression(ast.value) 
            elif type(ast.value) is Id:
                self.visit(ast.value, (c,Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id'))
                type_value = self.visit(ast.value, (c,class_belong_to,method_belong_to,block_number,None,'check_type'))
                for i in c: 
                    if ast.value.name == i.name and i.class_belong_to == class_belong_to and i.method_belong_to == method_belong_to and i.block_number <= block_number and type(i.kind) is Constant:
                        self.const_flag= False  
                        break
                    else: self.const_flag = True
                if self.const_flag == True or self.const_flag_2 == True:
                    raise IllegalConstantExpression(ast.value) 
            elif type(ast.value) is FieldAccess:   
                if (ast.value.obj) is not SelfLiteral:
                    self.visit(ast.value.obj, (c,Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id'))
                type_value = self.visit(ast.value.fieldname, (c,class_belong_to,method_belong_to,block_number,None,'check_type'))
                for i in c: 
                    if ast.value.fieldname.name == i.name and i.class_belong_to == class_belong_to and type(i.scope) in [Class,Global] and type(i.kind) is Constant:
                        self.const_flag= False
                        break
                    else: self.const_flag = True
                if self.const_flag == True or self.const_flag_2 == True:
                    raise IllegalConstantExpression(ast.value)              
            elif type(ast.value) in [IntLiteral,StringLiteral,FloatLiteral,BooleanLiteral]:
                type_value = self.visit(ast.value,c) 
            elif type(ast.value) is NewExpr:
                flag_class_name = True
                for i in c:
                    if ast.value.classname.name == i.name and type(i.kind) is Class:
                        flag_class_name = False
                        break
                if flag_class_name == True:
                    raise Undeclared(Class(),ast.value.classname.name)  
                param_list_constructor = []
                param_list_newexpr = []
                for i in c:
                    if i.name =="Constructor" and ast.value.classname.name == i.class_belong_to.name and type(i.kind) is Method:
                        param_list_constructor = i.param_list
                        break
                param_list_newexpr = ast.value.param
                type_list_constructor = []
                type_list_newexpr = []
                for i in param_list_newexpr:
                    type_list_newexpr.append(self.visit(i,(c,class_belong_to,method_belong_to,block_number,None,'check_type')))
                for i in param_list_constructor:
                    type_list_constructor.append(i[1])
                if len(type_list_newexpr) != len(type_list_constructor):
                    raise TypeMismatchInExpression(ast.value)
                else:
                    for i in range(len(type_list_newexpr)):
                        if type(type_list_constructor[i]) != type(type_list_newexpr[i]):
                            if type(type_list_constructor[i]) is FloatType and type(type_list_newexpr[i]) is IntType:
                                    continue
                            else:
                                raise TypeMismatchInExpression(ast.value)
                type_value = ClassType(Id('s'))
            elif type(ast.value) is NullLiteral:
                xyz=27
            elif type(ast.value) is ArrayCell:
                self.visit(ast.value.arr,(c,Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id'))
                for i in range(len(ast.value.idx)):
                    type_idx = None
                    if type(ast.value.idx[i]) is Id:
                        self.visit(ast.value.idx[i],(c,Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id'))    
                        type_idx = self.visit(ast.value.idx[i],(c,class_belong_to,method_belong_to,block_number,None,'check_type'))
                    elif type(ast.value.idx[i]) is FieldAccess:
                        tmp_class_refer = self.visit(ast.value.idx[i],(c,class_belong_to,method_belong_to,block_number))
                        type_idx = self.visit(ast.value.idx[i].fieldname,(c,class_belong_to,method_belong_to,block_number,tmp_class_refer,'check_type'))
                    elif type(ast.value.idx[i]) in [IntLiteral,FloatLiteral,BooleanLiteral,StringLiteral]:
                        type_idx = self.visit(ast.value.idx[i],c)
                
                    if type(type_idx) is not IntType:
                        raise TypeMismatchInExpression(ast.value)
                type_value = self.visit(ast.value.arr,(c,class_belong_to,method_belong_to,block_number,None,'check_type'))
                type_value = type_value.eleType
            elif type(mtype) is ArrayType:
                if type(ast.value) is not ArrayLiteral:
                    raise TypeMismatchInConstant(ast)    
                else:       ### ast value is ArrayLiteral
                    if len(ast.value.value) > arr_size:
                        raise TypeMismatchInStatement(ast)
                    tmp_type = None
                    tmp_type = self.visit(ast.value.value[0],c)
                    for i in ast.value.value:
                        if  type(self.visit(i,c)) != type(tmp_type):
                            raise IllegalArrayLiteral(ast.value)
                    sub_type = mtype.eleType
                    if type(sub_type) is FloatType and type(tmp_type) is IntType:
                        xyz =27  
                    elif type(tmp_type) != type(sub_type):
                        raise TypeMismatchInConstant(ast)    
                    type_value = mtype
            if type(type_value) !=  type(mtype):
                if type(type_value) is IntType and type(mtype) is FloatType:
                    xyz=27
                elif type(ast.value) is NullLiteral and type(mtype) is ClassType:
                    xyz=27
                else:
                    raise TypeMismatchInConstant(ast) 

            
        self.const_decl = False
        return
    
    A_flag = False
    def visitAssign(self,ast:Assign, c_class_method_block): 
        c,class_belong_to,method_belong_to,block_number = c_class_method_block
        type_LHS = None
        type_RHS = None
        arr_size_LHS = None
        sub_type_LHS = None
        arr_size_RHS = None
        sub_type_RHS = None
        ##### Left Hand Side ######
        if type(ast.lhs) is Id:
            self.visit(ast.lhs, (c, Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id'))
            self.visit(ast.lhs, (c,class_belong_to,method_belong_to,block_number,None,ast,'check_cannot_assign_to_constant'))
            for i in c:
                if i.name == ast.lhs.name and i.class_belong_to == class_belong_to and i.method_belong_to == method_belong_to and i.block_number <= block_number:
                    type_LHS = i.mtype
                    if type(type_LHS) is ArrayType:
                        sub_type_LHS = i.sub_type
                        arr_size_LHS = i.arr_size
        elif type(ast.lhs) is FieldAccess:       # Self.x or obj.x
            class_refer = self.visit(ast.lhs,(c_class_method_block))
            self.visit(ast.lhs.fieldname, (c,class_belong_to,method_belong_to,block_number,class_refer,ast,'check_cannot_assign_to_constant'))
            for i in c:
                if class_refer is not None and class_refer != class_belong_to:   # obj.x
                    if i.class_refer is not None:
                        if i.name == ast.lhs.fieldname.name and i.class_belong_to == class_refer :
                            type_LHS = i.mtype
                            if type(type_LHS) is ArrayType:
                                sub_type_LHS = i.sub_type
                                arr_size_LHS = i.arr_size
                            break
                else:   # Self.x
                    if i.name == ast.lhs.fieldname.name and  i.class_belong_to == class_belong_to and type(i.scope) in [Class,Global]:
                        type_LHS = i.mtype
                        if type(type_LHS) is ArrayType:
                            sub_type_LHS = i.sub_type
                            arr_size_LHS = i.arr_size
                        break
        elif type(ast.lhs) is ArrayCell: 
            type_idl = None
            if type(ast.lhs.arr) is Id:
                for i in c:
                    if i.name == ast.lhs.arr.name and i.class_belong_to == class_belong_to and i.method_belong_to == method_belong_to and i.block_number <= block_number:
                        type_LHS = i.sub_type
                        type_idl = i.mtype
                self.visit(ast.lhs.arr, (c, Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id'))
                self.visit(ast.lhs.arr, (c,class_belong_to,method_belong_to,block_number,None,ast,'check_cannot_assign_to_constant'))
                
                if type(type_idl) is not ArrayType :
                    raise TypeMismatchInExpression(ast.lhs)
                
                for i in c:
                    if i.name == ast.lhs.arr.name and i.class_belong_to == class_belong_to and i.method_belong_to == method_belong_to and i.block_number <= block_number :
                        for j in range(len(ast.lhs.idx)):
                            if type(ast.lhs.idx[j]) is Id:
                                self.visit(ast.lhs.idx[j],(c,Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id'))
                                type_idx = self.visit(ast.lhs.idx[j],(c,class_belong_to,method_belong_to,block_number,None,'check_type'))
                                if type(type_idx) is not IntType:
                                    raise TypeMismatchInExpression(ast.lhs)
                            elif type(ast.lhs.idx[j]) is FieldAccess:
                                tmp_class_refer = self.visit(ast.lhs.idx[j],(c,class_belong_to,method_belong_to,block_number))
                                type_idx = self.visit(ast.lhs.idx[j].fieldname,(c,class_belong_to,None,None,tmp_class_refer,'check_type'))
                                if type(type_idx) is not IntType:
                                    raise TypeMismatchInExpression(ast.lhs)
                            elif type(ast.lhs.idx[j]) is UnaryOp or (type(ast.lhs.idx[j]) is IntLiteral and i.arr_size < ast.lhs.idx[j].value ) or ast.lhs.idx[j].value == 0:
                                raise TypeMismatchInExpression(ast.lhs)
                            elif type(ast.lhs.idx[j]) in [FloatLiteral,BooleanLiteral,StringLiteral]: 
                                raise TypeMismatchInExpression(ast.lhs)
            elif type(ast.lhs.arr) is FieldAccess:
                class_refer = self.visit(ast.lhs.arr,(c_class_method_block))
                self.visit(ast.lhs.arr.fieldname, (c,class_belong_to,method_belong_to,block_number,class_refer,ast,'check_cannot_assign_to_constant'))
                arr_size = -1
                for i in c:
                    if class_refer is not None and class_refer != class_belong_to:   # obj.x
                        if i.class_refer is not None:
                            if i.name == ast.lhs.arr.fieldname.name and i.class_belong_to == class_refer and type(i.mtype) is ArrayType :
                                type_LHS = i.sub_type
                                type_idl = i.mtype
                                arr_size = i.arr_size
                                break
                    else:   # Self.x
                        if i.name == ast.lhs.arr.fieldname.name and  i.class_belong_to == class_belong_to and type(i.scope) in [Class,Global]and type(i.mtype) is ArrayType:
                            type_LHS = i.sub_type
                            type_idl = i.mtype
                            arr_size = i.arr_size
                            break
                for j in range(len(ast.lhs.idx)):
                    if type(ast.lhs.idx[j]) is Id:
                        self.visit(ast.lhs.idx[j],(c,Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id'))
                        type_idx = self.visit(ast.lhs.idx[j],(c,class_belong_to,method_belong_to,block_number,None,'check_type'))
                        if type(type_idx) is not IntType:
                            raise TypeMismatchInExpression(ast.lhs)
                    elif type(ast.lhs.idx[j]) is FieldAccess:
                        tmp_class_refer = self.visit(ast.lhs.idx[j],(c,class_belong_to,method_belong_to,block_number))
                        type_idx = self.visit(ast.lhs.idx[j].fieldname,(c,class_belong_to,None,None,tmp_class_refer,'check_type'))
                        if type(type_idx) is not IntType:
                            raise TypeMismatchInExpression(ast.lhs)
                    elif type(ast.lhs.idx[j]) is UnaryOp or (type(ast.lhs.idx[j]) is IntLiteral and arr_size < ast.lhs.idx[j].value ) or ast.lhs.idx[j].value == 0:
                        raise TypeMismatchInExpression(ast.lhs)
                    elif type(ast.lhs.idx[j]) in [FloatLiteral,BooleanLiteral,StringLiteral]: 
                        raise TypeMismatchInExpression(ast.lhs)
                        
            if type(type_idl) is not ArrayType :
                raise TypeMismatchInExpression(ast.lhs)
            
        # print('type_LHS:  ',type(type_LHS),arr_size_LHS,sub_type_LHS)
        
        ##### Right Hand Side ######
        if type(ast.exp) is Id:
            self.visit(ast.exp, (c, Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id'))
            for i in c:
                if i.name == ast.exp.name and i.class_belong_to == class_belong_to and i.method_belong_to == method_belong_to and i.block_number <= block_number:
                    type_RHS = i.mtype
                    if type(type_RHS) is ArrayType:
                        sub_type_RHS = i.sub_type
                        arr_size_RHS = i.arr_size
        elif type(ast.exp) is FieldAccess:       # Self.x or obj.x
            class_refer = self.visit(ast.exp,(c_class_method_block))
            for i in c:
                if class_refer is not None and class_refer != class_belong_to:   # obj.x
                    if i.class_refer is not None:
                        if i.name == ast.exp.fieldname.name and i.class_belong_to == class_refer :
                            type_RHS = i.mtype
                            if type(type_RHS) is ArrayType:
                                sub_type_RHS = i.sub_type
                                arr_size_RHS = i.arr_size
                            break
                else:   # Self.x
                    if i.name == ast.exp.fieldname.name and  i.class_belong_to == class_belong_to and type(i.scope) in [Class,Global]:
                        type_RHS = i.mtype
                        if type(type_RHS) is ArrayType:
                            sub_type_RHS = i.sub_type
                            arr_size_RHS = i.arr_size
                        break
        elif type(ast.exp) is ArrayCell: 
            type_idr = None
            if type(ast.exp.arr) is Id:
                self.visit(ast.exp.arr, (c, Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id')) 
                for i in c:
                    if i.name == ast.exp.arr.name and i.class_belong_to == class_belong_to and i.method_belong_to == method_belong_to and i.block_number <= block_number:
                        type_RHS = i.sub_type
                        type_idr = i.mtype
                for i in c:
                    if i.name == ast.exp.arr.name and i.class_belong_to == class_belong_to and i.method_belong_to == method_belong_to and i.block_number <= block_number :
                        for j in range(len(ast.exp.idx)):
                            if type(ast.exp.idx[j]) is Id:
                                self.visit(ast.exp.idx[j],(c,Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id'))
                                type_idx = self.visit(ast.exp.idx[j],(c,class_belong_to,method_belong_to,block_number,None,'check_type'))
                                if type(type_idx) is not IntType:
                                    raise TypeMismatchInExpression(ast.exp)
                            elif type(ast.exp.idx[j]) is FieldAccess:
                                tmp_class_refer = self.visit(ast.exp.idx[j],(c,class_belong_to,method_belong_to,block_number))
                                type_idx = self.visit(ast.exp.idx[j].fieldname,(c,class_belong_to,None,None,tmp_class_refer,'check_type'))
                                if type(type_idx) is not IntType:
                                    raise TypeMismatchInExpression(ast.exp)
                            elif type(ast.exp.idx[j]) is UnaryOp or (type(ast.exp.idx[j]) is IntLiteral and i.arr_size < ast.exp.idx[j].value )or ast.exp.idx[j].value == 0:
                                raise TypeMismatchInExpression(ast.exp)
                            elif type(ast.exp.idx[j]) in [FloatLiteral,BooleanLiteral,StringLiteral]: 
                                raise TypeMismatchInExpression(ast.exp)
            elif type(ast.exp.arr) is FieldAccess:
                class_refer = self.visit(ast.exp.arr,(c_class_method_block))
                arr_size = -1
                for i in c:
                    if class_refer is not None and class_refer != class_belong_to :   # obj.x  and class_refer != class_belong_to
                        if i.class_refer is not None:
                            if i.name == ast.exp.arr.fieldname.name and i.class_belong_to == class_refer and type(i.mtype) is ArrayType :
                                type_RHS = i.sub_type
                                type_idr = i.mtype
                                arr_size = i.arr_size
                                break
                    else:   # Self.x
                        if i.name == ast.exp.arr.fieldname.name and  i.class_belong_to == class_belong_to and type(i.scope) in [Class,Global]and type(i.mtype) is ArrayType:
                            type_RHS = i.sub_type
                            type_idr = i.mtype
                            arr_size = i.arr_size
                            break
                for j in range(len(ast.exp.idx)):
                    if type(ast.exp.idx[j]) is Id:
                        self.visit(ast.exp.idx[j],(c,Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id'))
                        type_idx = self.visit(ast.exp.idx[j],(c,class_belong_to,method_belong_to,block_number,None,'check_type'))
                        if type(type_idx) is not IntType:
                            raise TypeMismatchInExpression(ast.exp)
                    elif type(ast.exp.idx[j]) is FieldAccess:
                        tmp_class_refer = self.visit(ast.exp.idx[j],(c,class_belong_to,method_belong_to,block_number))
                        type_idx = self.visit(ast.exp.idx[j].fieldname,(c,class_belong_to,None,None,tmp_class_refer,'check_type'))
                        if type(type_idx) is not IntType:
                            raise TypeMismatchInExpression(ast.exp)
                    elif type(ast.exp.idx[j]) is UnaryOp or (type(ast.exp.idx[j]) is IntLiteral and arr_size < ast.exp.idx[j].value ) or ast.exp.idx[j].value == 0:
                        raise TypeMismatchInExpression(ast.exp)
                    elif type(ast.exp.idx[j]) in [FloatLiteral,BooleanLiteral,StringLiteral]: 
                        raise TypeMismatchInExpression(ast.exp)
                        
            if type(type_idr) is not ArrayType :
                raise TypeMismatchInExpression(ast.exp)
        elif type(ast.exp) in [BinaryOp, UnaryOp]:
            type_RHS = self.visit(ast.exp,c_class_method_block)   
        elif type(ast.exp) in [IntLiteral,FloatLiteral,BooleanLiteral,StringLiteral]:
            type_RHS = self.visit(ast.exp,c_class_method_block)    
        elif type(ast.exp) is CallExpr:
            type_RHS = self.visit(ast.exp,c_class_method_block)
        # print('type_RHS:  ',type(type_RHS),arr_size_RHS,sub_type_RHS)

        
        ####### Check type mis match   #######
        if type(type_LHS) is VoidType:
            raise TypeMismatchInStatement(ast)

        if self.A_flag == False:
            if type(type_LHS) is ArrayType and type(type_RHS) is ArrayType:
                if (arr_size_LHS == arr_size_RHS) and (type(sub_type_LHS) == type(sub_type_RHS)) :
                    xyz = 27 # do notthing
                elif (arr_size_LHS == arr_size_RHS) and (type(sub_type_LHS) != type(sub_type_RHS)) :
                        if type(sub_type_LHS) is FloatType and type(sub_type_RHS) is IntType:
                            xyz = 27  # do notthing
                        else:
                            raise TypeMismatchInStatement(ast)
                else:
                    raise TypeMismatchInStatement(ast)
            if type(type_LHS) != type(type_RHS):
                if type(type_LHS) is FloatType and type(type_RHS) is IntType:
                    xyz = 27  # do notthing
                else:
                    raise TypeMismatchInStatement(ast)

        return

    def visitIf(self,ast:If, c_class_method_block): 
        c,class_belong_to,method_belong_to,block_number = c_class_method_block
        type_expr = self.visit(ast.expr,c_class_method_block)
        if type(type_expr) is not BoolType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.thenStmt,(c,class_belong_to,method_belong_to,block_number+1))
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt,(c,class_belong_to,method_belong_to,block_number+1))
        return

    for_flag = False
    def visitFor(self,ast:For, c_class_method_block): 
        c,class_belong_to,method_belong_to,block_number = c_class_method_block
        type_expr1 = self.visit(ast.expr1,c_class_method_block)
        type_expr2 = self.visit(ast.expr2,c_class_method_block)
        type_expr3 = IntType()
        type_scalar= IntType()
        type_scalar = self.visit(ast.id,(c,Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id'))

        if ast.expr3 is not None:
            type_expr3 = self.visit(ast.expr3,c_class_method_block)
        if (type(type_expr1) is not IntType) or (type(type_expr2) is not IntType) or (type(type_expr3) is not IntType) or (type(type_scalar) is not IntType) :
            raise TypeMismatchInStatement(ast)
       
        c.append(Symbol(ast.id.name, type_scalar, None, Parameter(), ForScope(),class_belong_to,method_belong_to,block_number+1,None))
        self.for_flag = True
        self.visit(ast.loop,(c,class_belong_to,method_belong_to,block_number+1))
        self.for_flag = False
        return

    def visitBinaryOp(self,ast:BinaryOp, c_class_method_block): 
        c,class_belong_to,method_belong_to,block_number = c_class_method_block
        left_class_refer = None
        right_class_refer = None
        type_left= None
        type_right=None
        ## check undecl ##
        if type(ast.left) is Id:
            self.visit(ast.left, (c,Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id'))
            if self.const_decl == True:
                for i in c: 
                    if ast.left.name == i.name and i.class_belong_to == class_belong_to and i.method_belong_to == method_belong_to and i.block_number <= block_number and type(i.kind) is Constant:
                        self.const_flag_2 = False
                        break
                    else: self.const_flag_2 = True
            type_left = self.visit(ast.left, (c,class_belong_to,method_belong_to,block_number,left_class_refer,'check_type'))
        elif type(ast.left) is FieldAccess:
            left_class_refer = self.visit(ast.left,(c,class_belong_to,method_belong_to,block_number))
            if self.const_decl == True:
                for i in c: 
                    if ast.left.fieldname.name == i.name and i.class_belong_to == class_belong_to and type(i.scope) in [Class,Global] and type(i.kind) is Constant:
                        self.const_flag_2 = False
                        break
                    else: self.const_flag_2 = True
            type_left = self.visit(ast.left.fieldname, (c,class_belong_to,method_belong_to,block_number,left_class_refer,'check_type'))
        elif type(ast.left) is ArrayCell:
            if type(ast.left.arr) is Id:
                self.visit(ast.left.arr, (c, Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id'))
                if self.const_decl == True:
                    for i in c: 
                        if ast.left.arr.name == i.name and i.class_belong_to == class_belong_to and i.method_belong_to == method_belong_to and i.block_number <= block_number and type(i.kind) is Constant:
                            self.const_flag_2 = False
                            break
                        else: self.const_flag_2 = True
                type_left = self.visit(ast.left.arr, (c,class_belong_to,method_belong_to,block_number,left_class_refer,'check_type'))
            elif type(ast.left.arr) is FieldAccess:
                left_class_refer = self.visit(ast.left.arr,(c,class_belong_to,method_belong_to,block_number))
                if self.const_decl == True:
                    for i in c: 
                        if ast.left.fieldname.name == i.name and i.class_belong_to == class_belong_to and i.method_belong_to == method_belong_to and i.block_number <= block_number and type(i.kind) is Constant:
                            self.const_flag_2 = False
                            break
                        else: self.const_flag_2 = True
                type_left = self.visit(ast.left.arr.fieldname,(c,class_belong_to,method_belong_to,block_number,left_class_refer,'check_type'))
        elif type(ast.left) in [BinaryOp,UnaryOp]:
            type_left = self.visit(ast.left,c_class_method_block)
        else:
            type_left = self.visit(ast.left,c) 

        if type(ast.right) is Id:
            self.visit(ast.right, (c,Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id'))
            if self.const_decl == True:
                for i in c: 
                    if ast.right.name == i.name and i.class_belong_to == class_belong_to and i.method_belong_to == method_belong_to and i.block_number <= block_number and type(i.kind) is Constant:
                        self.const_flag = False
                        break
                    else: self.const_flag = True
            type_right = self.visit(ast.right, (c,class_belong_to,method_belong_to,block_number,right_class_refer,'check_type'))
        elif type(ast.right) is FieldAccess:
            right_class_refer = self.visit(ast.right,(c,class_belong_to,method_belong_to,block_number))
            if self.const_decl == True:
                for i in c: 
                    if ast.right.fieldname.name == i.name and i.class_belong_to == class_belong_to and type(i.scope) in [Class,Global] and type(i.kind) is Constant:
                        self.const_flag = False
                        break
                    else: self.const_flag = True
            type_right = self.visit(ast.right.fieldname, (c,class_belong_to,method_belong_to,block_number,right_class_refer,'check_type'))
        elif type(ast.right) is ArrayCell:
            if type(ast.right.arr) is Id:
                self.visit(ast.right.arr, (c, Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id'))
                if self.const_decl == True:
                    for i in c: 
                        if ast.right.arr.name == i.name and i.class_belong_to == class_belong_to and i.method_belong_to == method_belong_to and i.block_number <= block_number and type(i.kind) is Constant:
                            self.const_flag = False
                            break
                        else: self.const_flag = True
                type_right = self.visit(ast.right.arr, (c,class_belong_to,method_belong_to,block_number,right_class_refer,'check_type'))
            elif type(ast.right.arr) is FieldAccess:
                right_class_refer = self.visit(ast.right.arr,(c,class_belong_to,method_belong_to,block_number))
                if self.const_decl == True:
                    for i in c: 
                        if ast.right.arr.fieldname.name == i.name and i.class_belong_to == class_belong_to and i.method_belong_to == method_belong_to and i.block_number <= block_number and type(i.kind) is Constant:
                            self.const_flag = False
                            break
                        else: self.const_flag = True
                type_right = self.visit(ast.right.arr.fieldname,(c,class_belong_to,method_belong_to,block_number,right_class_refer,'check_type'))
        elif type(ast.right) in [BinaryOp,UnaryOp]:
            type_right = self.visit(ast.right,c_class_method_block)
        else:
            type_right = self.visit(ast.right,c) 

        op = ast.op
        if op in ['+', '-', '*', '/']:
            if type(type_left) is FloatType and type(type_right) in [IntType,FloatType]:
                return FloatType()
            elif type(type_left) in [IntType,FloatType]  and type(type_right) is FloatType:
                return FloatType()
            elif type(type_left) is IntType and type(type_right) is IntType:
                return IntType()
            else:
                raise TypeMismatchInExpression(ast)
        elif op in ['%']:
            if type(type_left) is IntType and type(type_right) is IntType:
                return IntType()
            else:
                raise TypeMismatchInExpression(ast)
        elif op in [ '+.']:
            if type(type_left) is not StringType or type(type_right) is not StringType:
                raise TypeMismatchInExpression(ast)
            return StringType()
        elif op in ['&&', '||']:
            if not isinstance(type_left, BoolType) or not isinstance(type_right, BoolType):
                return True
            return BoolType()
        elif op in ['==.']:
            if not isinstance(type_left, StringType) or not isinstance(type_right, StringType):
                return True # raise error in stmts like if ,for,...
            return BoolType()
        elif op in ['==', '!=']:
            if not isinstance(type_left, (IntType, BoolType)) or not isinstance(type_right, (IntType, BoolType)):
                return True # raise error in stmts like if ,for,...
            return BoolType()
        elif op in ['<', '>', '<=', '>=']:
            if not isinstance(type_left, (IntType, FloatType)) or not isinstance(type_right, (IntType, FloatType)):
                return True # raise error in stmts like if ,for,...
            return BoolType()

    def visitUnaryOp(self,ast:UnaryOp, c_class_method_block): 
        c,class_belong_to,method_belong_to,block_number = c_class_method_block
        type_exp = None
        class_refer = None
        if type(ast.body) is Id:
            self.visit(ast.body, (c,Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id'))
            if self.const_decl == True:
                for i in c: 
                    if ast.body.name == i.name and i.class_belong_to == class_belong_to and i.method_belong_to == method_belong_to and i.block_number <= block_number and type(i.kind) is Constant:
                        self.const_flag = False
                        break
                    else: self.const_flag = True
            type_exp = self.visit(ast.body, (c,class_belong_to,method_belong_to,block_number,class_refer,'check_type'))
        elif type(ast.body) is FieldAccess:
            class_refer = self.visit(ast.body,(c,class_belong_to,method_belong_to,block_number))
            if self.const_decl == True:
                for i in c: 
                    if ast.body.fieldname.name == i.name and i.class_belong_to == class_belong_to and i.method_belong_to == method_belong_to and i.block_number <= block_number and type(i.kind) is Constant:
                        self.const_flag = False
                        break
                    else: self.const_flag = True
            type_exp = self.visit(ast.body.fieldname, (c,class_belong_to,method_belong_to,block_number,class_refer,'check_type'))
        elif type(ast.body) is ArrayCell:
            if type(ast.body.arr) is Id:
                self.visit(ast.body.arr, (c, Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id'))
                if self.const_decl == True:
                    for i in c: 
                        if ast.body.arr.name == i.name and i.class_belong_to == class_belong_to and i.method_belong_to == method_belong_to and i.block_number <= block_number and type(i.kind) is Constant:
                            self.const_flag = False
                            break
                        else: self.const_flag = True
                type_exp = self.visit(ast.body.arr, (c,class_belong_to,method_belong_to,block_number,class_refer,'check_type'))
            elif type(ast.body.arr) is FieldAccess:
                class_refer = self.visit(ast.body.arr,(c,class_belong_to,method_belong_to,block_number))
                if self.const_decl == True:
                    for i in c: 
                        if ast.body.arr.fieldname.name == i.name and i.class_belong_to == class_belong_to and i.method_belong_to == method_belong_to and i.block_number <= block_number and type(i.kind) is Constant:
                            self.const_flag = False
                            break
                        else: self.const_flag = True
                type_exp = self.visit(ast.body.arr.fieldname,(c,class_belong_to,method_belong_to,block_number,class_refer,'check_type'))
        elif type(ast.body) is BinaryOp:
            type_exp = self.visit(ast.body,c_class_method_block)
        elif type(ast.body) is UnaryOp:
            type_exp = self.visit(ast.body,c_class_method_block)
        else:
            type_exp = self.visit(ast.body,c) 

        op = ast.op
        if op in ['-']:
            if not(type(type_exp)  in [IntType, FloatType]):
                raise TypeMismatchInExpression(ast)
            if type(type_exp) is IntType:   return IntType()
            else:                           return FloatType()
        elif op in ['!']:
            if type(type_exp)is not BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        return
    
    def visitCallStmt(self,ast:CallStmt, c_class_method_block): 
        c,class_belong_to,method_belong_to,block_number = c_class_method_block
        flag = self.visit(FieldAccess(ast.obj,ast.method),(c,class_belong_to,method_belong_to,block_number,Method()))
        class_refer = None
        param_list = []
        if flag == True:
            raise TypeMismatchInStatement(ast)
        else:
            class_refer = flag[0]
        for i in c: 
            if ast.method.name == i.name and type(i.kind) is Method:
                if i.class_belong_to == class_refer:
                    param_list = i.param_list
                    break
        l_type_param = []
        if len(ast.param) != 0:
            for j in ast.param:
                if type(j) is Id:
                    self.visit(j,(c,Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id'))  
                    for  i in c :
                        if i.name == j.name and i.class_belong_to == class_belong_to and i.method_belong_to == method_belong_to and i.block_number <= block_number:
                            l_type_param.append(i.mtype)
                elif type(j) is FieldAccess:
                    tmp_class_refer,ret_type = self.visit(j,(c,class_belong_to,method_belong_to,block_number))
                    l_type_param.append(self.visit(j.fieldname,(c,class_belong_to,None,None,tmp_class_refer,'check_type')))
                elif type(j) is ArrayCell:
                    self.visit(j.arr,(c,Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id'))
                    for i in c:
                        if i.name == j.arr.name and i.class_belong_to == class_belong_to and i.method_belong_to == method_belong_to and i.block_number <= block_number :
                            for k in range(len(j.idx)):
                                type_idx = None
                                if type(j.idx[k]) is Id:
                                    self.visit(j.idx[k],(c,Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id'))
                                    type_idx = (self.visit(j.idx[k],(c,class_belong_to,method_belong_to,block_number,None,'check_type')))
                                elif type(j.idx[k]) is FieldAccess:
                                    tmp_class_refer,ret_type = self.visit(j.idx[k],(c,class_belong_to,method_belong_to,block_number))
                                    type_idx = self.visit(j.idx[k].fieldname,(c,class_belong_to,None,None,tmp_class_refer,'check_type'))     
                                elif type(j.idx[k]) is UnaryOp or (type(j.idx[k]) is IntLiteral and i.arr_size < j.idx[k].value ) or j.idx[k].value == 0: 
                                    raise TypeMismatchInExpression(j)
                                elif type(j.idx[k]) in [IntLiteral,FloatLiteral,BooleanLiteral,StringLiteral]: 
                                    type_idx = self.visit(j.idx[k],c)
                                if type(type_idx) is not IntType:
                                    raise TypeMismatchInExpression(j)
                            l_type_param.append(i.sub_type)
                            break 
                elif type(j) in [IntLiteral,FloatLiteral,BooleanLiteral,StringLiteral]: 
                    l_type_param.append(self.visit(j,c))
        leng = 0
        if len(param_list) != len(l_type_param) :
            raise TypeMismatchInStatement(ast)
        else: 
            leng = len(l_type_param)

        if leng == 0:
            return
        else:
            for i in range (0,leng):
                if (type(l_type_param[i]) != type(param_list[i][1])):
                    if type(param_list[i][1]) is FloatType and   type(l_type_param[i]) is IntType:
                        xyz = 27
                    else:            
                        raise TypeMismatchInStatement(ast)
        self.call_flag = False
        return

    def visitReturn(self,ast:Return, c_class_method_block): 
        c,class_belong_to,method_belong_to,block_number = c_class_method_block
        
        if self.no_entry_flag == True and class_belong_to.name =="Program" and method_belong_to.name == "main" and self.main_flag==True and (ast.expr is not None):
            raise NoEntryPoint()
        else:
            self.number_of_return -= 1
        ret_type = VoidType()
        if type(ast.expr) is Id:
            self.visit(ast.expr, (c, Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id'))
            if type(ast.expr.mtype) is ArrayType:
                ret_type = ast.expr.sub_type
            else:
                ret_type = ast.expr.mtype
        elif type(ast.expr) is FieldAccess:
            class_refer = self.visit(ast.expr,(c_class_method_block))
            for i in c:
                if class_refer is not None and class_refer != class_belong_to:   # obj.x
                    if i.class_refer is not None:
                        if i.name == ast.expr.fieldname.name and i.class_belong_to == class_refer :
                            ret_type = i.mtype
                            if type(ret_type) is ArrayType:
                                ret_type = i.sub_type
                            break
                else:   # Self.x
                    if i.name == ast.expr.fieldname.name and  i.class_belong_to == class_belong_to and type(i.scope) in [Class,Global]:
                        ret_type = i.mtype
                        if type(ret_type) is ArrayType:
                            ret_type = i.sub_type
                        break
        elif type(ast.expr) is ArrayCell:
            type_arr = None
            if type(ast.expr.arr) is Id:
                for i in c:
                    if i.name == ast.exp.arr.name and i.class_belong_to == class_belong_to and i.method_belong_to == method_belong_to and i.block_number <= block_number:
                        ret_type = i.sub_type
                        type_arr = i.mtype
                self.visit(ast.expr.arr, (c, Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id'))
                for i in ast.expr.idx:
                    if type(self.visit(i,c)) is not IntType or type(type_arr) is not ArrayType :
                        raise TypeMismatchInExpression(ast.expr)
            elif type(ast.expr.arr) is FieldAccess:
                class_refer = self.visit(ast.expr.arr,(c_class_method_block))
                for i in c:
                    if class_refer is not None and class_refer != class_belong_to:   # obj.x
                        if i.class_refer is not None:
                            if i.name == ast.expr.arr.fieldname.name and i.class_belong_to == class_refer and type(i.mtype) is ArrayType :
                                ret_type = i.sub_type
                                type_arr = i.mtype
                                break
                    else:   # Self.x
                        if i.name == ast.exp.arr.fieldname.name and  i.class_belong_to == class_belong_to and type(i.scope) in [Class,Global]and type(i.mtype) is ArrayType:
                            ret_type = i.sub_type
                            type_arr = i.mtype
                            break
                for i in ast.expr.idx:
                    if type(self.visit(i,c)) is not IntType or type(type_arr) is not ArrayType :
                        raise TypeMismatchInExpression(ast.exp)
        elif type(ast.expr) in [IntLiteral,FloatLiteral,BooleanLiteral,StringLiteral]:
            ret_type = self.visit(ast.expr,c)
        elif type(ast.expr) in [BinaryOp, UnaryOp]:
            ret_type = self.visit(ast.expr,c_class_method_block)  

        for i in c:
            if i.name == method_belong_to.name and i.class_belong_to == class_belong_to:
                i.mtype = ret_type
                break
        return 

    def visitBreak(self,ast:Break, c_class_method_block): 
        if self.for_flag == False:
            raise MustInLoop(ast)
        return

    def visitContinue(self,ast:Continue, c_class_method_block): 
        if self.for_flag == False:
            raise MustInLoop(ast)
        return

    def visitNewExpr(self,ast:NewExpr, c): 
        pass

    def visitCallExpr(self, ast:CallExpr, c_class_method_block): 
        c,class_belong_to,method_belong_to,block_number = c_class_method_block
        class_refer = None
        ret_type = VoidType()
        type_obj = None
        if type(ast.obj) is FieldAccess: # Self.obj.method()  # obj.obj2.method
            class_refer = self.visit(ast.obj,(c,class_belong_to,method_belong_to,block_number))
            if class_refer is None  or class_refer == class_belong_to:   # obj.obj2  or type(ast.obj.fieldname)
                raise TypeMismatchInExpression(ast)
        elif type(ast.obj) is not SelfLiteral:  # obj.method()
            self.visit(ast.obj, (c, Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id') )
            for i in c:
                if i.name == ast.obj.name and type(i.scope) is not Global and type(i.mtype) is not Method :  
                    class_refer = i.class_refer   
                    type_obj = i.mtype    
                    break
            if type(type_obj) is not ClassType:
                raise TypeMismatchInExpression(ast)
        
        self.visit(ast.method, (c, Method(), class_belong_to,class_refer,'check_undeclared_me'))  
        
        l_type_param = []
        param_list = []
        for i in c:
            if i.name == ast.method.name and i.class_belong_to == class_refer and type(i.kind) is Method: 
                ret_type = i.mtype
                param_list = i.param_list
                break
        
        if len(ast.param) != 0:
            for j in ast.param:
                if type(j) is Id:
                    self.visit(j,(c,Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id'))  
                    for  i in c :
                        if i.name == j.name and i.class_belong_to == class_belong_to and i.method_belong_to == method_belong_to and i.block_number <= block_number:
                            l_type_param.append(i.mtype)
                elif type(j) is FieldAccess:
                    tmp_class_refer= self.visit(j,(c,class_belong_to,method_belong_to,block_number))
                    l_type_param.append(self.visit(j.fieldname,(c,class_belong_to,None,None,tmp_class_refer,'check_type')))   
                elif type(j) is ArrayCell:
                    self.visit(j.arr,(c,Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id'))
                    for i in c:
                        if i.name == j.arr.name and i.class_belong_to == class_belong_to and i.method_belong_to == method_belong_to and i.block_number <= block_number :
                            for k in range(len(j.idx)):
                                type_idx = None
                                if type(j.idx[k]) is Id:
                                    self.visit(j.idx[k],(c,Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id'))
                                    type_idx = self.visit(j.idx[k],(c,class_belong_to,method_belong_to,block_number,None,'check_type'))
                                elif type(j.idx[k]) is FieldAccess:
                                    tmp_class_refer = self.visit(j.idx[k],(c,class_belong_to,method_belong_to,block_number))
                                    type_idx = self.visit(j.idx[k].fieldname,(c,class_belong_to,None,None,tmp_class_refer,'check_type'))
                                elif type(j.idx[k]) is UnaryOp or (type(j.idx[k]) is IntLiteral and i.arr_size < j.idx[k].value ) or j.idx[k].value == 0:
                                    raise TypeMismatchInExpression(j)
                                elif type(j.idx[k]) in [IntLiteral,FloatLiteral,BooleanLiteral,StringLiteral]: 
                                    type_idx = self.visit(j.idx[k],c)
                                if type(type_idx) is not IntType:
                                    raise TypeMismatchInExpression(j)
                            l_type_param.append(i.sub_type)
                            break
                elif type(j) in [IntLiteral,FloatLiteral,BooleanLiteral,StringLiteral]: 
                    l_type_param.append(self.visit(j,c))

        leng = 0
        if len(param_list) != len(l_type_param) :
            raise TypeMismatchInExpression(ast)
        else: 
            leng = len(l_type_param)

        if leng == 0:
            return ret_type
        else:
            for i in range (0,leng):
                if (type(l_type_param[i]) != type(param_list[i][1])):
                    if type(param_list[i][1]) is FloatType and   type(l_type_param[i]) is IntType:
                        xyz = 27
                    else:
                        raise TypeMismatchInExpression(ast)
        
        if type(ret_type) is VoidType:
            raise TypeMismatchInExpression(ast) 
        return ret_type
    
    FA_flag=False
    call_flag = False
    def visitFieldAccess(self,ast:FieldAccess, c_class_method_block_kind):
        c = None
        class_belong_to =None
        method_belong_to = None
        block_number = None
        kind = None
        class_refer = None     
        check_type = None
        ret_type = None
        if len(c_class_method_block_kind) == 4:
            c,class_belong_to,method_belong_to,block_number = c_class_method_block_kind
        else:
            c,class_belong_to,method_belong_to,block_number,kind = c_class_method_block_kind
        if type(kind) is Method:  
            kind = Method()
            check_type ='check_undeclared_me'
            self.call_flag = True
        else: 
            kind = Attribute()
            check_type ='check_undeclared_at'
              
        if type(ast.obj) is FieldAccess: # Self.obj.att  or Self.obj.method()
            self.FA_flag = True
            if self.call_flag == True:
                class_refer,obj_type = self.visit(ast.obj,(c,class_belong_to,method_belong_to,block_number))
                if type(obj_type) is not ClassType:
                    self.call_flag = False
                    return True
                self.call_flag = False
            else:
                class_refer= self.visit(ast.obj,(c,class_belong_to,method_belong_to,block_number))
                
                
            if class_refer == class_belong_to:
                raise TypeMismatchInExpression(ast)

            self.visit(ast.fieldname, (c, kind, class_belong_to,class_refer,check_type))
            self.FA_flag = False
        elif type(ast.obj) is not SelfLiteral:       #  obj.att   A.b   A::b 
            class_flag_2 = False
            for i in c:   ## CLASS.instance 
                if i.name == ast.obj.name and ast.fieldname.name[0] != "$" and type(i.kind) is Class: 
                    for i in c:
                        if i.name == ast.obj.name and type(i.kind) is not Class:
                            class_flag_2 = False
                            break
                        if i ==c[-1]:
                            class_flag_2 = True
                    
            if class_flag_2 == True:
                raise IllegalMemberAccess(ast)
            class_list =[]
            for i in c:     ## CLASS::Static
                if  type(i.kind) is Class :
                    class_list.append(i)
            if ast.obj.name not in [i.name for i in class_list]:
                class_flag = True
                for i in c:
                    if ast.obj.name == i.name and type(i.kind) is not Class:
                        class_flag = False
                        break 
                if class_flag == True:
                    raise Undeclared(Class(),ast.obj.name)
            obj_type = self.visit(ast.obj, (c, Identifier(),class_belong_to,method_belong_to,block_number,'check_undeclared_id') )

            if type(obj_type) is not ClassType:
                self.call_flag = False
                raise TypeMismatchInExpression(ast)
            for i in c:
                if i.name == ast.obj.name  and type(i.scope) is not Global and type(i.mtype) is not Method:  
                    class_refer = i.class_refer    
                    break
            
            for i in c:   ## obj::Static 
                if i.name == ast.fieldname.name and i.class_belong_to == class_refer and type(i.scope) is Global: ## obj::Static 
                    raise IllegalMemberAccess(ast)
            ret_type = self.visit(ast.fieldname, (c, kind, class_belong_to,class_refer,check_type))
        elif type(ast.obj) is SelfLiteral:
            for i in c:
                if (i.name == ast.fieldname.name) and (type(i.scope) is not Global) and (type(i.mtype) is not Method) :  
                    class_refer = i.class_refer
                    if (self.FA_flag == True):
                        class_refer = i.class_refer    
                        break
            ret_type = self.visit(ast.fieldname, (c, kind, class_belong_to,class_refer, check_type))
        

        if self.call_flag == True:
            return (class_refer,ret_type)
        return class_refer

    def visitArrayCell(self,ast:ArrayCell, c_class_method_block):
        pass
        
    def visitInstance(self,ast, c): 
        pass

    def visitStatic(self,ast, c): 
        pass

    def visitArrayType(self,ast, c):
        return ArrayType
    
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
    

    def visitArrayLiteral(self,ast:ArrayLiteral, c): 
        return ArrayType

    def visitIntLiteral(self,ast:IntLiteral, c): 
        return IntType()

    def visitFloatLiteral(self,ast:FloatLiteral, c): 
        return FloatType()
    
    def visitStringLiteral(self,ast:StringLiteral, c): 
        return StringType()
    
    def visitBooleanLiteral(self,ast:BooleanLiteral, c): 
        return BoolType()
    
    def visitNullLiteral(self,ast:NullLiteral, c): 
        return NullLiteral()

    def visitSelfLiteral(self,ast, c): 
        pass

    
        


    

