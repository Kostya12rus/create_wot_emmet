# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/deserter_meta.py
from gui.Scaleform.daapi.view.dialogs import I18nConfirmDialogMeta
from gui.shared.events import ShowDialogEvent

class IngameDeserterDialogMeta(I18nConfirmDialogMeta):

    def __init__(self, key, additionalInfo='', focusedID=None):
        super(IngameDeserterDialogMeta, self).__init__(key, messageCtx={'additionalInfo': additionalInfo}, focusedID=focusedID)
        self.__imagePath = '../maps/icons/battle/deserterLeaveBattle.png'
        self.__offsetY = 270

    def getEventType(self):
        return ShowDialogEvent.SHOW_DESERTER_DLG

    def getImagePath(self):
        return self.__imagePath

    def getOffsetY(self):
        return self.__offsetY