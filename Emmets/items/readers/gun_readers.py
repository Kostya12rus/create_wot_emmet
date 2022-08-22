# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/items/readers/gun_readers.py
import ResMgr
from items import _xml
from items.components import component_constants
from items.components import gun_components
from items.components.component_constants import ZERO_FLOAT
from items.readers import shared_readers
from constants import IS_EDITOR

def readRecoilEffect(xmlCtx, section, cache):
    effName = _xml.readStringOrNone(xmlCtx, section, 'recoil/recoilEffect')
    if effName is not None:
        recoilEff = cache.getGunRecoilEffects(effName)
        if recoilEff is not None:
            backoffTime = recoilEff[0]
            returnTime = recoilEff[1]
        else:
            backoffTime = component_constants.ZERO_FLOAT
            returnTime = component_constants.ZERO_FLOAT
    else:
        backoffTime = _xml.readNonNegativeFloat(xmlCtx, section, 'recoil/backoffTime')
        returnTime = _xml.readNonNegativeFloat(xmlCtx, section, 'recoil/returnTime')
    recoil = gun_components.RecoilEffect(lodDist=shared_readers.readLodDist(xmlCtx, section, 'recoil/lodDist', cache), amplitude=_xml.readNonNegativeFloat(xmlCtx, section, 'recoil/amplitude'), backoffTime=backoffTime, returnTime=returnTime)
    if IS_EDITOR:
        recoil.effectName = effName
    return recoil


def readShot(xmlCtx, section, nationID, projectileSpeedFactor, cache):
    shellName = section.name
    shellID = cache.shellIDs(nationID).get(shellName)
    if shellID is None:
        _xml.raiseWrongXml(xmlCtx, '', 'unknown shell type name')
    shellDescr = cache.shells(nationID)[shellID]
    return gun_components.GunShot(shellDescr, ZERO_FLOAT if not section.has_key('defaultPortion') else _xml.readFraction(xmlCtx, section, 'defaultPortion'), _xml.readVector2(xmlCtx, section, 'piercingPower'), _xml.readPositiveFloat(xmlCtx, section, 'speed') * projectileSpeedFactor, _xml.readNonNegativeFloat(xmlCtx, section, 'gravity') * projectileSpeedFactor ** 2, _xml.readPositiveFloat(xmlCtx, section, 'maxDistance'), _xml.readFloat(xmlCtx, section, 'maxHeight', 1000000.0))