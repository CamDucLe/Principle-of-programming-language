# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_decl.
    def visitClass_decl(self, ctx:D96Parser.Class_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member_list.
    def visitMember_list(self, ctx:D96Parser.Member_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_decl.
    def visitAttribute_decl(self, ctx:D96Parser.Attribute_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_decl_1.
    def visitAttribute_decl_1(self, ctx:D96Parser.Attribute_decl_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_decl_2.
    def visitAttribute_decl_2(self, ctx:D96Parser.Attribute_decl_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_testing.
    def visitAttribute_testing(self, ctx:D96Parser.Attribute_testingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_decl.
    def visitMethod_decl(self, ctx:D96Parser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parameter_list.
    def visitParameter_list(self, ctx:D96Parser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parameter.
    def visitParameter(self, ctx:D96Parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constructor.
    def visitConstructor(self, ctx:D96Parser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destructor.
    def visitDestructor(self, ctx:D96Parser.DestructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_statement.
    def visitBlock_statement(self, ctx:D96Parser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statement.
    def visitStatement(self, ctx:D96Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_const_decl_statement.
    def visitVar_const_decl_statement(self, ctx:D96Parser.Var_const_decl_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_statement.
    def visitAssign_statement(self, ctx:D96Parser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_statement.
    def visitIf_statement(self, ctx:D96Parser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#for_statement.
    def visitFor_statement(self, ctx:D96Parser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#break_statement.
    def visitBreak_statement(self, ctx:D96Parser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continue_statement.
    def visitContinue_statement(self, ctx:D96Parser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return_statement.
    def visitReturn_statement(self, ctx:D96Parser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instance_call.
    def visitInstance_call(self, ctx:D96Parser.Instance_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_call.
    def visitStatic_call(self, ctx:D96Parser.Static_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_invocate_statement.
    def visitMethod_invocate_statement(self, ctx:D96Parser.Method_invocate_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_invocate_expression.
    def visitMethod_invocate_expression(self, ctx:D96Parser.Method_invocate_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instance_method_invocate.
    def visitInstance_method_invocate(self, ctx:D96Parser.Instance_method_invocateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_method_invocate.
    def visitStatic_method_invocate(self, ctx:D96Parser.Static_method_invocateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_access.
    def visitAttribute_access(self, ctx:D96Parser.Attribute_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instance_attribute_access.
    def visitInstance_attribute_access(self, ctx:D96Parser.Instance_attribute_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_attribute_access.
    def visitStatic_attribute_access(self, ctx:D96Parser.Static_attribute_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_const_decl_1.
    def visitVar_const_decl_1(self, ctx:D96Parser.Var_const_decl_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_const_decl_2.
    def visitVar_const_decl_2(self, ctx:D96Parser.Var_const_decl_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_const_testing.
    def visitVar_const_testing(self, ctx:D96Parser.Var_const_testingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#data_types.
    def visitData_types(self, ctx:D96Parser.Data_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#primitive_types.
    def visitPrimitive_types(self, ctx:D96Parser.Primitive_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_type.
    def visitArray_type(self, ctx:D96Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_type.
    def visitClass_type(self, ctx:D96Parser.Class_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_new_object.
    def visitClass_new_object(self, ctx:D96Parser.Class_new_objectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literals.
    def visitLiterals(self, ctx:D96Parser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#identifier.
    def visitIdentifier(self, ctx:D96Parser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_id.
    def visitIndex_id(self, ctx:D96Parser.Index_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx:D96Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_1.
    def visitExpr_1(self, ctx:D96Parser.Expr_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_2.
    def visitExpr_2(self, ctx:D96Parser.Expr_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_3.
    def visitExpr_3(self, ctx:D96Parser.Expr_3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_4.
    def visitExpr_4(self, ctx:D96Parser.Expr_4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_5.
    def visitExpr_5(self, ctx:D96Parser.Expr_5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_6.
    def visitExpr_6(self, ctx:D96Parser.Expr_6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_7.
    def visitExpr_7(self, ctx:D96Parser.Expr_7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_8.
    def visitExpr_8(self, ctx:D96Parser.Expr_8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_9.
    def visitExpr_9(self, ctx:D96Parser.Expr_9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_10.
    def visitExpr_10(self, ctx:D96Parser.Expr_10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_11.
    def visitExpr_11(self, ctx:D96Parser.Expr_11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multi_dimensional_arrays.
    def visitMulti_dimensional_arrays(self, ctx:D96Parser.Multi_dimensional_arraysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#indexed_array.
    def visitIndexed_array(self, ctx:D96Parser.Indexed_arrayContext):
        return self.visitChildren(ctx)



del D96Parser