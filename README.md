<br>
<p align=center>
 <img src=https://github.com/Maracujacake/callisto/blob/planetCatalogation_rs/callistoBanner.jpg alt="Callisto logo with callisto text in the middle :) " width=480 />
</p>

<p align=center>A linguagem para catalogação de corpos celestes</p>

<p align=center>
    <a href=https://elysiajs.com>Documentação</a> | <a href=https://discord.gg/eaFJ2KDJck>Exemplos de uso</a> |  <a href=https://elysiajs.com>História</a>
</p>

# Documentação

A estruturação de callisto é muito parecida com a forma que escrevemos arquivos JSON.
```
System BetaSystem {
    centralStar: Star BetaStar {
        spectralType: K,
        luminosity: 0.3,
        age: 9.7,
        mass: 0.6
    },
    planets: [
        Planet BetaPrime {
            diameter: 4500,
            mass: 0.92, 
            temperature: -15,
            atmosphere: "aluminio, hidrogenio",
            composition: "ferro, niquel, silicio",
            orbit: Orbit {
                semiMajorAxis: 0.7,
                eccentricity: 0.002
            },
            moons: []
            }
    ]
}

```

Visto que é uma linguagem para catalogação de corpos celestes, é necessário que não apenas o corpo em si seja catalogado, como também as características em volta do mesmo.
Veja que todo sistema deve, após a declaração de seu nome, possuir uma estrela central ( consideramos em ordem: Tamanho > Luminosidade > Densidade ), possivelmente mais estrelas,
planetas e as luas destes.

```python
        # verificacao de campos
        required_fields = ['SPECTRAL_TYPE', 'NUMBER', 'NUMBER', 'NUMBER']
        for field in required_fields:
            if not self.hasField(ctx, field):
                self.errors.append(f"Erro semântico: Estrela '{name}' está faltando o campo '{field}'")
```

Veja que conforme o código acima presente no analisador semântico, é necessário  que todos os campos (variam conforme o corpo celeste) 
sejam preenchidos ao menos com um valor, mesmo que, por algum estranho motivo, venham a ser nulos.

Para curiosidade de quais valores são tratados aqui:
### Recorte da gramática

```
system: SYSTEM NAME '{' CENTRALSTAR ':' star ',' PLANETS ':' planetList '}';
planetList: '[' (planet (',' planet)*)? ']';
planet
    : PLANET NAME '{' 'diameter' , 'mass' , 'temperature' , 'atmosphere' , 'composition' ,  'orbit' ':' orbit , 'moons' ':' moonList '}'
    ;

moonList: '[' (moon (',' moon)*)? ']';

moon
    : MOON NAME '{' 'diameter' , 'orbitPeriod' , 'density' , 'surfaceType' '}'
    ;

star
    : STAR NAME '{' 'spectralType' ':' SPECTRAL_TYPE ',' 'luminosity' , 'age' , 'mass' '}'
    ;

orbit
    : ORBIT '{' 'semiMajorAxis' , 'eccentricity' '}'
    ;
```

Para checar qual o tipo de cada característica, o usuário fica convidado a checar a gramática. Não se assuste, são tipos primitivos como números e strings, foram emitidos justamente
por trivialidade. As características que são tipos "diferentes" foram especificadas no recorte acima, por exemplo _'orbit' : orbit_ , 
afinal, orbita não representa uma string ou um número :)


Já que devemos classificar todas as informações de todos os corpos celestes, é provável que por engano nomeemos algum duplicadamente, a linguagem não permitirá e lhe informará quando
isso acontecer

Exemplo de planeta:
```python
        # Validação de nomes únicos
        if name in self.names['planets']:
            self.errors.append(f"Erro semântico: Nome de planeta duplicado '{name}'")
        else:
            self.names['planets'].add(name)
```

Algumas características também como _"Atmosfera"_ e _"Composição"_ não podem aceitar qualquer texto e sim, apenas compostos e elementos químicos previstos na tabela periódica. No entanto
embora seja possível mapear os elementos da tabela (o que, a propósito, é feito na linguagem), compostos químicos são infinitos. Pedimos a contribuição do usuário para adicionar compostos
no arquivo periodicTable.txt seguindo o padrão: CompostoQuímico - no final as strings serão comparadas sem acento e em minúsculo, apenas pedimos para que mantenham-a com as palavras unidas.


```python
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
```

Como dito anteriormente, há muitas semelhanças entre a escrita de callisto e JSON, porém, em JSON você não tem a padronização e controle que o compilador de callisto proporciona,
no entanto, foi pensado que a utilização destes dados podem vir a calhar em serviços web e bancos de dados. Portanto, ao compilar um arquivo corretamente, será gerado um arquivo 
convertendo o original tanto para JSON quanto para SQL.

![Callisto-removebg-preview](https://github.com/user-attachments/assets/cbffcdfe-a472-4ac5-982b-99ade7691c69)


# Exemplos de uso

1 - valores negativos e atmosfera e composição não coerentes.
```
System BetaSystem {
    centralStar: Star BetaStar {
        spectralType: K,
        luminosity: 0.3,
        age: 9.7,
        mass: 0.6
    },
    planets: [
        Planet BetaPrime {
            diameter: -4500,
            mass: -0.92, 
            temperature: -15,
            atmosphere: "Methane, Hydrogen",
            composition: "Iron, Nickel, Silicon",
            orbit: Orbit {
                semiMajorAxis: 0.7,
                eccentricity: 0.002
            },
            moons: []
            }
    ]
}

```
Resultado gerado:

![image](https://github.com/user-attachments/assets/e53c0e6f-7b81-4d65-809f-6c6c03b18f39)


2 - Valores ausentes
```
System GammaSystem {
    centralStar: Star GammaStar {
        spectralType: M,
        luminosity: 0.05,
        age: 10,
        mass: 0.1
    },
    planets: [
        Planet GammaPrime {
            diameter: 3000,
            mass: 0.2,
            atmosphere: "Carbon Dioxide",
            composition: "Iron, Magnesium",
            orbit: Orbit {
                semiMajorAxis: 0.05,
                eccentricity: 0.01
            },
            moons: []
        }
    ]
}

```

Resultado gerado:

![image](https://github.com/user-attachments/assets/a7bc3492-fc4c-4d78-8466-00174f238ccc)


3 - Tudo certo
```
System algum {
    centralStar: Star Sun {
        spectralType: G,
        luminosity: 1.0,
        age: 4.6,
        mass: 1.0
    },
    planets: [
        Planet Earth {
            diameter: 12742,
            mass: 5.97,
            temperature: 288,
            atmosphere: "nitrogenio, oxigenio",
            composition: "ferro, oxigenio, silicio",
            orbit: Orbit {
                semiMajorAxis: 1.0,
                eccentricity: 0.0167
            },
            moons: [
                Moon lua {
                    diameter: 3474,
                    orbitPeriod: 27.3,
                    density: 3.34,
                    surfaceType: "Regolith"
                }
            ]
        },
        Planet Mars {
            diameter: 6779,
            mass: 0.642,
            temperature: 210,
            atmosphere: "carbono",
            composition: "carbono, Silicio",
            orbit: Orbit {
                semiMajorAxis: 1.524,
                eccentricity: 0.0935
            },
            moons: [
                Moon Phobos {
                    diameter: 22.4,
                    orbitPeriod: 0.319,
                    density: 1.876,
                    surfaceType: "Regolith"
                },
                Moon Deimos {
                    diameter: 12.4,
                    orbitPeriod: 1.263,
                    density: 1.471,
                    surfaceType: "Regolith"
                }
            ]
        }
    ]
}
```

Resultado gerado:

![image](https://github.com/user-attachments/assets/2194b134-7458-4ac6-a9d1-63440279ab6a)


# História

A catalogação de planetas e corpos celestes por muito tempo se deu, seja com a digitação padronizada porém manual de pesquisadores, utilizando padrões improvisados utilizando
linguagens de programação ou ainda sem controle algum e salvos em diferentes bancos de dados. Em minhas buscas, não encontrei um compilador ou algum controlador 
que permitisse impor controle sobre essa prática. Com essa ideia em mente, criei esse compilador. O mesmo, por conta do código aberto, pode ser modificado para atender as necessidades
dos mais diversos pesquisadores e impor controle sobre suas anotações e catalogações. 

Sinta-se livre para contribuir com o projeto! :)

_Produzido para a disciplina de Construção de compiladores - UFSCAR 2024/1_

