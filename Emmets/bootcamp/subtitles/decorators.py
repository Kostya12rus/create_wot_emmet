# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/bootcamp/subtitles/decorators.py


def subtitleDecorator(function):

    def onCall(self, *args, **kwargs):
        if getattr(self.__class__, 'content', False) and self.content and self.content['voiceovers']:
            data = self.content['voiceovers'].pop(0)
            if data['voiceover']:
                self.soundManager.playSound(data['voiceover'])
            if data['subtitle']:
                if getattr(self.__class__, 'tutorial', False) and self.tutorial is not None:
                    from tutorial.data.effects import HasTargetEffect, EFFECT_TYPE
                    effects = [
                     HasTargetEffect(data['subtitle'], EFFECT_TYPE.SHOW_WINDOW, None)]
                    self.tutorial.storeEffectsInQueue(effects, benefit=True, isGlobal=True)
                    funcEffect = self.tutorial.getFirstElementOfTop()
                    funcEffect.triggerEffect()
                else:
                    from gui.shared.event_dispatcher import showSubtitleWindow
                    showSubtitleWindow(messageVO={'voiceovers': [data]})
        return function(self, *args, **kwargs)

    return onCall