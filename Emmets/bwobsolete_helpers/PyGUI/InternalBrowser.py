# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/bwobsolete_helpers/PyGUI/InternalBrowser.py
import BigWorld, Math, types, GUI
from PyGUIBase import PyGUIBase
from VisualStateComponent import VisualState, VisualStateComponent
import Utils, Keys, LLMozlibKeys, FantasyDemo
from FocusManager import setFocusedComponent, isFocusedComponent

class InternalBrowser(PyGUIBase):
    factoryString = 'PyGUI.InternalBrowser'
    visualStateString = 'PyGUI.ButtonVisualState'

    def __init__(self, component=None):
        PyGUIBase.__init__(self, component)
        self.component.script = self
        self.mozillaHandlesKeyboard = True
        self.prevCursorManagement = True
        self.focusObserver = None
        return

    def onLoad(self, dataSection):
        self.exactWidth = dataSection.readInt('exactWidth', 0)
        self.exactHeight = dataSection.readInt('exactHeight', 0)
        if self.exactHeight == 0 and self.exactWidth == 0:
            resQuality = 'EFFECT_SCROLLING'
        else:
            resQuality = 'EFFECT_QUALITY'
        componentWidth, componentHeight = Utils.pixelSize(self.component)
        self.webPage = BigWorld.WebPageProvider(componentWidth, componentHeight, True, False, 'LLMozlib', 'http://www.google.com', resQuality)
        self.updateResolutionOverride()
        FantasyDemo.rds.fdgui.addResolutionOverrideHandler(self)
        self.component.focus = False
        self.component.mouseButtonFocus = True
        self.component.moveFocus = True
        self.component.crossFocus = True
        self.component.texture = self.webPage.texture()
        self.component.materialFX = GUI.Simple.eMaterialFX.SOLID

    def __del__(self):
        FantasyDemo.rds.fdgui.removeResolutionOverrideHandler(self)

    def _getWebCoordinates(self, cursorPosition):
        c = self.component
        pos = c.screenToLocal(cursorPosition)
        if pos.x > c.width or pos.y > c.height or pos.x < 0 or pos.y < 0:
            return None
        componentWidth, componentHeight = Utils.pixelSize(self.component)
        pos.x = pos.x * self.webPage.width() / componentWidth
        pos.y = pos.y * self.webPage.height() / componentHeight
        return pos

    def handleMouseButtonEvent(self, comp, event):
        PyGUIBase.handleMouseButtonEvent(self, comp, event)
        pos = self._getWebCoordinates(event.cursorPosition)
        if pos is None:
            return False
        else:
            if event.isKeyDown():
                setFocusedComponent(self.component)
            self.webPage.handleMouseButtonEvent(pos, event.isKeyDown())
            return True

    def handleMouseEvent(self, comp, event):
        if event.dz != 0:
            self.webPage.scrollByLines(event.dz / -40)
        pos = self._getWebCoordinates(event.cursorPosition)
        if pos is None:
            return False
        else:
            self.webPage.handleMouseMove(pos)
            return True

    def handleMouseEnterEvent(self, comp):
        self.prevCursorManagement = GUI.mcursor().automaticCursorManagement
        GUI.mcursor().automaticCursorManagement = False
        self.webPage.allowCursorInteraction(True)
        return True

    def handleMouseLeaveEvent(self, comp):
        self.webPage.allowCursorInteraction(False)
        GUI.mcursor().automaticCursorManagement = self.prevCursorManagement
        return True

    def handleKeyEvent(self, event):
        if event.isMouseButton():
            return False
        else:
            if not isFocusedComponent(self.component) and not self.mozillaHandlesKeyboard:
                return False
            character = event.character
            if event.isKeyDown():
                callKeyboardEvent = False
                callUnicodeEvent = False
                if event.key == Keys.KEY_ESCAPE:
                    usedKey = LLMozlibKeys.LL_DOM_VK_ESCAPE
                    callKeyboardEvent = True
                elif event.key == Keys.KEY_BACKSPACE:
                    usedKey = LLMozlibKeys.LL_DOM_VK_BACK_SPACE
                    callKeyboardEvent = True
                elif event.key == Keys.KEY_RETURN:
                    usedKey = LLMozlibKeys.LL_DOM_VK_RETURN
                    callKeyboardEvent = True
                elif event.key == Keys.KEY_TAB:
                    usedKey = LLMozlibKeys.LL_DOM_VK_TAB
                    callKeyboardEvent = True
                elif character is not None:
                    callUnicodeEvent = True
                if not self.mozillaHandlesKeyboard:
                    if callUnicodeEvent:
                        self.webPage.handleUnicodeInput(character)
                        return 1
                    if callKeyboardEvent:
                        self.webPage.handleKeyboardEvent(usedKey)
                        return 1
                else:
                    return True
            return True

    def addFocusObserver(self, focusObserver):
        self.focusObserver = focusObserver

    def focus(self, state):
        if self.mozillaHandlesKeyboard:
            self.webPage.focusBrowser(state, state)
        if self.focusObserver:
            self.focusObserver.focus(state)

    def setRatePerSecond(self, rate):
        self.webPage.ratePerSecond = rate

    def getRatePerSecond(self):
        return self.webPage.ratePerSecond

    def navigate(self, url):
        self.webPage.navigate(url)

    def navigateBack(self):
        self.webPage.navigateBack()

    def navigateForward(self):
        self.webPage.navigateForward()

    def addObserver(self, observer):
        self.webPage.addObserver(observer)

    def updateResolutionOverride(self):
        webPageWidth, webPageHeight = Utils.pixelSize(self.component)
        screenWidth = BigWorld.screenWidth()
        screenHeight = BigWorld.screenHeight()
        usedResolutionOverride = GUI.screenResolution()
        if usedResolutionOverride != (0, 0):
            webPageWidth *= BigWorld.screenWidth() / usedResolutionOverride[0]
            webPageHeight *= BigWorld.screenHeight() / usedResolutionOverride[1]
        self.webPage.setSize(webPageWidth, webPageHeight, self.exactWidth, self.exactHeight)