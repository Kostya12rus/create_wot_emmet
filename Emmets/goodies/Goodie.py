# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/goodies/Goodie.py
import time
from goodie_constants import GOODIE_STATE

class Goodie(object):
    __slots__ = [
     'uid', 'state', 'expiration', 'counter']

    def __init__(self, uid, state=GOODIE_STATE.INACTIVE, expiration=0, counter=0):
        self.uid = uid
        self.state = state
        self.expiration = expiration
        self.counter = counter

    def isActive(self):
        return self.state == GOODIE_STATE.ACTIVE

    def isExpired(self):
        if self.expiration and self.expiration < time.time():
            return True
        else:
            return False

    def toPdata(self):
        return (self.state, self.expiration, self.counter)