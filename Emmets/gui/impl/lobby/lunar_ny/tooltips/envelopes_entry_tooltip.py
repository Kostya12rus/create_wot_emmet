# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/lunar_ny/tooltips/envelopes_entry_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.lunar_ny.tooltips.envelopes_entry_tooltip_model import EnvelopesEntryTooltipModel
from gui.impl.pub import ViewImpl

class EnvelopesEntryTooltip(ViewImpl):
    __slots__ = ()

    def __init__(self):
        settings = ViewSettings(R.views.lobby.lunar_ny.tooltips.EnvelopesEntryTooltip())
        settings.model = EnvelopesEntryTooltipModel()
        super(EnvelopesEntryTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return self.getViewModel()