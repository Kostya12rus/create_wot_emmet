# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/messages/vehicle_errors.py
import typing
from debug_utils import LOG_DEBUG
from gui.Scaleform.daapi.view.battle.shared.messages import fading_messages
if typing.TYPE_CHECKING:
    from items.vehicles import VehicleDescriptor

class VehicleErrorMessages(fading_messages.FadingMessages):

    def __init__(self):
        super(VehicleErrorMessages, self).__init__('VehicleErrorsPanel', 'vehicle_errors_panel.xml')
        self.__ignoreKeys = ()
        self._keyReplacers = {'cantShootNoAmmo': self.__noAmmoReplacer}

    @property
    def ignoreKeys(self):
        return self.__ignoreKeys

    @ignoreKeys.setter
    def ignoreKeys(self, keys):
        self.__ignoreKeys = keys

    def __del__(self):
        LOG_DEBUG('VehicleErrorMessages panel is deleted')

    def _addGameListeners(self):
        super(VehicleErrorMessages, self)._addGameListeners()
        ctrl = self.sessionProvider.shared.messages
        if ctrl is not None:
            ctrl.onShowVehicleErrorByKey += self.__onShowVehicleErrorByKey
        return

    def _removeGameListeners(self):
        ctrl = self.sessionProvider.shared.messages
        if ctrl is not None:
            ctrl.onShowVehicleErrorByKey -= self.__onShowVehicleErrorByKey
        super(VehicleErrorMessages, self)._removeGameListeners()
        return

    def __onShowVehicleErrorByKey(self, key, args=None, extra=None):
        if key not in self.__ignoreKeys:
            if key in self._keyReplacers:
                key = self._keyReplacers[key](key, args)
            self.showMessage(key, args, extra)

    @staticmethod
    def __noAmmoReplacer(key, args):
        typeDescriptor = args['typeDescriptor']
        if typeDescriptor.isFlamethrower:
            key = 'cantShootNoFlameAmmo'
        return key