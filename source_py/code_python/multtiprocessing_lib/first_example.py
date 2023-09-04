#!/usr/bin/env python3
import time
import multiprocessing

def amostra():
    print('iniciando a funcao')
    for num in range(500_000_00):
        num


if __name__ == "__main__":

    inicio = time.perf_counter()
    c1 = multiprocessing.Process(target=amostra)
    c2 = multiprocessing.Process(target=amostra)

    c1.start()
    c2.start()

    c1.join()
    c2.join()

    fim = time.perf_counter()
    total = round(fim - inicio,2)
    print("time execution", total)