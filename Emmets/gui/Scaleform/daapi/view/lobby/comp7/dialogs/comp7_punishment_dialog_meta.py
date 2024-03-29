# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/comp7/dialogs/comp7_punishment_dialog_meta.py
from gui.Scaleform.daapi.view.dialogs import I18nInfoDialogMeta
from gui.shared.events import ShowDialogEvent

class Comp7PunishmentDialogMeta(I18nInfoDialogMeta):

    def getTitle(self):
        return self._makeString(('{}/title').format(self._key), {})

    def getMsgTitle(self):
        return self._makeString(('{}/msgTitle').format(self._key), {})

    def getMessage(self):
        return self._makeString(('{}/message').format(self._key), self._messageCtx)

    def getEventType(self):
        return ShowDialogEvent.SHOW_COMP7_PUNISHMENT_DIALOG