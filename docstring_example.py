
class Animais:
    '''
    Esta função faz referencia aos animais que porventura iremos representar
    com esta classe: Animais
    '''
    def __init__(self):
        '''
        Método construtor onde devemos elaborar a criação dos atributos que utilizaremos
        nesta classe para representar bem os animais aqui referenciados
        '''
        self._especie: str
        self._nome: str
        self._idade: int
        self._habitat: str


    @property
    def nome(self):
        '''
        Método que obtem os dados sobre nome dos animais de forma segura
        dentro da classe protected
        '''
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        '''
        Método que permite de forma segura, o ajuste ou troca do nome
        do animal instânciado por esta classe
        '''
        self._nome = novo_nome