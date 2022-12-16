#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

from abc import abstractmethod
from abc import ABCMeta

class guia_metodos(metaclass=ABCMeta):

    @abstractmethod
    def __repr__():
        pass

    @abstractmethod
    def __version__():
        pass

    @abstractmethod
    def __getitem__():
        pass
