#!/usr/bin/env python3

class filter_data:


    def __init__(self, *args):
        self._nomes: tuple = ('supernatural','riverdale','serie1','serie2','serie3')
        self._selecionadas: list = args
        self._f: filter = None


    func_filter: filter = lambda x: x if x == 'riverdale' else False


    def filtro(self):
        self._f = filter(__class__.func_filter, self._nomes)
        return print(tuple(self._f))


    def colheita(self):
        yield self._nomes
        yield self._selecionadas
        yield tuple(self._f)


if __name__ != '__main__':
    pass
else:
    obj1 = filter_data(1,2,3,4,5,'ramon','palavras','riverdale','carol','chico')
    obj1.filtro()
    data = obj1.colheita()
    print(next(data))
    print(next(data))
    print(next(data))
