#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

class use_raise:

    def __init__(self):
        self.data = 6

    def condition_data(self):
        if self.data != 1:
            print(self.data)
            raise Exception('wrong data')

if __name__ == '__main__':
    obj = use_raise()
    obj.condition_data()