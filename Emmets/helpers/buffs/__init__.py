# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/buffs/__init__.py
import logging
from typing import List
import BigWorld
from buffs_common import Buff, BuffComponent, BuffsRepository, BuffFactory
from vehicle_systems.entity_components import VehicleComponent
from constants import BuffComponentVisibilityMode
import configs
_logger = logging.getLogger(__name__)
COMPONENTS_FACTORIES = {}

class ClientBuffsRepository(BuffsRepository):

    @property
    def _buffFactory(self):
        return ClientBuffFactory


class ClientBuff(Buff):
    pass


class ClientBuffComponent(BuffComponent):
    VisibilityModes = BuffComponentVisibilityMode

    def apply(self, ctx=None):
        if self._isVisible():
            self._apply()

    def unapply(self):
        if self._isVisible():
            self._unapply()

    def _apply(self):
        pass

    def _unapply(self):
        pass

    def _isVehicleObservedByAvatar(self):
        avatar = BigWorld.player()
        if not avatar:
            return False
        return avatar.getVehicleAttached() == self._owner

    def _shouldShowForSelf(self):
        return self._owner.isPlayerVehicle or self._isVehicleObservedByAvatar()

    def _isVisible(self):
        if self._config.visibleTo == self.VisibilityModes.ALL:
            return True
        if self._config.visibleTo == self.VisibilityModes.SELF and self._shouldShowForSelf():
            return True
        if self._config.visibleTo == self.VisibilityModes.OTHERS and not self._shouldShowForSelf():
            return True
        return False


class BuffContainer(VehicleComponent):

    def __init__(self):
        self._buffs = {}

    def set_buffs(self, prevBuffs=None):
        if not self.isStarted:
            return
        else:
            buffsRepo = ClientBuffsRepository.getInstance()
            prevBuffs = set(prevBuffs) if prevBuffs else set()
            currentBuffs = set(self.buffs)
            toAddBuffIndices = currentBuffs - prevBuffs
            toRemoveBuffIndices = prevBuffs - currentBuffs
            for index in toAddBuffIndices:
                buffFactory = buffsRepo.getBuffFactoryByIndex(index)
                if buffFactory:
                    buff = buffFactory.createBuff(self)
                    buff.apply()
                    self._buffs[index] = buff

            for index in toRemoveBuffIndices:
                buff = self._buffs.pop(index, None)
                if buff:
                    buff.unapply()

            return

    def clearBuffs(self):
        for buff in self._buffs.itervalues():
            buff.unapply()

        self._buffs.clear()


class ClientBuffFactory(BuffFactory):
    COMPONENTS_CONFIGS = configs

    @property
    def _buffClass(self):
        return ClientBuff

    @property
    def _xmlFactories(self):
        import helpers.buffs.components
        return self.COMPONENTS_FACTORIES

    @property
    def _component(self):
        return 'client'


clientBuffComponent = ClientBuffFactory.registerBuffComponent