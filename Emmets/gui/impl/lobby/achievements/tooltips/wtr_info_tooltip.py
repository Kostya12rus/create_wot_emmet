# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/achievements/tooltips/wtr_info_tooltip.py
from frameworks.wulf import ViewSettings, ViewModel
from gui.impl.pub import ViewImpl
from gui.impl.gen import R

class WTRInfoTooltip(ViewImpl):

    def __init__(self):
        settings = ViewSettings(R.views.lobby.achievements.tooltips.WTRInfoTooltip(), model=ViewModel())
        super(WTRInfoTooltip, self).__init__(settings)