#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

class camisas:


    def __init__(self, marca, modelo, tamanho, cor):
        if all([type(marca)==str, type(modelo)==str, type(tamanho)==str, type(cor)==str]):
            self._marca = marca
            self._modelo = modelo
            self._tamanho = tamanho
            self._cor = cor
            self._quantidade = None
        else:
            raise Exception('dados inseridos precisam ser do tipo string')


    def selecao(self) -> bool:
        if self._marca == 'adidas' and self._cor == 'cinza'\
        or self._cor == 'azul' and self._cor == 'bege'\
        and self._cor == 'vinho':
            return True
        else:
            return False