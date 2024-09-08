import json
import os
import sys
from antlr4 import FileStream, CommonTokenStream
from grammar.callistoLexer import callistoLexer
from grammar.callistoParser import callistoParser
from grammar.callistoVisitor import callistoVisitor
from unidecode import unidecode

from sql_generator import generate_sql_output

class SemanticChecker(callistoVisitor):
    def __init__(self):
        self.errors = []
        self.names = {
            'planets': set(),
            'stars': set(),
            'moons': set()
        }
        self.details = {
            'planets': [],
            'stars': [],
            'moons': []
        }
        self.elements = self.load_elements("periodicTable.txt")

    def hasField(self, ctx, field_name):
        return hasattr(ctx, field_name) is not None and getattr(ctx, field_name) is not None

    # Carrega e ajusta os nomes dos elementos químicos (tabela periodica)
    def normalize_string(self, s):
        return unidecode(s).strip().lower()
    def load_elements(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            return set(self.normalize_string(line) for line in file)

    # Checa se é um elemento compatível
    def validate_string_list(self, string, context):
        for word in string.split(','):
            element = self.normalize_string(word)
            if element and element not in self.elements:
                self.errors.append(f"Erro semântico: '{element}' não é um elemento válido na {context}.")

    def visitPlanet(self, ctx):
        name = ctx.NAME().getText()
        diameter = float(ctx.NUMBER(0).getText())
        mass = float(ctx.NUMBER(1).getText())
        temperature = float(ctx.NUMBER(2).getText())
        orbit_ctx = ctx.orbit()
        moons_ctx = ctx.moonList()
        atmosphere = self.normalize_string(ctx.STRING(0).getText().strip('"'))
        composition = self.normalize_string(ctx.STRING(1).getText().strip('"'))

         # verificacao de campos
        required_fields = ['NUMBER', 'NUMBER', 'NUMBER', 'STRING', 'STRING', 'orbit', 'moonList']
        for field in required_fields:
            if not self.hasField(ctx, field):
                self.errors.append(f"Erro semântico: Planeta '{name}' está faltando o campo '{field}'")


        # Validação de nomes únicos
        if name in self.names['planets']:
            self.errors.append(f"Erro semântico: Nome de planeta duplicado '{name}'")
        else:
            self.names['planets'].add(name)

        
        # Diâmetro e massa devem ser positivos
        if diameter <= 0:
            self.errors.append(f"Erro semântico: Planeta '{name}' tem diâmetro não positivo: {diameter}")
        if mass <= 0:
            self.errors.append(f"Erro semântico: Planeta '{name}' tem massa não positiva: {mass}")
        if temperature < -273.15:  # Temperatura não pode ser menor que o zero absoluto
            self.errors.append(f"Erro semântico: Planeta '{name}' tem temperatura não válida: {temperature}")

        # Deve possuir uma orbita e uma lua
        if not orbit_ctx:
            self.errors.append(f"Erro semântico: Planeta '{ctx.NAME().getText()}' não tem um orbit definido")

        # Validação de atmosfera e composição
        self.validate_string_list(atmosphere, "atmosfera")
        self.validate_string_list(composition, "composição")

        self.details['planets'].append({
                'name': name,
                'diameter': diameter,
                'mass': mass,
                'temperature': temperature,
                'atmosphere': atmosphere,
                'composition': composition,
                'orbit': self.visitOrbit(orbit_ctx),
        })

        return self.visitChildren(ctx)




    def visitStar(self, ctx):
        name = ctx.NAME().getText()
        luminosity = float(ctx.NUMBER(0).getText())
        age = float(ctx.NUMBER(1).getText())
        mass = float(ctx.NUMBER(2).getText())
        tipoEspectral = ctx.SPECTRAL_TYPE().getText()

        # verificacao de campos
        required_fields = ['SPECTRAL_TYPE', 'NUMBER', 'NUMBER', 'NUMBER']
        for field in required_fields:
            if not self.hasField(ctx, field):
                self.errors.append(f"Erro semântico: Estrela '{name}' está faltando o campo '{field}'")

        # Validação de nomes únicos
        if name in self.names['stars']:
            self.errors.append(f"Erro semântico: Nome de estrela duplicado '{name}'")
        else:
            self.names['stars'].add(name)

        # Checagem semântica: luminosidade e massa devem ser positivas
        if luminosity <= 0:
            self.errors.append(f"Erro semântico: Estrela '{name}' tem luminosidade não positiva: {luminosity}")
        if mass <= 0:
            self.errors.append(f"Erro semântico: Estrela '{name}' tem massa não positiva: {mass}")
        if age <= 0:
            self.errors.append(f"Erro semântico: Estrela '{name}' tem idade não válida: {age}")

        self.details['stars'].append({
                'name': name,
                'luminosity': luminosity,
                'age': age,
                'mass': mass,
                'spectral_type': tipoEspectral
        })

        return self.visitChildren(ctx)
    



    def visitMoon(self, ctx):
        name = ctx.NAME().getText()
        diameter = float(ctx.NUMBER(0).getText())
        orbitalPeriod = float(ctx.NUMBER(1).getText())
        density = float(ctx.NUMBER(2).getText())

        if diameter <= 0: # Não encontrei diametro mínimo para ser considerado lua
            self.errors.append(f"Erro semântico: Lua '{name}' tem diametro inconsistente: {diameter}")
        if orbitalPeriod <= 0:
            self.errors.append(f"Erro semântico: Lua '{name}' tem periodo orbital inconsistente: {orbitalPeriod}")
        if density <= 0:
            self.errors.append(f"Erro semântico: Lua '{name}' tem densidade não válida, eh um buraco negro por acaso?: {density}")

        # Validação de nomes únicos
        if name in self.names['moons']:
            self.errors.append(f"Erro semântico: Nome de lua duplicado '{name}'")
        else:
            self.names['moons'].add(name)

        # verificacao de campos
        required_fields = ['NUMBER', 'NUMBER', 'NUMBER', 'STRING']
        for field in required_fields:
            if not self.hasField(ctx, field):
                self.errors.append(f"Erro semântico: Lua '{name}' está faltando o campo '{field}'")

        self.details['moons'].append({
                'name': name,
                'diameter': diameter,
                'orbital_period': orbitalPeriod,
                'density': density
        })

        return self.visitChildren(ctx)
    

    def visitOrbit(self, ctx):
        semiMajorAxis = float(ctx.NUMBER(0).getText())
        eccentricity = float(ctx.NUMBER(1).getText())

        # Checagem de consistência: semiMajorAxis e eccentricity devem ser positivos e dentro de limites razoáveis
        if semiMajorAxis <= 0: # distancia do centro ao canto mais distante da elipse
            self.errors.append(f"Erro semântico: semiMajorAxis não positivo: {semiMajorAxis}")
        if eccentricity < 0 or eccentricity >= 1: # varia de 0 a 1
            self.errors.append(f"Erro semântico: eccentricity fora do intervalo [0,1): {eccentricity}")


        required_fields = ['NUMBER', 'NUMBER']
        for field in required_fields:
            if not self.hasField(ctx, field):
                self.errors.append(f"Erro semântico: Orbita está com campos faltando '{field}'")

        return self.visitChildren(ctx)



    def hasErrors(self):
        return len(self.errors) > 0

    def getErrors(self):
        return self.errors
    
    def generate_json_output(self, output_filename):
        systems = {
            "planets": self.details['planets'],
            "stars": self.details['stars'],
            "moons": self.details['moons']
        }
        with open(output_filename, 'w', encoding='utf-8') as json_file:
            json.dump(systems, json_file, ensure_ascii=False, indent=4)

    def checkFile(self, file_name):
        # Leia o arquivo de entrada
        input_stream = FileStream(file_name)
        
        # Crie um lexer e um parser
        lexer = callistoLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = callistoParser(token_stream)
        
        # Gere a árvore sintática a partir do nó raiz (ajuste o método conforme sua gramática)
        tree = parser.system()
        
        # Visite a árvore com o analisador semântico
        self.visit(tree)

        # Se houver erros, mostre-os
        if self.hasErrors():
            print("\n".join(self.getErrors()))
        else:
            print("Sem erros semânticos.")
            output_json = f"{file_name}_output.json"
            self.generate_json_output(output_json)
            print(f"Arquivo JSON '{output_json}' gerado com sucesso.")

            output_sql = f"{os.path.splitext(file_name)[0]}_output.sql"
            generate_sql_output(output_sql, self.details)  # Chama a função importada
            print(f"Arquivo SQL '{output_sql}' gerado com sucesso.")

# Exemplo de uso:
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python semanticAnalyzer.py <nome_do_arquivo>")
    else:
        semantic_checker = SemanticChecker()
        semantic_checker.checkFile(sys.argv[1])