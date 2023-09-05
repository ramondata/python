#!/usr/bin/env python3

n = 10

#comportamento like lazy iterator
def sum(var: int):
    global n
    out: int = var + n
    yield out, type(out) # primeiro retorno: tipo integer
    out_1: str = str(out)
    yield out_1, type(out_1)  # segundo retorno: tipo string
    out_2: float = float(out)
    yield out_2, type(out_2) # terceiro retorno: tipo float

data = sum(90) # instanciada apenas uma vez e iterada n vezes para colher todos os retornos

# iterando a função.
#p.s. lembra de instanciar a função uma vez e salvá-la na memória pra colher os returns
#e não instanciar varias vezes a mesma função pra colher os returns, apenas uma vez, lembrar disso.
print(next(data))
print(next(data))
print(next(data))