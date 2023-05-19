# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/component_override.py
from helpers import dependency
from skeletons.gui.game_control import IBootcampController

class BootcampComponentOverride(object):
    __slots__ = ('__usualObject', '__bootcampObject')
    bootcampController = dependency.descriptor(IBootcampController)

    def __init__(self, usualObject, bootcampObject):
        super(BootcampComponentOverride, self).__init__()
        self.__usualObject = usualObject
        self.__bootcampObject = bootcampObject

    def __call__(self):
        isBootcamp = self.bootcampController.isInBootcamp()
        if isBootcamp:
            return self.__bootcampObject
        return self.__usualObject