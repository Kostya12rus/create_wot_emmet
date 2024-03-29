# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/bwobsolete_helpers/PyGUI/Console.py
import BigWorld, GUI, Keys, math
from Listeners import registerDeviceListener
from PyGUIBase import PyGUIBase
MAX_HISTORY_ENTRIES = 50

class Console(PyGUIBase):
    factoryString = 'PyGUI.Console'

    def __init__(self, component=None):
        PyGUIBase.__init__(self, component)
        self.__history = []
        self.__historyShown = -1
        if component == None:
            self.component = GUI.Window('system/maps/col_white.bmp')
            self.component.colour = (0, 0, 0, 255)
            self.component.materialFX = GUI.Simple.eMaterialFX.SOLID
            self.component.height = 0.75
            self.component.width = 1.5
            self.component.addChild(ScrollableText().component, 'buffer')
            self.component.buffer.colour = (0, 0, 0, 0)
            self.component.buffer.widthMode = GUI.Simple.eSizeMode.CLIP
            self.component.buffer.width = 2.0
            self.component.buffer.height = 1.8
            self.component.buffer.verticalAnchor = GUI.Simple.eVAnchor.TOP
            self.component.buffer.verticalPositionMode = GUI.Simple.ePositionMode.CLIP
            self.component.buffer.position.y = 1.0
            self.component.addChild(EditField().component, 'editField')
            self.component.editField.colour = (64, 64, 64, 255)
            self.component.editField.verticalPositionMode = GUI.Simple.ePositionMode.CLIP
            self.component.editField.verticalAnchor = GUI.Simple.eVAnchor.BOTTOM
            self.component.editField.position.y = -1.0
            self.component.editField.height = 0.2
            self.component.editField.widthMode = GUI.Simple.eSizeMode.CLIP
            self.component.editField.width = 2.0
            self.component.script = self
            self.onBound()
        registerDeviceListener(self)
        return

    def enableEditField(self, state):
        self.component.editField.script.setEnabled(state)

    def clear(self):
        self.component.buffer.script.clear()

    def editFieldChangeFocus(self, editField, state):
        try:
            languageIndicator = self.component.languageIndicator
            languageIndicator.visible = state and editField.enabled
        except AttributeError:
            pass

    def _onEnterText(self, text):
        self.component.editField.script.setText('')
        if len(text) > 0:
            self._insertHistory(text)
        self.handleConsoleInput(text)

    def _onEscape(self):
        self.handleEscapeKey()

    def handleConsoleInput(self, msg):
        pass

    def handleEscapeKey(self):
        pass

    def getMaxLines(self):
        return self.component.buffer.script.getMaxLines()

    def setMaxLines(self, maxLines):
        self.component.editField.script.setMaxLines(maxLines)

    def appendLine(self, msg, colour):
        self.component.buffer.script.appendLine(msg, colour)

    def setEditText(self, text):
        self.component.editField.script.setText(text)

    def getEditText(self):
        return self.component.editField.script.getText()

    def fini(self):
        if self.editable:
            self.editCallback(None)
        self.active(False)
        return

    def enableEdit(self):
        self.component.editField.script.setKeyFocus(True)

    def disableEdit(self):
        self.component.editField.script.setKeyFocus(False)

    def handleEditFieldKeyEvent(self, event):
        handled = False
        if event.isKeyDown():
            if event.key == Keys.KEY_PGDN:
                self.component.buffer.script.scrollDown()
                handled = True
            else:
                if event.key == Keys.KEY_PGUP:
                    self.component.buffer.script.scrollUp()
                    handled = True
                else:
                    if event.key == Keys.KEY_UPARROW:
                        editText = self.getEditText()
                        if len(self.__history) > 0:
                            if self.__historyShown == -1:
                                self.__history.insert(0, editText)
                                self.__historyShown = 1
                            else:
                                if len(editText) > 0:
                                    self.__history[self.__historyShown] = editText
                                self.__historyShown += 1
                            self._showHistory()
                        handled = True
                    elif event.key == Keys.KEY_DOWNARROW:
                        editText = self.getEditText()
                        if len(self.__history) > 0:
                            if self.__historyShown == -1:
                                self.__history.insert(0, editText)
                                self.__historyShown = len(self.__history) - 1
                            else:
                                if len(editText) > 0:
                                    self.__history[self.__historyShown] = editText
                                self.__historyShown -= 1
                            self._showHistory()
                        handled = True
        return handled

    def _insertHistory(self, s):
        if len(s) > 0:
            if len(self.__history) > 0 and self.__historyShown != -1:
                self.__history[0] = s
            else:
                self.__history.insert(0, s)
        elif len(self.__history) > 0 and len(self.__history[0]) == 0:
            self.__history.pop(0)
        if len(self.__history) > MAX_HISTORY_ENTRIES:
            self.__history.pop()
        self.__historyShown = -1

    def _showHistory(self):
        if self.__historyShown < 0:
            self.__historyShown = len(self.__history) - 1
        elif self.__historyShown == len(self.__history):
            self.__historyShown = 0
        self.setEditText(self.__history[self.__historyShown])

    def onBound(self):
        PyGUIBase.onBound(self)
        self.component.editField.script.onBound()
        self.component.editField.script.onEnter = self._onEnterText
        self.component.editField.script.onEscape = self._onEscape
        self.component.editField.script.setExternalKeyEventHandler(self.handleEditFieldKeyEvent)

    def onRecreateDevice(self):
        self.component.editField.script.onRecreateDevice()
        self.component.editField.script.fitVertically()
        self.component.editField.heightMode = GUI.Simple.eSizeMode.CLIP
        self.component.buffer.heightMode = GUI.Simple.eSizeMode.CLIP
        self.component.buffer.height = 2.0 - self.component.editField.height

    def isShowing(self):
        return self.alphaShader.value > 0