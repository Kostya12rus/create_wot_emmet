# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/tutorial_helper.py
from debug_utils import LOG_ERROR

def getTutorialGlobalStorage():
    try:
        from tutorial.control.context import GlobalStorage
    except ImportError:
        LOG_ERROR('Can not load package tutorial')
        GlobalStorage = None

    return GlobalStorage