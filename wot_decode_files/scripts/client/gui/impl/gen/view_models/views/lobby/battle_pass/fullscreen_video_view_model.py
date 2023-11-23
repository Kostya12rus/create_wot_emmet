# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/fullscreen_video_view_model.py
from frameworks.wulf import ViewModel

class FullscreenVideoViewModel(ViewModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=3, commands=1):
        super(FullscreenVideoViewModel, self).__init__(properties=properties, commands=commands)

    def getVideoName(self):
        return self._getString(0)

    def setVideoName(self, value):
        self._setString(0, value)

    def getAudioName(self):
        return self._getString(1)

    def setAudioName(self, value):
        self._setString(1, value)

    def getIsWindowAccessible(self):
        return self._getBool(2)

    def setIsWindowAccessible(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(FullscreenVideoViewModel, self)._initialize()
        self._addStringProperty('videoName', '')
        self._addStringProperty('audioName', '')
        self._addBoolProperty('isWindowAccessible', False)
        self.onClose = self._addCommand('onClose')