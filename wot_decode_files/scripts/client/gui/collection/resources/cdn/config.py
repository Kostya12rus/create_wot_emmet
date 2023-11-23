# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/collection/resources/cdn/config.py
import typing
from dict2model import fields, schemas, validate
from gui.collection.resources.cdn.models import ConfigModel, Group, ImageModel, Sub
if typing.TYPE_CHECKING:
    from typing import Dict, Optional
imageSchema = schemas.Schema(fields={'group': fields.Enum(Group, required=True), 
   'sub': fields.Enum(Sub, required=True), 
   'name': fields.String(required=True, serializedValidators=validate.Length(minValue=1), deserializedValidators=validate.Length(minValue=1)), 
   'url': fields.Url(required=True, relative=False)}, modelClass=ImageModel, checkUnknown=True)
configSchema = schemas.Schema(fields={'images': fields.List(fieldOrSchema=imageSchema, required=True)}, modelClass=ConfigModel, checkUnknown=True)

def createConfigModel(rawData):
    return configSchema.deserialize(rawData, silent=True)