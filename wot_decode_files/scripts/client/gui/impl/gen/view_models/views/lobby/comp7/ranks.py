# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/comp7/ranks.py
from frameworks.wulf import ViewModel

class Ranks(ViewModel):
    __slots__ = ()
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    FIFTH = 5
    SIXTH = 6
    SEVENTH = 7

    def __init__(self, properties=0, commands=0):
        super(Ranks, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(Ranks, self)._initialize()