# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/backport/backport_time_utils.py
import time
from gui.impl.backport import text
from helpers import time_utils

def getTillTimeStringByRClass(timeValue, stringRClass, isRoundUp=False, removeLeadingZeros=True):
    gmtime = time.gmtime(timeValue)
    if isRoundUp and gmtime.tm_sec > 0:
        timeValue += time_utils.ONE_MINUTE
        gmtime = time.gmtime(timeValue)
    if timeValue >= time_utils.ONE_DAY:
        fmtKey = 'days'
        gmtime = time.gmtime(timeValue - time_utils.ONE_DAY)
    elif timeValue >= time_utils.ONE_HOUR:
        fmtKey = 'hours'
    elif timeValue >= time_utils.ONE_MINUTE:
        fmtKey = 'min'
    else:
        fmtKey = 'lessMin'
    tm = time.struct_time(gmtime)
    fmtValues = {'day': str(tm.tm_yday), 
       'hour': (removeLeadingZeros or time.strftime)('%H', gmtime) if 1 else str(tm.tm_hour), 
       'min': (removeLeadingZeros or time.strftime)('%M', gmtime) if 1 else str(tm.tm_min), 
       'sec': time.strftime('%S', gmtime)}
    return text(stringRClass.dyn(fmtKey)(), **fmtValues)