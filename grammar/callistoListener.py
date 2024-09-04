# Generated from callisto.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .callistoParser import callistoParser
else:
    from callistoParser import callistoParser

# This class defines a complete listener for a parse tree produced by callistoParser.
class callistoListener(ParseTreeListener):

    # Enter a parse tree produced by callistoParser#program.
    def enterProgram(self, ctx:callistoParser.ProgramContext):
        pass

    # Exit a parse tree produced by callistoParser#program.
    def exitProgram(self, ctx:callistoParser.ProgramContext):
        pass


    # Enter a parse tree produced by callistoParser#system.
    def enterSystem(self, ctx:callistoParser.SystemContext):
        pass

    # Exit a parse tree produced by callistoParser#system.
    def exitSystem(self, ctx:callistoParser.SystemContext):
        pass


    # Enter a parse tree produced by callistoParser#planetList.
    def enterPlanetList(self, ctx:callistoParser.PlanetListContext):
        pass

    # Exit a parse tree produced by callistoParser#planetList.
    def exitPlanetList(self, ctx:callistoParser.PlanetListContext):
        pass


    # Enter a parse tree produced by callistoParser#planet.
    def enterPlanet(self, ctx:callistoParser.PlanetContext):
        pass

    # Exit a parse tree produced by callistoParser#planet.
    def exitPlanet(self, ctx:callistoParser.PlanetContext):
        pass


    # Enter a parse tree produced by callistoParser#moonList.
    def enterMoonList(self, ctx:callistoParser.MoonListContext):
        pass

    # Exit a parse tree produced by callistoParser#moonList.
    def exitMoonList(self, ctx:callistoParser.MoonListContext):
        pass


    # Enter a parse tree produced by callistoParser#moon.
    def enterMoon(self, ctx:callistoParser.MoonContext):
        pass

    # Exit a parse tree produced by callistoParser#moon.
    def exitMoon(self, ctx:callistoParser.MoonContext):
        pass


    # Enter a parse tree produced by callistoParser#star.
    def enterStar(self, ctx:callistoParser.StarContext):
        pass

    # Exit a parse tree produced by callistoParser#star.
    def exitStar(self, ctx:callistoParser.StarContext):
        pass


    # Enter a parse tree produced by callistoParser#orbit.
    def enterOrbit(self, ctx:callistoParser.OrbitContext):
        pass

    # Exit a parse tree produced by callistoParser#orbit.
    def exitOrbit(self, ctx:callistoParser.OrbitContext):
        pass



del callistoParser