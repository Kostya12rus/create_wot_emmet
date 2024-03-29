# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/bwobsolete_helpers/PyGUI/Grid.py
import BigWorld, GUI, Keys
from PyGUIBase import PyGUIBase

class Grid(PyGUIBase):
    factoryString = 'PyGUI.Grid'

    def __init__(self, component):
        PyGUIBase.__init__(self, component)
        component.script = self
        self.component.focus = True
        self.component.moveFocus = True
        self.component.crossFocus = True
        self.horizontalFirst = True
        self.gridWidth = 1
        self.gridHeight = 1
        self.borderTop = 0
        self.borderBottom = 0
        self.borderLeft = 0
        self.borderRight = 0
        self.horizontalGap = 0
        self.verticalGap = 0

    def onSave(self, dataSection):
        dataSection.writeBool('horizontalFirst', self.horizontalFirst)
        dataSection.writeFloat('gridWidth', self.gridWidth)
        dataSection.writeFloat('gridHeight', self.gridHeight)
        dataSection.writeFloat('borderTop', self.borderTop)
        dataSection.writeFloat('borderBottom', self.borderBottom)
        dataSection.writeFloat('borderLeft', self.borderLeft)
        dataSection.writeFloat('borderRight', self.borderRight)
        dataSection.writeFloat('horizontalGap', self.horizontalGap)
        dataSection.writeFloat('verticalGap', self.verticalGap)

    def onLoad(self, dataSection):
        self.horizontalFirst = dataSection.readBool('horizontalFirst', self.horizontalFirst)
        self.gridWidth = dataSection.readFloat('gridWidth', self.gridWidth)
        self.gridHeight = dataSection.readFloat('gridHeight', self.gridHeight)
        self.borderTop = dataSection.readFloat('borderTop', self.borderTop)
        self.borderBottom = dataSection.readFloat('borderBottom', self.borderBottom)
        self.borderLeft = dataSection.readFloat('borderLeft', self.borderLeft)
        self.borderRight = dataSection.readFloat('borderRight', self.borderRight)
        self.horizontalGap = dataSection.readFloat('horizontalGap', self.horizontalGap)
        self.verticalGap = dataSection.readFloat('verticalGap', self.verticalGap)

    def doLayout(self):
        widthMode = self.component.widthMode
        heightMode = self.component.heightMode
        if widthMode == GUI.Simple.eSizeMode.PIXEL:
            horizSize = (self.component.width - self.borderLeft - self.borderRight - self.horizontalGap * (self.gridWidth - 1)) / self.gridWidth
            horizOffset = horizSize + self.horizontalGap
            horizStart = self.borderLeft
        if widthMode == GUI.Simple.eSizeMode.CLIP:
            horizSize = (2.0 - self.borderLeft - self.borderRight - self.horizontalGap * (self.gridWidth - 1)) / self.gridWidth
            horizOffset = horizSize + self.horizontalGap
            horizStart = -1.0 + self.borderLeft
        if heightMode == GUI.Simple.eSizeMode.PIXEL:
            vertSize = (self.component.height - self.borderTop - self.borderBottom - self.verticalGap * (self.gridHeight - 1)) / self.gridHeight
            vertOffset = vertSize + self.verticalGap
            vertStart = self.borderTop
        if heightMode == GUI.Simple.eSizeMode.CLIP:
            vertSize = (2.0 - self.borderTop - self.borderBottom - self.verticalGap * (self.gridHeight - 1)) / self.gridHeight
            vertOffset = -(vertSize + self.verticalGap)
            vertStart = 1.0 - self.borderTop
        horizPos = horizStart
        vertPos = vertStart
        count = 1
        for discard, i in self.component.children:
            i.widthMode = widthMode
            i.width = horizSize
            i.heightMode = heightMode
            i.height = vertSize
            i.horizontalPositionMode = widthMode
            i.verticalPositionMode = heightMode
            i.horizontalAnchor = 'LEFT'
            i.verticalAnchor = 'TOP'
            i.position = (horizPos, vertPos, i.position[2])
            if self.horizontalFirst:
                if count == self.gridWidth:
                    count = 1
                    horizPos = horizStart
                    vertPos += vertOffset
                else:
                    count += 1
                    horizPos += horizOffset
            elif count == self.gridHeight:
                count = 1
                vertPos = vertStart
                horizPos += horizOffset
            else:
                count += 1
                vertPos += vertOffset

    @staticmethod
    def create(texture, gridSize=(1, 1), horizontalFirst=True, **kwargs):
        c = GUI.Window(texture)
        c.materialFX = GUI.Simple.eMaterialFX.BLEND
        c.widthMode = GUI.Simple.eSizeMode.CLIP
        c.heightMode = GUI.Simple.eSizeMode.CLIP
        c.horizontalPositionMode = GUI.Simple.ePositionMode.CLIP
        c.verticalPositionMode = GUI.Simple.ePositionMode.CLIP
        g = Grid(c, **kwargs)
        if len(gridSize) == 2:
            g.gridWidth = gridSize[0]
            g.gridHeight = gridSize[1]
        else:
            g.gridWidth = 1
            g.gridHeight = 1
        g.horizontalFirst = horizontalFirst
        return g.component