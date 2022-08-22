# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/Crypto/Util/randpool.py
__revision__ = '$Id$'
from Crypto.pct_warnings import RandomPool_DeprecationWarning
import Crypto.Random, warnings

class RandomPool:

    def __init__(self, numbytes=160, cipher=None, hash=None, file=None):
        warnings.warn('This application uses RandomPool, which is BROKEN in older releases.  See http://www.pycrypto.org/randpool-broken', RandomPool_DeprecationWarning)
        self.__rng = Crypto.Random.new()
        self.bytes = numbytes
        self.bits = self.bytes * 8
        self.entropy = self.bits

    def get_bytes(self, N):
        return self.__rng.read(N)

    def _updateEntropyEstimate(self, nbits):
        self.entropy += nbits
        if self.entropy < 0:
            self.entropy = 0
        elif self.entropy > self.bits:
            self.entropy = self.bits

    def _randomize(self, N=0, devname='/dev/urandom'):
        self.__rng.flush()

    def randomize(self, N=0):
        self.__rng.flush()

    def stir(self, s=''):
        self.__rng.flush()

    def stir_n(self, N=3):
        self.__rng.flush()

    def add_event(self, s=''):
        self.__rng.flush()

    def getBytes(self, N):
        return self.get_bytes(N)

    def addEvent(self, event, s=''):
        return self.add_event()