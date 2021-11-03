# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/halloween/tooltips/event_banner_tooltip_model.py
from frameworks.wulf import ViewModel

class EventBannerTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(EventBannerTooltipModel, self).__init__(properties=properties, commands=commands)

    def getAvailable(self):
        return self._getNumber(0)

    def setAvailable(self, value):
        self._setNumber(0, value)

    def getTotal(self):
        return self._getNumber(1)

    def setTotal(self, value):
        self._setNumber(1, value)

    def getCountdownValue(self):
        return self._getNumber(2)

    def setCountdownValue(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(EventBannerTooltipModel, self)._initialize()
        self._addNumberProperty('available', 0)
        self._addNumberProperty('total', 0)
        self._addNumberProperty('countdownValue', 0)