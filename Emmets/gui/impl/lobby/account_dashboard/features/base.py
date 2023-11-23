# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/account_dashboard/features/base.py
import typing
if typing.TYPE_CHECKING:
    from typing import Union
    from gui.impl.gen.view_models.views.lobby.account_dashboard.account_dashboard_model import AccountDashboardModel

class FeatureItem(object):

    def __init__(self, viewModel):
        self._viewModel = viewModel

    def initialize(self, *args, **kwargs):
        pass

    def finalize(self):
        self._viewModel = None
        return

    def createToolTipContent(self, event, contentID):
        pass

    def createPopOverContent(self, event):
        pass

    def _fillModel(self, model):
        raise NotImplementedError

    def fill(self, ctx=None):
        if ctx is None:
            with self._viewModel.transaction() as (tx):
                self._fillModel(tx)
        else:
            self._fillModel(ctx)
        return

    def getViewModel(self):
        return self._viewModel