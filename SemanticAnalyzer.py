from grammar.callistoVisitor import callistoVisitor

class SemanticChecker(callistoVisitor):
    def __init__(self):
        self.errors = []

    def visitPlanet(self, ctx):
        name = ctx.NAME().getText()
        diameter = float(ctx.NUMBER(0).getText())
        mass = float(ctx.NUMBER(1).getText())

        # Checagem semântica: diâmetro e massa devem ser positivos
        if diameter <= 0:
            self.errors.append(f"Erro semântico: Planeta '{name}' tem diâmetro não positivo: {diameter}")
        if mass <= 0:
            self.errors.append(f"Erro semântico: Planeta '{name}' tem massa não positiva: {mass}")

        return self.visitChildren(ctx)

    def visitStar(self, ctx):
        name = ctx.NAME().getText()
        luminosity = float(ctx.NUMBER(0).getText())
        mass = float(ctx.NUMBER(2).getText())

        # Checagem semântica: luminosidade e massa devem ser positivas
        if luminosity <= 0:
            self.errors.append(f"Erro semântico: Estrela '{name}' tem luminosidade não positiva: {luminosity}")
        if mass <= 0:
            self.errors.append(f"Erro semântico: Estrela '{name}' tem massa não positiva: {mass}")

        return self.visitChildren(ctx)

    def hasErrors(self):
        return len(self.errors) > 0

    def getErrors(self):
        return self.errors
