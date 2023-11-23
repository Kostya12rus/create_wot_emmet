# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/mapbox/__init__.py
from helpers import dependency
from skeletons.gui.game_control import IMapboxController
from web.web_client_api import w2c, w2capi, W2CSchema, Field

class _SurveyCompletedSchema(W2CSchema):
    name = Field(required=True, type=basestring)


@w2capi(name='mapbox', key='action')
class MapboxWebApi(W2CSchema):
    __mapboxCtrl = dependency.descriptor(IMapboxController)

    @w2c(_SurveyCompletedSchema, name='survey_complete')
    def handleSurveyCompleted(self, cmd):
        self.__mapboxCtrl.handleSurveyCompleted(cmd.name)