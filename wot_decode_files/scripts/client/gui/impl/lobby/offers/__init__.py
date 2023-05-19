# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/offers/__init__.py
import typing
from constants import GF_RES_PROTOCOL
from gui.shared.utils.functions import getAbsoluteUrl

def getGfImagePath(imgPath):
    if imgPath is None:
        return
    else:
        newPath = getAbsoluteUrl(imgPath)
        newPath = newPath.replace('\\', '/')
        if not newPath.startswith(GF_RES_PROTOCOL.IMG):
            newPath = ('').join([GF_RES_PROTOCOL.IMG, newPath])
        return newPath