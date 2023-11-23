# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/Crypto/pct_warnings.py


class CryptoWarning(Warning):
    pass


class CryptoDeprecationWarning(DeprecationWarning, CryptoWarning):
    pass


class CryptoRuntimeWarning(RuntimeWarning, CryptoWarning):
    pass


class RandomPool_DeprecationWarning(CryptoDeprecationWarning):
    pass


class ClockRewindWarning(CryptoRuntimeWarning):
    pass


class GetRandomNumber_DeprecationWarning(CryptoDeprecationWarning):
    pass


class DisableShortcut_DeprecationWarning(CryptoDeprecationWarning):
    pass


class PowmInsecureWarning(CryptoRuntimeWarning):
    pass


import warnings as _warnings
_warnings.filterwarnings('always', category=ClockRewindWarning, append=1)