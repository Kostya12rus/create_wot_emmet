# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/managers/windows_stored_data.py
import logging
from collections import namedtuple, defaultdict
import functools, types
from gui.Scaleform.daapi.view.meta.WindowViewMeta import WindowViewMeta
from gui.doc_loaders.WindowsStoredDataLoader import WindowsStoredDataLoader
from messenger.ext.channel_num_gen import isClientIDValid
from soft_exception import SoftException
WindowGeometry = namedtuple('WindowGeometry', ('x', 'y', 'width', 'height'))
_logger = logging.getLogger(__name__)

class DATA_TYPE(object):
    UNIQUE_WINDOW = 1
    CAROUSEL_WINDOW = 2
    CHANNEL_WINDOW = 3
    RANGE = (
     UNIQUE_WINDOW, CAROUSEL_WINDOW, CHANNEL_WINDOW)


class TARGET_ID(object):
    CHANNEL_CAROUSEL = 1
    CHAT_MANAGEMENT = 2
    ALL = CHANNEL_CAROUSEL | CHAT_MANAGEMENT


DEF_TARGET_MASK = TARGET_ID.CHANNEL_CAROUSEL | TARGET_ID.CHAT_MANAGEMENT
STORED_DATA_MAX_LENGTH = 64
STORED_DATA_REV = 1

def _populateStoredData(targetID, window):
    storedData = g_windowsStoredData.getData(targetID, window)
    if storedData is not None:
        geom = storedData.getGeometry()
        if geom is not None:
            window.as_setGeometryS(*geom)
    return


def _updateStoredData(targetID, dataType, pyWindow):
    storedData = g_windowsStoredData.getData(targetID, pyWindow)
    if storedData is None:
        storedData = g_windowsStoredData.addData(targetID, dataType, pyWindow)
    if storedData is not None:
        geom = pyWindow.as_getGeometryS()
        if geom:
            x, y, width, height = geom[:4]
            storedData.setGeometry(WindowGeometry(int(round(x)), int(round(y)), int(round(width)), int(round(height))))
    return storedData


class stored_window(object):

    def __init__(self, dataType, targetID, sideEffect=None):
        super(stored_window, self).__init__()
        self.__dataType = dataType
        self.__targetID = targetID
        if sideEffect is not None and not callable(sideEffect):
            raise UserWarning('Value of sideEffect is not callable')
        self.__sideEffect = sideEffect
        return

    def __call__(self, clazz):
        if not hasattr(clazz, '__mro__'):
            raise SoftException('First argument is not class')
        if WindowViewMeta not in clazz.__mro__:
            raise SoftException('Class must be extends WindowViewMeta')

        def wrapPopulate(func):

            @functools.wraps(func)
            def wrapper(window, *args, **kwargs):
                func(window, *args, **kwargs)
                _populateStoredData(self.__targetID, window)

            return wrapper

        def wrapDispose(func):

            @functools.wraps(func)
            def wrapper(window, *args, **kwargs):
                data = _updateStoredData(self.__targetID, self.__dataType, window)
                if self.__sideEffect is not None and data is not None:
                    self.__sideEffect(window, data)
                func(window, *args, **kwargs)
                return

            return wrapper

        if not getattr(clazz, '__stored_window__', False):
            clazz._populate = wrapPopulate(clazz._populate)
            clazz._dispose = wrapDispose(clazz._dispose)
            clazz.__stored_window__ = True
        else:
            _logger.warning('Class already wrapped: %r', clazz)
        return clazz


class WindowStoredData(object):
    __slots__ = ('_trusted', '_geometry')

    def __init__(self, *args):
        super(WindowStoredData, self).__init__()
        self._trusted = True
        if len(args) > 3:
            self._geometry = WindowGeometry(*args[:4])
        else:
            self._geometry = None
        return

    @classmethod
    def make(cls, window):
        raise NotImplementedError

    @classmethod
    def getDataType(cls):
        return NotImplementedError

    def pack(self):
        raise NotImplementedError

    def getFindCriteria(self):
        raise NotImplementedError

    def isRequiredWindow(self, window):
        return False

    def isTrusted(self):
        return self._trusted

    def setTrusted(self, value):
        self._trusted = value

    def getGeometry(self):
        return self._geometry

    def setGeometry(self, value):
        self._geometry = value


class UniqueWindowStoredData(WindowStoredData):
    __slots__ = ('_uniqueName', )

    def __init__(self, name, *args):
        super(UniqueWindowStoredData, self).__init__(*args)
        if type(name) not in types.StringTypes:
            _logger.warning('Unique name must be string. It is ignored: %r', name)
            name = ''
            self._trusted = False
        self._uniqueName = name

    def __repr__(self):
        return ('UniqueWindowStoredData(uniqueName = {0:>s}, geometry = {1!r:s}, trusted = {2!r:s})').format(self._uniqueName, self._geometry, self._trusted)

    @classmethod
    def make(cls, window):
        return UniqueWindowStoredData(window.uniqueName)

    @classmethod
    def getDataType(cls):
        return DATA_TYPE.UNIQUE_WINDOW

    def pack(self):
        if not self._uniqueName:
            return
        else:
            if self._geometry is None:
                return
            return (self._uniqueName,) + self._geometry

    def getFindCriteria(self):
        return self._uniqueName

    def isRequiredWindow(self, window):
        return window.uniqueName == self._uniqueName


class CarouselWindowStoredData(WindowStoredData):
    __slots__ = ('_clientID', )

    def __init__(self, clientID, *args):
        super(CarouselWindowStoredData, self).__init__(*args)
        self._clientID = clientID
        self._trusted = isClientIDValid(clientID)

    def __repr__(self):
        return ('CarouselWindowStoredData(clientID = {0:n}, geometry = {1!r:s}, trusted = {2!r:s})').format(self._clientID, self._geometry, self._trusted)

    @classmethod
    def make(cls, window):
        getter = getattr(window, 'getClientID', None)
        if getter and callable(getter):
            clientID = getter()
        else:
            _logger.error('Can not get clientID: %r', window)
            return
        return CarouselWindowStoredData(clientID)

    @classmethod
    def getDataType(cls):
        return DATA_TYPE.CAROUSEL_WINDOW

    def pack(self):
        if not self._clientID:
            return
        else:
            if self._geometry is None:
                return
            return (self._clientID,) + self._geometry

    def getFindCriteria(self):
        return self._clientID

    def isRequiredWindow(self, window):
        result = False
        getter = getattr(window, 'getClientID', None)
        if getter and callable(getter):
            result = getter() == self._clientID
        return result


class ChannelWindowStoredData(WindowStoredData):
    __slots__ = ('_protoType', '_channelID')

    def __init__(self, protoType, channelID, *args):
        super(ChannelWindowStoredData, self).__init__(*args)
        self._protoType = protoType
        self._channelID = channelID
        self._trusted = False

    def __repr__(self):
        return ('ChannelWindowStoredData(protoType = {0:n}, channelID = {1!r:s}, geometry = {2!r:s}, trusted = {3!r:s})').format(self._protoType, self._channelID, self._geometry, self._trusted)

    @classmethod
    def make(cls, window):
        getter = getattr(window, 'getProtoType', None)
        if getter and callable(getter):
            protoType = getter()
        else:
            _logger.error('Can not get protoType: %r', window)
            return
        getter = getattr(window, 'getChannelID', None)
        if getter and callable(getter):
            channelID = getter()
        else:
            _logger.error('Can not get channelID: %r', window)
            return
        return ChannelWindowStoredData(protoType, channelID)

    @classmethod
    def getDataType(cls):
        return DATA_TYPE.CHANNEL_WINDOW

    def pack(self):
        if not self._protoType:
            return
        else:
            if not self._channelID:
                return
            if self._geometry is None:
                return
            return (self._protoType, self._channelID) + self._geometry

    def getFindCriteria(self):
        return (self._protoType, self._channelID)

    def isRequiredWindow(self, window):
        result = False
        getter = getattr(window, 'getProtoType', None)
        if getter and callable(getter):
            result = getter() == self._protoType
        if result:
            getter = getattr(window, 'getChannelID', None)
            if getter and callable(getter):
                result = getter() == self._channelID
        return result


class _WindowsStoredDataManager(object):

    def __init__(self, supported):
        super(_WindowsStoredDataManager, self).__init__()
        self.__storedData = defaultdict(list)
        self.__targetMask = DEF_TARGET_MASK
        self.__loader = None
        self.__supported = dict((clazz.getDataType(), clazz) for clazz in supported)
        self.__trustedCriteria = defaultdict(set)
        self.__isStarted = False
        return

    def start(self):
        if self.__isStarted:
            return
        self.__isStarted = True
        self.__loader = WindowsStoredDataLoader(STORED_DATA_REV, STORED_DATA_MAX_LENGTH, DEF_TARGET_MASK)
        mask, records = self.__loader.load()
        mask |= TARGET_ID.CHAT_MANAGEMENT
        mask |= TARGET_ID.CHANNEL_CAROUSEL
        self.__targetMask = mask & TARGET_ID.ALL
        for record in records:
            if len(record) < 2:
                _logger.error('Invalid record: %r', record)
                continue
            targetID, dataType = record[:2]
            if not targetID & TARGET_ID.ALL:
                _logger.error('Invalid target ID: %r', record)
                continue
            if not self.isTargetEnabled(targetID):
                _logger.warning('Target is not enabled. Records are ignored to load: %r, %r', self.__targetMask, record)
                continue
            if dataType not in DATA_TYPE.RANGE:
                _logger.error('Invalid data type: %r', record)
                continue
            if dataType not in self.__supported:
                _logger.error('Data type is not supported: %r', dataType)
                continue
            try:
                self.__storedData[targetID].append(self.__supported[dataType](*record[2:]))
            except TypeError:
                _logger.error('Invalid record: %r', record)

    def stop(self):
        if not self.__isStarted:
            return
        else:
            self.__isStarted = False
            records = []
            for targetID, windowsData in self.__storedData.iteritems():
                if not self.__targetMask & targetID and windowsData:
                    _logger.warning('Target is not enabled. Records are ignored to flush: %r, %r', targetID, self.__targetMask)
                    continue
                for data in windowsData:
                    if not data.isTrusted():
                        _logger.debug('Data is not trusted. It do not write to file: %r', data)
                        continue
                    record = data.pack()
                    if record is None:
                        continue
                    records.append((targetID, data.getDataType()) + record)

            self.__loader.flush(self.__targetMask, records)
            self.__loader = None
            self.__storedData.clear()
            self.__trustedCriteria.clear()
            return

    def isTargetEnabled(self, targetID):
        return self.__isStarted and self.__targetMask & targetID > 0

    def addTarget(self, targetID):
        if self.__targetMask & targetID > 0:
            return
        if not targetID & TARGET_ID.ALL:
            return
        self.__targetMask |= targetID

    def removeTarget(self, targetID):
        if not self.__targetMask & targetID:
            return
        else:
            if not targetID & TARGET_ID.ALL:
                return
            self.__targetMask ^= targetID
            self.__storedData.pop(targetID, None)
            return

    def addData(self, targetID, dataType, window):
        if not self.isTargetEnabled(targetID):
            return
        else:
            if dataType not in self.__supported:
                _logger.error('Data type is not supported: %r', dataType)
                return
            clazz = self.__supported[dataType]
            data = clazz.make(window)
            if data is not None:
                if data.getFindCriteria() in self.__trustedCriteria[targetID]:
                    data.setTrusted(True)
                self.__storedData[targetID].append(data)
            return data

    def getData(self, targetID, window):
        if not self.isTargetEnabled(targetID):
            return
        else:
            result = None
            for data in self.__storedData[targetID]:
                if data.isRequiredWindow(window):
                    result = data
                    break

            return result

    def getMap(self, targetID, dataType):
        result = {}
        for item in self.__storedData[targetID]:
            if item.getDataType() == dataType:
                result[item.getFindCriteria()] = item

        return result

    def setTrustedCriteria(self, targetID, criteria):
        self.__trustedCriteria[targetID].add(criteria)
        for item in self.__storedData[targetID]:
            if item.getFindCriteria() == criteria:
                item.setTrusted(True)


g_windowsStoredData = _WindowsStoredDataManager((
 UniqueWindowStoredData, CarouselWindowStoredData, ChannelWindowStoredData))