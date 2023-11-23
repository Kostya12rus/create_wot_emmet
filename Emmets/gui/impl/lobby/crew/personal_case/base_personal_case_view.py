# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/personal_case/base_personal_case_view.py
from gui.impl.pub import ViewImpl
from uilogging.crew.loggers import CrewPersonalCaseTabLogger

class BasePersonalCaseView(ViewImpl):
    __slots__ = ('uiLogger', )

    def __init__(self, settings, **kwargs):
        self.uiLogger = CrewPersonalCaseTabLogger(self, kwargs.get('parentView'), settings.layoutID, kwargs.get('parentViewKey'))
        super(BasePersonalCaseView, self).__init__(settings)

    def _onLoading(self, *args, **kwargs):
        self.uiLogger.initialize()
        super(BasePersonalCaseView, self)._onLoading(*args, **kwargs)

    def _finalize(self):
        self.uiLogger.finalize()
        super(BasePersonalCaseView, self)._finalize()