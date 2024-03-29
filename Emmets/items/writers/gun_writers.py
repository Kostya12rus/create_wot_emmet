# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/items/writers/gun_writers.py
from items import _xml
from items.writers import shared_writers

def writeRecoilEffect(item, section, cache):
    if item.effectName != 'none':
        _xml.rewriteString(section, 'recoilEffect', item.effectName)
        section.deleteSection('backoffTime')
        section.deleteSection('returnTime')
    else:
        _xml.rewriteFloat(section, 'backoffTime', item.backoffTime)
        _xml.rewriteFloat(section, 'returnTime', item.returnTime)
        section.deleteSection('recoilEffect')
    _xml.rewriteFloat(section, 'amplitude', item.amplitude)
    shared_writers.writeLodDist(item.lodDist, section, 'lodDist', cache)