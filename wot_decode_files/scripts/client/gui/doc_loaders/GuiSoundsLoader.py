# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/doc_loaders/GuiSoundsLoader.py
import ResMgr
from debug_utils import LOG_WARNING
from items import _xml
from gui import doc_loaders
import WWISE

class GuiSoundsLoader(object):
    XML_PATH = 'gui/gui_sounds.xml'
    CONTROLS = 'controls'
    CONTROLS_DEFAULT = 'default'
    CONTROLS_SCHEMAS = 'schemas'
    CONTROLS_OVERRIDES = 'overrides'
    SCHEMA_SOUNDS = 'sounds'
    SCHEMA_GROUPS = 'groups'
    EFFECTS = 'effects'

    def __init__(self):
        self.__schemas = {}
        self.__groups = {}
        self.__overrides = {}
        self.__default = {}
        self.__effects = {}

    def __readControlsSounds(self, xmlCtx):
        controlsSection = _xml.getSubsection(xmlCtx, xmlCtx, self.CONTROLS)
        self.__default = doc_loaders.readDict(xmlCtx, controlsSection, self.CONTROLS_DEFAULT)
        controlsOverridesSection = _xml.getSubsection(xmlCtx, controlsSection, self.CONTROLS_OVERRIDES)
        for name in controlsOverridesSection.keys():
            self.__overrides[name] = doc_loaders.readDict(xmlCtx, controlsOverridesSection, name)

        for schemaName, schemaSection in _xml.getChildren(xmlCtx, controlsSection, self.CONTROLS_SCHEMAS):
            self.__schemas[schemaName] = doc_loaders.readDict(xmlCtx, schemaSection, self.SCHEMA_SOUNDS)
            for groupName in _xml.getSubsection(xmlCtx, schemaSection, self.SCHEMA_GROUPS).asString.split():
                if groupName in self.__groups:
                    LOG_WARNING('Group has already been read. Will be overriden', groupName, schemaName)
                self.__groups[groupName] = schemaName

    def __readEffectsSounds(self, xmlCtx):
        self.__effects = doc_loaders.readDict(xmlCtx, xmlCtx, self.EFFECTS)

    def load(self):
        xmlCtx = ResMgr.openSection(self.XML_PATH)
        if xmlCtx is None:
            _xml.raiseWrongXml(None, self.XML_PATH, 'can not open or read')
        self.__readControlsSounds(xmlCtx)
        self.__readEffectsSounds(xmlCtx)
        _xml.clearCaches()
        ResMgr.purge(self.XML_PATH, True)
        return

    def getControlSound(self, controlType, state, controlID=None):
        if WWISE.enabled:
            state = 'ww' + state
        if controlID is not None and controlID in self.__overrides:
            return self.__overrides[controlID].get(state)
        else:
            if controlType in self.__groups:
                schemaName = self.__groups[controlType]
                return self.__schemas.get(schemaName, {}).get(state)
            if controlType in self.__schemas:
                return self.__schemas[controlType].get(state)
            return self.__default.get(state)

    def getEffectSound(self, effectName):
        return self.__effects.get(effectName)