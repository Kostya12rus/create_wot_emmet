# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BCNationsWindowMeta.py
from tutorial.gui.Scaleform.pop_ups import TutorialDialog

class BCNationsWindowMeta(TutorialDialog):

    def onNationSelected(self, nationId):
        self._printOverrideError('onNationSelected')

    def onNationShow(self, nationId):
        self._printOverrideError('onNationShow')

    def onHighlightShow(self):
        self._printOverrideError('onHighlightShow')

    def as_selectNationS(self, selectedIndex, nationsList, promoNationsList):
        if self._isDAAPIInited():
            return self.flashObject.as_selectNation(selectedIndex, nationsList, promoNationsList)