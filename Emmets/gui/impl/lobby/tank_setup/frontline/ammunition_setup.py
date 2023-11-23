# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/frontline/ammunition_setup.py
from gui.impl.lobby.tank_setup.ammunition_setup.hangar import HangarAmmunitionSetupView
from gui.impl.gen import R

class FrontlineAmmunitionSetupView(HangarAmmunitionSetupView):

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.frontline.lobby.tooltips.SkillOrderTooltip():
            from frontline.gui.impl.lobby.tooltips.skill_order_tooltip import SkillOrderTooltip
            return SkillOrderTooltip()
        if contentID == R.views.frontline.lobby.tooltips.LevelReservesTooltip():
            from frontline.gui.impl.lobby.tooltips.level_reserves_tooltip import LevelReservesTooltip
            return LevelReservesTooltip()
        if contentID == R.views.frontline.lobby.tooltips.NotEnoughPointsTooltip():
            from frontline.gui.impl.lobby.tooltips.not_enough_points_tooltip import NotEnoughPointsTooltip
            return NotEnoughPointsTooltip(event.getArgument('points'))
        return super(FrontlineAmmunitionSetupView, self).createToolTipContent(event, contentID)