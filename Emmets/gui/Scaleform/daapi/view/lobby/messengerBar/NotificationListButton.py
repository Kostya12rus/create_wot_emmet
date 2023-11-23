# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/messengerBar/NotificationListButton.py
from gui.Scaleform.daapi.view.meta.NotificationListButtonMeta import NotificationListButtonMeta
from notification import NotificationMVC
from gui.shared.formatters import text_styles

class NotificationListButton(NotificationListButtonMeta):

    def __init__(self):
        super(NotificationListButton, self).__init__()
        NotificationMVC.g_instance.getModel().onNotifiedMessagesCountChanged += self.__notifiedMessagesCountChangeHandler

    def _populate(self):
        super(NotificationListButton, self)._populate()
        self.__setState(NotificationMVC.g_instance.getModel().getNotifiedMessagesCount())

    def handleClick(self):
        NotificationMVC.g_instance.getModel().setListDisplayState()

    def _dispose(self):
        model = NotificationMVC.g_instance.getModel()
        if model:
            model.onNotifiedMessagesCountChanged -= self.__notifiedMessagesCountChangeHandler
        super(NotificationListButton, self)._dispose()

    def __notifiedMessagesCountChangeHandler(self, notifyMessagesCount):
        self.__setState(notifyMessagesCount)

    def __setState(self, count):
        counterValue = ''
        if count > 0:
            counterValue = text_styles.counterLabelText(str(count))
        self.as_setStateS(count > 0, counterValue)