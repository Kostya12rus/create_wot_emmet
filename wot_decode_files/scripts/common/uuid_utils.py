# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/uuid_utils.py
import os, random
from uuid import uuid1
_node = None

def _getNode():
    global _node
    if _node is not None:
        return _node
    else:
        _node = random.randrange(0, 4294967296) << 16
        _node = _node | os.getpid() & 65535
        _node = _node | 1099511627776
        return _node


def genUUID():
    return uuid1(_getNode())