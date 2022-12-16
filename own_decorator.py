#!/usr/bin/env python3

def insert_item(func):
    def inside(lister, value):
        return lister.insert(0,int(value))
    return inside


@insert_item
def data(lister, value):
    return lister, value


my_list = [25, 56, 67, 12]

data(my_list, 67)

print(my_list)

