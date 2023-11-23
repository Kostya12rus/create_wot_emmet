# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_loading/resources/cdn/types.py
import typing
from gui.game_loading.resources.cdn.models import ConfigSequenceModel, ConfigSlideModel, LocalSlideModel, LocalSequenceModel
SequenceType = typing.Union[(ConfigSequenceModel, LocalSequenceModel)]
SlideType = typing.Union[(ConfigSlideModel, LocalSlideModel)]