# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/hero_tank/__init__.py
from web.web_client_api import w2capi
from web.web_client_api.hero_tank.vehicle import HeroTankWebApiMixin

@w2capi(name='hero_tank', key='action')
class HeroTankWebApi(HeroTankWebApiMixin):
    pass