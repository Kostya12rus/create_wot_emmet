# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/hangar_cameras/hangar_space_listener.py
from helpers import dependency
from skeletons.gui.shared.utils import IHangarSpace

class HangarSpaceListener(object):
    hangarSpace = dependency.descriptor(IHangarSpace)

    def __init__(self):
        self.hangarSpace.onSpaceCreate += self._onSpaceCreated
        self.hangarSpace.onSpaceDestroy += self._onSpaceDestroy

    def destroy(self):
        self.hangarSpace.onSpaceCreate -= self._onSpaceCreated
        self.hangarSpace.onSpaceDestroy -= self._onSpaceDestroy

    def _onSpaceCreated(self):
        pass

    def _onSpaceDestroy(self, inited):
        pass