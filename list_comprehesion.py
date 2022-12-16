#!/usr/bin/env python3

# -*- encoding:utf-8 -*-

lista_de_valores: list = [1.0, 2.3, 12.5, 15.3, 19.0, 35.0, 192.57, 2.99, 2,8887, 3.5, 79.000, 4.4, 5.59, 6.0102, 8.888, 10.01, 10.0]

valores_gt_10: list = [item for item in lista_de_valores if item > 10.0]

valores_le_10: list = [item for item in lista_de_valores if item <= 10.0]


print("Valores maiores que 10 ", valores_gt_10)
print("Valores menores ou igual a 10 ", valores_le_10)