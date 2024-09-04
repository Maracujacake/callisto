# Generated from callisto.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .callistoParser import callistoParser
else:
    from callistoParser import callistoParser

# This class defines a complete generic visitor for a parse tree produced by callistoParser.

class callistoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by callistoParser#program.
    def visitProgram(self, ctx:callistoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by callistoParser#system.
    def visitSystem(self, ctx:callistoParser.SystemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by callistoParser#planetList.
    def visitPlanetList(self, ctx:callistoParser.PlanetListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by callistoParser#planet.
    def visitPlanet(self, ctx:callistoParser.PlanetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by callistoParser#moonList.
    def visitMoonList(self, ctx:callistoParser.MoonListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by callistoParser#moon.
    def visitMoon(self, ctx:callistoParser.MoonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by callistoParser#star.
    def visitStar(self, ctx:callistoParser.StarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by callistoParser#orbit.
    def visitOrbit(self, ctx:callistoParser.OrbitContext):
        return self.visitChildren(ctx)



del callistoParser