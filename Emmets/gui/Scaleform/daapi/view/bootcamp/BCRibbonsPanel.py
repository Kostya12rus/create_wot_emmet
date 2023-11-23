# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCRibbonsPanel.py
from gui.Scaleform.daapi.view.battle.shared.ribbons_panel import BattleRibbonsPanel
from bootcamp.Bootcamp import g_bootcamp

class BCRibbonsPanel(BattleRibbonsPanel):

    def __init__(self):
        super(BCRibbonsPanel, self).__init__()
        self._ribbonsSettings = None
        return

    def _populate(self):
        super(BCRibbonsPanel, self)._populate()
        self._ribbonsSettings = g_bootcamp.getBattleRibbonsSettings()

    def _shouldShowRibbon(self, ribbon):
        ribbonName = ribbon.getType()
        if ribbonName in self._ribbonsSettings:
            return super(BCRibbonsPanel, self)._shouldShowRibbon(ribbon)
        return False

    def _dispose(self):
        super(BCRibbonsPanel, self)._dispose()
        self._ribbonsSettings = None
        return