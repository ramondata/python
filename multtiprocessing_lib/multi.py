#!/usr/bin/env python3

import concurrent.futures
import time

def amostra(numero):
    print('iniciando a funcao')
    for num in range(numero):
        num
    return 'pool finalizado %s' % numero

if __name__ == '__main__':

    inicio = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        nums = [50_000_000, 30_000_000, 1_000_000]
        cods = executor.map(amostra, nums)

        for cod in cods:
            print(cod)

    fim = time.perf_counter()
    total = round(fim - inicio,2)
    print("time execution", total)