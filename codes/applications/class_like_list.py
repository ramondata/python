#!/usr/bin/env python3

class myList:


    def __init__(self, itens):
        self.itens: list = itens


    #def __str__(self):
        #return "classe dedicada a duck typing comportamento de list"


    def __getitem__(self, index: int):
        return self.itens[index]


    def __len__(self):
        return len(self.itens)
