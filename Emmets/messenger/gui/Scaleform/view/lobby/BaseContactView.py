# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/gui/Scaleform/view/lobby/BaseContactView.py
from debug_utils import LOG_ERROR
from messenger.gui.Scaleform.meta.BaseContactViewMeta import BaseContactViewMeta

class BaseContactView(BaseContactViewMeta):

    def onCancel(self):
        pass

    def _populate(self):
        super(BaseContactView, self)._populate()
        self.as_setInitDataS(self._getInitDataObject())

    def _getInitDataObject(self):
        LOG_ERROR('this method have to be overridden!')
        return self._getDefaultInitData('', '', '', '', '')

    def _getDefaultInitData(self, mainLbl, btOkLbl, btnCancelLbl, btOkTooltip, btnCancelTooltip):
        return {'btOkLbl': btOkLbl, 
           'btnCancelLbl': btnCancelLbl, 
           'mainLbl': mainLbl, 
           'btOkTooltip': btOkTooltip, 
           'btnCancelTooltip': btnCancelTooltip}