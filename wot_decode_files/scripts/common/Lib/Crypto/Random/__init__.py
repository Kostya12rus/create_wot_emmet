# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/Crypto/Random/__init__.py
__revision__ = '$Id$'
__all__ = ['new', '_UserFriendlyRNG', 'OSRNG', 'Fortuna']
import OSRNG, Fortuna
from Crypto.Random import _UserFriendlyRNG

def new(*args, **kwargs):
    return _UserFriendlyRNG.new(*args, **kwargs)


def atfork():
    _UserFriendlyRNG.reinit()


def get_random_bytes(n):
    return _UserFriendlyRNG.get_random_bytes(n)