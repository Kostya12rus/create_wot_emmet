# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/rally/AbstractRallyView.py
from gui.Scaleform.daapi.view.meta.AbstractRallyViewMeta import AbstractRallyViewMeta

class AbstractRallyView(AbstractRallyViewMeta):

    def __init__(self):
        super(AbstractRallyView, self).__init__()
        self.isMinimising = False

    def setData(self, itemID):
        pass