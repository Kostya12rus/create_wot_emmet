# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/tooltips/advanced_tooltip_view.py
import logging
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.tooltips.advanced_tooltip_view_model import AdvancedTooltipViewModel
from gui.impl.pub import ViewImpl
_logger = logging.getLogger(__name__)

class AdvancedTooltipView(ViewImpl):
    __slots__ = ('_movie', '_header', '_description')

    def __init__(self, movie, header, description):
        settings = ViewSettings(R.views.lobby.crew.tooltips.AdvancedTooltipView(), model=AdvancedTooltipViewModel())
        super(AdvancedTooltipView, self).__init__(settings)
        self._movie = movie
        self._header = header
        self._description = description

    def onError(self, args):
        errorFilePath = str(args.get('errorFilePath', ''))
        _logger.error('Reward video error: %s', errorFilePath)
        self.destroyWindow()

    @property
    def viewModel(self):
        return super(AdvancedTooltipView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(AdvancedTooltipView, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as (tx):
            tx.setMovie(self._movie)
            tx.setHeader(self._header)
            tx.setDescription(self._description)

    def _getEvents(self):
        return (
         (
          self.viewModel.onError, self.onError),)