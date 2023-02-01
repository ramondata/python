#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from functools import reduce
from random import shuffle

#exemplo com string.

nomes = "ramon carol chico".split()

#map com função estruturada
def transform(name):
    return "%s barbosa" % name

transformar = list(map(transform, nomes))
print("transformação com função def ",transformar)

#map com função lambda:

transformar_2 = list(map(lambda x: "%s Barbosa" % x, nomes))
print("transformaçÃo com função lambda", transformar_2)

#exemplo com inteiros e reduce

vendas = [35, 30, 98, 15]

imposto_diario = list(map(lambda x: x * 0.05, vendas))

embaralhar = shuffle(imposto_diario)

total_imposto = reduce(lambda x,y: x + y, imposto_diario)
print("Imposto diário", total_imposto)