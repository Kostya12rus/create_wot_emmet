# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/tutorial/gui/Scaleform/battle_v2/settings.py
from frameworks.wulf import WindowLayer
from gui.Scaleform.framework import GroupedViewSettings, ScopeTemplates
from tutorial.gui.Scaleform.battle_v2.pop_ups import ReplenishAmmoDialog

class BATTLE_VIEW_ALIAS(object):
    REPLENISH_AMMO_DIALOG = 'replenishAmmoDialog'


BATTLE_VIEW_SETTINGS = (
 GroupedViewSettings(BATTLE_VIEW_ALIAS.REPLENISH_AMMO_DIALOG, ReplenishAmmoDialog, 'replenishAmmoDialog.swf', WindowLayer.TOP_WINDOW, '', None, ScopeTemplates.DEFAULT_SCOPE, isModal=True, canClose=False, isCentered=False),)
DIALOG_ALIAS_MAP = {'replenishAmmo': BATTLE_VIEW_ALIAS.REPLENISH_AMMO_DIALOG}