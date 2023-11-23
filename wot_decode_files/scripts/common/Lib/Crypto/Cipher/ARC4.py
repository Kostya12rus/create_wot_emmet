# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/Crypto/Cipher/ARC4.py
__revision__ = '$Id$'
from .Crypto.Util.py3compat import *
import _ARC4

class ARC4Cipher:

    def __init__(self, key, *args, **kwargs):
        if len(args) > 0:
            ndrop = args[0]
            args = args[1:]
        else:
            ndrop = kwargs.get('drop', 0)
            if ndrop:
                del kwargs['drop']
        self._cipher = _ARC4.new(key, *args, **kwargs)
        if ndrop:
            self._cipher.encrypt(b('\x00') * ndrop)
        self.block_size = self._cipher.block_size
        self.key_size = self._cipher.key_size

    def encrypt(self, plaintext):
        return self._cipher.encrypt(plaintext)

    def decrypt(self, ciphertext):
        return self._cipher.decrypt(ciphertext)


def new(key, *args, **kwargs):
    return ARC4Cipher(key, *args, **kwargs)


block_size = 1
key_size = xrange(1, 257)