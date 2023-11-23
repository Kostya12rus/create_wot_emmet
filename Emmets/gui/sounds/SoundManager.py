# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/sounds/SoundManager.py
import logging
from debug_utils import LOG_ERROR, LOG_CURRENT_EXCEPTION
from gui.Scaleform.framework.entities.abstract.SoundManagerMeta import SoundManagerMeta
from gui.doc_loaders.GuiSoundsLoader import GuiSoundsLoader
import SoundGroups
_logger = logging.getLogger(__name__)

class SoundManager(SoundManagerMeta):

    def __init__(self):
        super(SoundManager, self).__init__()
        self.sounds = GuiSoundsLoader()

    def _populate(self):
        super(SoundManager, self)._populate()
        try:
            self.sounds.load()
        except Exception:
            LOG_ERROR('There is error while loading sounds xml data')
            LOG_CURRENT_EXCEPTION()

    def soundEventHandler(self, soundsTypeSection, state, eventType, eventID):
        self.playControlSound(state, eventType, eventID)

    def playControlSound(self, state, eventType, eventID):
        sound = self.sounds.getControlSound(eventType, state, eventID)
        if sound is not None:
            SoundGroups.g_instance.playSound2D(sound)
        return

    def playEffectSound(self, effectName):
        sound = self.sounds.getEffectSound(effectName)
        if sound is not None:
            SoundGroups.g_instance.playSound2D(sound)
        else:
            _logger.warning('Sound effect "%s" not found', effectName)
        return