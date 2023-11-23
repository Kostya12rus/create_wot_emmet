# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCBattleSelector.py
import logging
from gui.Scaleform.daapi.view.lobby.header.BattleTypeSelectPopover import BattleTypeSelectPopover
_logger = logging.getLogger(__name__)

class BCBattleSelector(BattleTypeSelectPopover):

    def as_updateS(self, items, extraItems, isShowDemonstrator, demonstratorEnabled):
        _logger.debug('BCBattleSelector, %s', items)
        for battleTypeItem in items:
            if battleTypeItem['data'] != 'random':
                battleTypeItem['disabled'] = True

        super(BCBattleSelector, self).as_updateS(items, extraItems, isShowDemonstrator, demonstratorEnabled)