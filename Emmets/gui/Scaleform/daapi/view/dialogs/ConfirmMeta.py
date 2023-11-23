# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/ConfirmMeta.py
from gui.Scaleform.daapi.view.dialogs import IDialogMeta
from gui.Scaleform.framework import ScopeTemplates
from gui.shared import events
from helpers import i18n

class ConfirmMeta(IDialogMeta):

    def __init__(self, title, description, submitBtn, cancelBtn, checkBox, selected=False):
        self.__title = title
        self.__description = description
        self.__submitLabel = submitBtn
        self.__cancelLabel = cancelBtn
        self.__checkBoxLabel = checkBox
        self.__checkBoxSelected = selected

    def destroy(self):
        pass

    def getEventType(self):
        return events.ShowDialogEvent.SHOW_CONFIRM_DIALOG

    def getTitle(self):
        return i18n.makeString(self.__title)

    def getDescription(self):
        return i18n.makeString(self.__description)

    def getSubmitButtonLabel(self):
        return i18n.makeString(self.__submitLabel)

    def getCancelButtonLabel(self):
        return i18n.makeString(self.__cancelLabel)

    def getCheckBoxButtonLabel(self):
        return i18n.makeString(self.__checkBoxLabel)

    def getCheckBoxSelected(self):
        return self.__checkBoxSelected

    def getViewScopeType(self):
        return ScopeTemplates.DYNAMIC_SCOPE