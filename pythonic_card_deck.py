
import collections


Card = collections.namedtuple('Card', ['rank', 'suit']) #Uma classe simplificada que contem uma tupla nomeada para utilizar em outras classes 

#Essa classe cria uma lista de cartões com dados de numero e nipe das cartas de baralho 
class FrenchDeck:

    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A'] #feito na mão, like hands on
    ranks_pythonic = [str(item) for item in range(2,11)] + list('JQKA') # modo pythonico de fazer essa lista de cartas

    suits = ['spades','diamonds','clubs','hearts'] #Lista de nipes feitos a mão
    suits_pythonic = 'spades diamonds clubs hearts'.split() #list of nipes created by pythonic method
    
    #método construtor FrenchDeck()
    def __init__(self):
        self._cards_pythonic = [Card(rank, suit) for suit in self.suits_pythonic for rank in self.ranks_pythonic] #ranks e suits na tupla cards
    
    # Permite contagem de itens, Duck typing no objeto
    def __len__(self):
        return len(self._cards_pythonic)

    #Duck typing iteravel de lista, objeto se comporta como uma lista mas não é uma lista
    def __getitem__(self, index):
        return self._cards_pythonic[index]

#Função principal, instância construida com o método construtor
if __name__ == "__main__":
    sessao = FrenchDeck()
    #iterando a lista de cartas para poder visualizar cada item do deck/baralho
    for carta in range(len(sessao)):
        print(sessao[carta])