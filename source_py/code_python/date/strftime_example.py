#!/usr/bin/env python3

from datetime import datetime as dt

class hoje:


    def __init__(self):
        self._data = dt.today()


    def dia_da_semana(self, formato):
        if formato == 'abreviado':
            return self._data.strftime('%a')
        elif formato == 'extenso':
            return self._data.strftime('%A')
        elif formato == 'numeral':
            return self._data.strftime('%w')


    def dia_do_mes(self, formato):
        if formato == 'com_zero':
            return self._data.strftime('%d')
        elif formato == 'zem zero':
            return self._data.strftime('%-d')