# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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