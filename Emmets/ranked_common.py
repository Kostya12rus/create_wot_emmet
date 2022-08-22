# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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