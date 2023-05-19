# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/base/listener.py
from gui.prb_control import prbDispatcherProperty, prbEntityProperty

class IPrbListener(object):

    @prbDispatcherProperty
    def prbDispatcher(self):
        return

    @prbEntityProperty
    def prbEntity(self):
        return

    def startPrbListening(self):
        if self.prbEntity is not None and hasattr(self.prbEntity, 'addListener'):
            self.prbEntity.addListener(self)
        return

    def stopPrbListening(self):
        if self.prbEntity is not None:
            self.prbEntity.removeListener(self)
        return