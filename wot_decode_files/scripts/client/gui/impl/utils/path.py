# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/utils/path.py
import logging, typing
from constants import GF_RES_PROTOCOL
from gui.shared.utils.functions import getAbsoluteUrl
if typing.TYPE_CHECKING:
    from typing import Optional
_logger = logging.getLogger(__name__)

def normalizeGfImagePath(imgPath):
    if not isinstance(imgPath, (str, unicode)) or not imgPath:
        _logger.warning('Wrong image path: %s.', imgPath)
        return None
    else:
        newPath = getAbsoluteUrl(str(imgPath))
        newPath = newPath.replace('\\', '/')
        if not newPath.startswith(GF_RES_PROTOCOL.IMG):
            newPath = ('').join((GF_RES_PROTOCOL.IMG, newPath))
        return newPath