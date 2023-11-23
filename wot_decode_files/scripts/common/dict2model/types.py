# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/dict2model/types.py
from __future__ import absolute_import
import typing
from dict2model.models import Model
from dict2model.schemas import Schema
from dict2model.validate import Validator
ModelType = typing.TypeVar('ModelType', bound=Model)
SchemaType = typing.TypeVar('SchemaType', bound=Schema)
SchemaModelTypes = typing.Union[(ModelType, typing.Dict)]
SchemaModelClassesType = typing.Union[(typing.Type[ModelType], typing.Type[typing.Dict])]
ValidatorType = typing.Union[(Validator, typing.Callable[([typing.Any], typing.Any)])]
ValidatorsType = typing.Optional[typing.Union[(ValidatorType, typing.List[ValidatorType])]]