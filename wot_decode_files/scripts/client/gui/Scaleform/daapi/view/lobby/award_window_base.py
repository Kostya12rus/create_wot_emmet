# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/award_window_base.py
from gui.Scaleform.daapi.view.meta.AwardWindowsBaseMeta import AwardWindowsBaseMeta
from gui.server_events.awards import AwardAbstract

class AwardWindowBase(AwardWindowsBaseMeta):

    def __init__(self, ctx):
        super(AwardWindowBase, self).__init__()
        if 'award' not in ctx:
            raise UserWarning('Key "award" is not found in context', ctx)
        if not isinstance(ctx['award'], AwardAbstract):
            raise UserWarning('Value of "award" should be instance of AwardAbstract', ctx)
        self._award = ctx['award']

    def onWindowClose(self):
        self.destroy()

    def _populate(self):
        super(AwardWindowBase, self)._populate()
        data = {'windowTitle': self._award.getWindowTitle(), 
           'backImage': self._award.getBackgroundImage(), 
           'header': self._award.getHeader(), 
           'description': self._award.getDescription()}
        data.update(self._getTypeSpecificFields())
        self.as_setDataS(data)
        self.__playSound()

    def _getTypeSpecificFields(self):
        return {}

    def _dispose(self):
        if self._award is not None:
            self._award.clear()
            self._award = None
        super(AwardWindowBase, self)._dispose()
        return

    def __playSound(self):
        sound = self._award.getSound()
        if sound is not None:
            self.soundManager.playInstantSound(sound)
        return