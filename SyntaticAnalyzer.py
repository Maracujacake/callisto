import sys
from antlr4 import *
from grammar.callistoLexer import callistoLexer
from grammar.callistoParser import callistoParser
from antlr4.error.ErrorListener import ErrorListener

# Classe para capturar erros de sintaxe
class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super(SyntaxErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Syntax error at line {line}, column {column}: {msg}")

    def hasErrors(self):
        return len(self.errors) > 0

    def getErrors(self):
        return self.errors

def parse_file(file_name):
    # Abra o arquivo de entrada
    input_stream = FileStream(file_name)
    
    # Crie um lexer para o input stream
    lexer = callistoLexer(input_stream)
    
    # Gere tokens
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    
    # Crie um parser para os tokens
    parser = callistoParser(token_stream)
    
    # Adicione o listener de erro personalizado
    error_listener = SyntaxErrorListener()
    parser.removeErrorListeners()  # Remove os ouvintes de erro padrão
    parser.addErrorListener(error_listener)
    
    # Inicie a análise sintática (parse)
    tree = parser.program()  # 'program' é a regra inicial na gramática
    
    # Verifique se há erros de sintaxe
    if error_listener.hasErrors():
        print("Erros de Sintaxe encontrados:")
        for error in error_listener.getErrors():
            print(error)
    else:
        print("Análise sintática concluída sem erros.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python ParserAnalyzer.py <nome_do_arquivo>")
    else:
        parse_file(sys.argv[1])