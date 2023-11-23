# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/base_schema_manager.py
import logging, typing
from dict2model.schemas import Schema
from soft_exception import SoftException
if typing.TYPE_CHECKING:
    from dict2model.fields import Field
    from dict2model.types import SchemaModelClassesType, ValidatorsType
_logger = logging.getLogger(__name__)

class GameParamsSchema(Schema):
    __slots__ = ('_gameParamsKey', )

    def __init__(self, gameParamsKey, fields, modelClass=dict, checkUnknown=True, serializedValidators=None, deserializedValidators=None):
        super(GameParamsSchema, self).__init__(fields=fields, modelClass=modelClass, checkUnknown=checkUnknown, serializedValidators=serializedValidators, deserializedValidators=deserializedValidators)
        self._gameParamsKey = gameParamsKey

    @property
    def gpKey(self):
        return self._gameParamsKey


class BaseSchemaManager(object):
    __slots__ = ('_schemas', '_configs')

    def __init__(self):
        self._schemas = {}

    def registerClientServerSchema(self, *args, **kwargs):
        raise NotImplementedError

    def getSchemas(self):
        return self._schemas.values()

    def _addSchema(self, schema):
        if not isinstance(schema, GameParamsSchema):
            raise SoftException('Registered root schema must be instance of GameParamsSchema. schema=%s', schema)
        if schema.gpKey in self._schemas:
            raise SoftException('Schema gameParamsKey duplication. Schema "%s" is already registered.' % schema.gpKey)
        self._schemas[schema.gpKey] = schema