# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCVehicleBuyView.py
from Event import Event
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BCVehicleBuyView(BaseDAAPIComponent):

    def __init__(self):
        super(BCVehicleBuyView, self).__init__()
        self.__academySelected = False
        self.onAcademyClicked = Event()

    def onAcademyClick(self):
        if not self.__academySelected:
            self.__academySelected = True
            self.onAcademyClicked()

    def _dispose(self):
        self.onAcademyClicked.clear()
        super(BCVehicleBuyView, self)._dispose()