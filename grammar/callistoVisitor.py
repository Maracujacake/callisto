# Generated from grammar\callisto.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .callistoParser import callistoParser
else:
    from callistoParser import callistoParser

# This class defines a complete generic visitor for a parse tree produced by callistoParser.

class callistoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by callistoParser#prog.
    def visitProg(self, ctx:callistoParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by callistoParser#printStatement.
    def visitPrintStatement(self, ctx:callistoParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by callistoParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:callistoParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by callistoParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:callistoParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by callistoParser#expressionStatement.
    def visitExpressionStatement(self, ctx:callistoParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by callistoParser#params.
    def visitParams(self, ctx:callistoParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by callistoParser#stringExpr.
    def visitStringExpr(self, ctx:callistoParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by callistoParser#variableExpr.
    def visitVariableExpr(self, ctx:callistoParser.VariableExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by callistoParser#arrayExpr.
    def visitArrayExpr(self, ctx:callistoParser.ArrayExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by callistoParser#addExpr.
    def visitAddExpr(self, ctx:callistoParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by callistoParser#numberExpr.
    def visitNumberExpr(self, ctx:callistoParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by callistoParser#functionCallExpr.
    def visitFunctionCallExpr(self, ctx:callistoParser.FunctionCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by callistoParser#mulExpr.
    def visitMulExpr(self, ctx:callistoParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by callistoParser#divExpr.
    def visitDivExpr(self, ctx:callistoParser.DivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by callistoParser#parensExpr.
    def visitParensExpr(self, ctx:callistoParser.ParensExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by callistoParser#dictExpr.
    def visitDictExpr(self, ctx:callistoParser.DictExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by callistoParser#subExpr.
    def visitSubExpr(self, ctx:callistoParser.SubExprContext):
        return self.visitChildren(ctx)



del callistoParser