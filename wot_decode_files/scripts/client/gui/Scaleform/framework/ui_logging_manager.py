# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/framework/ui_logging_manager.py
from gui.Scaleform.framework.entities.abstract.UILoggerManagerMeta import UILoggerManagerMeta
from gui.shared.utils import flashObject2Dict
from helpers import dependency
from skeletons.ui_logging import IUILoggingCore
from wotdecorators import noexcept

class UILoggerManager(UILoggerManagerMeta):
    _logger = dependency.descriptor(IUILoggingCore)

    @noexcept
    def onLog(self, feature, group, action, logLevel, params):
        self._logger.log(feature, group, action, logLevel, **flashObject2Dict(params))