########## Aula 2: Tipos e estruturas de Dados

#principais tipos de dados
inteiro: int = 10
ponto_flutuante: float = 3.11
string: str = "hello guys"
string_como_unidade: str = "beleza", #tuple, veremos nas aulas de estruturas de dados
caracter: chr = "a"

# TODO criar conteudo de estrutura de dados
#Estruturas de dados

# TODO criar conteudo de manipulação de strings
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