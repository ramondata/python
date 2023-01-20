
########## Aula 1: Curiosidades da linguagem Python

import this

numero = 123_456_789
print(numero)

var_1: int = 1
_id_1 = id(var_1)
var_2: int = 1
_id_2 = id(var_2)
_is = _id_1 is _id_2
_in = _id_1 in [_id_2]
print(_is)
print(_in)

recebe_varias_entradas = 1,2,3
a, b, c = recebe_varias_entradas

########## Aula 2: Tipos e estruturas de Dados

#principais tipos de dados
inteiro: int = 10
ponto_flutuante: float = 3.11
string: str = "hello guys"
string_como_unidade: str = "beleza", #tuple, veremos nas aulas de estruturas de dados
caracter: chr = "a"

#Estruturas de dados

#strings


#Formas de criar uma lista:
nomes_1: list = ["ramon", "carol", "chico"] #tipo 1
nomes_2: list = "ramon|carol|chico".split("|") #tipo 2
sobrenomes = ("barbosa", "freitas")
sobre_nomes_3: list = list(sobrenomes) #tipo 3
nomes_4: list = [item for item in sobrenomes if item == "barbosa"] #list comprehensions #tipo 4
nomes_5: list = list(map(lambda x: x, ("chico dogao", "chico bonitao", "chico sapecao"))) #tipo 5

#tuplas
vendas: tuple = (123_321, 891_451, 111_569, 123_893_830) #tipo 1
_uma_venda: tuple = (789_435_972,) #tipo 2 
preco_televisores: tuple = tuple("3_500*2_900*4_699".split("*")) #tipo 3
value_tvs: tuple = tuple(preco_televisores) #tipo 4
blend_dados: tuple = 126, "vendas", 345.991, "e" #tuple packing #tipo 5
numeracao, status_produto, valor_geral = blend_dados #sequence unpacking

#Dictionaies - dict:
altura_1: dict = {"jogador1": 
                {
                    "nome": "Pedro queixo rubro",
                    "altura": 1.89
                },
                
                "jogador2":
                {
                    "nome": "Gabigol",
                    "altura": 1.73
                }
                } #tipo 1
_alt_1 = 1.99
_alt_2 = 1.65
altura_2: dict = dict(
                      altura1 = "%3.2f" % _alt_1,
                      altura2 = "%3.2f" % _alt_2
                    ) #tipo 2
altura_3: dict = dict({
                      ("alt1", 1.92),
                      ("alt2", 1.73)
                    }) # tipo 3
estados = "RJ SP MG RS PR".split()
pais = ["BR"]
info_Estados = dict.fromkeys(estados, pais) #tipo 4
nomes_dict: dict = {"nome_%s" % name: name for name in ("ronaldo", "neymar", "pombo")} #dict comprehensions #tipo 5

#set:
kilometragem = "13_000 100_345 13_000 991_001 328_056 100_345 22_090".split()
km_unicas_1: set = {13_000, 100_345, 13_000, 991_001, 328_056, 100_345, 22_090} #tipo 1
km_unicas_2: set = set(kilometragem) #tipo 2
km_unicas_3: set = {km for km in kilometragem if km > 13_000} #set comprehensions #tipo 3


########## Aula 3: Convertendo tipos de dados

numero_inteiro: int = 144
numero_inteiro_convertido_para_texto: str = str(numero_inteiro)

numero_float: float = 987.03
numero_float_convertido_para_inteiro: int = int(numero_float)

numero_como_texto: str = "098"
numero_texto_convertido_para_inteiro: int = int(numero_como_texto)

letra: str = "y"
letra_convertida_para_caracter: chr = chr(letra)

condicao: bool = "python" == "Python"
condicao_convertido_para_texto: str = str(condicao)

nulo: None = None
nulo_convertido_para_booleano: bool = bool(nulo)


########## Aula 4: Manipulando estruturas no Python com as principais funções

#https://docs.python.org/3/tutorial/datastructures.html

#listas:
nomes: list = "ramon|carol|chico".split("|")
#acessando lista pelo index:
nomes[0] #index 0
nomes[1:2] #slice na lista
#adicionar dados:
nomes.append("estela")
nomes.insert(2, "lindon")
#apagar dados:
nomes.pop(1) #Apaga o ultimo index
nomes.remove("ramon")
#contagem de itens:
len(nomes) # total de dados
nomes.count("estela")
#união de listas:
produtos: list = "tv notebook echo-dot headphone".split()
outros_produtos: list = "cadeira|mesa|monitor|teclado".split("|")
valores: list = "2_989 12_000 500 300 2_000 3_000 2_000 500".split()
produtos.extend(outros_produtos)
produto_e_valores: list = list(zip(produtos, valores))

#Dict:
numeros: dict = {"num_%s" % num: num for num in ("1", "2", "3")}
#Acessando os dados do dicinário:
numeros['num_1']
numeros.keys() # todas as chaves
numeros.values() #todos os valores
numeros.items() #Todos os pares chave:valor

#Set:
marcas_1: set = {"amazon", "tesla", "apple", "microsoft", "apple", "samsung"}
marcas_2: set = {"amazon", "xiaomi", "dell", "microsoft", "apple"}
#acrescentando dados:
marcas_1.add("flamengo")
#copiando dados:
marcas_1_copy = marcas_1.copy()
#limpando um set inteiro
marcas_1.clear()
#diferença entre sets em novo set:
diferenca: set = marcas_1_copy.difference(marcas_2)
#diferença entre sets no set da esquerda ou principal:
marcas_1_copy.difference_update(marcas_2)
#apagando dados especificos:
marcas_2.discard("xiaomi")
#interseção entre sets:
set_1: set = {155, 235, 689, 987, 987, 155}
set_2: set = {209, 498, 138, 2305, 689, 155, 235}
intersecao: set = set_1.intersection(set_2)
#interseção entre sets no set da esquerda ou principal:
set_1.intersection_update(set_2)


#Aula de slice -> não esquecer
#del slice