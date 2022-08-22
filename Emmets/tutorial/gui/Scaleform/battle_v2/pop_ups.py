# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/tutorial/gui/Scaleform/battle_v2/pop_ups.py
from tutorial.gui.Scaleform.pop_ups import TutorialDialog

class ReplenishAmmoDialog(TutorialDialog):

    def _populate(self):
        self.app.enterGuiControlMode(self.uniqueName)
        super(ReplenishAmmoDialog, self)._populate()
        data = self._content
        self.as_setContentS({'title': data['title'], 
           'message': data['message'], 
           'submitLabel': data['_submitLabel'], 
           'align': data['_align'], 
           'offsetX': data['_popupOffsetX'], 
           'offsetY': data['_popupOffsetY']})

    def _dispose(self):
        self.app.leaveGuiControlMode(self.uniqueName)
        super(ReplenishAmmoDialog, self)._dispose()