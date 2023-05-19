# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCPrebattleHints.py
import SoundGroups
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from gui.Scaleform.daapi.view.meta.BCPrebattleHintsMeta import BCPrebattleHintsMeta

class BCPrebattleHints(BCPrebattleHintsMeta):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, settings):
        super(BCPrebattleHints, self).__init__()
        self.__visibleHints = settings.get('visible_hints', set())
        self.__invisibleHints = settings.get('invisible_hints', set())
        self.__wwSound = settings.get('wwSound')

    def _populate(self):
        super(BCPrebattleHints, self)._populate()
        self.as_setHintsVisibilityS(self.__visibleHints, self.__invisibleHints)
        crewRoles = self.sessionProvider.shared.vehicleState.getControllingVehicle().typeDescriptor.type.crewRoles
        self.as_setCrewCountS(len(crewRoles))
        if self.__wwSound is not None:
            SoundGroups.g_instance.playSound2D(self.__wwSound)
        return

    def _dispose(self):
        super(BCPrebattleHints, self)._dispose()
        self.__visibleHints = None
        self.__invisibleHints = None
        return