#!/usr/bin/env python3

from use_interface import usaInterface

class subInter(usaInterface):


    def __init__(self):
        self._data = "subclass_test"


    @property
    def data(self):
        return self._data


