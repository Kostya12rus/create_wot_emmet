# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/ext/dictionaries.py
import re, types, sre_compile, ResMgr
from debug_utils import LOG_CURRENT_EXCEPTION, LOG_ERROR
from helpers import html
_defaultReplacementFunction = lambda word: '*' * len(word)

class ObsceneLanguageDictionary(object):
    replace = staticmethod(_defaultReplacementFunction)

    @staticmethod
    def overrideReplacementFunction(function):
        ObsceneLanguageDictionary.replace = staticmethod(function)

    @staticmethod
    def resetReplacementFunction():
        ObsceneLanguageDictionary.replace = staticmethod(_defaultReplacementFunction)

    def searchAndReplace(self, text):
        return text


class BasicOLDictionary(ObsceneLanguageDictionary):
    __nonAlphaNumPattern = re.compile('[^a-zA-Z]', re.M | re.S | re.U | re.I)
    __equivalents = {}
    __badWordPatterns = []

    @classmethod
    def load(cls, resourceId):
        obj = BasicOLDictionary.__new__(cls)
        dSection = ResMgr.openSection(resourceId)
        if dSection is None:
            return obj
        else:
            eqsSection = dSection['equivalents']
            if eqsSection is not None:
                for eqSection in eqsSection.values():
                    find = eqSection['find'].asWideString if eqSection.has_key('find') else None
                    replace = eqSection['replace'].asWideString if eqSection.has_key('replace') else None
                    if find and replace:
                        obj.__equivalents[find] = replace

            nonAnSection = dSection['nonAlphanumericCharacter']
            if nonAnSection is not None:
                nonAnPattern = nonAnSection.asWideString
                try:
                    obj.__nonAlphaNumPattern = re.compile(nonAnPattern, re.M | re.S | re.U | re.I)
                except sre_compile.error:
                    LOG_CURRENT_EXCEPTION()

            badWordsSection = dSection['badWords']
            if badWordsSection is not None:
                for badWordSet in badWordsSection.values():
                    try:
                        if badWordSet.has_key('include'):
                            include = re.compile(badWordSet['include'].asWideString, re.M | re.S | re.U | re.I)
                        else:
                            include = re.compile(badWordSet.asWideString, re.M | re.S | re.U | re.I)
                        exclude = None
                        if badWordSet.has_key('exclude'):
                            exclude = re.compile(badWordSet['exclude'].asWideString, re.M | re.S | re.U | re.I)
                        obj.__badWordPatterns.append((include, exclude))
                    except sre_compile.error:
                        LOG_CURRENT_EXCEPTION()

            ResMgr.purge(resourceId, True)
            return obj

    def searchAndReplace(self, text):
        words = text.split(' ')
        for idx, word in enumerate(words):
            parsing = self.__nonAlphaNumPattern.sub('', word.lower())
            for find, replace in self.__equivalents.iteritems():
                parsing = parsing.replace(find, replace)

            for include, exclude in self.__badWordPatterns:
                match = include.search(parsing)
                if match and (exclude is None or not exclude.search(parsing)):
                    words[idx] = self.replace(word)
                    break

        return (' ').join(words)


class SpecialOLDictionary(ObsceneLanguageDictionary):
    __badWordPatterns = []

    @classmethod
    def load(cls, resourceId):
        obj = SpecialOLDictionary.__new__(cls)
        dSection = ResMgr.openSection(resourceId)
        if dSection is None:
            return obj
        else:
            badWordsSection = dSection['badWords']
            if badWordsSection is not None:
                for badWordSet in badWordsSection.values():
                    try:
                        if not badWordSet.keys():
                            badWordC = re.compile(badWordSet.asWideString, re.M | re.S | re.U | re.I)
                            obj.__badWordPatterns.append(badWordC)
                    except sre_compile.error:
                        LOG_CURRENT_EXCEPTION()

            ResMgr.purge(resourceId, True)
            return obj

    def searchAndReplace(self, text):
        try:
            for pat in self.__badWordPatterns:
                lowerText = text.lower()
                processed = []
                offset = 0
                for m in pat.finditer(lowerText):
                    start = m.start()
                    end = m.end()
                    processed.append(text[offset:start])
                    processed.append(self.replace(text[start:end]))
                    offset = end

                if offset:
                    processed.append(text[offset:])
                if processed:
                    text = ('').join(processed)

        except Exception:
            LOG_ERROR('There is exception in special bad words filter')
            LOG_CURRENT_EXCEPTION()

        return text


class ChinaOLDictionary(SpecialOLDictionary):
    __badWordPatterns = []
    __equivalents = {}

    @classmethod
    def load(cls, resourceId):
        obj = ChinaOLDictionary.__new__(cls)
        dSection = ResMgr.openSection(resourceId)
        if dSection is None:
            return obj
        else:
            eqsSection = dSection['equivalents']
            if eqsSection is not None:
                for eqSection in eqsSection.values():
                    find = eqSection['find'].asWideString if eqSection.has_key('find') else None
                    replace = eqSection['replace'].asWideString if eqSection.has_key('replace') else None
                    if find and replace:
                        obj.__equivalents[find] = replace

            badWordsSection = dSection['badWords']
            if badWordsSection is not None:
                for badWordSet in badWordsSection.values():
                    try:
                        badWordWS = badWordSet.asWideString
                        if not isinstance(badWordWS, types.UnicodeType):
                            badWordWS = unicode(badWordWS, 'utf-8')
                        badWordWS = html.escape(badWordWS)
                        badWordC = re.compile(badWordWS, re.M | re.S | re.U | re.I)
                        obj.__badWordPatterns.append(badWordC)
                    except sre_compile.error:
                        LOG_CURRENT_EXCEPTION()

            ResMgr.purge(resourceId, True)
            return obj

    def searchAndReplace(self, text):
        try:
            if not isinstance(text, types.UnicodeType):
                text = unicode(text, 'utf-8')
            lowerText = text.lower()
            for find, replace in self.__equivalents.iteritems():
                lowerText = lowerText.replace(find, replace)

            for pat in self.__badWordPatterns:
                processed = []
                offset = 0
                for m in pat.finditer(lowerText):
                    start = m.start()
                    end = m.end()
                    processed.append(text[offset:start])
                    processed.append(self.replace(text[start:end]))
                    offset = end

                if offset:
                    processed.append(text[offset:])
                if processed:
                    text = ('').join(processed)

        except Exception:
            LOG_ERROR('There is exception in special bad words filter')
            LOG_CURRENT_EXCEPTION()

        return text


class DomainNameDictionary(object):
    __webPrefix = '^(http(s)?://)?(www\\.)?'
    __domainNamePatterns = []
    replace = staticmethod(_defaultReplacementFunction)

    @classmethod
    def load(cls, resourceId):
        obj = DomainNameDictionary.__new__(cls)
        dSection = ResMgr.openSection(resourceId)
        if dSection is None:
            return obj
        else:
            domainNameSection = dSection['domainNames']
            if domainNameSection is not None:
                for domainNameSet in domainNameSection.values():
                    try:
                        include = re.compile(obj.__webPrefix + domainNameSet.asWideString, re.M | re.S | re.U | re.I)
                        obj.__domainNamePatterns.append(include)
                    except sre_compile.error:
                        LOG_CURRENT_EXCEPTION()

            ResMgr.purge(resourceId, True)
            return obj

    @staticmethod
    def overrideReplacementFunction(function):
        DomainNameDictionary.replace = staticmethod(function)

    @staticmethod
    def resetReplacementFunction():
        DomainNameDictionary.replace = staticmethod(_defaultReplacementFunction)

    def searchAndReplace(self, text):
        words = text.split(' ')
        for idx, word in enumerate(words):
            for pattern in self.__domainNamePatterns:
                match = pattern.search(word)
                if match:
                    words[idx] = self.replace(word)
                    break

        return (' ').join(words)