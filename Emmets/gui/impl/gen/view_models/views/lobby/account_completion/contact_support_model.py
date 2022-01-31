# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/account_completion/contact_support_model.py
from gui.impl.gen.view_models.views.lobby.account_completion.common.base_overlay_view_model import BaseOverlayViewModel

class ContactSupportModel(BaseOverlayViewModel):
    __slots__ = ('onContactClicked', )

    def __init__(self, properties=3, commands=3):
        super(ContactSupportModel, self).__init__(properties=properties, commands=commands)

    def getMessage(self):
        return self._getString(2)

    def setMessage(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(ContactSupportModel, self)._initialize()
        self._addStringProperty('message', '')
        self.onContactClicked = self._addCommand('onContactClicked')