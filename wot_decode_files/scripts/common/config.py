# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/config.py
from abc import ABCMeta, abstractmethod

class Config(object):
    __metaclass__ = ABCMeta

    def __init__(self, **kwargs):
        map((lambda item: setattr(self, *item)), kwargs.iteritems())

    @classmethod
    @abstractmethod
    def create(cls, *args, **kwargs):
        pass