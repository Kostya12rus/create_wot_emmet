# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gui_loader.py
import typing
from frameworks.wulf import GuiApplication
from skeletons.gui.impl import IGuiLoader
if typing.TYPE_CHECKING:
    from frameworks.wulf import ViewModel
    from frameworks.wulf.tutorial import Tutorial
    from frameworks.wulf.ui_logger import UILogger

class GuiLoader(IGuiLoader):
    __slots__ = ('__gui', )

    def __init__(self):
        super(GuiLoader, self).__init__()
        self.__gui = GuiApplication()

    @property
    def resourceManager(self):
        return self.__gui.resourceManager

    @property
    def windowsManager(self):
        return self.__gui.windowsManager

    @property
    def systemLocale(self):
        return self.__gui.systemLocale

    @property
    def tutorial(self):
        return self.__gui.tutorial

    @property
    def uiLogger(self):
        return self.__gui.uiLogger

    def init(self, tutorialModel, uiLoggerModel):
        self.__gui.init(tutorialModel, uiLoggerModel)

    def fini(self):
        self.__gui.destroy()