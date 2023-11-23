# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/Crypto/Cipher/CAST.py
__revision__ = '$Id$'
from Crypto.Cipher import blockalgo
import _CAST

class CAST128Cipher(blockalgo.BlockAlgo):

    def __init__(self, key, *args, **kwargs):
        blockalgo.BlockAlgo.__init__(self, _CAST, key, *args, **kwargs)


def new(key, *args, **kwargs):
    return CAST128Cipher(key, *args, **kwargs)


MODE_ECB = 1
MODE_CBC = 2
MODE_CFB = 3
MODE_PGP = 4
MODE_OFB = 5
MODE_CTR = 6
MODE_OPENPGP = 7
MODE_EAX = 9
block_size = 8
key_size = xrange(5, 17)