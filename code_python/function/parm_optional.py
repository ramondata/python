#!/usr/bin/env python3

from typing import Optional

def opt(var1: int, var2: Optional[str] = None) -> any([None, str]):
    if var2 == None:
        var2 = "String vazia"
        print ("[inteiro: %d || string: %s]" %(var1, var2))
    else:
        print ("[inteiro: %d || string: %s]" %(var1, var2))
