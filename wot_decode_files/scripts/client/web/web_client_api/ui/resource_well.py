# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/ui/resource_well.py
import logging
from gui.shared.event_dispatcher import showShop, showHangar
from helpers import dependency
from skeletons.gui.game_control import IResourceWellController
from web.web_client_api import w2c, W2CSchema, Field
from gui.shared import event_dispatcher as shared_events
_logger = logging.getLogger(__name__)

class _ResourceWellTabSchema(W2CSchema):
    back_to_shop = Field(required=False, type=bool, default=True)


class ResourceWellWebApiMixin(object):
    __resourceWell = dependency.descriptor(IResourceWellController)

    @w2c(_ResourceWellTabSchema, 'resource_well')
    def showResourceWell(self, cmd):
        if self.__resourceWell.isActive():
            backToShop = cmd.back_to_shop
            shared_events.showResourceWellProgressionWindow(backCallback=showShop if backToShop else showHangar)
        else:
            _logger.error('Resource Well is not active at the moment!')