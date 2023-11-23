# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/pub/main_view.py
from frameworks.wulf import ViewFlags, ViewSettings, ViewModel
from gui.impl.pub import ViewImpl

class MainView(ViewImpl):
    __slots__ = ()

    def __init__(self, entryID):
        super(MainView, self).__init__(ViewSettings(entryID, ViewFlags.MAIN_VIEW, ViewModel()))