# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/bootcamp/BootcampLobbyHintsConfig.py
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from Bootcamp import BOOTCAMP_UI_COMPONENTS

class BootcampLobbyHintsConfig:
    battleButton = {'viewAlias': VIEW_ALIAS.BOOTCAMP_INTRO_VIDEO, 
       'path': 'btnSelect', 
       'hideBorder': True, 
       'customHint': 'BCIconTextBigButtonFxUI'}
    objects = {'InBattleRepairKit': {'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE, 
                             'path': 'consumablesPanel:index=slotIndex', 
                             'slotIndex': 4, 
                             'customHint': 'BCHudConsumableHintUI', 
                             'padding': {'left': 6, 'right': -6, 'top': 28, 'bottom': -6}}, 
       'InBattleHealKit': {'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE, 
                           'path': 'consumablesPanel:index=slotIndex', 
                           'slotIndex': 3, 
                           'customHint': 'BCHudConsumableHintUI', 
                           'padding': {'left': 6, 'right': -6, 'top': 28, 'bottom': -6}}, 
       'InBattleExtinguisher': {'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE, 
                                'path': 'consumablesPanel:index=slotIndex', 
                                'slotIndex': 5, 
                                'customHint': 'BCHudConsumableHintUI', 
                                'padding': {'left': 6, 'right': -6, 'top': 28, 'bottom': -6}}, 
       'FragCorrelationBar': {'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE, 
                              'path': 'fragCorrelationBar', 
                              'padding': {'bottom': -7}, 'customHint': 'BCAppearFragCorrelationHintUI'}, 
       'Minimap': {'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE, 
                   'path': 'minimap.mapHit', 
                   'padding': {'left': -15, 'top': -15, 'right': 2, 'bottom': 2}, 'customHint': 'BCHudMinimapHintUI'}, 
       'ConsumablesAppear': {'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE, 
                             'path': 'consumablesPanel:index=slotIndex.iconLoader', 
                             'slotIndex': 4, 
                             'customHint': 'BCAppearEquipmentHintUI'}, 
       'MinimapAppear': {'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE, 
                         'path': 'minimap.background', 
                         'padding': {'left': -14, 'right': 1, 'top': -14, 'bottom': 1}, 'customHint': 'BCAppearMinimapHintUI'}, 
       'ConsumableSlot4': {'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE, 
                           'path': 'consumablesPanel:index=slotIndex.iconLoader', 
                           'slotIndex': 3, 
                           'customHint': 'BCHudTintHintUI'}, 
       'ConsumableSlot5': {'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE, 
                           'path': 'consumablesPanel:index=slotIndex.iconLoader', 
                           'slotIndex': 4, 
                           'customHint': 'BCHudTintHintUI'}, 
       'ConsumableSlot6': {'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE, 
                           'path': 'consumablesPanel:index=slotIndex.iconLoader', 
                           'slotIndex': 5, 
                           'customHint': 'BCHudTintHintUI'}, 
       'DamagePanelHealthbar': {'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE, 
                                'path': 'damagePanel.healthBar', 
                                'customHint': 'BCHudTintHintUI'}, 
       'LoadingRightButton': {'viewAlias': VIEW_ALIAS.BOOTCAMP_INTRO_VIDEO, 
                              'path': 'btnRight', 
                              'customHint': 'BCHudTintHintUI'}, 
       'LoadingLeftButton': {'viewAlias': VIEW_ALIAS.BOOTCAMP_INTRO_VIDEO, 
                             'path': 'btnLeft', 
                             'customHint': 'BCHudTintHintUI'}, 
       BOOTCAMP_UI_COMPONENTS.START_BATTLE_BUTTON: battleButton, 
       BOOTCAMP_UI_COMPONENTS.WELCOME_START_BATTLE_BUTTON: battleButton}

    def getItems(self):
        return self.objects


g_bootcampHintsConfig = BootcampLobbyHintsConfig()