# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/FreeXPInfoWindow.py
from gui.Scaleform.daapi.view.meta.FreeXPInfoWindowMeta import FreeXPInfoWindowMeta
__author__ = 'd_savitski'

class FreeXPInfoWindow(FreeXPInfoWindowMeta):

    def __init__(self, ctx=None):
        super(FreeXPInfoWindow, self).__init__()
        self.meta = ctx.get('meta')
        self.handler = ctx.get('handler')

    def _populate(self):
        super(FreeXPInfoWindow, self)._populate()
        self.as_setTitleS(self.meta.getTitle())
        self.as_setSubmitLabelS(self.meta.getSubmitLbl())
        self.as_setTextS(self.meta.getTextInfo())

    def onWindowClose(self):
        self.handler(True)
        self.destroy()

    def onSubmitButton(self):
        self.onWindowClose()

    def onCancelButton(self):
        self.onWindowClose()

    def _dispose(self):
        super(FreeXPInfoWindow, self)._dispose()
        self.handler = None
        return