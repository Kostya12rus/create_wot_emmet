# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/items/customization_slot_tags_validator.py
import logging
from items.components import c11n_constants
_logger = logging.getLogger(__name__)

def customizationSlotTagsValidator(tag):
    availableTags = c11n_constants.ProjectionDecalDirectionTags.ALL + c11n_constants.ProjectionDecalFormTags.ALL + c11n_constants.ProjectionDecalPreferredTags.ALL + c11n_constants.ProjectionDecalMatchingTags.ALL
    return tag in availableTags


def getDirectionAndFormFactorTags(slotParams):
    directionTag = None
    formfactorTag = None
    for tag in slotParams.tags:
        if tag in (
         c11n_constants.ProjectionDecalDirectionTags.FRONT,
         c11n_constants.ProjectionDecalDirectionTags.LEFT,
         c11n_constants.ProjectionDecalDirectionTags.RIGHT) and directionTag is None:
            directionTag = tag
        if tag in c11n_constants.ProjectionDecalFormTags.ALL and formfactorTag is None:
            formfactorTag = tag

    if formfactorTag is None:
        _logger.error("There is tags mismatch, formfactorTag wasn't found!!!")
        return
    else:
        return (
         directionTag, formfactorTag)