#!/usr/bin/env python3

class ValorInferiorError(Exception):
    def __init__(self, msg):
        self._msg = msg
        return self._msg