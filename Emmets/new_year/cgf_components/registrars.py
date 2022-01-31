# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/new_year/cgf_components/registrars.py
from cgf_script.managers_registrator import registerManager, Rule
from new_year.cgf_components.other_entity_manager import OtherEntityManager

class OtherEntityCreatorRule(Rule):
    category = 'Hangar rules'

    @registerManager(OtherEntityManager)
    def reg1(self):
        return