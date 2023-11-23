# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/shop/base_loggers.py
import abc, logging
from uilogging.base.logger import FlowLogger, MetricsLogger
from uilogging.shop.logging_constants import FEATURE
_logger = logging.getLogger(__name__)

class ShopPreviewFlowLogger(FlowLogger):
    __metaclass__ = abc.ABCMeta
    __slots__ = ()

    def __init__(self):
        super(ShopPreviewFlowLogger, self).__init__(FEATURE)

    @abc.abstractmethod
    def logOpenPreview(self):
        pass


class ShopPreviewMetricsLogger(MetricsLogger):
    __metaclass__ = abc.ABCMeta
    __slots__ = ()

    def __init__(self):
        super(ShopPreviewMetricsLogger, self).__init__(FEATURE)

    @abc.abstractmethod
    def onViewOpen(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def onViewClosed(self, *args, **kwargs):
        pass

    def logOpenPurchaseConfirmation(self):
        _logger.warning('[SHOPUILOG] %s not implemented logOpenPurchaseConfirmation.', self.__class__.__name__)

    def logBundlePurchased(self):
        _logger.warning('[SHOPUILOG] %s not implemented logBundlePurchased.', self.__class__.__name__)

    def logPurchaseConfirmationClosed(self):
        _logger.warning('[SHOPUILOG] %s not implemented logPurchaseConfirmationClosed.', self.__class__.__name__)