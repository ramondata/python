#!/usr/bin/env python3

from default_interface import interface

class usaInterface(interface):

    name: str = "Dago"


    def __init__(self, data):
        self._data = data


    def __str__(self):
        return "dado cheio de classe"


    def __len__(self) -> len:
        return self._data.__len__()


    def __getitem__(self, index: int) -> None:
        return self._data[index]


    def __eq__(self, other: None) -> bool:
        return self._data == other


    def __ne__(self, other: None) -> bool:
        return self._data != other


    @classmethod
    def name_dev(cls=name):
        from sys import ps1
        ps1 = __class__.cls
        return "ps1 do app : %s" % ps1

