#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

class operation:


    def __init__(self, n: int):
        self._n = n


    def __eq__(self, other):
        return self._n == other


    def __ne__(self, other):
        return self._n != other


    def __gt__(self, other):
        return self._n > other


    def __lt__(self, other):
        return self._n < other


    def __ge__(self, other):
        return self._n >= other


    def __le__(self, other):
        return self._n <= other

