# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/common/base_sub_model_view.py
import typing
from frameworks.wulf import ViewModel
TViewModel = typing.TypeVar('TViewModel', bound=ViewModel)

class BaseSubModelView(typing.Generic[TViewModel], object):
    __slots__ = ('_viewModel', '_isLoaded')

    def __init__(self, viewModel):
        self._viewModel = viewModel
        self._isLoaded = False

    def isLoaded(self):
        return self._isLoaded

    def onLoading(self, *args, **kwargs):
        self._isLoaded = True

    def initialize(self, *args, **kwargs):
        self._addListeners()

    def update(self, *args, **kwargs):
        pass

    def finalize(self):
        self._removeListeners()
        self._viewModel = None
        return

    def _addListeners(self):
        pass

    def _removeListeners(self):
        pass