# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/bootcamp_dialogs_meta.py
from constants import PREMIUM_ENTITLEMENTS
from gui.impl import backport
from gui.impl.gen import R
from gui.Scaleform.daapi.view.dialogs import I18nConfirmDialogMeta
from gui.shared.events import ShowDialogEvent
_MSG_POSTFIX = '/message'
_DEFAULT_PREMIUM_STR = R.strings.dialogs.bootcamp.premiumType.plus()

class ExecutionChooserDialogMeta(I18nConfirmDialogMeta):
    SKIP = 'skip'
    SKIP_REFERRAL = 'skip/referral'
    RETRY = 'retry'
    START = 'start'

    def __init__(self, dialogType, key, focusedID, showAwardIcon, premiumType):
        super(ExecutionChooserDialogMeta, self).__init__(key, focusedID=focusedID)
        self.__showAwardIcon = showAwardIcon
        self.__premiumType = premiumType
        self.__imagePath = self.__createImagePathWithTankPremium(dialogType)

    def getEventType(self):
        return ShowDialogEvent.SHOW_EXECUTION_CHOOSER_DIALOG

    def getImagePath(self):
        return self.__imagePath

    def getShowAwardIcon(self):
        return self.__showAwardIcon

    def getAwardingText(self):
        return backport.text(R.strings.bootcamp.message.restart.reward(), **self._messageCtx)

    def getLabel(self):
        I18N_LABEL_KEY = '{0:>s}/label'
        return self._makeString(I18N_LABEL_KEY.format(self._key), self._messageCtx)

    def getMessage(self):
        if self.__premiumType == PREMIUM_ENTITLEMENTS.BASIC:
            premiumStr = backport.text(R.strings.dialogs.bootcamp.premiumType.basic())
        elif self.__premiumType == PREMIUM_ENTITLEMENTS.PLUS:
            premiumStr = backport.text(R.strings.dialogs.bootcamp.premiumType.plus())
        else:
            premiumStr = backport.text(_DEFAULT_PREMIUM_STR)
        premiumCtx = {'premiumType': premiumStr}
        return self._makeString(('').join((self._key, _MSG_POSTFIX)), premiumCtx)

    def __createImagePathWithTankPremium(self, dialogType):
        if dialogType == self.SKIP and self.__premiumType == PREMIUM_ENTITLEMENTS.PLUS:
            return backport.image(R.images.gui.maps.icons.bootcamp.dialog.skip_with_tank_premium())
        return backport.image(R.images.gui.maps.icons.bootcamp.dialog.dyn(dialogType)())