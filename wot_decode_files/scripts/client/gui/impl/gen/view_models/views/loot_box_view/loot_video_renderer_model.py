# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/loot_box_view/loot_video_renderer_model.py
from gui.impl.gen.view_models.views.loot_box_view.loot_def_renderer_model import LootDefRendererModel

class LootVideoRendererModel(LootDefRendererModel):
    __slots__ = ()

    def __init__(self, properties=14, commands=0):
        super(LootVideoRendererModel, self).__init__(properties=properties, commands=commands)

    def getVideoSrc(self):
        return self._getString(13)

    def setVideoSrc(self, value):
        self._setString(13, value)

    def _initialize(self):
        super(LootVideoRendererModel, self)._initialize()
        self._addStringProperty('videoSrc', '')