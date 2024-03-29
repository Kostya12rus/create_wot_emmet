# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/items/components/skills_constants.py
SKILL_NAMES = ('reserved', 'commander', 'radioman', 'driver', 'gunner', 'loader', 'repair',
               'fireFighting', 'camouflage', 'brotherhood', 'any', 'reserved', 'reserved',
               'reserved', 'reserved', 'reserved', 'commander_tutor', 'commander_eagleEye',
               'commander_sixthSense', 'commander_expert', 'commander_universalist',
               'commander_enemyShotPredictor', 'reserved', 'reserved', 'reserved',
               'reserved', 'reserved', 'reserved', 'driver_virtuoso', 'driver_smoothDriving',
               'driver_badRoadsKing', 'driver_rammingMaster', 'driver_tidyPerson',
               'reserved', 'reserved', 'reserved', 'reserved', 'gunner_gunsmith',
               'gunner_sniper', 'gunner_smoothTurret', 'gunner_rancorous', 'reserved',
               'reserved', 'reserved', 'reserved', 'reserved', 'loader_pedant', 'loader_desperado',
               'loader_intuition', 'reserved', 'reserved', 'reserved', 'reserved',
               'radioman_inventor', 'radioman_finder', 'radioman_retransmitter',
               'radioman_lastEffort', 'reserved', 'reserved', 'reserved', 'reserved')
SKILL_INDICES = dict((x[1], x[0]) for x in enumerate(SKILL_NAMES) if not x[1].startswith('reserved'))
ORDERED_ROLES = ('commander', 'gunner', 'driver', 'radioman', 'loader')
ROLES = frozenset(('commander', 'radioman', 'driver', 'gunner', 'loader'))
ROLE_LIMITS = {'commander': 1, 'driver': 1}
COMMON_SKILLS = frozenset(('repair', 'camouflage', 'brotherhood', 'fireFighting'))
SEPARATE_SKILLS = frozenset(('radioman_lastEffort', ))
ROLES_AND_COMMON_SKILLS = ROLES | COMMON_SKILLS
COMMANDER_SKILLS = frozenset(('commander_tutor', 'commander_expert', 'commander_universalist',
                              'commander_sixthSense', 'commander_eagleEye', 'commander_enemyShotPredictor'))
SKILLS_BY_ROLES = {'commander': COMMON_SKILLS.union(COMMANDER_SKILLS), 
   'driver': COMMON_SKILLS.union(('driver_tidyPerson', 'driver_smoothDriving', 'driver_virtuoso',
                     'driver_badRoadsKing', 'driver_rammingMaster')), 
   'gunner': COMMON_SKILLS.union(('gunner_smoothTurret', 'gunner_sniper', 'gunner_rancorous', 'gunner_gunsmith')), 
   'loader': COMMON_SKILLS.union(('loader_pedant', 'loader_desperado', 'loader_intuition')), 
   'radioman': COMMON_SKILLS.union(('radioman_finder', 'radioman_inventor', 'radioman_lastEffort',
                     'radioman_retransmitter'))}
ROLES_BY_SKILLS = {}
for role, skills in SKILLS_BY_ROLES.iteritems():
    for skill in skills:
        ROLES_BY_SKILLS.setdefault(skill, set()).add(role)

ACTIVE_SKILLS = SKILLS_BY_ROLES['commander'] | SKILLS_BY_ROLES['radioman'] | SKILLS_BY_ROLES['driver'] | SKILLS_BY_ROLES['gunner'] | SKILLS_BY_ROLES['loader']
ACTIVE_FREE_SKILLS = ACTIVE_SKILLS | {'any'}
UNLEARNABLE_SKILLS = ('commander_sixthSense', )
LEARNABLE_ACTIVE_SKILLS = ACTIVE_SKILLS.difference(UNLEARNABLE_SKILLS)

class ParamMeasureType(object):
    PERCENTS = 'percents'
    SECONDS = 'seconds'
    PERCENT_GAP = 'percentGap'
    MPH = 'mph'
    METERS = 'meters'


class ParamSignType(object):
    PLUS = 'plus'
    MINUS = 'minus'
    SIGN_LESS = 'signLess'


class SkillTypeName(object):
    MAIN = 'main'
    SITUATIONAL = 'situational'
    COMMON = 'common'
    COMMANDER_SPECIAL = 'commanderSpecial'