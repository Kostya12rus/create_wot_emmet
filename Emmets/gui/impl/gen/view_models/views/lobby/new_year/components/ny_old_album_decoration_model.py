# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/new_year/components/ny_old_album_decoration_model.py
from gui.impl.gen.view_models.views.lobby.new_year.components.ny_album_decoration_model import NyAlbumDecorationModel

class NyOldAlbumDecorationModel(NyAlbumDecorationModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(NyOldAlbumDecorationModel, self).__init__(properties=properties, commands=commands)

    def getShards(self):
        return self._getNumber(6)

    def setShards(self, value):
        self._setNumber(6, value)

    def getIsCanCraft(self):
        return self._getBool(7)

    def setIsCanCraft(self, value):
        self._setBool(7, value)

    def _initialize(self):
        super(NyOldAlbumDecorationModel, self)._initialize()
        self._addNumberProperty('shards', 0)
        self._addBoolProperty('isCanCraft', False)