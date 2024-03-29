# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/view_components.py
import logging, weakref
from collections import defaultdict
from soft_exception import SoftException
from gui.battle_control.battle_constants import VIEW_COMPONENT_RULE
from gui.battle_control.controllers.interfaces import IBattleController
_logger = logging.getLogger(__name__)

class IViewComponentsCtrlListener(object):

    def detachedFromCtrl(self, ctrlID):
        pass


class IViewComponentsController(IBattleController):
    __slots__ = ()

    def getControllerID(self):
        raise NotImplementedError

    def stopControl(self):
        raise NotImplementedError

    def startControl(self, *args):
        raise NotImplementedError

    def setViewComponents(self, *components):
        raise NotImplementedError

    def clearViewComponents(self):
        raise NotImplementedError


class ViewComponentsController(IViewComponentsController):
    __slots__ = ('_viewComponents', )

    def __init__(self):
        super(ViewComponentsController, self).__init__()
        self._viewComponents = []

    def setViewComponents(self, *components):
        self._viewComponents = components

    def clearViewComponents(self):
        self._viewComponents = []


class ComponentsBridgeError(SoftException):
    pass


class _ComponentsBridge(object):

    def __init__(self):
        super(_ComponentsBridge, self).__init__()
        self.__components = {}
        self.__ctrls = {}
        self.__indexes = {}
        self.__componentToCrl = defaultdict(list)

    def clear(self):
        for componentID in self.__componentToCrl:
            self.removeViewComponent(componentID)

        self.__components.clear()
        self.__ctrls.clear()
        self.__indexes.clear()
        self.__componentToCrl.clear()

    def registerViewComponents(self, *data):
        for item in data:
            if len(item) < 2:
                raise ComponentsBridgeError(('Item is invalid: {}').format(item))
            ctrlID, componentsIDs = item[:2]
            if not isinstance(componentsIDs, (tuple, list)):
                raise ComponentsBridgeError(('Item is invalid: {}').format(item))
            if ctrlID in self.__components:
                sameViewAliases = set(componentsIDs).intersection(self.__indexes[ctrlID])
                if sameViewAliases:
                    raise ComponentsBridgeError('Linkage of controller ID to view alias have to be defined only once! ' + ('Controller ID: {}, same view aliases: {}').format(ctrlID, sameViewAliases))
                else:
                    self.__components[ctrlID].extend([None] * len(componentsIDs))
                    self.__indexes[ctrlID].extend(componentsIDs)
            else:
                self.__components[ctrlID] = [
                 None] * len(componentsIDs)
                self.__indexes[ctrlID] = list(componentsIDs)
            for componentID in componentsIDs:
                self.__componentToCrl[componentID].append(ctrlID)

        return

    def addViewComponent(self, componentID, component, rule=VIEW_COMPONENT_RULE.PROXY):
        if componentID not in self.__componentToCrl:
            return
        else:
            ctrlsIDs = self.__componentToCrl[componentID]
            for ctrlID in ctrlsIDs:
                index = self.__getIndexByComponentID(ctrlID, componentID)
                if index is None:
                    _logger.error('View component data is broken: %r, %r, %r', ctrlID, componentID, self.__indexes)
                    continue
                components = self.__components[ctrlID]
                if rule == VIEW_COMPONENT_RULE.PROXY:
                    components[index] = weakref.proxy(component)
                else:
                    components[index] = component
                if [ item for item in components if item is None ]:
                    continue
                if ctrlID in self.__ctrls:
                    ctrl = self.__ctrls[ctrlID]
                    ctrl.setViewComponents(*components)
                else:
                    _logger.warning('Controller is not found: %r', ctrlID)

            return

    def removeViewComponent(self, componentID):
        if componentID not in self.__componentToCrl:
            return
        else:
            ctrlsIDs = self.__componentToCrl[componentID]
            for ctrlID in ctrlsIDs:
                index = self.__getIndexByComponentID(ctrlID, componentID)
                if index is None:
                    _logger.error('View component data is broken: %r, %r, %r', ctrlID, componentID, self.__indexes)
                    continue
                if ctrlID not in self.__components:
                    continue
                components = self.__components[ctrlID]
                viewComponent = components[index]
                if isinstance(viewComponent, IViewComponentsCtrlListener):
                    viewComponent.detachedFromCtrl(ctrlID)
                components[index] = None
                if [ item for item in components if item is not None ]:
                    continue
                if ctrlID in self.__ctrls:
                    ctrl = self.__ctrls[ctrlID]
                    ctrl.clearViewComponents()

            return

    def registerController(self, ctrl):
        if not isinstance(ctrl, IViewComponentsController):
            raise ComponentsBridgeError(('Controller {0} is not extended IViewComponentsController').format(ctrl))
        self.__ctrls[ctrl.getControllerID()] = weakref.proxy(ctrl)

    def registerControllers(self, *ctrls):
        for ctrl in ctrls:
            self.registerController(ctrl)

    def __getIndexByComponentID(self, ctrlID, componentID):
        if ctrlID not in self.__indexes:
            return
        else:
            indexes = self.__indexes[ctrlID]
            if componentID in indexes:
                return indexes.index(componentID)
            return


def createComponentsBridge():
    return _ComponentsBridge()