# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/distutils/log.py
DEBUG = 1
INFO = 2
WARN = 3
ERROR = 4
FATAL = 5
import sys

class Log:

    def __init__(self, threshold=WARN):
        self.threshold = threshold

    def _log(self, level, msg, args):
        if level not in (DEBUG, INFO, WARN, ERROR, FATAL):
            raise ValueError('%s wrong log level' % str(level))
        if level >= self.threshold:
            if args:
                msg = msg % args
            if level in (WARN, ERROR, FATAL):
                stream = sys.stderr
            else:
                stream = sys.stdout
            stream.write('%s\n' % msg)
            stream.flush()

    def log(self, level, msg, *args):
        self._log(level, msg, args)

    def debug(self, msg, *args):
        self._log(DEBUG, msg, args)

    def info(self, msg, *args):
        self._log(INFO, msg, args)

    def warn(self, msg, *args):
        self._log(WARN, msg, args)

    def error(self, msg, *args):
        self._log(ERROR, msg, args)

    def fatal(self, msg, *args):
        self._log(FATAL, msg, args)


_global_log = Log()
log = _global_log.log
debug = _global_log.debug
info = _global_log.info
warn = _global_log.warn
error = _global_log.error
fatal = _global_log.fatal

def set_threshold(level):
    old = _global_log.threshold
    _global_log.threshold = level
    return old


def set_verbosity(v):
    if v <= 0:
        set_threshold(WARN)
    elif v == 1:
        set_threshold(INFO)
    elif v >= 2:
        set_threshold(DEBUG)