# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/bwobsolete_helpers/PyGUI/LanguageIndicator.py
import BigWorld, GUI
from PyGUIBase import PyGUIBase
import Utils, weakref
_indicators = []

def handleIMEEvent(event):
    global _indicators
    if not event.stateChanged:
        return
    else:
        for indicator in [ x() for x in _indicators if x() is not None ]:
            indicator.setupLanguageState()

        return


def _indicatorString():
    return BigWorld.localeInfo()[3][:2]


class LanguageIndicator(PyGUIBase):
    factoryString = 'PyGUI.LanguageIndicator'

    def __init__(self, component):
        PyGUIBase.__init__(self, component)
        component.script = self
        self.padding = 5
        self.square = True
        self.autoSize = True
        _indicators.append(weakref.ref(self))
        import bwobsolete_helpers.PyGUI as PyGUI
        PyGUI.registerInputLangChangeListener(self)

    def handleInputLangChangeEvent(self):
        self.component.label.text = _indicatorString()
        self.setupLanguageState()
        self.sizeToFit()

    def setupLanguageState(self):
        if BigWorld.ime.state == 'ON' or BigWorld.ime.language == 'NON_IME':
            colour = (255, 255, 255, 255)
        else:
            colour = (0, 0, 0, 255)
        self.component.label.colour = colour

    def sizeToFit(self):
        if not self.autoSize:
            return
        label = self.component.label
        w, h = label.stringDimensions(label.text)
        w = w + self.padding
        h = h + self.padding
        if self.square:
            sz = max(w, h)
            w = sz
            h = sz
        oldMode = self.component.widthMode
        self.component.widthMode = GUI.Simple.eSizeMode.PIXEL
        self.component.width = w
        self.component.widthMode = oldMode
        oldMode = self.component.heightMode
        self.component.heightMode = GUI.Simple.eSizeMode.PIXEL
        self.component.height = h
        self.component.heightMode = oldMode

    def onLoad(self, dataSection):
        PyGUIBase.onLoad(self, dataSection)
        self.autoSize = dataSection.readBool('autoSize', True)
        self.padding = dataSection.readInt('padding', 5)
        self.square = dataSection.readBool('square', True)

    def onSave(self, dataSection):
        PyGUIBase.onSave(self, dataSection)
        dataSection.writeBool('autoSize', self.autoSize)
        dataSection.writeInt('padding', self.padding)
        dataSection.writeBool('square', self.square)

    def onBound(self):
        PyGUIBase.onBound(self)
        self.handleInputLangChangeEvent()

    @staticmethod
    def create():
        c = GUI.Window('system/maps/col_white.bmp')
        c.materialFX = GUI.Simple.eMaterialFX.BLEND
        c.colour = (255, 128, 64, 255)
        c.focus = True
        t = GUI.Text(_indicatorString())
        t.colour = (255, 255, 255, 255)
        c.addChild(t, 'label')
        li = LanguageIndicator(c)
        li.handleInputLangChangeEvent()
        return li.component