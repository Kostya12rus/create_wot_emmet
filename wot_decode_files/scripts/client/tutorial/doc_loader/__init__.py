# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/tutorial/doc_loader/__init__.py
import ResMgr
from tutorial import settings
from tutorial.doc_loader import gui_config
from tutorial.doc_loader.parsers import DescriptorParser, ChapterParser
from tutorial.logger import LOG_CURRENT_EXCEPTION

def loadDescriptorData(setting, exParsers=None, clearCache=False):
    try:
        if exParsers is not None:
            imported = __import__(exParsers, globals(), locals(), ['init'])
            getattr(imported, 'init')()
        if clearCache:
            ResMgr.purge(setting.descriptorPath)
        classPath = setting.descriptorParser
        parser = settings.createTutorialElement(classPath)
        return parser.parse(setting.descriptorPath)
    except Exception:
        LOG_CURRENT_EXCEPTION()
        return

    return


def loadChapterData(chapter, chapterParser, afterBattle=False, initial=False):
    if chapter is not None and not chapter.isValid():
        try:
            parser = settings.createTutorialElement(chapterParser)
            parser.parse(chapter, afterBattle=afterBattle, initial=initial)
        except Exception:
            LOG_CURRENT_EXCEPTION()
            return

    return chapter


def clearChapterData(chapter):
    ResMgr.purge(settings.GLOBAL_REFS_FILE_PATH)
    defPath = chapter.getFilePath(afterBattle=False)
    abPath = chapter.getFilePath(afterBattle=True)
    ResMgr.purge(defPath)
    if defPath != abPath:
        ResMgr.purge(abPath)
    chapter.clear()


def getQuestsDescriptor():
    setting = settings.TUTORIAL_SETTINGS.QUESTS
    if setting.enabled:
        return loadDescriptorData(setting)
    else:
        return