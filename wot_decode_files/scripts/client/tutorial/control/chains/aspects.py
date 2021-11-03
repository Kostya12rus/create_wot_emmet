# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/tutorial/control/chains/aspects.py
import weakref
from gui.Scaleform.daapi.view.dialogs import DIALOG_BUTTON_ID
from helpers import aop

class SimpleDialogResultAspect(aop.Aspect):

    def __init__(self, trigger):
        super(SimpleDialogResultAspect, self).__init__()
        self._trigger = weakref.proxy(trigger)

    def clear(self):
        self._trigger = None
        super(SimpleDialogResultAspect, self).clear()
        return

    def atCall(self, cd):
        if len(cd.args) > 1:
            _, submitID = cd.args[:2]
            result = submitID == DIALOG_BUTTON_ID.SUBMIT
        else:
            result = False
        self._trigger.setResult(result)


class SimpleDialogClosePointcut(aop.Pointcut):

    def __init__(self):
        super(SimpleDialogClosePointcut, self).__init__('gui.Scaleform.daapi.view.dialogs.SimpleDialog', 'SimpleDialog', '^_SimpleDialog__callHandler$')