# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/comp7/comp7_c11n_helpers.py
import logging
from customization_quests_common import serializeToken
from gui.shared.gui_items import GUI_ITEM_TYPE
from helpers import dependency
from items.components.c11n_constants import CustomizationType
from shared_utils import first
from skeletons.gui.customization import ICustomizationService
_logger = logging.getLogger(__name__)

@dependency.replace_none_kwargs(c11nService=ICustomizationService)
def getComp7ProgressionStyleCamouflage(styleID, branch, level, c11nService=None):
    style = c11nService.getItemByID(GUI_ITEM_TYPE.STYLE, styleID)
    tokenID = serializeToken(styleID, branch)
    c11nQuestProgress = style.descriptor.questsProgression
    groupItems = c11nQuestProgress.getItemsForGroup(tokenID)
    if level >= len(groupItems):
        _logger.error('Wrong progress level [%s] for customization progress group [%s]', level, tokenID)
        return
    else:
        levelItems = groupItems[level]
        camoID = first(levelItems.get(CustomizationType.CAMOUFLAGE, ()))
        if camoID is None:
            _logger.error('Missing camouflage for level [%s] in customization progress group [%s]', level, tokenID)
            return
        return c11nService.getItemByID(GUI_ITEM_TYPE.CAMOUFLAGE, camoID)