# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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