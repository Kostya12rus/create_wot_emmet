# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/ui/frontline.py
from constants import QUEUE_TYPE
from gui.prb_control.dispatcher import g_prbLoader
from gui.prb_control.entities.base.ctx import PrbAction
from gui.prb_control.settings import PREBATTLE_ACTION_NAME
from gui.shared.event_dispatcher import showHangar
from helpers import dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController
from web.web_client_api import w2c, W2CSchema

class OpenFrontLinePagesMixin(object):
    __epicController = dependency.descriptor(IEpicBattleMetaGameController)

    @w2c(W2CSchema, 'frontline_hangar')
    def selectMode(self, _):
        result = False
        dispatcher = g_prbLoader.getDispatcher()
        if dispatcher is not None and self.__epicController.isEnabled():
            isPrbActive = dispatcher.getFunctionalState().isInPreQueue(QUEUE_TYPE.EPIC)
            if not isPrbActive:
                actionName = PREBATTLE_ACTION_NAME.EPIC
                result = yield dispatcher.doSelectAction(PrbAction(actionName))
            else:
                result = isPrbActive
            if result:
                showHangar()
        yield {'success': result}
        return