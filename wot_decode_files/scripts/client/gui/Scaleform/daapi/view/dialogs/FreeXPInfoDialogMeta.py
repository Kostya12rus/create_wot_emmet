# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/FreeXPInfoDialogMeta.py
from gui import makeHtmlString
from gui.Scaleform.daapi.view.dialogs import IDialogMeta
from gui.Scaleform.framework import ScopeTemplates
from gui.Scaleform.locale.DIALOGS import DIALOGS
from helpers import i18n
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS

class FreeXPInfoBaseMeta(IDialogMeta):

    def getTitle(self):
        return ''

    def getSubmitLbl(self):
        return ''

    def getTextInfo(self):
        return ''

    def getViewScopeType(self):
        return ScopeTemplates.DEFAULT_SCOPE

    def getEventType(self):
        return VIEW_ALIAS.FREE_X_P_INFO_WINDOW


class FreeXPInfoMeta(FreeXPInfoBaseMeta):

    def getTitle(self):
        return i18n.makeString(DIALOGS.FREEXPINFO_TITLE)

    def getSubmitLbl(self):
        return i18n.makeString(DIALOGS.FREEXPINFO_SUBMITBTNLBL)

    def getTextInfo(self):
        text = {}
        msgFormatted = makeHtmlString('html_templates:lobby/dialogs', 'freeXPInfo', {})
        text['body'] = msgFormatted
        return text