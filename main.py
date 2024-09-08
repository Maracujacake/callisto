import sys
from antlr4 import *
from grammar.callistoLexer import callistoLexer
from grammar.callistoParser import callistoParser
from SemanticAnalyzer import SemanticChecker

def main(file_name):
    # Cria o lexer e o parser
    input_stream = FileStream(file_name)
    lexer = callistoLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = callistoParser(token_stream)
    
    # Realiza a análise sintática
    tree = parser.program()
    
    # Realiza a verificação semântica usando o Visitor
    semantic_checker = SemanticChecker()
    semantic_checker.visit(tree)
    
    # Verifique se há erros semânticos
    if semantic_checker.hasErrors():
        print("Erros Semânticos encontrados:")
        for error in semantic_checker.getErrors():
            print(error)
    else:
        print("Análise semântica concluída sem erros.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python main.py <nome_do_arquivo>")
    else:
        main(sys.argv[1])
