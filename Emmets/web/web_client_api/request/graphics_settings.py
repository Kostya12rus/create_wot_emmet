# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/request/graphics_settings.py
from debug_utils import LOG_DEBUG
from gui.shared.utils import graphics
from web.web_client_api import w2c, W2CSchema

class GraphicsSettingsWebApiMixin(object):

    @w2c(W2CSchema, 'graphics_settings')
    def graphicsSettings(self, cmd):
        settings = {}
        settingNames = ('TEXTURE_QUALITY', 'LIGHTING_QUALITY', 'SHADOWS_QUALITY', 'SNIPER_MODE_GRASS_ENABLED',
                        'EFFECTS_QUALITY', 'SNIPER_MODE_EFFECTS_QUALITY', 'FLORA_QUALITY',
                        'POST_PROCESSING_QUALITY', 'VEHICLE_DUST_ENABLED', 'CUSTOM_AA_MODE',
                        'MSAA_QUALITY', 'RENDER_PIPELINE')
        for settingName in settingNames:
            setting = graphics.getGraphicsSetting(settingName)
            if setting is not None:
                settings[settingName] = setting.value
            else:
                LOG_DEBUG('Settings "%s" not found!' % settingName)

        return {'request_id': 'graphics_settings', 'settings': settings}