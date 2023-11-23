# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/fortifications/ConfirmOrderDialogMeta.py
from gui.Scaleform.daapi.view.dialogs import IDialogMeta
from gui.Scaleform.framework import ScopeTemplates
from gui.Scaleform.locale.DIALOGS import DIALOGS
from gui.shared import events
from web_stubs import i18n

class ConfirmOrderDialogMeta(IDialogMeta):

    def __init__(self, orderID, title, submitBtn, cancelBtn):
        self.__orderID = orderID
        self.__title = title
        self.__submitLabel = submitBtn
        self.__cancelLabel = cancelBtn

    def submit(self, count):
        pass

    def getEventType(self):
        return events.ShowDialogEvent.SHOW_CONFIRM_ORDER_DIALOG

    def getTitle(self):
        return i18n.makeString(self.__title)

    def getSubmitButtonLabel(self):
        return i18n.makeString(self.__submitLabel)

    def getCancelButtonLabel(self):
        return i18n.makeString(self.__cancelLabel)

    def getOrderID(self):
        return self.__orderID

    def getViewScopeType(self):
        return ScopeTemplates.DEFAULT_SCOPE

    def destroy(self):
        pass


class BuyOrderDialogMeta(ConfirmOrderDialogMeta):

    def __init__(self, orderID):
        super(BuyOrderDialogMeta, self).__init__(orderID, DIALOGS.CREATEORDERCONFIRMATION_TITLE, DIALOGS.CREATEORDERCONFIRMATION_SUBMIT, DIALOGS.CREATEORDERCONFIRMATION_CANCEL)