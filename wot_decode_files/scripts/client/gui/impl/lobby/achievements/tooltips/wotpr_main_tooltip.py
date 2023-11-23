# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/achievements/tooltips/wotpr_main_tooltip.py
from frameworks.wulf import ViewSettings, ViewModel
from gui.impl.pub import ViewImpl
from gui.impl.gen import R

class WOTPRMainTooltip(ViewImpl):

    def __init__(self):
        settings = ViewSettings(R.views.lobby.achievements.tooltips.WOTPRMainTooltip(), model=ViewModel())
        super(WOTPRMainTooltip, self).__init__(settings)