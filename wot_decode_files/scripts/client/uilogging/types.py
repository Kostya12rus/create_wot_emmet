# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/types.py
import typing
from enum import Enum
FeatureType = typing.Union[(str, Enum)]
GroupType = typing.Union[(str, Enum)]
ActionType = typing.Union[(str, Enum)]
LogLevelType = typing.Union[(int, Enum)]
TimeLimitType = float
PartnerIdType = typing.Optional[str]
ItemType = typing.Union[(str, Enum)]
ItemStateType = typing.Optional[typing.Union[(str, Enum)]]
ParentScreenType = typing.Optional[typing.Union[(str, Enum)]]
InfoType = typing.Optional[typing.Union[(str, Enum)]]
SourceItemType = typing.Union[(str, Enum)]
DestinationItemType = typing.Union[(str, Enum)]
TransitionMethodType = typing.Union[(str, Enum)]