# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/log/adapters.py
import logging

class LoggerAdapter(logging.LoggerAdapter):

    def debug(self, msg, *args, **kwargs):
        self.log(logging.DEBUG, msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.log(logging.INFO, msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.log(logging.WARNING, msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.log(logging.ERROR, msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        self.log(logging.CRITICAL, msg, *args, **kwargs)

    def log(self, level, msg, *args, **kwargs):
        if self.isEnabledFor(level):
            super(LoggerAdapter, self).log(level, msg, *args, **kwargs)


class InstanceContextLoggerAdapter(LoggerAdapter):

    def __init__(self, logger, instance=None, **context):
        if instance is not None:
            context['cls'] = instance.__class__.__name__
            context['iid'] = id(instance)
        super(InstanceContextLoggerAdapter, self).__init__(logger, context)
        return

    def process(self, msg, kwargs):
        if self.extra:
            msg = ('{} {}').format(self.extra, msg)
        return (
         msg, kwargs)


def getWithContext(loggerName, instance=None, **context):
    return InstanceContextLoggerAdapter(logging.getLogger(loggerName), instance=instance, **context)