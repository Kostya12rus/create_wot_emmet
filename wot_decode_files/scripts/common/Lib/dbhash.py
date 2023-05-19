# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/dbhash.py
import sys, warnings
warnings.warnpy3k('in 3.x, the dbhash module has been removed', stacklevel=2)
try:
    import bsddb
except ImportError:
    del sys.modules[__name__]
    raise

__all__ = ['error', 'open']
error = bsddb.error

def open(file, flag='r', mode=438):
    return bsddb.hashopen(file, flag, mode)