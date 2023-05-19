# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/sqlite3/dbapi2.py
import collections, datetime, time
from _sqlite3 import *
paramstyle = 'qmark'
threadsafety = 1
apilevel = '2.0'
Date = datetime.date
Time = datetime.time
Timestamp = datetime.datetime

def DateFromTicks(ticks):
    return Date(*time.localtime(ticks)[:3])


def TimeFromTicks(ticks):
    return Time(*time.localtime(ticks)[3:6])


def TimestampFromTicks(ticks):
    return Timestamp(*time.localtime(ticks)[:6])


version_info = tuple([ int(x) for x in version.split('.') ])
sqlite_version_info = tuple([ int(x) for x in sqlite_version.split('.') ])
Binary = buffer
collections.Sequence.register(Row)

def register_adapters_and_converters():

    def adapt_date(val):
        return val.isoformat()

    def adapt_datetime(val):
        return val.isoformat(' ')

    def convert_date(val):
        return datetime.date(*map(int, val.split('-')))

    def convert_timestamp(val):
        datepart, timepart = val.split(' ')
        year, month, day = map(int, datepart.split('-'))
        timepart_full = timepart.split('.')
        hours, minutes, seconds = map(int, timepart_full[0].split(':'))
        if len(timepart_full) == 2:
            microseconds = int(('{:0<6.6}').format(timepart_full[1].decode()))
        else:
            microseconds = 0
        val = datetime.datetime(year, month, day, hours, minutes, seconds, microseconds)
        return val

    register_adapter(datetime.date, adapt_date)
    register_adapter(datetime.datetime, adapt_datetime)
    register_converter('date', convert_date)
    register_converter('timestamp', convert_timestamp)


register_adapters_and_converters()
del register_adapters_and_converters