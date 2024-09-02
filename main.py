import sys
from antlr4 import FileStream, CommonTokenStream
from src.CallistoInterpreter import CallistoInterpreter
from grammar.callistoLexer import callistoLexer
from grammar.callistoParser import callistoParser

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = callistoLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = callistoParser(stream)
    tree = parser.prog()

    interpreter = CallistoInterpreter()
    interpreter.visit(tree)

if __name__ == '__main__':
    main(sys.argv)
