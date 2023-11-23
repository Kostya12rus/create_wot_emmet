# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/hangar_cameras/hangar_space_listener.py
from helpers import dependency
from skeletons.gui.shared.utils import IHangarSpace

class HangarSpaceListener(object):
    hangarSpace = dependency.descriptor(IHangarSpace)

    def __init__(self):
        self.hangarSpace.onSpaceCreate += self._activate
        self.hangarSpace.onSpaceDestroy += self._deactivate

    def destroy(self):
        self.hangarSpace.onSpaceCreate -= self._activate
        self.hangarSpace.onSpaceDestroy -= self._deactivate

    def _activate(self):
        pass

    def _deactivate(self, inited):
        pass