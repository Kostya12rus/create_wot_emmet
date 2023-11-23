# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/LobbySelectableView.py
from gui.Scaleform.daapi import LobbySubView
from hangar_selectable_objects import ISelectableLogicCallback, HangarSelectableLogic

class LobbySelectableView(LobbySubView, ISelectableLogicCallback):

    def __init__(self, ctx=None):
        super(LobbySelectableView, self).__init__(ctx)
        self.__selectableLogic = None
        return

    def onHighlight3DEntity(self, entity):
        self._highlight3DEntityAndShowTT(entity)

    def onFade3DEntity(self, entity):
        self._fade3DEntityAndHideTT(entity)

    def _populate(self):
        super(LobbySelectableView, self)._populate()
        self._activateSelectableLogic()

    def _dispose(self):
        self._deactivateSelectableLogic()
        super(LobbySelectableView, self)._dispose()

    def _highlight3DEntityAndShowTT(self, entity):
        pass

    def _fade3DEntityAndHideTT(self, entity):
        pass

    def _activateSelectableLogic(self):
        if self.__selectableLogic is not None:
            return
        else:
            self.__selectableLogic = self._createSelectableLogic()
            self.__selectableLogic.init(self)
            return

    def _deactivateSelectableLogic(self):
        if self.__selectableLogic is not None:
            self.__selectableLogic.fini()
            self.__selectableLogic = None
        return

    def _createSelectableLogic(self):
        return HangarSelectableLogic()