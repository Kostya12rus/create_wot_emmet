# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/gui/Scaleform/view/lobby/FAQWindow.py
from gui.shared.events import OpenLinkEvent
from messenger.gui.Scaleform.data.faq_data import FAQList
from messenger.gui.Scaleform.meta.FAQWindowMeta import FAQWindowMeta
from messenger import g_settings
FAQ_BATCH_SIZE = 5

class FAQWindow(FAQWindowMeta):

    def __init__(self, ctx=None):
        super(FAQWindow, self).__init__()
        self.__list = None
        return

    def onWindowClose(self):
        self.destroy()

    def onLinkClicked(self, eventType):
        self.fireEvent(OpenLinkEvent(eventType))

    def updateData(self):
        formatHtml = g_settings.htmlTemplates.format
        batch = []
        item = self.__list.getItem(0)
        if item.question and item.answer:
            batch = [
             formatHtml('firstFAQItem', ctx=item._asdict())]
        for item in self.__list.getIterator(offset=1):
            if FAQ_BATCH_SIZE > len(batch):
                self.as_appendTextS(('').join(batch))
                batch = []
            batch.append(formatHtml('nextFAQItem', ctx=item._asdict()))

        if batch:
            self.as_appendTextS(('').join(batch))

    def _populate(self):
        super(FAQWindow, self)._populate()
        self.__list = FAQList()
        self.updateData()

    def _dispose(self):
        if self.__list:
            self.__list.clear()
            self.__list = None
        super(FAQWindow, self)._dispose()
        return