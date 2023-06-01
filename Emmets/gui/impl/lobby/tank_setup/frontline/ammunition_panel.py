# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/frontline/ammunition_panel.py
from gui.impl.gen import R
from gui.impl.lobby.tank_setup.ammunition_panel.hangar_view import HangarAmmunitionPanelView

class FrontlineAmmunitionPanelView(HangarAmmunitionPanelView):

    def createToolTipContent(self, event, contentID):
        if event.contentID == R.views.frontline.lobby.tooltips.SkillOrderTooltip():
            from frontline.gui.impl.lobby.tooltips.skill_order_tooltip import SkillOrderTooltip
            return SkillOrderTooltip()
        return super(FrontlineAmmunitionPanelView, self).createToolTipContent(event, contentID)