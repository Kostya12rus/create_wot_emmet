# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/pub/pop_over_window.py
import typing
from frameworks.wulf import WindowFlags, ViewFlags, WindowLayer
from gui.impl.gen import R
from gui.impl.gen.view_models.windows.pop_over_window_model import PopOverWindowModel
from gui.impl.pub.window_impl import WindowImpl
from gui.impl.pub.window_view import WindowView

class PopOverWindow(WindowImpl):
    __slots__ = ()

    def __init__(self, event, content, parent, layer=WindowLayer.UNDEFINED):
        super(PopOverWindow, self).__init__(wndFlags=WindowFlags.POP_OVER, decorator=WindowView(layoutID=event.decoratorID, flags=ViewFlags.POP_OVER_DECORATOR, viewModelClazz=PopOverWindowModel), content=content, parent=parent, areaID=R.areas.pop_over(), layer=layer)
        with self.popOverModel.transaction() as (tx):
            tx.setBoundX(event.bbox.positionX)
            tx.setBoundY(event.bbox.positionY)
            tx.setBoundWidth(event.bbox.width)
            tx.setBoundHeight(event.bbox.height)
            tx.setDirectionType(event.direction)
            tx.setIsCloseBtnVisible(content.isCloseBtnVisible)

    @property
    def popOverModel(self):
        return super(PopOverWindow, self)._getDecoratorViewModel()