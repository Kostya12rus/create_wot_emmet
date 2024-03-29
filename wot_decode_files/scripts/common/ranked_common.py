# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/ranked_common.py
import season_common

def getShieldsConfig(rankedConfig, now):
    result = {}
    res, seasonInfo = season_common.getSeason(rankedConfig, now)
    if not res:
        return result
    _, _, seasonID, cycleID = seasonInfo
    season = rankedConfig['seasons'].get(seasonID)
    if season:
        cycle = season['cycles'].get(cycleID, {})
        result.update(cycle.get('shields', rankedConfig['shields']))
    return result


class SwitchState(object):
    ENABLED = 'enabled'
    DISABLED = 'disabled'
    HIDDEN = 'hidden'
    ALL = ('enabled', 'disabled', 'hidden')