# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/Crypto/Random/OSRNG/nt.py
__revision__ = '$Id$'
__all__ = ['WindowsRNG']
import _winrandom as winrandom
from rng_base import BaseRNG

class WindowsRNG(BaseRNG):
    name = '<CryptGenRandom>'

    def __init__(self):
        self.__winrand = winrandom.new()
        BaseRNG.__init__(self)

    def flush(self):
        if self.closed:
            raise ValueError('I/O operation on closed file')
        data = self.__winrand.get_bytes(131072)
        BaseRNG.flush(self)

    def _close(self):
        self.__winrand = None
        return

    def _read(self, N):
        self.flush()
        data = self.__winrand.get_bytes(N)
        self.flush()
        return data


def new(*args, **kwargs):
    return WindowsRNG(*args, **kwargs)