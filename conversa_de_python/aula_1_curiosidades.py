# Aula 1: Curiosidades da linguagem Python

import this

numero = 123_456_789
print(numero)

var_1: int = 1
_id_1 = id(var_1)
var_2: int = 1
_id_2 = id(var_2)
_is = _id_1 is _id_2
_in = _id_1 in [_id_2]
print(_is)
print(_in)

recebe_varias_entradas = 1,2,3
a, b, c = recebe_varias_entradas