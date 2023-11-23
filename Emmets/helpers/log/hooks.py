# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/log/hooks.py
import logging, traceback, sys, ResMgr

def formatException(excType, excValue, excTraceback):
    extracted = traceback.extract_tb(excTraceback)
    converted = []
    for filename, lineno, name, line in extracted:
        if filename.endswith('.py'):
            converted.append((
             ResMgr.resolveToAbsolutePath(filename), lineno, name, line))
        else:
            converted.append((filename, lineno, name, line))

    converted = traceback.format_list(converted)
    converted += traceback.format_exception(excType, excValue, None)
    return ('').join(converted)


def setupUserExceptionHook():

    def exceptionHook(excType, excValue, excTraceback):
        logging.critical(formatException(excType, excValue, excTraceback))

    sys.excepthook = exceptionHook