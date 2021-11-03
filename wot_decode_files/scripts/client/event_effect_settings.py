# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/event_effect_settings.py
import ResMgr

class EventEffectsSettings(object):
    EVENTS_EFFECTS_CONFIG_FILE = 'scripts/event_effects.xml'
    DYNAMIC_OBJECTS_CONFIG_FILE = 'scripts/dynamic_objects.xml'

    def __init__(self):
        section = ResMgr.openSection(self.EVENTS_EFFECTS_CONFIG_FILE + '/effects_list')
        self.eventEffectsSettings = self._effectsSettingsReader(section)
        self.dynamicObjects = ResMgr.openSection(self.DYNAMIC_OBJECTS_CONFIG_FILE)

    def _effectsSettingsReader(self, section):
        result = {}
        for name, subSection in section.items():
            result[name] = self._readEffectList(subSection)

        return result

    def _readEffectList(self, section):
        result = {}
        for name, subSection in section.items():
            result[name] = self._readEffectSettins(subSection)

        return result

    def _readEffectSettins(self, section):
        result = {}
        result['name'] = section.readString('name', '')
        result['duration'] = section.readFloat('duration', 0.0)
        return result