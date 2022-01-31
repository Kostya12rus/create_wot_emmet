# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/ny/mixins.py
from gui.impl.new_year.navigation import NewYearNavigation
from uilogging.ny.loggers import NySelectableObjectLogger, NySelectableObjectFlowLogger

class SelectableObjectLoggerMixin(object):
    __selectableObjectLogger = NySelectableObjectLogger()
    __flowUILogger = NySelectableObjectFlowLogger()

    def logClick(self, anchorName):
        currentObject = NewYearNavigation.getCurrentObject()
        self.__selectableObjectLogger.logClick(anchorName, currentObject)
        self.__flowUILogger.logClick(anchorName, currentObject)