import sys
from antlr4 import *
from grammar.callistoLexer import callistoLexer

def generate_tokens(file_name):
    # Abra o arquivo de entrada
    input_stream = FileStream(file_name)
    
    # Crie um lexer para o input stream
    lexer = callistoLexer(input_stream)
    
    # Gere tokens
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    
    # Imprima todos os tokens
    for token in token_stream.tokens:
        token_type = token.type
        if token_type >= 0 and token_type < len(lexer.symbolicNames):
            token_name = lexer.literalNames[token_type]
        elif token_type >= 0 and token_type < len(lexer.ruleNames):
            token_name = lexer.ruleNames[token_type-1]
        else:
            token_name = "UNKNOWN"
        print(f"Token Type: {token_name}, Token Text: '{token.text}'")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python TokenGenerator.py <nome_do_arquivo>")
    else:
        generate_tokens(sys.argv[1])