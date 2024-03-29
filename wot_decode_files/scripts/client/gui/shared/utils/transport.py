# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/transport.py
import zlib, cPickle
from debug_utils import LOG_ERROR

def z_dumps(obj, protocol=-1, level=1):
    return zlib.compress(cPickle.dumps(obj, protocol), level)


def z_loads(value):
    try:
        result = zlib.decompress(value)
    except zlib.error:
        LOG_ERROR('Can not decompress value', value)
        return

    try:
        result = cPickle.loads(result)
    except cPickle.PickleError:
        LOG_ERROR('Can not unpickle value', value)
        result = None

    return result