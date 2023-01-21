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
