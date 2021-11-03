# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/techtree/event_helpers.py
from gui.impl import backport
from gui.impl.gen import R
from helpers.time_utils import getTimeStructInLocal

class TechTreeFormatters(object):

    @staticmethod
    def getActionInfoStr(title, finishTime):
        return backport.text(R.strings.tutorial.techtree.nationDiscount.title(), name=title, time=TechTreeFormatters.__getDateTimeText(finishTime))

    @staticmethod
    def __getDateTimeText(dateTime):
        localDateTime = getTimeStructInLocal(dateTime)
        monthName = backport.text(R.strings.menu.dateTime.months.dyn(('c_{}').format(localDateTime.tm_mon))())
        dateTimeText = backport.text(R.strings.tutorial.techtree.nationDiscount.dateTime(), day=localDateTime.tm_mday, monthName=monthName, year=localDateTime.tm_year)
        return dateTimeText