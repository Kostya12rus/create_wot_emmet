# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/Crypto/Random/OSRNG/__init__.py
__revision__ = '$Id$'
import os
if os.name == 'posix':
    from Crypto.Random.OSRNG.posix import new
elif os.name == 'nt':
    from Crypto.Random.OSRNG.nt import new
elif hasattr(os, 'urandom'):
    from Crypto.Random.OSRNG.fallback import new
else:
    raise ImportError('Not implemented')