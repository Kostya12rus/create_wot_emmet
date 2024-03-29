# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/dog_tag_composer.py
from dog_tags_common.config.common import ComponentViewType
from dog_tags_common.number_formatter import formatComponentValue
from dog_tags_common.player_dog_tag import DisplayableDogTag
from gui.dog_tag_composer import DogTagComposerClient
from helpers import getLanguageCode
STARTING_GRADE_OFFSET = 1

class DogTagComposerInBattle(DogTagComposerClient):

    def getModel(self, dt):
        engraving = dt.getComponentByType(ComponentViewType.ENGRAVING)
        background = dt.getComponentByType(ComponentViewType.BACKGROUND)
        isMaxLevel = engraving.grade + STARTING_GRADE_OFFSET == len(engraving.componentDefinition.grades)
        return {'background': {'componentID': background.compId, 
                          'imageStr': self.getComponentImage(background.compId, 0)}, 
           'engraving': {'componentID': engraving.compId, 
                         'imageStr': self.getComponentImage(engraving.compId, engraving.grade), 
                         'name': self.getComponentTitle(engraving.compId), 
                         'value': formatComponentValue(getLanguageCode(), engraving.value, engraving.componentDefinition.numberType)}, 
           'playerName': dt.getNickName(), 
           'clanTag': dt.getClanTag(), 
           'isEngravingMaxLevel': isMaxLevel}

    def getModelFromDict(self, dogTag):
        return self.getModel(DisplayableDogTag.fromDict(dogTag))


layoutComposer = DogTagComposerInBattle()