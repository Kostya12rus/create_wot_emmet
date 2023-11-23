# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/formatters/servers.py
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import icons
from gui.shared.formatters import text_styles
from predefined_hosts import HOST_AVAILABILITY, PING_STATUSES
_UNAVAILABLE_DATA_PLACEHOLDER = '--'

def formatPingStatus(csisStatus, isColorBlind, isSelected, pingStatus, pingValue, useBigSize=False):
    if pingStatus == PING_STATUSES.REQUESTED:
        return None
    else:
        if csisStatus != HOST_AVAILABILITY.NOT_AVAILABLE and pingStatus != PING_STATUSES.UNDEFINED:
            if pingStatus == PING_STATUSES.LOW:
                formattedPing = text_styles.goodPing(pingValue)
            else:
                formattedPing = text_styles.main(pingValue) if isSelected else text_styles.standartPing(pingValue)
        else:
            pingValue = _UNAVAILABLE_DATA_PLACEHOLDER
            pingStatus = PING_STATUSES.UNDEFINED
            formattedPing = text_styles.standartPing(pingValue)
        colorBlindName = ''
        if isColorBlind and pingStatus == PING_STATUSES.HIGH:
            colorBlindName = '_color_blind'
        pingStatusIcon = makePingStatusIcon(pingStatus, colorBlindName)
        if useBigSize:
            return text_styles.concatStylesToSingleLine(text_styles.main(' '), formattedPing, pingStatusIcon)
        return text_styles.concatStylesToSingleLine(formattedPing, '', pingStatusIcon)


def makePingStatusIcon(pingStatus, colorBlindName=''):
    icon = backport.image(R.images.gui.maps.icons.pingStatus.dyn(('stairs_indicator_{}{}').format(pingStatus, colorBlindName), R.invalid)())
    return icons.makeImageTag(icon, 14, 14, -3)