#!/usr/bin/env python3

from abc import ABCMeta
from abc import abstractmethod

class interface(metaclass = ABCMeta):


    @abstractmethod
    def __str__(self) -> None:
        pass


    @abstractmethod
    def __getitem__(self, index) -> None:
        pass


    @abstractmethod
    def __len__(self):
        pass


    @abstractmethod
    def __eq__(self, other):
        pass


    @abstractmethod
    def __ne__(self, other):
        pass
