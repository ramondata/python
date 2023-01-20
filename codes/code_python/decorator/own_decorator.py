#!/usr/bin/env python3

def validador(func):
    def inside(var):
        return var + 1
    return inside

@validador
def data(var):
    return var

print(data(9))