# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/server_events/personal_progress/builders.py
import typing, quest_progress
from gui.server_events.personal_progress import progress
from gui.server_events.personal_progress import strategy
from personal_missions_constants import DISPLAY_TYPE, CONTAINER, DESCRIPTIONS

class ClientProgressBuilder(quest_progress.IProgressBuilder):

    @classmethod
    def build(cls, progressID, progressData):
        commonProgress = cls._getCommonProgress(progressID, progressData)
        clientData = progressData['description']
        if clientData.getContainerType() == CONTAINER.HEADER:
            clientProgress = cls._createHeaderProgress(commonProgress, clientData)
            clientProgress.setLabelsGetter(cls._getHeaderLabelsStrategy(clientData))
        else:
            clientProgress = cls._createBodyProgress(commonProgress, clientData)
        clientProgress.setProgressGetter(cls._getValuesStrategy(clientData))
        return clientProgress

    @classmethod
    def _createBodyProgress(cls, commonProgress, clientData):
        return progress.BodyProgress(commonProgress, clientData, cls.getTemplateID())

    @classmethod
    def _createHeaderProgress(cls, commonProgress, clientData):
        return progress.HeaderProgress(commonProgress, clientData)

    @classmethod
    def _getCommonProgress(cls, progressID, progressData):
        raise NotImplementedError

    @classmethod
    def _getValuesStrategy(cls, clientData):
        raise NotImplementedError

    @classmethod
    def _getHeaderLabelsStrategy(cls, clientData):
        displayType = clientData.displayType
        if displayType == DISPLAY_TYPE.BIATHLON:
            return strategy.BiathlonLabelGetter
        if displayType == DISPLAY_TYPE.SERIES:
            return strategy.SeriesLabelGetter
        if displayType == DISPLAY_TYPE.LIMITED:
            return strategy.LimitedTriesLabelGetter
        return strategy.CounterLabelGetter


class BinaryProgressBuilder(ClientProgressBuilder, quest_progress.BinaryProgressBuilder):

    @classmethod
    def _getValuesStrategy(cls, clientData):
        return strategy.BinaryProgressGetter

    @classmethod
    def _getCommonProgress(cls, progressID, progressData):
        return quest_progress.BinaryProgressBuilder.build(progressID, progressData)


class ValueProgressBuilder(ClientProgressBuilder, quest_progress.ValueProgressBuilder):

    @classmethod
    def _getValuesStrategy(cls, clientData):
        if isinstance(clientData, DESCRIPTIONS.AVERAGE):
            return strategy.AverageProgressGetter
        return strategy.ValueProgressGetter

    @classmethod
    def _createBodyProgress(cls, commonProgress, clientData):
        if isinstance(clientData, DESCRIPTIONS.AVERAGE):
            return progress.AverageProgress(commonProgress, clientData, cls.getTemplateID())
        return progress.BodyProgress(commonProgress, clientData, cls.getTemplateID())

    @classmethod
    def _getCommonProgress(cls, progressID, progressData):
        return quest_progress.ValueProgressBuilder.build(progressID, progressData)


class VehicleTypesProgressBuilder(ClientProgressBuilder, quest_progress.CounterProgressBuilder):

    @classmethod
    def _getValuesStrategy(cls, clientData):
        return strategy.CounterProgressGetter

    @classmethod
    def _createBodyProgress(cls, commonProgress, clientData):
        return progress.VehicleTypesProgress(commonProgress, clientData, cls.getTemplateID())

    @classmethod
    def _getCommonProgress(cls, progressID, progressData):
        return quest_progress.CounterProgressBuilder.build(progressID, progressData)


class BiathlonProgressBuilder(ClientProgressBuilder, quest_progress.BattlesSeriesProgressBuilder):

    @classmethod
    def _getValuesStrategy(cls, clientData):
        return strategy.BiathlonProgressGetter

    @classmethod
    def _createHeaderProgress(cls, commonProgress, clientData):
        return progress.BiathlonProgress(commonProgress, clientData)

    @classmethod
    def _getCommonProgress(cls, progressID, progressData):
        return quest_progress.BattlesSeriesProgressBuilder.build(progressID, progressData)