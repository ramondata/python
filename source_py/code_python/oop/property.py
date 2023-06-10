#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
import sys
sys.path.append('/Users/ramon/codes/source_py/code_python')
from custom_exception.exceptions import ValorInferiorError

class compareNumbers:
    def __init__(self, n1, n2):
        self._int_1 = n1
        self._int_2 = n2


    @property
    def int_1(self):
        return self._int_1
    

    @property
    def int_2(self):
        return self._int_2
    

    def diference(self):
        if self._int_1 > self._int_2:
            print('ok')
        else:
            raise ValorInferiorError('My first exceptions error was working')
        

if(__name__ != '__main__'):
    pass
else:
    a = compareNumbers(2,3)
    print(a.int_1)
    print(a.int_2)
    a.diference()