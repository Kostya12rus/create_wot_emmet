# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/mode_selector/items/bootcamp_mode_selector_item.py
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.lobby.mode_selector.items.base_item import ModeSelectorNormalCardItem
from gui.impl.lobby.mode_selector.items.items_constants import CustomModeName
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext

class BootcampModeSelectorItem(ModeSelectorNormalCardItem):
    __slots__ = ()
    __lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self, _=None):
        super(BootcampModeSelectorItem, self).__init__()

    @property
    def modeName(self):
        return CustomModeName.BOOTCAMP

    def handleClick(self):
        self._bootcamp.runBootcamp()

    def _onInitializing(self):
        super(BootcampModeSelectorItem, self)._onInitializing()
        self.viewModel.setName(backport.text(R.strings.mode_selector.mode.bootcamp.name()))
        if self._bootcamp.hasFinishedBootcampBefore():
            self.viewModel.setStatusActive(backport.text(R.strings.mode_selector.mode.bootcamp.call.c_2()))
        else:
            self.viewModel.setStatusActive(backport.text(R.strings.mode_selector.mode.bootcamp.call.c_1()))

    def _getIsDisabled(self):
        return not self.__lobbyContext.getServerSettings().isBootcampEnabled()