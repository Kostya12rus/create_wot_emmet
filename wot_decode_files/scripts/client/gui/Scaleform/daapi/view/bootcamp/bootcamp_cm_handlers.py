# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/bootcamp_cm_handlers.py
from gui.Scaleform.daapi.view.lobby.techtree.research_cm_handlers import ResearchVehicleContextMenuHandler
from gui.Scaleform.daapi.view.lobby.techtree.research_cm_handlers import ResearchItemContextMenuHandler
from gui.Scaleform.daapi.view.lobby.hangar.hangar_cm_handlers import VehicleContextMenuHandler
from gui.Scaleform.daapi.view.lobby.hangar.hangar_cm_handlers import CrewContextMenuHandler, CREW
from gui.Scaleform.daapi.view.lobby.hangar.hangar_cm_handlers import TechnicalMaintenanceCMHandler

def _disableContextMenuItem(item):
    if item['initData'] is None:
        item['initData'] = {}
    item['initData'].update({'enabled': False})
    return


def _disableAllContextMenuItems(options, exceptions=()):
    for item in options:
        if item['id'] not in exceptions:
            _disableContextMenuItem(item)


class BCResearchVehicleContextMenuHandler(ResearchVehicleContextMenuHandler):

    def _generateOptions(self, ctx=None):
        options = super(BCResearchVehicleContextMenuHandler, self)._generateOptions(ctx)
        _disableAllContextMenuItems(options)
        return options


class BCResearchItemContextMenuHandler(ResearchItemContextMenuHandler):

    def _generateOptions(self, ctx=None):
        options = super(BCResearchItemContextMenuHandler, self)._generateOptions(ctx)
        _disableAllContextMenuItems(options)
        return options


class BCVehicleContextMenuHandler(VehicleContextMenuHandler):

    def _generateOptions(self, ctx=None):
        options = super(BCVehicleContextMenuHandler, self)._generateOptions(ctx)
        _disableAllContextMenuItems(options)
        return options


class BCCrewContextMenuHandler(CrewContextMenuHandler):

    def _generateOptions(self, ctx=None):
        options = super(BCCrewContextMenuHandler, self)._generateOptions(ctx)
        _disableAllContextMenuItems(options, exceptions=(
         CREW.PERSONAL_CASE,))
        return options


class BCTechnicalMaintenanceCMHandler(TechnicalMaintenanceCMHandler):

    def _generateOptions(self, ctx=None):
        options = super(BCTechnicalMaintenanceCMHandler, self)._generateOptions(ctx)
        _disableAllContextMenuItems(options)
        return options