# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/header/SquadTypeSelectPopover.py
from adisp import process
from debug_utils import LOG_ERROR
from gui.Scaleform.daapi.view.lobby.header import battle_selector_items
from gui.Scaleform.daapi.view.meta.BattleTypeSelectPopoverMeta import BattleTypeSelectPopoverMeta
from gui.Scaleform.locale.PLATOON import PLATOON
from gui.prb_control.entities.base.ctx import PrbAction
from gui.prb_control.entities.listener import IGlobalListener

class SquadTypeSelectPopover(BattleTypeSelectPopoverMeta, IGlobalListener):

    def __init__(self, _=None):
        super(SquadTypeSelectPopover, self).__init__()

    def selectFight(self, actionName):
        if self.prbDispatcher:
            self.__doSelect(actionName)
        else:
            LOG_ERROR('Prebattle dispatcher is not defined')

    def getTooltipData(self, itemData, itemIsDisabled):
        tooltip = ''
        if itemData == 'eventSquad':
            tooltip = PLATOON.HEADERBUTTON_TOOLTIPS_EVENTSQUAD
        elif itemData == 'squad':
            tooltip = PLATOON.HEADERBUTTON_TOOLTIPS_SQUAD
        return tooltip

    def demoClick(self):
        pass

    def update(self):
        if not self.isDisposed():
            self.as_updateS(*battle_selector_items.getSquadItems().getVOs())

    def _populate(self):
        super(SquadTypeSelectPopover, self)._populate()
        self.update()

    @process
    def __doSelect(self, prebattleActionName):
        yield self.prbDispatcher.doSelectAction(PrbAction(prebattleActionName))