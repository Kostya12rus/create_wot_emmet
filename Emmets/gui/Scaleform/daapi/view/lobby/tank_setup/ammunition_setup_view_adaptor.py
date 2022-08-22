# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/tank_setup/ammunition_setup_view_adaptor.py
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.impl.lobby.tank_setup.ammunition_setup.hangar import HangarAmmunitionSetupView
from gui.impl.lobby.tank_setup.bootcamp.ammunition_setup import BootcampAmmunitionSetupView
from helpers import dependency
from skeletons.gui.game_control import IBootcampController

class AmmunitionSetupViewAdaptor(InjectComponentAdaptor):
    __bootcampController = dependency.descriptor(IBootcampController)

    def __init__(self, ctx):
        super(AmmunitionSetupViewAdaptor, self).__init__()
        self.__ctx = ctx

    def _makeInjectView(self):
        if self.__bootcampController.isInBootcamp():
            injectView = BootcampAmmunitionSetupView(**self.__ctx)
        else:
            injectView = HangarAmmunitionSetupView(**self.__ctx)
        self.__ctx = None
        return injectView