#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

class list_comp:


    def __init__(self, *values):
        self._values_array: list = values


    def __getitem__(self, index):
        return self._values_array[index]


    def __len__(self):
        return len(self._values_array)
        
        
    def gt_10(self):
        _gt_10: list = [item for item in self._values_array if item > 10.0]
        return _gt_10


    def le_10(self):
        _le_10: list = [item for item in self._values_array if item <= 10.0]
        return _le_10


if __name__ == '__main__':
    obj: list_comp = list_comp(1.0, 2.3, 12.5, 15.3, 19.0, 10.0, 35.0, 192.57, 2.99, 2,8887, 3.5, 79.000, 4.4)
    a = obj.gt_10()
    b = obj.le_10()
    print("Valores maiores que 10 ", a)
    print("Valores menores ou igual a 10 ", b)