# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/new_year/views/albums/ny_current_album_model.py
from gui.impl.gen.view_models.views.lobby.new_year.views.albums.ny_open_album_model import NyOpenAlbumModel

class NyCurrentAlbumModel(NyOpenAlbumModel):
    __slots__ = ('onHangMegaToy', )

    def __init__(self, properties=15, commands=5):
        super(NyCurrentAlbumModel, self).__init__(properties=properties, commands=commands)

    def getBonusValue(self):
        return self._getReal(11)

    def setBonusValue(self, value):
        self._setReal(11, value)

    def getCreditBonusValue(self):
        return self._getReal(12)

    def setCreditBonusValue(self, value):
        self._setReal(12, value)

    def getIsToysHidden(self):
        return self._getBool(13)

    def setIsToysHidden(self, value):
        self._setBool(13, value)

    def getIsAnimationStarted(self):
        return self._getBool(14)

    def setIsAnimationStarted(self, value):
        self._setBool(14, value)

    def _initialize(self):
        super(NyCurrentAlbumModel, self)._initialize()
        self._addRealProperty('bonusValue', 0.0)
        self._addRealProperty('creditBonusValue', 0.0)
        self._addBoolProperty('isToysHidden', False)
        self._addBoolProperty('isAnimationStarted', False)
        self.onHangMegaToy = self._addCommand('onHangMegaToy')