from ast import stmt
from pickletools import read_unicodestringnl
from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *
# Le Duc Cam - 1952588

class ASTGeneration(D96Visitor):
    prog_flag = 0
    # ret_flag  = 0
    # Visit a parse tree produced by D96Parser#program.
    # program : (class_decl)+ EOF
    # checked
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return Program([self.visit(i) for i in ctx.class_decl()])


    # Visit a parse tree produced by D96Parser#class_decl.
    # class_decl: CLASS identifier (COLON identifier)? LCB member_list*  RCB
    # checked
    def visitClass_decl(self, ctx:D96Parser.Class_declContext):
        ids = [self.visit(i) for i in ctx.identifier()]
        classname = ids[0]
        if str(classname)[3:-1]=="Program" and len(ids) == 1:
            self.prog_flag = 1
        memlist = []
        if ctx.member_list():
            tmplist = [self.visit(x) for x in ctx.member_list()]
            for i in tmplist:
                if isinstance(i,list):
                    for ite in i:
                        memlist += [ite]
                else:
                    memlist += [i]
        self.prog_flag = 0
        if ctx.identifier(1) and ctx.COLON():
            parentname = self.visit(ctx.identifier(1)) 
            return ClassDecl(classname,memlist,parentname)
        else:
            return ClassDecl(classname,memlist)
        

    # Visit a parse tree produced by D96Parser#member_list.
    # member_list: attribute_decl | method_decl | constructor | destructor
    # checked
    def visitMember_list(self, ctx:D96Parser.Member_listContext):
        if ctx.attribute_decl():
            return self.visit(ctx.attribute_decl())
        elif ctx.method_decl():
            return self.visit(ctx.method_decl())
        elif ctx.constructor():
            return self.visit(ctx.constructor())
        elif ctx.destructor():
            return self.visit(ctx.destructor())


    # Visit a parse tree produced by D96Parser#attribute_decl.
    # attribute_decl: attribute_decl_1 | attribute_decl_2
    def visitAttribute_decl(self, ctx:D96Parser.Attribute_declContext):
        if ctx.attribute_decl_1():
            return self.visit(ctx.attribute_decl_1())
        else:
            return self.visit(ctx.attribute_decl_2())


    # Visit a parse tree produced by D96Parser#attribute_decl_1.
    # attribute_decl_1: (VAL|VAR) identifier (COMMA identifier)* COLON data_types  SEMI
    def visitAttribute_decl_1(self, ctx:D96Parser.Attribute_decl_1Context):
        ctype = self.visit(ctx.data_types())
        exp = None
        res = []
        if ctx.VAL(): # Val a,$b:Int
            for i in ctx.identifier():
                id = str(self.visit(i)) # return: Id(text)
                if id[3] == "$":
                    kind = Static()
                    const = Id(id[3:-1])
                else:
                    kind = Instance()  
                    const = Id(id[3:-1])
                const_decl = ConstDecl(const,ctype,exp)
                res += [AttributeDecl(kind,const_decl)]
            return res # return 1-d array [AttributeDecl(Instance,ConstDecl(Id(a),IntType)), AttributeDecl(Static,ConstDecl(Id(b),IntType))]
        elif ctx.VAR():
            for i in ctx.identifier():
                id = str(self.visit(i)) # return: Id(text)
                if str(ctype)[0] =="C": # class type -> var decl's exp = nullLit()
                    exp = NullLiteral()
                if id[3] == "$":
                    kind = Static()
                    const = Id(id[3:-1])
                else:
                    kind = Instance()  
                    const = Id(id[3:-1])
                const_decl = VarDecl(const,ctype,exp)
                res += [AttributeDecl(kind,const_decl)]
            return res 


    # Visit a parse tree produced by D96Parser#attribute_decl_2.
    # attribute_decl_2: (VAL|VAR) attribute_testing SEMI
    def visitAttribute_decl_2(self, ctx:D96Parser.Attribute_decl_2Context):
        tmp = self.visit(ctx.attribute_testing())
        ids = tmp[0] # [Id(a),Id(b)]
        exps = tmp[1]
        exps.reverse()
        type = tmp[2]
        res = []
        if ctx.VAL(): # Val a,$b:Int = 1,2,3
            for i in range(len(ids)):
                if ids[i].name[0] == "$":
                    kind = Static()
                    ids[i].name = ids[i].name[0:] 
                else:
                    kind = Instance()  
                const_decl = ConstDecl(ids[i],type,exps[i])
                res += [AttributeDecl(kind,const_decl)]
            return res # return 1-d array [AttributeDecl(Instance,ConstDecl(Id(a),IntType)), AttributeDecl(Static,ConstDecl(Id(b),IntType))]
        elif ctx.VAR():
            for i in range(len(ids)):
                if ids[i].name[0] == "$":
                    kind = Static()
                    ids[i].name = ids[i].name[0:] 
                else:
                    kind = Instance()  
                var_decl = VarDecl(ids[i],type,exps[i])
                res += [AttributeDecl(kind,var_decl)]
            return res 


    # Visit a parse tree produced by D96Parser#attribute_testing.
    # attribute_testing : (identifier COLON data_types ASSIGN expr) | (identifier COMMA attribute_testing (COMMA expr))
    # a,b,c:Int = 1,2,3
    def visitAttribute_testing(self, ctx:D96Parser.Attribute_testingContext):
        id = [self.visit(ctx.identifier())]
        exp = [self.visit(ctx.expr())]
        if ctx.attribute_testing():
            tmp = self.visit(ctx.attribute_testing())
            id.extend(tmp[0])
            exp.extend(tmp[1])
            return (id,exp,tmp[2])
        else:
            type = self.visit(ctx.data_types())
            return (id,exp,type)
    

    # Visit a parse tree produced by D96Parser#method_decl.
    # method_decl: identifier LP parameter_list? RP block_statement
    def visitMethod_decl(self, ctx:D96Parser.Method_declContext):
        id = str(self.visit(ctx.identifier())) # return: Id(text)
        if ctx.parameter_list():
            param = self.visit(ctx.parameter_list())
        else: param = []
        body = self.visit(ctx.block_statement())
        if id[3] == "$":
            kind = Static()
            name = Id(id[3:-1])
        else:
            if id[3:-1] =="main" and len(param) == 0 and self.prog_flag==1 : # main trong Program 
                kind = Static()
            else:
                kind = Instance()  
            name = Id(id[3:-1])
        # self.ret_flag = 0
        return MethodDecl(kind,name,param,body)


    # Visit a parse tree produced by D96Parser#parameter_list.
    # parameter_list: parameter (SEMI parameter)* 
    def visitParameter_list(self, ctx:D96Parser.Parameter_listContext):
        param_list = [self.visit(i) for i in ctx.parameter()]  ## return 2-d list
        param_list = [ item for sublist in param_list for item in sublist] # flatten list
        return param_list # return 1-d array
    

    # Visit a parse tree produced by D96Parser#parameter.
    # parameter: identifier (COMMA identifier)* COLON data_types 
    # toParam() function auto called
    def visitParameter(self, ctx:D96Parser.ParameterContext):
        params = []
        for i in ctx.identifier():
            params += [VarDecl(self.visit(i),self.visit(ctx.data_types()))]
        return params        # return  [param(Id(a),IntType),param(Id(b),IntType)]


    # Visit a parse tree produced by D96Parser#constructor.
    # constructor : CONSTRUCTOR LP (parameter_list)? RP block_statement
    # checked
    def visitConstructor(self, ctx:D96Parser.ConstructorContext):
        kind = Instance()
        name = Id("Constructor")
        if ctx.parameter_list():
            param = self.visit(ctx.parameter_list()) 
        else: 
            param = []
        body = self.visit(ctx.block_statement())
        return MethodDecl(kind,name,param,body)


    # Visit a parse tree produced by D96Parser#destructor.
    # destructor  : DESTRUCTOR LP RP block_statement
    # checked
    def visitDestructor(self, ctx:D96Parser.DestructorContext):
        kind = Instance()
        name = Id("Destructor")
        param = []
        body = self.visit(ctx.block_statement())
        return MethodDecl(kind,name,param,body)


    # Visit a parse tree produced by D96Parser#block_statement.
    # block_statement: LCB statement* RCB
    # checked
    def visitBlock_statement(self, ctx:D96Parser.Block_statementContext):
        stmtlist = []
        if ctx.statement():
            tmplist = [self.visit(i) for i in ctx.statement()]
            for i in tmplist:
                if isinstance(i,list):
                    for ite in i:
                        stmtlist +=[ite]
                else:
                    stmtlist += [i]
            return Block(stmtlist)
        return Block(stmtlist)


    # Visit a parse tree produced by D96Parser#statement.
    # statement:
	#   var_const_decl_statement | assign_statement 
	# | if_statement | for_statement | break_statement 
	# | continue_statement | return_statement | method_invocate_statement| block_statement;
    # checked
    def visitStatement(self, ctx:D96Parser.StatementContext):
        if ctx.var_const_decl_statement():
            return self.visit(ctx.var_const_decl_statement())
        elif ctx.assign_statement() :
            return self.visit(ctx.assign_statement())
        elif ctx.if_statement() :
            return self.visit(ctx.if_statement())
        elif ctx.for_statement() :
            return self.visit(ctx.for_statement())
        elif ctx.break_statement() :
            return self.visit(ctx.break_statement())
        elif ctx.continue_statement() :
            return self.visit(ctx.continue_statement())
        elif ctx.return_statement() :
            return self.visit(ctx.return_statement())
        elif ctx.method_invocate_statement() :
            return self.visit(ctx.method_invocate_statement())
        elif ctx.block_statement():
            return self.visit(ctx.block_statement())
        

    # Visit a parse tree produced by D96Parser#var_const_decl_statement.
    # var_const_decl_statement 	: var_const_decl_1 | var_const_decl_2
    # checked
    def visitVar_const_decl_statement(self, ctx:D96Parser.Var_const_decl_statementContext):
        if ctx.var_const_decl_1():
            return self.visit(ctx.var_const_decl_1())
        elif ctx.var_const_decl_2():
            return self.visit(ctx.var_const_decl_2())


    # Visit a parse tree produced by D96Parser#assign_statement.
    # assign_statement 	: expr (ASSIGN expr)+ 
    ## ?? kiem tra lhs vs rhs
    def visitAssign_statement(self, ctx:D96Parser.Assign_statementContext):
        exp = [self.visit(i) for i in ctx.expr()]
        assign = [i.getText() for i in ctx.ASSIGN()]
        lhs = exp[0]
        for i in range(len(assign)):
            rhs =  exp[i+1]
            lhs = Assign(lhs,rhs)
        return lhs


    # Visit a parse tree produced by D96Parser#if_statement.
    # if_statement : IF LP  expr RP block_statement (ELSEIF LP expr RP block_statement)* (ELSE block_statement)?
    def visitIf_statement(self, ctx:D96Parser.If_statementContext):
        if ctx.ELSE():
            if ctx.ELSEIF(): # if exp elseif exp else exp
                tmp_if = self.visit(ctx.block_statement(len(ctx.block_statement()) - 1 ))
                for i in range(len(ctx.expr())-1,-1,-1):
                    tmp_if = If(self.visit(ctx.expr(i)),self.visit(ctx.block_statement(i)),tmp_if) # return if
                return tmp_if
            else: # if exp else exp
                return If(self.visit(ctx.expr(0)),self.visit(ctx.block_statement(0)),self.visit(ctx.block_statement(1)))
        else : # case no else:
            if ctx.ELSEIF(): # if exp elseif exp elseif exp
                tmp_if = None
                for i in range(len(ctx.expr())-1,-1,-1):
                    tmp_if = If(self.visit(ctx.expr(i)),self.visit(ctx.block_statement(i)),tmp_if) # return if
                return tmp_if
            else: # if exp
                return If(self.visit(ctx.expr(0)),self.visit(ctx.block_statement(0))) 


    # Visit a parse tree produced by D96Parser#for_statement.
    # for_statement : FOREACH LP ID IN expr DOUBLEDOT expr (BY expr)? RP block_statement
    def visitFor_statement(self, ctx:D96Parser.For_statementContext):
        id = Id(ctx.ID().getText())
        exprs = [self.visit(i) for i in ctx.expr()]
        expr1 = exprs[0]
        expr2 = exprs[1]
        if len(exprs) == 3:
            expr3 = exprs[2]
        else: expr3 = IntLiteral(1)
        loop = self.visit(ctx.block_statement())
        return For(id,expr1,expr2,loop,expr3)


    # Visit a parse tree produced by D96Parser#break_statement.
    # break_statement : BREAK SEMI
    def visitBreak_statement(self, ctx:D96Parser.Break_statementContext):
        return Break()


    # Visit a parse tree produced by D96Parser#continue_statement.
    # continue_statement : CONTINUE SEMI
    def visitContinue_statement(self, ctx:D96Parser.Continue_statementContext):
        return Continue()


    # Visit a parse tree produced by D96Parser#return_statement.
    # return_statement : RETURN expr? SEMI
    def visitReturn_statement(self, ctx:D96Parser.Return_statementContext):
        if ctx.expr():
            # self.ret_flag = 1
            return Return(self.visit(ctx.expr()))
        else: 
            return Return()
    

    
    # Visit a parse tree produced by D96Parser#method_invocate_expression.
    # method_invocate_expression	: instance_method_invocate | static_method_invocate 
    # def visitMethod_invocate_expression(self, ctx:D96Parser.Method_invocate_expressionContext):
    #     if ctx.instance_method_invocate():
    #         tmp = self.visit(ctx.instance_method_invocate())
    #         return CallExpr(tmp[0],tmp[1],tmp[2])
    #     else:
    #         tmp = self.visit(ctx.static_method_invocate())
    #         return CallExpr(tmp[0],tmp[1],tmp[2])

    # Visit a parse tree produced by D96Parser#method_invocate_statement.
    # method_invocate_statement	: instance_method_invocate | static_method_invocate 
    def visitMethod_invocate_statement(self, ctx:D96Parser.Method_invocate_statementContext):
        if ctx.instance_method_invocate():
            tmp = self.visit(ctx.instance_method_invocate())
            return CallStmt(tmp[0],tmp[1],tmp[2])
        else:
            tmp = self.visit(ctx.static_method_invocate())
            return CallStmt(tmp[0],tmp[1],tmp[2])
    
    # Visit a parse tree produced by D96Parser#instance_method_invocate.
    # instance_method_invocate : expr_7  DOT ID LP (expr (COMMA expr)* )? RP SEMI? 
    def visitInstance_method_invocate(self, ctx:D96Parser.Instance_method_invocateContext):
            obj = self.visit(ctx.expr_7())
            method = Id(ctx.ID().getText())
            exprs = [self.visit(i) for i in ctx.expr()]
            return (obj,method,exprs) 


    # Visit a parse tree produced by D96Parser#static_method_invocate.
    # static_method_invocate   : expr_7  STATIC_GLOBAL_DOT DOLLAR_ID LP (expr (COMMA expr)* )? RP SEMI?
    def visitStatic_method_invocate(self, ctx:D96Parser.Static_method_invocateContext):
        obj = self.visit(ctx.expr_7())
        method = Id(ctx.DOLLAR_ID().getText())
        exprs = [self.visit(i) for i in ctx.expr()]
        return (obj,method,exprs) 



    # Visit a parse tree produced by D96Parser#var_const_decl_1.
    # var_const_decl_1 : (VAR|VAL) ID (COMMA ID )* COLON data_types SEMI
    def visitVar_const_decl_1(self, ctx:D96Parser.Var_const_decl_1Context):
        ctype = self.visit(ctx.data_types())
        exp = None
        res = []
        if ctx.VAL(): # Val a,$b:Int
            for i in ctx.ID():
                id = i.getText() # return: Id(text)
                if id[0] == "$":
                    const = Id(id)
                else:
                    const = Id(id)
                const_decl = ConstDecl(const,ctype,exp)
                res += [const_decl]
            return res # return 1-d array [AttributeDecl(Instance,ConstDecl(Id(a),IntType)), AttributeDecl(Static,ConstDecl(Id(b),IntType))]
        elif ctx.VAR():
            for i in ctx.ID():
                id = i.getText() # return: Id(text)
                if str(ctype)[0] == "C":
                    exp = NullLiteral()
                if id[0] == "$":
                    const = Id(id)
                else:
                    const = Id(id)
                var_decl = VarDecl(const,ctype,exp)
                res += [var_decl]
            return res 


    # Visit a parse tree produced by D96Parser#var_const_decl_2.
    # var_const_decl_2 : (VAR|VAL) var_const_testing SEMI
    def visitVar_const_decl_2(self, ctx:D96Parser.Var_const_decl_2Context):
        tmp = self.visit(ctx.var_const_testing())
        ids = tmp[0] # ['a','b']
        exps = tmp[1]
        exps.reverse()
        type = tmp[2]
        res = []
        if ctx.VAL(): # Val a,$b:Int = 1,2,3
            for i in range(len(ids)):
                # if ids[i][0] == "$":
                #     kind = Static()
                # else:
                #     kind = Instance()  
                const_decl = ConstDecl(Id(ids[i]),type,exps[i])
                res += [const_decl]
            return res # return 1-d array [AttributeDecl(Instance,ConstDecl(Id(a),IntType)), AttributeDecl(Static,ConstDecl(Id(b),IntType))]
        elif ctx.VAR():
            for i in range(len(ids)):
                # if ids[i][0] == "$":
                #     kind = Static()
                # else:
                #     kind = Instance()  
                var_decl = VarDecl(Id(ids[i]),type,exps[i])
                res += [var_decl]
            return res 


    # Visit a parse tree produced by D96Parser#var_const_testing.
    # var_const_testing: ((ID COLON data_types ASSIGN expr) | (ID COMMA var_const_testing (COMMA expr)))
    def visitVar_const_testing(self, ctx:D96Parser.Var_const_testingContext):
        id = [ctx.ID().getText() ] # a,b int = 2,3

        exp = [self.visit(ctx.expr())] # reversed list: [3,2]
        if ctx.var_const_testing():
            tmp = self.visit(ctx.var_const_testing())
            id.extend(tmp[0])
            exp.extend(tmp[1])
            return (id,exp,tmp[2])
        else:
            type = self.visit(ctx.data_types())
            return (id,exp,type)

    # Visit a parse tree produced by D96Parser#data_types.
    # data_types: primitive_types | array_type | class_type
    # checked
    def visitData_types(self, ctx:D96Parser.Data_typesContext):
        if ctx.primitive_types():
            return self.visit(ctx.primitive_types())
        elif ctx.array_type():
            return self.visit(ctx.array_type())
        elif ctx.class_type():
            return self.visit(ctx.class_type())


    # Visit a parse tree produced by D96Parser#primitive_types.
    # primitive_types: INT_TYPE | FLOAT_TYPE | STRING_TYPE | BOOLEAN_TYPE
    # checked
    def visitPrimitive_types(self, ctx:D96Parser.Primitive_typesContext):
        if ctx.INT_TYPE():
            return IntType()
        elif ctx.FLOAT_TYPE():
            return FloatType()
        elif ctx.BOOLEAN_TYPE():
            return BoolType()
        elif ctx.STRING_TYPE():
            return StringType()


    # Visit a parse tree produced by D96Parser#array_type.
    # array_type: ARRAY LSB (data_types) COMMA NATURAL  RSB
    # checked
    def visitArray_type(self, ctx:D96Parser.Array_typeContext):
        num = ctx.NATURAL().getText()
        if num[:2] == "0x" or num[:2] == "0X": 
            size = int(num,16)
        elif num[:2] == "0b" or num[:2] == "0B": 
            size = int(num,2)
        elif num[0] == "0": 
            size = int(num,8)
        else: 
            size = int(num,10)
        eleType =  self.visit(ctx.data_types())
        return ArrayType(size,eleType)


    # Visit a parse tree produced by D96Parser#class_type.
    # checked
    def visitClass_type(self, ctx:D96Parser.Class_typeContext):
        return ClassType(Id(ctx.ID().getText()))


    # Visit a parse tree produced by D96Parser#class_new_object.
    # class_new_object: NEW ID LP (expr (COMMA expr)* )? RP
    # checked
    def visitClass_new_object(self, ctx:D96Parser.Class_new_objectContext):
        # id = ClassType(Id(ctx.ID().getText()))
        id = Id(ctx.ID().getText())
        exprs = [ self.visit(i) for i in ctx.expr()]
        return NewExpr(id,exprs)


    # Visit a parse tree produced by D96Parser#expr.
    # expr   : expr_1 (STRING_CONCATE | STRING_COMPARE) expr_1 | expr_1
    def visitExpr(self, ctx:D96Parser.ExprContext):
        if ctx.STRING_COMPARE():
            l = self.visit(ctx.expr_1(0))
            r = self.visit(ctx.expr_1(1))
            return BinaryOp(ctx.STRING_COMPARE().getText(),l,r)
        elif ctx.STRING_CONCATE():
            l = self.visit(ctx.expr_1(0))
            r = self.visit(ctx.expr_1(1))
            return BinaryOp(ctx.STRING_CONCATE().getText(),l,r)
        else: 
            return self.visit(ctx.expr_1(0))


    # Visit a parse tree produced by D96Parser#expr_1.
    # expr_1 : expr_2 (EQUAL | NOT_EQUAL | LESS_THAN | GREATER_THAN | LESS_THAN_EQUAL | GREATER_THAN_EQUAL ) expr_2 | expr_2
    def visitExpr_1(self, ctx:D96Parser.Expr_1Context):
        if ctx.EQUAL():
            l = self.visit(ctx.expr_2(0))
            r = self.visit(ctx.expr_2(1))
            return BinaryOp(ctx.EQUAL().getText(),l,r)
        elif ctx.NOT_EQUAL():
            l = self.visit(ctx.expr_2(0))
            r = self.visit(ctx.expr_2(1))
            return BinaryOp(ctx.NOT_EQUAL().getText(),l,r)
        elif ctx.LESS_THAN():
            l = self.visit(ctx.expr_2(0))
            r = self.visit(ctx.expr_2(1))
            return BinaryOp(ctx.LESS_THAN().getText(),l,r)
        elif ctx.LESS_THAN_EQUAL():
            l = self.visit(ctx.expr_2(0))
            r = self.visit(ctx.expr_2(1))
            return BinaryOp(ctx.LESS_THAN_EQUAL().getText(),l,r)
        elif ctx.GREATER_THAN():
            l = self.visit(ctx.expr_2(0))
            r = self.visit(ctx.expr_2(1))
            return BinaryOp(ctx.GREATER_THAN().getText(),l,r)    
        elif ctx.GREATER_THAN_EQUAL():
            l = self.visit(ctx.expr_2(0))
            r = self.visit(ctx.expr_2(1))
            return BinaryOp(ctx.GREATER_THAN_EQUAL().getText(),l,r)
        else: 
            return self.visit(ctx.expr_2(0))


    # Visit a parse tree produced by D96Parser#expr_2.
    # expr_2 : expr_2 (AND|OR) expr_3 | expr_3 
    def visitExpr_2(self, ctx:D96Parser.Expr_2Context):
        if ctx.AND():
            l = self.visit(ctx.expr_2())
            r = self.visit(ctx.expr_3())
            return BinaryOp(ctx.AND().getText(),l,r)
        elif ctx.OR():
            l = self.visit(ctx.expr_2())
            r = self.visit(ctx.expr_3())
            return BinaryOp(ctx.OR().getText(),l,r)
        else: 
            return self.visit(ctx.expr_3())


    # Visit a parse tree produced by D96Parser#expr_3.
    # expr_3 : expr_3 (ADD|SUB) expr_4 | expr_4
    def visitExpr_3(self, ctx:D96Parser.Expr_3Context):
        if ctx.ADD():
            l = self.visit(ctx.expr_3())
            r = self.visit(ctx.expr_4())
            return BinaryOp(ctx.ADD().getText(),l,r)
        elif ctx.SUB():
            l = self.visit(ctx.expr_3())
            r = self.visit(ctx.expr_4())
            return BinaryOp(ctx.SUB().getText(),l,r)
        else: 
            return self.visit(ctx.expr_4())


    # Visit a parse tree produced by D96Parser#expr_4.
    # expr_4 : expr_4 (MUL|DIV|MOD) expr_5 | expr_5
    def visitExpr_4(self, ctx:D96Parser.Expr_4Context):
        if ctx.MOD():
            l = self.visit(ctx.expr_4())
            r = self.visit(ctx.expr_5())
            return BinaryOp(ctx.MOD().getText(),l,r)
        elif ctx.MUL():
            l = self.visit(ctx.expr_4())
            r = self.visit(ctx.expr_5())
            return BinaryOp(ctx.MUL().getText(),l,r)
        elif ctx.DIV():
            l = self.visit(ctx.expr_4())
            r = self.visit(ctx.expr_5())
            return BinaryOp(ctx.DIV().getText(),l,r)
        else:
            return self.visit(ctx.expr_5())


    # Visit a parse tree produced by D96Parser#expr_5.
    # expr_5 : NOT expr_5| expr_6;
    def visitExpr_5(self, ctx:D96Parser.Expr_5Context):
        if ctx.NOT():
            r = self.visit(ctx.expr_5())
            return UnaryOp(ctx.NOT().getText(),r)
        else:
            return self.visit(ctx.expr_6())


    # Visit a parse tree produced by D96Parser#expr_6.
    # expr_6 : SUB expr_6| expr_7
    def visitExpr_6(self, ctx:D96Parser.Expr_6Context):
        if ctx.SUB():
            r = self.visit(ctx.expr_6())
            return UnaryOp(ctx.SUB().getText(),r)
        else:
            return self.visit(ctx.expr_7())


    # Visit a parse tree produced by D96Parser#expr_7.
    # expr_7 : expr_7 index_id | expr_8
    # a[4][2][3] 
    def visitExpr_7(self, ctx:D96Parser.Expr_7Context):
        if ctx.index_id():
            exps = self.visit(ctx.index_id()) # list of exprs
            return ArrayCell(self.visit(ctx.expr_7()),exps) 
        else:
            return self.visit(ctx.expr_8())


    # Visit a parse tree produced by D96Parser#expr_8.
    # expr_8 : expr_8 DOT ID (LP (expr (COMMA expr)*)? RP)?   | expr_9
    def visitExpr_8(self, ctx:D96Parser.Expr_8Context):
        if ctx.DOT():
            l = self.visit(ctx.expr_8())
            if ctx.LP():
                if ctx.expr():
                    exps = [self.visit(i) for i in ctx.expr()]
                else: exps = []
                method = Id(ctx.ID().getText())
                return CallExpr(l,method,exps)
            else:
                return FieldAccess(l,Id(ctx.ID().getText()))
        else:
            return self.visit(ctx.expr_9())


    # Visit a parse tree produced by D96Parser#expr_9.
    # expr_9 : expr_10 STATIC_GLOBAL_DOT DOLLAR_ID (LP (expr (COMMA expr)*)? RP)? | expr_10
    def visitExpr_9(self, ctx:D96Parser.Expr_9Context):
        if ctx.STATIC_GLOBAL_DOT():
            l = self.visit(ctx.expr_10())
            if ctx.LP():
                if ctx.expr():
                    exps = [self.visit(i) for i in ctx.expr()]
                else: exps = []
                method = Id(ctx.DOLLAR_ID().getText())
                return CallExpr(l,method,exps)
            else:
                return FieldAccess(l,Id(ctx.DOLLAR_ID().getText()))
        else:
            return self.visit(ctx.expr_10())


    # Visit a parse tree produced by D96Parser#expr_10.
    # expr_10: NEW expr_10 | expr_11 ;
    def visitExpr_10(self, ctx:D96Parser.Expr_10Context):
        if ctx.NEW():
            r = self.visit(ctx.expr_10()) 
            return UnaryOp(ctx.NEW().getText(),r)
        else:
            return self.visit(ctx.expr_11())


    # Visit a parse tree produced by D96Parser#expr_11.
    # expr_11: literals  | method_invocate_expression  | SELF  
    # |((ID|DOLLAR_ID)index_id) | indexed_array  |  NULL | class_new_object 
    # | identifier  |(LP expr+ RP); 
    def visitExpr_11(self, ctx:D96Parser.Expr_11Context):
        if ctx.literals():
            return self.visit(ctx.literals())
        # elif ctx.method_invocate_expression(): 
        #     return self.visit(ctx.method_invocate_expression())
        elif ctx.SELF():
            return SelfLiteral()    
        elif ctx.index_id():
            if ctx.DOLLAR_ID():
                arr = ctx.DOLLAR_ID().getText()
            else:
                arr = ctx.ID().getText()
            return ArrayCell(Id(arr),self.visit(ctx.index_id()))
        elif ctx.indexed_array(): 
            return self.visit(ctx.indexed_array())
        elif ctx.NULL(): 
            return  NullLiteral()
        elif ctx.class_new_object(): 
            return self.visit(ctx.class_new_object())
        elif ctx.identifier():
            return self.visit(ctx.identifier())
        else: 
            return self.visit(ctx.expr())


    # Visit a parse tree produced by D96Parser#indexed_array.
    # indexed_array : ARRAY LP (expr (COMMA expr)* RP)?   ## array_literal
    def visitIndexed_array(self, ctx:D96Parser.Indexed_arrayContext):
        l = [self.visit(i) for i in ctx.expr()]
        return ArrayLiteral(l)


    # Visit a parse tree produced by D96Parser#literals.
    # literals: (NATURAL | INTEGER_LIERAL | FLOAT_LITERAL  | BOOLEAN_LITERAL | STRING_LITERAL ) 
    # checked
    def visitLiterals(self, ctx:D96Parser.LiteralsContext):
        if ctx.NATURAL():
            num = ctx.NATURAL().getText()
            if num[:2] == "0x" or num[:2] == "0X": 
                return IntLiteral(int(ctx.NATURAL().getText(),16))
            elif num[:2] == "0b" or num[:2] == "0B": 
                return IntLiteral(int(ctx.NATURAL().getText(),2))
            elif num[0] == "0": 
                return IntLiteral(int(ctx.NATURAL().getText(),8))
            else: 
                return IntLiteral(int(ctx.NATURAL().getText(),10))
        elif ctx.INTEGER_LIERAL():
            num = ctx.INTEGER_LIERAL().getText()
            if num[:2] == "0x" or num[:2] == "0X": 
                return IntLiteral(int(ctx.INTEGER_LIERAL().getText(),16))
            elif num[:2] == "0b" or num[:2] == "0B": 
                return IntLiteral(int(ctx.INTEGER_LIERAL().getText(),2))
            elif num[:1] == "0" : 
                return IntLiteral(int(ctx.INTEGER_LIERAL().getText(),8))
            else: 
                return IntLiteral(int(ctx.INTEGER_LIERAL().getText(),10))
        elif ctx.FLOAT_LITERAL():
            return FloatLiteral(float(ctx.FLOAT_LITERAL().getText()))
        elif ctx.BOOLEAN_LITERAL():
            return BooleanLiteral(ctx.BOOLEAN_LITERAL().getText()=="True" )
        elif ctx.STRING_LITERAL():
            return StringLiteral(str(ctx.STRING_LITERAL().getText()))

    # Visit a parse tree produced by D96Parser#identifier.
    # identifier: (ID | DOLLAR_ID );
    # checked
    def visitIdentifier(self, ctx:D96Parser.IdentifierContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        else: 
            return Id(ctx.DOLLAR_ID().getText())


    # Visit a parse tree produced by D96Parser#index_id.
    # (LSB expr RSB)+    
    ## can be concerned as multi-dim array
    def visitIndex_id(self, ctx:D96Parser.Index_idContext):
        exps = [self.visit(i) for i in ctx.expr()]
        return exps

        

