#!/usr/bin/env python3


def insert(func):
    global lister
    def into(v):
        return lister.append(v)
    return into


@insert
def app_dt(v):
    return v


lister = [33,44,55,77,88]

a = map(app_dt, [66])

list(a)
