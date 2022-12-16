#!/usr/bin/env python3

from functools import total_ordering

@total_ordering
class comparison:


    def __init__(self, data: int) -> None:
        self.data: int = data


    def __eq__(self, other: None) -> any([bool, None]):
        if type(other.data) == comparison:
            return self.data == other.data
        else:
            return False


    def __lt__(self, other: None) -> any([bool, None]):
        if self.data != other.data:
            return self.data < other.data
        else:
            return False


    def __str__(self):
        return "class to practice functools with total_ordering function"
