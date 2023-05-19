# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/ui/maps_training.py
from helpers import dependency
from skeletons.gui.game_control import IMapsTrainingController
from web.web_client_api import w2c, W2CSchema

class OpenMapsTrainingMixin(object):
    mapsTrainingController = dependency.descriptor(IMapsTrainingController)

    @w2c(W2CSchema, 'maps_training')
    def selectMapsTrainingMode(self, _):
        if self.mapsTrainingController.isMapsTrainingEnabled:
            self.mapsTrainingController.selectMapsTrainingMode()