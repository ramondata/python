#!/usr/bin/env python3

from source_py.code_python.date.strftime_example import hoje

if __name__ != '__main__':
    pass
else:
    hoje = hoje()
    dia_semana = hoje.dia_da_semana('abreviado')
    dia_mes = hoje.dia_do_mes('com_zero')
    print(dia_semana)
    print(dia_mes)