#!/usr/bin/env python3

#aplicando a função next e iter

nomes = "ramon carol chico maria bento".split()
contagem = len(nomes)
#--------------------------
i = 0
nomes_iter = iter(nomes)

while i <= contagem -1:
    print(next(nomes_iter, "%s" % nomes_iter), i)
    i+=1
#-------------------------
rascunho = """
nomes_aiter = aiter(nomes)

print(nomes_aiter)
"""