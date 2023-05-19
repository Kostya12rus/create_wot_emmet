# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/tutorial/doc_loader/parsers/bootcamp_lobby.py
import ResMgr
from tutorial.doc_loader.parsers import DescriptorParser, ChapterParser
from tutorial.data.bootcamp.chapter import BootcampLobbyChapter
from items import _xml

class BootcampLobbyDescriptorParser(DescriptorParser):

    def _parseChapter(self, bonuses, descriptor, subSection, xmlCtx):
        sharedTriggers = subSection.readString('shared-triggers')
        sharedVars = subSection.readString('shared-vars')
        descriptor.addChapter(BootcampLobbyChapter(sharedTriggers, sharedVars, *self._getCommonChapterValues(bonuses, subSection, xmlCtx)))


class BootcampLobbyChapterParser(ChapterParser):

    def parse(self, chapter, initial=False):
        chapter = super(BootcampLobbyChapterParser, self).parse(chapter, initial)
        self.__parseSharedTriggers(chapter)
        self.__parseSharedVars(chapter)
        return chapter

    def __parseSharedTriggers(self, chapter):
        filePath = chapter.getSharedTriggersPath()
        if not filePath:
            return
        else:
            section = ResMgr.openSection(filePath)
            if section is None:
                _xml.raiseWrongXml(None, filePath, 'can not open or read')
            self._parseTriggers((None, filePath), section, [], chapter)
            return

    def __parseSharedVars(self, chapter):
        filePath = chapter.getSharedVarsPath()
        if not filePath:
            return
        else:
            section = ResMgr.openSection(filePath)
            if section is None:
                _xml.raiseWrongXml(None, filePath, 'cannot open or read')
            self._parseVars((None, filePath), section, [], chapter)
            return