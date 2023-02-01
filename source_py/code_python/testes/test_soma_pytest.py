#!/usr/bin/env python3

def func(x):
    return x + 1

def test_answer1():
    assert func(3) == 20, "pass"

def test_answer2():
    assert func(5) == 89, "pass"

def test_answer3():
    assert func(10) == 120, "pass"
    assert func(3) == 0, "pass"


def func2(x,y):
    return x + y


def testando1():
    assert func2(12,1) == 15, "pass"
