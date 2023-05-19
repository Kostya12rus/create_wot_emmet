# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client_common/pwd_token.py
import hashlib
from constants import DEFAULT_LANGUAGE
__all__ = ('generate', )

def _generateMd5Hash(pwd):
    md = hashlib.md5()
    md.update(pwd)
    return md.hexdigest()


_BY_LANG = {'cn': _generateMd5Hash, 
   'vn': _generateMd5Hash}

def generate(pwd):
    return pwd


if DEFAULT_LANGUAGE in _BY_LANG:
    generate = _BY_LANG[DEFAULT_LANGUAGE]