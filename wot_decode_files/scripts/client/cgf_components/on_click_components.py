# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_components/on_click_components.py
import logging, CGF, Event
from GenericComponents import VSEComponent
from adisp import adisp_process
from cgf_script.component_meta_class import CGFMetaTypes, ComponentProperty, registerComponent
from cgf_script.managers_registrator import autoregister, onAddedQuery, onRemovedQuery
from constants import MarathonConfig, IS_CLIENT
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared.utils import IHangarSpace
from hover_component import IsHovered
if IS_CLIENT:
    from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
    from gui.game_control.links import URLMacros
    from gui.shared.event_dispatcher import showBrowserOverlayView
_logger = logging.getLogger(__name__)

@registerComponent
class OnClickComponent(object):
    editorTitle = 'OnClick'
    category = 'Common'
    domain = CGF.DomainOption.DomainClient

    def __init__(self):
        super(OnClickComponent, self).__init__()
        self.onClickAction = Event.Event()


@registerComponent
class OpenBrowserOnClickComponent(object):
    domain = CGF.DomainOption.DomainClient
    urlProvider = ComponentProperty(type=CGFMetaTypes.STRING, editorName='url provider', value='MARATHON_VIDEO_URL_PROVIDER')

    def __init__(self):
        super(OpenBrowserOnClickComponent, self).__init__()
        self.__urlParser = URLMacros()

    def doAction(self):
        self.__openBrowser()

    @adisp_process
    def __openBrowser(self):
        getterFunc = URL_PROVIDERS[self.urlProvider]
        unparsedUrl = getterFunc()
        url = yield self.__urlParser.parse(unparsedUrl)
        showBrowserOverlayView(url, alias=VIEW_ALIAS.BROWSER_OVERLAY)


def getMarathonVideoUrl():
    lobbyContext = dependency.instance(ILobbyContext)
    return lobbyContext.getServerSettings().getMarathonConfig()[MarathonConfig.VIDEO_CONTENT_URL]


URL_PROVIDERS = {'MARATHON_VIDEO_URL_PROVIDER': getMarathonVideoUrl}

@autoregister(presentInAllWorlds=False, category='lobby')
class ClientSelectableComponentsManager(CGF.ComponentManager):

    @onAddedQuery(OpenBrowserOnClickComponent, OnClickComponent)
    def handleOpenBrowserOnClickAdded(self, openBrowserOnClickComponent, onClickComponent):
        onClickComponent.onClickAction += openBrowserOnClickComponent.doAction

    @onRemovedQuery(OpenBrowserOnClickComponent, OnClickComponent)
    def handleOpenBrowserOnClickRemoved(self, openBrowserOnClickComponent, onClickComponent):
        onClickComponent.onClickAction -= openBrowserOnClickComponent.doAction


@autoregister(presentInAllWorlds=True, category='lobby')
class ClickVSEComponentsManager(CGF.ComponentManager):

    @onAddedQuery(OnClickComponent, VSEComponent)
    def handleComponentAdded(self, onClickComponent, vseComponent):
        onClickComponent.onClickAction += vseComponent.context.onGameObjectClick

    @onRemovedQuery(OnClickComponent, VSEComponent)
    def handleComponentRemoved(self, onClickComponent, vseComponent):
        onClickComponent.onClickAction -= vseComponent.context.onGameObjectClick


class ClickManager(CGF.ComponentManager):
    _hangarSpace = dependency.descriptor(IHangarSpace)

    def __init__(self, *args):
        super(ClickManager, self).__init__(*args)
        self._selectedGO = None
        return

    def activate(self):
        self._hangarSpace.onMouseDown += self._onMouseDown
        self._hangarSpace.onMouseUp += self._onMouseUp

    def deactivate(self):
        self._hangarSpace.onMouseDown -= self._onMouseDown
        self._hangarSpace.onMouseUp -= self._onMouseUp

    def _onMouseDown(self):
        clickQuery = CGF.Query(self.spaceID, (CGF.GameObject, IsHovered, OnClickComponent))
        for go, _, __ in clickQuery:
            self._selectedGO = go

    def _onMouseUp(self):
        clickQuery = CGF.Query(self.spaceID, (CGF.GameObject, IsHovered, OnClickComponent))
        for go, _, onClick in clickQuery:
            if self._selectedGO == go:
                _logger.info('ClickManager::Clicked')
                onClick.onClickAction()