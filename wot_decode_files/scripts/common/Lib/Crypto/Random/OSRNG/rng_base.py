# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/Crypto/Random/OSRNG/rng_base.py
__revision__ = '$Id$'
import sys
if sys.version_info[0] == 2 and sys.version_info[1] == 1:
    from .Crypto.Util.py21compat import *

class BaseRNG(object):

    def __init__(self):
        self.closed = False
        self._selftest()

    def __del__(self):
        self.close()

    def _selftest(self):
        data = self.read(16)
        if len(data) != 16:
            raise AssertionError('read truncated')
        data2 = self.read(16)
        if data == data2:
            raise AssertionError('OS RNG returned duplicate data')

    def __enter__(self):
        pass

    def __exit__(self):
        self.close()

    def close(self):
        if not self.closed:
            self._close()
        self.closed = True

    def flush(self):
        pass

    def read(self, N=-1):
        if self.closed:
            raise ValueError('I/O operation on closed file')
        if not isinstance(N, (long, int)):
            raise TypeError('an integer is required')
        if N < 0:
            raise ValueError('cannot read to end of infinite stream')
        elif N == 0:
            return ''
        data = self._read(N)
        if len(data) != N:
            raise AssertionError('%s produced truncated output (requested %d, got %d)' % (self.name, N, len(data)))
        return data

    def _close(self):
        raise NotImplementedError('child class must implement this')

    def _read(self, N):
        raise NotImplementedError('child class must implement this')