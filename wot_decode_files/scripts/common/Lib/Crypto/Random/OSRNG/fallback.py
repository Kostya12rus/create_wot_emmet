# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/Crypto/Random/OSRNG/fallback.py
__revision__ = '$Id$'
__all__ = ['PythonOSURandomRNG']
import os
from rng_base import BaseRNG

class PythonOSURandomRNG(BaseRNG):
    name = '<os.urandom>'

    def __init__(self):
        self._read = os.urandom
        BaseRNG.__init__(self)

    def _close(self):
        self._read = None
        return


def new(*args, **kwargs):
    return PythonOSURandomRNG(*args, **kwargs)