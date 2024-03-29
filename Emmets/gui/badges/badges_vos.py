# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/badges/badges_vos.py
from gui.impl import backport
from gui.impl.gen.resources import R
from gui.shared.formatters import text_styles, icons
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.Scaleform.settings import ICONS_SIZES
_UNIQUE_SUFFIX_BADGE_TOOLTIPS = {'ranked_2020_leader_suffix': TOOLTIPS_CONSTANTS.BADGES_SUFFIX_RANKED_ITEM}

def getSuffixBadgeTooltip(badge):
    if badge.isSuffixLayout():
        return _UNIQUE_SUFFIX_BADGE_TOOLTIPS.get(badge.getName(), TOOLTIPS_CONSTANTS.BADGES_SUFFIX_ITEM)
    return ''


def makeBadgeVO(badge):
    return {'id': badge.badgeID, 
       'title': text_styles.stats(badge.getUserName()), 
       'description': text_styles.main(badge.getUserDescription()), 
       'enabled': badge.isAchieved, 
       'selected': badge.isSelected, 
       'highlightIcon': badge.getHighlightIcon(), 
       'isFirstLook': badge.isNew(), 
       'visual': badge.getBadgeVO(ICONS_SIZES.X80)}


def makeSuffixBadgeVO(badge):
    stripImg = R.images.gui.maps.icons.library.badges.strips.c_68x28.dyn(('strip_{}').format(badge.badgeID))
    labelDyn = R.strings.badge.suffix.dyn(('badge_{}').format(badge.badgeID))
    labelText = text_styles.main(backport.text(labelDyn())) if labelDyn else ''
    activeLabelText = text_styles.stats(backport.text(labelDyn())) if labelDyn else ''
    return {'id': badge.badgeID, 
       'label': text_styles.concatStylesToSingleLine(labelText, icons.starYellow(0)) if badge.isTemporary else labelText, 
       'activeLabel': text_styles.concatStylesToSingleLine(activeLabelText, icons.starYellow(0)) if badge.isTemporary else activeLabelText, 
       'tooltip': getSuffixBadgeTooltip(badge), 
       'stripImg': backport.image(stripImg()) if stripImg else '', 
       'img': badge.getSuffixSmallIcon(), 
       'hasFootnoteMark': badge.isTemporary}