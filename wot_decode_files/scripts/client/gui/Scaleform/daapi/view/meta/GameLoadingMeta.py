# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/GameLoadingMeta.py
from gui.Scaleform.daapi.view.meta.DAAPISimpleContainerMeta import DAAPISimpleContainerMeta

class GameLoadingMeta(DAAPISimpleContainerMeta):

    def as_setLocaleS(self, locale):
        if self._isDAAPIInited():
            return self.flashObject.as_setLocale(locale)

    def as_setVersionS(self, version):
        if self._isDAAPIInited():
            return self.flashObject.as_setVersion(version)

    def as_setInfoS(self, info):
        if self._isDAAPIInited():
            return self.flashObject.as_setInfo(info)

    def as_setProgressS(self, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgress(progress)

    def as_updateStageS(self, width, height, scale):
        if self._isDAAPIInited():
            return self.flashObject.as_updateStage(width, height, scale)