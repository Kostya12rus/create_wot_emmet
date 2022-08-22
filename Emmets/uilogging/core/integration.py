# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/core/integration.py
import json, logging, typing
from gui.impl.gen.view_models.common.ui_logger_model import UiLoggerModel
from skeletons.gui.impl import IGuiLoader
from helpers import dependency
from skeletons.ui_logging import IUILoggingCore, IUILoggingListener
from wotdecorators import noexcept
_logger = logging.getLogger(__name__)

class UILoggingListener(IUILoggingListener):
    _core = dependency.descriptor(IUILoggingCore)
    __slots__ = ('__model', )

    def __init__(self):
        super(UILoggingListener, self).__init__()
        guiLoader = dependency.instance(IGuiLoader)
        self.__model = typing.cast(UiLoggerModel, guiLoader.uiLogger.getModel())
        self.__model.log += self._log

    def fini(self):
        if self.__model is not None:
            self.__model.log -= self._log
            _logger.debug('UIGFLoggingListener unsubscribed from model.')
        self.__model = None
        _logger.debug('UIGFLoggingListener destroyed.')
        return

    @noexcept
    def _log(self, args):
        self._core.log(feature=args['feature'], group=args['group'], action=args['action'], loglevel=args['logLevel'], **json.loads(args['params']))