#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

class classe_metodo:

    nome_dev: str = 'Ramon Barbosa'

    def __init__(self):
        self._ano = 2023


    @property
    def ano(self):
        return self._ano


    @classmethod
    def get_var(cls):
        return cls.nome_dev

    
    def another_get_var(self):
        return __class__.nome_dev


if __name__ == '__main__':
    obj = classe_metodo()
    print('get de atributo', obj.ano)
    print('get de variavel classmethod', obj.get_var())
    print('get direto do dunder class', obj.another_get_var())