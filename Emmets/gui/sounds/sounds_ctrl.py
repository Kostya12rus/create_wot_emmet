# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/sounds/sounds_ctrl.py
import weakref, MusicControllerWWISE as _MC, SoundGroups
from gui.sounds.ambients import GuiAmbientsCtrl
from gui.sounds.event_sound_subctrl import EventSoundSubController
from gui.sounds.sound_constants import EnabledStatus
from gui.sounds.sound_systems import getCurrentSoundSystem
from gui.sounds.sound_utils import SOUND_DEBUG
from helpers import dependency
from skeletons.gui.game_control import IGameSessionController
from skeletons.gui.shared import IItemsCache
from skeletons.gui.sounds import ISoundsController

class SoundsController(ISoundsController):
    itemsCache = dependency.descriptor(IItemsCache)
    gameSession = dependency.descriptor(IGameSessionController)

    def __init__(self):
        super(SoundsController, self).__init__()
        self.__soundSystem = getCurrentSoundSystem()
        self.__guiAmbients = GuiAmbientsCtrl(weakref.proxy(self))
        self.__eventSoundSubCtrl = EventSoundSubController()
        SOUND_DEBUG('Sound system has been created', self.__soundSystem)

    def init(self):
        self.__soundSystem.init()
        self.__guiAmbients.init()
        self.__eventSoundSubCtrl.init()

    def fini(self):
        self.__soundSystem.fini()
        self.__guiAmbients.fini()
        self.__eventSoundSubCtrl.fini()

    def start(self):
        self.__guiAmbients.start()
        self.gameSession.onPremiumNotify += self.__onPremiumChanged
        self.__setAccountAttrs()

    def stop(self, isDisconnected=False):
        self.gameSession.onPremiumNotify -= self.__onPremiumChanged
        self.__guiAmbients.stop(isDisconnected)
        if isDisconnected:
            _MC.g_musicController.unloadServerSounds(isDisconnected)

    @property
    def system(self):
        return self.__soundSystem

    def enable(self):
        if not self.isEnabled():
            SoundGroups.g_instance.setEnableStatus(EnabledStatus.ENABLED_BY_USER)

    def disable(self):
        if self.isEnabled():
            SoundGroups.g_instance.setEnableStatus(EnabledStatus.DISABLED)

    def isEnabled(self):
        return EnabledStatus.isEnabled(SoundGroups.g_instance.getEnableStatus())

    def setEnvForSpace(self, spaceID, newEnv):
        return self.__guiAmbients.setEnvForSpace(spaceID, newEnv)

    def __onPremiumChanged(self, isPremium, attrs, premiumExpiryTime):
        SOUND_DEBUG('Premium account status changed', isPremium, attrs, premiumExpiryTime)
        self.__setAccountAttrs(restartSounds=True)

    def __setAccountAttrs(self, restartSounds=False):
        SOUND_DEBUG('Set current account premium state', self.itemsCache.items.stats.isPremium, restartSounds)
        _MC.g_musicController.setAccountPremiumState(self.itemsCache.items.stats.isPremium, restart=restartSounds)