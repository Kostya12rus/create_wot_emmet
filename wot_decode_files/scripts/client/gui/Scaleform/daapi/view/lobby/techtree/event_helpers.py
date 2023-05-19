# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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