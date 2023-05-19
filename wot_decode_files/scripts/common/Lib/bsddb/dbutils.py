# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/bsddb/dbutils.py
from time import sleep as _sleep
import sys
absolute_import = sys.version_info[0] >= 3
if absolute_import:
    exec 'from . import db'
else:
    import db
_deadlock_MinSleepTime = 1.0 / 128
_deadlock_MaxSleepTime = 3.14159
_deadlock_VerboseFile = None

def DeadlockWrap(function, *_args, **_kwargs):
    sleeptime = _deadlock_MinSleepTime
    max_retries = _kwargs.get('max_retries', -1)
    if 'max_retries' in _kwargs:
        del _kwargs['max_retries']
    while True:
        try:
            return function(*_args, **_kwargs)
        except db.DBLockDeadlockError:
            if _deadlock_VerboseFile:
                _deadlock_VerboseFile.write('dbutils.DeadlockWrap: sleeping %1.3f\n' % sleeptime)
            _sleep(sleeptime)
            sleeptime *= 2
            if sleeptime > _deadlock_MaxSleepTime:
                sleeptime = _deadlock_MaxSleepTime
            max_retries -= 1
            if max_retries == -1:
                raise