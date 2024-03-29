# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_control/IGR.py
import Event, constants
from PlayerEvents import g_playerEvents
from skeletons.gui.game_control import IIGRController

class IGRController(IIGRController):

    def __init__(self):
        super(IGRController, self).__init__()
        self.__xpFactor = 1.0
        self.__roomType = constants.IGR_TYPE.NONE
        self.onIgrTypeChanged = Event.Event()

    def init(self):
        g_playerEvents.onIGRTypeChanged += self.__onIGRTypeChanged

    def fini(self):
        g_playerEvents.onIGRTypeChanged -= self.__onIGRTypeChanged
        self.onIgrTypeChanged.clear()
        super(IGRController, self).fini()

    def onLobbyStarted(self, ctx=None):
        data = (ctx or {}).get('igrData', {})
        self.__roomType = data.get('roomType', constants.IGR_TYPE.NONE)
        self.__xpFactor = data.get('igrXPFactor', 1.0)
        self.onIgrTypeChanged(self.__roomType, self.__xpFactor)

    def onDisconnected(self):
        self.__xpFactor = 1.0
        self.__roomType = constants.IGR_TYPE.NONE

    def getXPFactor(self):
        return self.__xpFactor

    def getRoomType(self):
        return self.__roomType

    def __onIGRTypeChanged(self, roomType, xpFactor):
        if roomType is not None:
            self.__roomType = roomType
        if xpFactor is not None:
            self.__xpFactor = xpFactor
        self.onIgrTypeChanged(self.__roomType, self.__xpFactor)
        return