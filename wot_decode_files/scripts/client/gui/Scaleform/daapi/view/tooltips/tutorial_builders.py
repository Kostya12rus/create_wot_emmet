# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/tooltips/tutorial_builders.py
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts
from gui.shared.tooltips import tutorial
from gui.shared.tooltips.builders import DataBuilder
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     DataBuilder(TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_CUSTOMIZATION_TYPES, TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_CUSTOMIZATION_TYPES_UI, tutorial.CustomizationTypesPacker(contexts.HangarTutorialContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_PERSONAL_CASE_SKILLS, TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_PERSONAL_CASE_SKILLS_UI, tutorial.PersonalCaseSkillsPacker(contexts.HangarTutorialContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_PERSONAL_CASE_FREE_SKILLS, TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_PERSONAL_CASE_FREE_SKILLS_UI, tutorial.PersonalCaseFreeSkillsPacker(contexts.HangarTutorialContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_PERSONAL_CASE_PERKS, TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_PERSONAL_CASE_PERKS_UI, tutorial.PersonalCasePerksPacker(contexts.HangarTutorialContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_PERSONAL_CASE_ADDITIONAL, TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_PERSONAL_CASE_ADDITIONAL_UI, tutorial.PersonalCaseAdditionalPacker(contexts.HangarTutorialContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_AMMUNITION, TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_AMMUNITION_UI, tutorial.AmmunitionPacker(contexts.HangarTutorialContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_EQUPMENT, TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_EQUPMENT_UI, tutorial.EquipmentPacker(contexts.HangarTutorialContext())))