# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/mapbox/mapbox_survey_manager.py
import logging, operator, typing
from account_helpers.AccountSettings import MAPBOX_SURVEYS
from account_helpers import AccountSettings
from constants import ARENA_BONUS_TYPE
from gui.doc_loaders.surveys_loader import getSurvey
from gui.impl.gen.view_models.views.lobby.mapbox.map_box_question_model import QuestionType
from gui.mapbox.mapbox_survey_helper import AlternativeQuestion
from shared_utils import findFirst, first
from soft_exception import SoftException
if typing.TYPE_CHECKING:
    from gui.mapbox.mapbox_survey_helper import IQuestion
_logger = logging.getLogger(__name__)

class MapboxSurveyManager(object):
    __slots__ = ('__questions', '__currentQuestionIdx', '__mapId', '__surveyData')

    def __init__(self):
        self.__mapId = None
        self.__questions = None
        self.__surveyData = None
        self.__currentQuestionIdx = 0
        return

    def fini(self):
        self.__surveyData = None
        self.__mapId = None
        self.__questions = None
        return

    def startSurvey(self, mapId):
        self.__mapId = mapId
        self.__questions = getSurvey(ARENA_BONUS_TYPE.MAPBOX)
        if not self.__questions:
            raise SoftException('Invalid survey config for Mapbox mode')
        self.__surveyData = AccountSettings.getSettings(MAPBOX_SURVEYS).get(self.__mapId, {})
        if not self.__surveyData:
            self.__surveyData['geometry_name'] = self.__mapId
            self.__surveyData['data'] = {}
        self.__currentQuestionIdx = 0

    def clearSurvey(self):
        self.__mapId = None
        self.__currentQuestionIdx = 0
        self.__surveyData = None
        return

    def resetSurvey(self):
        if self.__mapId and self.__surveyData:
            self.__surveyData['data'] = {}
            surveys = AccountSettings.getSettings(MAPBOX_SURVEYS)
            surveys[self.__mapId] = self.__surveyData
            AccountSettings.setSettings(MAPBOX_SURVEYS, surveys)

    def getMapId(self):
        return self.__mapId

    def getSelectedAnswers(self, questionId, optionId=None):
        question = self.getQuestion(questionId)
        if question is None:
            _logger.error('Unable to get the saved answers for the question with id=%s', questionId)
            return []
        else:
            answers = self.__surveyData['data'].get(questionId, [])
            return question.convertAnswers(answers, optionId)

    def saveAnswers(self, questionId, answers):
        question = self.getQuestion(questionId)
        if question is None:
            _logger.error('There is not a question with id=%s', questionId)
            return
        else:
            surveyData = self.__surveyData['data']
            if question.isMultipleChoice():
                savedAnswers = surveyData.get(questionId, [])
                answers = question.validateAnswers(answers, savedAnswers) if answers else []
            for q in self.__questions:
                if q != question and q.getLinkedQuestionId() == question.getQuestionId():
                    if q.getQuestionType() == QuestionType.ALTERNATIVE:
                        for alternative in q.getAlternatives():
                            surveyData.pop(alternative.getQuestionId(), None)

                    else:
                        surveyData.pop(q.getQuestionId(), None)

            if question.getLinkedQuestionId():
                selectedAnswers = self.getSelectedAnswers(question.getLinkedQuestionId())
                if len(selectedAnswers) == 1:
                    for answer in answers:
                        answer['optionId'] = first(selectedAnswers)

            surveyData[questionId] = answers
            if question.getQuestionType() == QuestionType.TEXT:
                if answers:
                    choice = first(first(answers)['choices'])
                    if not choice:
                        surveyData.pop(questionId, None)
            surveys = AccountSettings.getSettings(MAPBOX_SURVEYS)
            surveys[self.__mapId] = self.__surveyData
            AccountSettings.setSettings(MAPBOX_SURVEYS, surveys)
            return

    def canContinue(self):
        if self.__isShownAllQuestions():
            return False
        else:
            question = self.getQuestion()
            if question is None:
                return False
            if question.isRequired():
                return bool(self.getSelectedAnswers(question.getQuestionId()))
            return True

    def getQuestion(self, qId=None):
        if qId is not None:
            parts = qId.split('_')
            if len(parts) > 1:
                question = findFirst(lambda q: q.getQuestionId() == parts[0], self.__questions)
                return question.getAlternative(qId)
            return findFirst(lambda q: q.getQuestionId() == qId, self.__questions)
        else:
            if not self.__isShownAllQuestions():
                return self.__questions[self.__currentQuestionIdx]
            return

    def getPreviousQuestion(self):
        question, idx = self.__findQuestionToShow(self.__questions[self.__currentQuestionIdx - 1::-1])
        self.__currentQuestionIdx = idx
        return question

    def getNextQuestion(self):
        prevIdx = self.__currentQuestionIdx
        question, idx = self.__findQuestionToShow(self.__questions[self.__currentQuestionIdx + 1:])
        self.__currentQuestionIdx = idx
        surveyData = self.__surveyData['data']
        if self.__currentQuestionIdx - prevIdx > 1:
            skippedIdxs = range(prevIdx + 1, self.__currentQuestionIdx)
            for idx in skippedIdxs:
                skippedQuestion = self.__questions[idx]
                if skippedQuestion.getQuestionType() == QuestionType.ALTERNATIVE:
                    for alternative in skippedQuestion.getAlternatives():
                        surveyData.pop(alternative.getQuestionId(), None)

                else:
                    surveyData.pop(skippedQuestion.getQuestionId(), None)

        return question

    def getTotalQuestionsCount(self):
        return len(self.__questions)

    def getCurrentQuestionIdx(self):
        return self.__currentQuestionIdx

    def getSurveyData(self):
        result = []
        for qId, answers in self.__surveyData['data'].iteritems():
            question = self.getQuestion(qId)
            for answer in answers:
                for choice in answer['choices']:
                    if question.getQuestionType() == QuestionType.INTERACTIVE_MAP:
                        choice = '[%s, %s] %s' % (choice['x'], choice['y'], choice['comment'])
                    result.append({'question_id': qId.split('_')[0], 
                       'answer_choice': choice, 
                       'answer_option': answer['optionId']})

        result.sort(key=operator.itemgetter('question_id', 'answer_choice', 'answer_option'))
        return {'name': self.__mapId, 
           'answers': result}

    def __findQuestionToShow(self, questions):
        question = findFirst(lambda q: q.isReadyToShow(), questions)
        if isinstance(question, AlternativeQuestion):
            return (question.selectAlternative(), self.__questions.index(question))
        else:
            questionIdx = self.__questions.index(question) if question is not None else len(self.__questions)
            return (question, questionIdx)

    def __isShownAllQuestions(self):
        return self.__currentQuestionIdx >= len(self.__questions)