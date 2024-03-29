# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/Crypto/PublicKey/_RSA.py
__revision__ = '$Id$'
from Crypto.PublicKey import pubkey
from Crypto.Util import number

def generate_py(bits, randfunc, progress_func=None, e=65537):
    obj = RSAobj()
    obj.e = long(e)
    if progress_func:
        progress_func('p,q\n')
    p = q = 1
    while number.size(p * q) < bits:
        p = pubkey.getStrongPrime(bits >> 1, obj.e, 1e-12, randfunc)
        q = pubkey.getStrongPrime(bits - (bits >> 1), obj.e, 1e-12, randfunc)

    if p > q:
        p, q = q, p
    obj.p = p
    obj.q = q
    if progress_func:
        progress_func('u\n')
    obj.u = pubkey.inverse(obj.p, obj.q)
    obj.n = obj.p * obj.q
    if progress_func:
        progress_func('d\n')
    obj.d = pubkey.inverse(obj.e, (obj.p - 1) * (obj.q - 1))
    return obj


class RSAobj(pubkey.pubkey):

    def size(self):
        return number.size(self.n) - 1