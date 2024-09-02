from grammar.callistoVisitor import callistoVisitor as CallistoVisitor
from grammar.callistoParser import  callistoParser as CallistoParser

class CallistoInterpreter(CallistoVisitor):
    def __init__(self):
        self.variables = {}
        self.functions = {}

    def visitPrintStatement(self, ctx: CallistoParser.PrintStatementContext):
        result = self.visit(ctx.expr())
        print(result)

    def visitFunctionDeclaration(self, ctx: CallistoParser.FunctionDeclarationContext):
        func_name = ctx.ID().getText()
        params = [p.getText() for p in ctx.params().ID()]
        body = [self.visit(s) for s in ctx.statement()]
        self.functions[func_name] = (params, body)
        return None

    def visitVariableDeclaration(self, ctx: CallistoParser.VariableDeclarationContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.variables[var_name] = value
        return None

    def visitExpressionStatement(self, ctx: CallistoParser.ExpressionStatementContext):
        return self.visit(ctx.expr())

    def visitAddExpr(self, ctx: CallistoParser.AddExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left + right

    def visitSubExpr(self, ctx: CallistoParser.SubExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left - right

    def visitMulExpr(self, ctx: CallistoParser.MulExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left * right

    def visitDivExpr(self, ctx: CallistoParser.DivExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left / right

    def visitNumberExpr(self, ctx: CallistoParser.NumberExprContext):
        return int(ctx.NUMBER().getText())

    def visitStringExpr(self, ctx: CallistoParser.StringExprContext):
        return ctx.STRING().getText().strip('"')

    def visitVariableExpr(self, ctx: CallistoParser.VariableExprContext):
        var_name = ctx.ID().getText()
        if var_name in self.variables:
            return self.variables[var_name]
        raise RuntimeError(f"Undefined variable '{var_name}'")

    def visitParensExpr(self, ctx: CallistoParser.ParensExprContext):
        return self.visit(ctx.expr())

    def visitFunctionCallExpr(self, ctx: CallistoParser.FunctionCallExprContext):
        func_name = ctx.ID().getText()
        if func_name not in self.functions:
            raise RuntimeError(f"Undefined function '{func_name}'")

        params = [self.visit(arg) for arg in ctx.expr()]
        param_names, body = self.functions[func_name]

        if len(params) != len(param_names):
            raise RuntimeError(f"Function '{func_name}' expects {len(param_names)} arguments")

        local_vars = dict(zip(param_names, params))
        prev_vars = self.variables.copy()
        self.variables.update(local_vars)

        result = None
        for stmt in body:
            result = stmt  # assume the last statement's result is the return value
        self.variables = prev_vars  # restore previous variables
        return result

    def visitArrayExpr(self, ctx: CallistoParser.ArrayExprContext):
        return [self.visit(expr) for expr in ctx.expr()]

    def visitDictExpr(self, ctx: CallistoParser.DictExprContext):
        return {self.visit(ctx.ID(i)): self.visit(ctx.expr(i)) for i in range(len(ctx.ID()))}
