#!/usr/bin/en python3
# -*- encoding: utf-8 -*-

import xlsxwriter
import os

class cria_planilha_nova:


    def __init__(self):
        self._path_nome_planilha = "/Users/ramon/codes/data/membros_da_familia.xlsx"
        self._workbook = xlsxwriter.Workbook(self._path_nome_planilha)
        self._worksheet = None


    def create_new_wb(self):
        self._worksheet = self._workbook.add_worksheet()


    def write_cells(self, coluna: str, linha: str, valor: str):
        self._worksheet.write("%s%s" %(coluna.upper(), linha), valor)
        print('Informação %s inserida na célula %s%s ' %(valor, coluna.upper(), linha))

    def finish(self):
        self._workbook.close()


if(__name__ != "__main__"):
    pass
else:
    obj1 = cria_planilha_nova();
    obj1.create_new_wb();
    obj1.write_cells('a', '1', 'Membros da familia');
    obj1.write_cells('a', '2', 'Carol Izidro');
    obj1.write_cells('a', '3', 'Chico Bento');
    obj1.write_cells('a', '4', 'Ramon Barbosa');
    obj1.finish();
    print("Planilha pronta no path %s" %(os.getcwd()));

