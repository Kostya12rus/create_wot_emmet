# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/dialogs/custom_sound_button_model.py
from gui.impl.gen.view_models.views.dialogs.dialog_template_button_view_model import DialogTemplateButtonViewModel

class CustomSoundButtonModel(DialogTemplateButtonViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(CustomSoundButtonModel, self).__init__(properties=properties, commands=commands)

    def getSoundClick(self):
        return self._getString(5)

    def setSoundClick(self, value):
        self._setString(5, value)

    def _initialize(self):
        super(CustomSoundButtonModel, self)._initialize()
        self._addStringProperty('soundClick', '')