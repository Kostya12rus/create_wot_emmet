# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/personal_reserves/personal_reserves_widget_inject.py
import logging
from gui.Scaleform.daapi.view.meta.PersonalReservesWidgetInjectMeta import PersonalReservesWidgetInjectMeta
from gui.impl.lobby.personal_reserves.personal_reserves_widget import PersonalReservesWidget
_logger = logging.getLogger(__name__)

class PersonalReservesWidgetInject(PersonalReservesWidgetInjectMeta):
    WIDGET_WIDTH_SMALL = 58
    WIDGET_ITEM_WIDTH = 40

    def _onPopulate(self):
        super(PersonalReservesWidgetInject, self)._onPopulate()
        if self._injectView:
            self._injectView.onUpdate += self._updateSize
        else:
            _logger.warning("Couldn't perform the event subscription, the injected view is None")
        self._updateSize()

    def _dispose(self):
        if self._injectView:
            self._injectView.onUpdate -= self._updateSize
        super(PersonalReservesWidgetInject, self)._dispose()

    def _makeInjectView(self, *args):
        return PersonalReservesWidget()

    def _updateSize(self):
        activeBoosterCount = self._injectView.activeBoostersCount
        targetWidth = max(self.WIDGET_ITEM_WIDTH * activeBoosterCount, self.WIDGET_WIDTH_SMALL)
        self.as_setTargetWidthS(targetWidth)