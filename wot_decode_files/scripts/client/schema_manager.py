# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/schema_manager.py
import logging
from base_schema_manager import BaseSchemaManager, GameParamsSchema
_logger = logging.getLogger(__name__)

class SchemaManager(BaseSchemaManager):

    def __init__(self):
        super(SchemaManager, self).__init__()
        self._models = {}

    def registerClientServerSchema(self, schema):
        self._addSchema(schema)

    def set(self, serverSettings):
        for schema in self.getSchemas():
            if schema.gpKey in serverSettings:
                rawConfig = serverSettings[schema.gpKey]
                self._models[schema.gpKey] = schema.deserialize(rawConfig, onlyPublic=True)
                from PlayerEvents import g_playerEvents
                g_playerEvents.onConfigModelUpdated(schema.gpKey)

    def update(self, serverSettingsDiff):
        for schema in self.getSchemas():
            if schema.gpKey in serverSettingsDiff:
                if schema.gpKey not in self._models:
                    _logger.error('Update is called before set. schema=%s', schema.gpKey)
                    continue
                rawConfig = serverSettingsDiff[schema.gpKey]
                self._models[schema.gpKey] = schema.deserialize(rawConfig, onlyPublic=True)
                from PlayerEvents import g_playerEvents
                g_playerEvents.onConfigModelUpdated(schema.gpKey)

    def get(self, schema):
        model = self._models.get(schema.gpKey)
        if model is None:
            _logger.error('No such schema: %s.', schema.gpKey)
        return model

    def clear(self):
        self._models.clear()


g_SchemaManager = None

def getSchemaManager():
    global g_SchemaManager
    if g_SchemaManager is None:
        g_SchemaManager = SchemaManager()
    return g_SchemaManager