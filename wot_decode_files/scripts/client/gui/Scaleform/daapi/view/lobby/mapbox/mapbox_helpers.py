# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/mapbox/mapbox_helpers.py
from gui.impl import backport
from gui.impl.gen import R
from gui.periodic_battles.models import AlertData
from gui.periodic_battles.models import PrimeTimeStatus
from gui.shared.formatters import text_styles
from helpers import dependency, time_utils
from skeletons.connection_mgr import IConnectionManager
from skeletons.gui.game_control import IMapboxController

def getPrimeTimeStatusVO():
    mapboxCtrl = dependency.instance(IMapboxController)
    connectionMgr = dependency.instance(IConnectionManager)
    status, _, _ = mapboxCtrl.getPrimeTimeStatus()
    errorStr = backport.text(R.strings.mapbox.serverAlertMessage(), serverName=connectionMgr.serverUserNameShort)
    showPrimeTimeAlert = status != PrimeTimeStatus.AVAILABLE
    return AlertData(alertIcon=backport.image(R.images.gui.maps.icons.library.alertBigIcon()) if showPrimeTimeAlert else None, buttonIcon='', buttonLabel=backport.text(R.strings.mapbox.serverAlertMessage.button()), buttonVisible=showPrimeTimeAlert and mapboxCtrl.hasAvailablePrimeTimeServers(), buttonTooltip=None, statusText=text_styles.vehicleStatusCriticalText(errorStr), popoverAlias=None, bgVisible=True, shadowFilterVisible=showPrimeTimeAlert, tooltip=None, isSimpleTooltip=False)


def getTillTimeString(timeStamp):
    timeLeft = time_utils.getTimeDeltaFromNow(timeStamp)
    modeStrBase = R.strings.menu.headerButtons.battle.types.mapbox.availability
    if timeLeft < time_utils.ONE_HOUR:
        res = backport.text(modeStrBase.lessThanHour())
    else:
        res = backport.backport_time_utils.getTillTimeStringByRClass(timeLeft, modeStrBase)
    return res