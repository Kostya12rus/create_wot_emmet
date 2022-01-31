# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/wo2022/wo_helpers.py
from gui.impl import backport
from gui.impl.gen import R

def getEventName():
    return backport.text(R.strings.wo2022.eventName())


def getTimeLeftString(timeLeft):
    return backport.getTillTimeStringByRClass(timeLeft, R.strings.menu.Time.timeLeftShort, isRoundUp=True)