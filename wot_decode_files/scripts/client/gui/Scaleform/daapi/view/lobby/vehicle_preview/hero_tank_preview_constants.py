# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/hero_tank_preview_constants.py
from collections import namedtuple
from gui.impl.gen import R
from helpers import dependency
from skeletons.gui.game_control import IHeroTankController
_VehicleData = namedtuple('_SpecialParamsVehicle', ('name', 'styleID'))
_OFFSPRING_VEHICLE = _VehicleData(name='usa:A127_TL_1_LPC', styleID=83)
_PreviewParams = namedtuple('_PreviewParams', ('buyButtonLabel', 'enterEvent', 'exitEvent'))
_SPECIAL_PREVIEW_PARAMS = {_OFFSPRING_VEHICLE: _PreviewParams(buyButtonLabel=R.strings.vehicle_preview.buyingPanel.buyBtn.label.offspring(), enterEvent='ev_fest_off_hero_tank_in', exitEvent='ev_fest_off_hero_tank_out')}

@dependency.replace_none_kwargs(heroTanksControl=IHeroTankController)
def getHeroTankPreviewParams(heroTanksControl=None):
    vName = heroTanksControl.getCurrentVehicleName()
    vStyleId = heroTanksControl.getCurrentTankStyleId()
    vData = _VehicleData(vName, vStyleId)
    return _SPECIAL_PREVIEW_PARAMS.get(vData)