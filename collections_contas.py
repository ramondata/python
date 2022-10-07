#!/usr/bin/env python3

from abc import abstractmethod

class contas:


    def __init__(self, code):
        self._code = code
        self._saldo = 0
        self._nome = None


    def __str__(self):
        return "[codigo:%s - saldo:%s]" %(self._code,self._saldo)


    def deposita(self, valor):
        self._saldo += valor
        return self.saldo

    
    @abstractmethod
    def taxa_mensal(self):
        pass


    @staticmethod
    def banco_nome():
        return "pybank"

    
    @property
    def nome(self):
        return self._nome


    @nome.setter
    def nome(self, name):
        self._nome = name


    @property
    def code(self):
        return self._code


    @property
    def saldo(self):
        return self._saldo


class contaCorrente(contas):


    def __init__(self, code):
        super().__init__(code)


    def taxa_mensal(self):
        self._saldo -= 2


class contaPoupanca(contas):


    def __init__(self, code):
        super().__init__(code)


    def taxa_mensal(self):
        self._saldo += 1.01
        self._saldo -= 3
