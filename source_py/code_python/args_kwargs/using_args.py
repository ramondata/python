#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

class notebooks:

    def __init__(self, *args):
        self._marca = args[0]
        self._modelo = args[1]
        self._cor = args[2]
        self._tela = args[3]
        self._ano = args[4]


    def __str__(self):
        return str(self._marca)

if __name__ != '__main__':
    pass
else:
    laptop = notebooks('apple', 'pro m1', 'prata space', '13', '2021')
    print(laptop)
    print(laptop._modelo, laptop._ano)