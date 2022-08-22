# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/premacc/dashboard/prem_dashboard_header_clan_info_model.py
from frameworks.wulf import ViewModel

class PremDashboardHeaderClanInfoModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(PremDashboardHeaderClanInfoModel, self).__init__(properties=properties, commands=commands)

    def getClanAbbrev(self):
        return self._getString(0)

    def setClanAbbrev(self, value):
        self._setString(0, value)

    def getRoleInClan(self):
        return self._getString(1)

    def setRoleInClan(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(PremDashboardHeaderClanInfoModel, self)._initialize()
        self._addStringProperty('clanAbbrev', '')
        self._addStringProperty('roleInClan', '')