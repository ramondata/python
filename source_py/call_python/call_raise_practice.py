#!/usr/bin/env python3
#! -*- encoding: utf-8 -*-

from source_py.code_python.function.raise_practice import camisas

if __name__ != '__main__':
    pass
else:
    obj1 = camisas('adidas','basic classic','G','cinza')
    print(obj1._marca)
    print(obj1.selecao())

    obj2 = camisas('nike', '1', '3', 'azul')
    print(obj2._marca)
    print(obj2.selecao())

    obj3 = camisas('adidas', 'minimal basic', 'M', 'preta')
    print(obj3._marca)
    print(obj3.selecao())
