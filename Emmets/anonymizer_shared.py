# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/anonymizer_shared.py
import struct, zlib

def getUsersListCheckSum(usersList):
    if len(usersList) == 0:
        return 0
    sortedList = sorted(list(usersList))
    return zlib.crc32((' ').join(sortedList))