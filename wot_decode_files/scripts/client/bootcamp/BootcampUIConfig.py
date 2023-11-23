# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/bootcamp/BootcampUIConfig.py
from copy import copy
import ResMgr
from soft_exception import SoftException
g_defaultBattleRibbonsSettings = {'damage': False, 
   'kill': False, 
   'armor': False, 
   'ram': False, 
   'spotted': False, 
   'capture': False, 
   'crits': False}
XML_CONFIG_PATH = 'scripts/bootcamp_docs/battle_page_visibility.xml'

def readUISettingsFile(path):
    settingsConfig = ResMgr.openSection(path)
    if settingsConfig is None:
        raise SoftException("Can't open config file (%s)" % path)
    allPrebattleSettings = {}
    allRibbonsSettings = {}
    for name, section in settingsConfig.items():
        if name == 'lesson':
            lessonId = section['id'].asInt
            ribbonsSettings = copy(g_defaultBattleRibbonsSettings)
            ribString = section['ribbons'].asString
            ribbonNames = ribString.split()
            for ribName in ribbonNames:
                if ribName in ribbonsSettings:
                    ribbonsSettings[ribName] = True

            allRibbonsSettings[lessonId] = ribbonsSettings
            prebattleSettings = {}
            prebattleSection = section['prebattle']
            if prebattleSection.has_key('timeout'):
                prebattleSettings['timeout'] = prebattleSection['timeout'].asFloat
            allPrebattleSettings[lessonId] = prebattleSettings

    return (
     allPrebattleSettings, allRibbonsSettings)


g_prebattleSettings, g_battleRibbonsSettings = readUISettingsFile(XML_CONFIG_PATH)

def getBattleRibbonsSettings(lessonId):
    return g_battleRibbonsSettings[lessonId]


def getPrebattleSettings(lessonId):
    return g_prebattleSettings[lessonId]