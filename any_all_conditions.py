#!/usr/bin/env python3

from abc import ABCMeta
from abc import abstractmethod

class interface(metaclass = ABCMeta):


    def __str__(self):
        pass


class anyAll(interface):


    def __init__(self):
        self._count = 35
        self._name = "duck"


    def __str__(self):
        return "[name : %d | count : %s]" %(self._count, self._name)


    def verify_any(self):
        if any([self._name == "duck", self._count == 40]):
            print("pelo menos uma das opções foi contemplada")
        else:
            print(1)


    def verify_all(self):
        if all([self._name == "duck", self._count == 35]):
            print("todas as condições sendo contempladas")
