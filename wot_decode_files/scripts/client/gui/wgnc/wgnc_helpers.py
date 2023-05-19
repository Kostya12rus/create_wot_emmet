# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgnc/wgnc_helpers.py
from debug_utils import LOG_ERROR

def parseSize(sizeStr):
    if sizeStr:
        try:
            size = tuple(map(int, sizeStr.split('x')))
            if len(size) != 2:
                return
        except ValueError:
            LOG_ERROR('Failed to parse size: %s' % sizeStr)
            size = None

    else:
        size = None
    return size