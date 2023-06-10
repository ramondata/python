#!usr/bin/env python3
# -*- encoding: utf-8 -*-

from source_py.code_python.dogao import Dog

class tdd_treinando:

    def tdd_my_first_tdd_test_pytest(self):
        #given
        entrada = "chico"
        esperado = "CHICO"
        #when
        cao = Dog(entrada)
        resultado = cao.name_upper()
        #then
        assert resultado == esperado