# Generated from grammar\callisto.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,21,119,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,5,0,10,8,0,10,0,12,
        0,13,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,22,8,1,1,1,1,1,1,1,5,1,
        27,8,1,10,1,12,1,30,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,
        41,8,1,1,2,1,2,1,2,5,2,46,8,2,10,2,12,2,49,9,2,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,64,8,3,10,3,12,3,67,9,3,3,
        3,69,8,3,1,3,1,3,1,3,1,3,1,3,5,3,76,8,3,10,3,12,3,79,9,3,3,3,81,
        8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,92,8,3,10,3,12,3,95,
        9,3,3,3,97,8,3,1,3,3,3,100,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,5,3,114,8,3,10,3,12,3,117,9,3,1,3,0,1,6,4,0,2,4,6,
        0,0,137,0,11,1,0,0,0,2,40,1,0,0,0,4,42,1,0,0,0,6,99,1,0,0,0,8,10,
        3,2,1,0,9,8,1,0,0,0,10,13,1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,
        1,1,0,0,0,13,11,1,0,0,0,14,15,3,6,3,0,15,16,5,1,0,0,16,41,1,0,0,
        0,17,18,5,2,0,0,18,19,5,20,0,0,19,21,5,3,0,0,20,22,3,4,2,0,21,20,
        1,0,0,0,21,22,1,0,0,0,22,23,1,0,0,0,23,24,5,4,0,0,24,28,5,5,0,0,
        25,27,3,2,1,0,26,25,1,0,0,0,27,30,1,0,0,0,28,26,1,0,0,0,28,29,1,
        0,0,0,29,31,1,0,0,0,30,28,1,0,0,0,31,41,5,6,0,0,32,33,5,20,0,0,33,
        34,5,7,0,0,34,35,3,6,3,0,35,36,5,1,0,0,36,41,1,0,0,0,37,38,3,6,3,
        0,38,39,5,1,0,0,39,41,1,0,0,0,40,14,1,0,0,0,40,17,1,0,0,0,40,32,
        1,0,0,0,40,37,1,0,0,0,41,3,1,0,0,0,42,47,5,20,0,0,43,44,5,8,0,0,
        44,46,5,20,0,0,45,43,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,
        0,0,0,48,5,1,0,0,0,49,47,1,0,0,0,50,51,6,3,-1,0,51,100,5,18,0,0,
        52,100,5,19,0,0,53,100,5,20,0,0,54,55,5,3,0,0,55,56,3,6,3,0,56,57,
        5,4,0,0,57,100,1,0,0,0,58,59,5,20,0,0,59,68,5,3,0,0,60,65,3,6,3,
        0,61,62,5,8,0,0,62,64,3,6,3,0,63,61,1,0,0,0,64,67,1,0,0,0,65,63,
        1,0,0,0,65,66,1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,68,60,1,0,0,0,
        68,69,1,0,0,0,69,70,1,0,0,0,70,100,5,4,0,0,71,80,5,13,0,0,72,77,
        3,6,3,0,73,74,5,8,0,0,74,76,3,6,3,0,75,73,1,0,0,0,76,79,1,0,0,0,
        77,75,1,0,0,0,77,78,1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,80,72,1,
        0,0,0,80,81,1,0,0,0,81,82,1,0,0,0,82,100,5,14,0,0,83,96,5,15,0,0,
        84,85,5,20,0,0,85,86,5,16,0,0,86,93,3,6,3,0,87,88,5,8,0,0,88,89,
        5,20,0,0,89,90,5,16,0,0,90,92,3,6,3,0,91,87,1,0,0,0,92,95,1,0,0,
        0,93,91,1,0,0,0,93,94,1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,96,84,
        1,0,0,0,96,97,1,0,0,0,97,98,1,0,0,0,98,100,5,17,0,0,99,50,1,0,0,
        0,99,52,1,0,0,0,99,53,1,0,0,0,99,54,1,0,0,0,99,58,1,0,0,0,99,71,
        1,0,0,0,99,83,1,0,0,0,100,115,1,0,0,0,101,102,10,11,0,0,102,103,
        5,9,0,0,103,114,3,6,3,12,104,105,10,10,0,0,105,106,5,10,0,0,106,
        114,3,6,3,11,107,108,10,9,0,0,108,109,5,11,0,0,109,114,3,6,3,10,
        110,111,10,8,0,0,111,112,5,12,0,0,112,114,3,6,3,9,113,101,1,0,0,
        0,113,104,1,0,0,0,113,107,1,0,0,0,113,110,1,0,0,0,114,117,1,0,0,
        0,115,113,1,0,0,0,115,116,1,0,0,0,116,7,1,0,0,0,117,115,1,0,0,0,
        14,11,21,28,40,47,65,68,77,80,93,96,99,113,115
    ]

class callistoParser ( Parser ):

    grammarFileName = "callisto.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'fn'", "'('", "')'", "'do'", "'end'", 
                     "'='", "','", "'+'", "'-'", "'*'", "'/'", "'['", "']'", 
                     "'{'", "':'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUMBER", "STRING", "ID", 
                      "WS" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_params = 2
    RULE_expr = 3

    ruleNames =  [ "prog", "statement", "params", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    NUMBER=18
    STRING=19
    ID=20
    WS=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(callistoParser.StatementContext)
            else:
                return self.getTypedRuleContext(callistoParser.StatementContext,i)


        def getRuleIndex(self):
            return callistoParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = callistoParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1875980) != 0):
                self.state = 8
                self.statement()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return callistoParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a callistoParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(callistoParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStatement" ):
                return visitor.visitPrintStatement(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a callistoParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(callistoParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStatement" ):
                return visitor.visitExpressionStatement(self)
            else:
                return visitor.visitChildren(self)


    class FunctionDeclarationContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a callistoParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(callistoParser.ID, 0)
        def params(self):
            return self.getTypedRuleContext(callistoParser.ParamsContext,0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(callistoParser.StatementContext)
            else:
                return self.getTypedRuleContext(callistoParser.StatementContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclaration" ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)


    class VariableDeclarationContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a callistoParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(callistoParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(callistoParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = callistoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = callistoParser.PrintStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.expr(0)
                self.state = 15
                self.match(callistoParser.T__0)
                pass

            elif la_ == 2:
                localctx = callistoParser.FunctionDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                self.match(callistoParser.T__1)
                self.state = 18
                self.match(callistoParser.ID)
                self.state = 19
                self.match(callistoParser.T__2)
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 20
                    self.params()


                self.state = 23
                self.match(callistoParser.T__3)
                self.state = 24
                self.match(callistoParser.T__4)
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1875980) != 0):
                    self.state = 25
                    self.statement()
                    self.state = 30
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 31
                self.match(callistoParser.T__5)
                pass

            elif la_ == 3:
                localctx = callistoParser.VariableDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.match(callistoParser.ID)
                self.state = 33
                self.match(callistoParser.T__6)
                self.state = 34
                self.expr(0)
                self.state = 35
                self.match(callistoParser.T__0)
                pass

            elif la_ == 4:
                localctx = callistoParser.ExpressionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 37
                self.expr(0)
                self.state = 38
                self.match(callistoParser.T__0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(callistoParser.ID)
            else:
                return self.getToken(callistoParser.ID, i)

        def getRuleIndex(self):
            return callistoParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = callistoParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(callistoParser.ID)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 43
                self.match(callistoParser.T__7)
                self.state = 44
                self.match(callistoParser.ID)
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return callistoParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class StringExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a callistoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(callistoParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpr" ):
                return visitor.visitStringExpr(self)
            else:
                return visitor.visitChildren(self)


    class VariableExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a callistoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(callistoParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableExpr" ):
                return visitor.visitVariableExpr(self)
            else:
                return visitor.visitChildren(self)


    class ArrayExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a callistoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(callistoParser.ExprContext)
            else:
                return self.getTypedRuleContext(callistoParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayExpr" ):
                return visitor.visitArrayExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a callistoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(callistoParser.ExprContext)
            else:
                return self.getTypedRuleContext(callistoParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddExpr" ):
                return visitor.visitAddExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumberExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a callistoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(callistoParser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class FunctionCallExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a callistoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(callistoParser.ID, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(callistoParser.ExprContext)
            else:
                return self.getTypedRuleContext(callistoParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCallExpr" ):
                return visitor.visitFunctionCallExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a callistoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(callistoParser.ExprContext)
            else:
                return self.getTypedRuleContext(callistoParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulExpr" ):
                return visitor.visitMulExpr(self)
            else:
                return visitor.visitChildren(self)


    class DivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a callistoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(callistoParser.ExprContext)
            else:
                return self.getTypedRuleContext(callistoParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivExpr" ):
                return visitor.visitDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParensExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a callistoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(callistoParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParensExpr" ):
                return visitor.visitParensExpr(self)
            else:
                return visitor.visitChildren(self)


    class DictExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a callistoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(callistoParser.ID)
            else:
                return self.getToken(callistoParser.ID, i)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(callistoParser.ExprContext)
            else:
                return self.getTypedRuleContext(callistoParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDictExpr" ):
                return visitor.visitDictExpr(self)
            else:
                return visitor.visitChildren(self)


    class SubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a callistoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(callistoParser.ExprContext)
            else:
                return self.getTypedRuleContext(callistoParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubExpr" ):
                return visitor.visitSubExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = callistoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = callistoParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 51
                self.match(callistoParser.NUMBER)
                pass

            elif la_ == 2:
                localctx = callistoParser.StringExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 52
                self.match(callistoParser.STRING)
                pass

            elif la_ == 3:
                localctx = callistoParser.VariableExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 53
                self.match(callistoParser.ID)
                pass

            elif la_ == 4:
                localctx = callistoParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 54
                self.match(callistoParser.T__2)
                self.state = 55
                self.expr(0)
                self.state = 56
                self.match(callistoParser.T__3)
                pass

            elif la_ == 5:
                localctx = callistoParser.FunctionCallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 58
                self.match(callistoParser.ID)
                self.state = 59
                self.match(callistoParser.T__2)
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1875976) != 0):
                    self.state = 60
                    self.expr(0)
                    self.state = 65
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==8:
                        self.state = 61
                        self.match(callistoParser.T__7)
                        self.state = 62
                        self.expr(0)
                        self.state = 67
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 70
                self.match(callistoParser.T__3)
                pass

            elif la_ == 6:
                localctx = callistoParser.ArrayExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 71
                self.match(callistoParser.T__12)
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1875976) != 0):
                    self.state = 72
                    self.expr(0)
                    self.state = 77
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==8:
                        self.state = 73
                        self.match(callistoParser.T__7)
                        self.state = 74
                        self.expr(0)
                        self.state = 79
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 82
                self.match(callistoParser.T__13)
                pass

            elif la_ == 7:
                localctx = callistoParser.DictExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 83
                self.match(callistoParser.T__14)
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 84
                    self.match(callistoParser.ID)
                    self.state = 85
                    self.match(callistoParser.T__15)
                    self.state = 86
                    self.expr(0)
                    self.state = 93
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==8:
                        self.state = 87
                        self.match(callistoParser.T__7)
                        self.state = 88
                        self.match(callistoParser.ID)
                        self.state = 89
                        self.match(callistoParser.T__15)
                        self.state = 90
                        self.expr(0)
                        self.state = 95
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 98
                self.match(callistoParser.T__16)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 115
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 113
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = callistoParser.AddExprContext(self, callistoParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 101
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 102
                        self.match(callistoParser.T__8)
                        self.state = 103
                        self.expr(12)
                        pass

                    elif la_ == 2:
                        localctx = callistoParser.SubExprContext(self, callistoParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 104
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 105
                        self.match(callistoParser.T__9)
                        self.state = 106
                        self.expr(11)
                        pass

                    elif la_ == 3:
                        localctx = callistoParser.MulExprContext(self, callistoParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 107
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 108
                        self.match(callistoParser.T__10)
                        self.state = 109
                        self.expr(10)
                        pass

                    elif la_ == 4:
                        localctx = callistoParser.DivExprContext(self, callistoParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 110
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 111
                        self.match(callistoParser.T__11)
                        self.state = 112
                        self.expr(9)
                        pass

             
                self.state = 117
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         




