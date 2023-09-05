#!/usr/bin/env python3

from abc import ABCMeta
from abc import abstractmethod

class myabstract(metaclass = ABCMeta):

    @abstractmethod
    def __str__(self):
        pass
