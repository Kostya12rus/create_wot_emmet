# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCIntroFadeOut.py
from gui.Scaleform.daapi.view.meta.BCIntroFadeOutMeta import BCIntroFadeOutMeta
from bootcamp.BootCampEvents import g_bootcampEvents

class BCIntroFadeOut(BCIntroFadeOutMeta):

    def __init__(self, settings):
        super(BCIntroFadeOut, self).__init__()
        self.__duration = settings['duration']

    def finished(self):
        self.destroy()

    def _populate(self):
        super(BCIntroFadeOut, self)._populate()
        g_bootcampEvents.onArenaStarted()
        self.__start()

    def __start(self):
        self.as_startFadeoutS(self.__duration)

    def __onFinish(self, destroyView):
        g_bootcampEvents.onIntroVideoStop()
        if destroyView:
            self.destroy()