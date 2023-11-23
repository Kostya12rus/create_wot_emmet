# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/tutorial/stubs.py
from skeletons.tutorial import ITutorialLoader, IGuiController

class StubGuiController(IGuiController):

    @property
    def lastHangarMenuButtonsOverride(self):
        return

    @property
    def lastHeaderMenuButtonsOverride(self):
        return

    @property
    def hangarHeaderEnabled(self):
        return False

    @property
    def lastBattleSelectorHintOverride(self):
        return

    def getViewTutorialID(self, _):
        return

    def init(self, guiProviders):
        pass

    def setup(self, isEnabled=False, path=''):
        pass

    def fini(self):
        pass

    def setHintsWithClientTriggers(self, clientTriggers):
        pass

    def getFoundComponentsIDs(self):
        return []

    def setCriteria(self, name, value):
        pass

    def setViewCriteria(self, componentID, viewUniqueName):
        pass

    def setTriggers(self, componentID, triggers):
        pass

    def clearTriggers(self, componentID):
        pass

    def showInteractiveHint(self, componentID, content, triggers=None, silent=False):
        pass

    def closeInteractiveHint(self, componentID):
        pass

    def setComponentProps(self, componentID, props):
        pass

    def playComponentAnimation(self, componentID, animType):
        pass

    def stopComponentAnimation(self, componentID, animType):
        pass

    def showBootcampHint(self, componentID):
        pass

    def hideBootcampHint(self, componentID):
        pass

    def setupViewContextHints(self, viewTutorialID, hintsData, hintsArgs=None):
        pass

    def overrideHangarMenuButtons(self, buttonsList=None):
        pass

    def overrideHeaderMenuButtons(self, buttonsList=None):
        pass

    def setHangarHeaderEnabled(self, enabled):
        pass

    def overrideBattleSelectorHint(self, overrideType=None):
        pass

    def clear(self):
        pass


class StubTutorialLoader(ITutorialLoader):

    def __init__(self):
        super(StubTutorialLoader, self).__init__()
        self.__gui = StubGuiController()

    @property
    def gui(self):
        return self.__gui

    @property
    def tutorial(self):
        return

    @property
    def tutorialID(self):
        return ''

    @property
    def isRunning(self):
        return False

    def isTutorialStopped(self):
        return False

    def init(self):
        pass

    def fini(self):
        pass

    def run(self, settingsID, state=None):
        pass

    def stop(self, restore=True):
        pass

    def refuse(self):
        pass