# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_components/highlight_component.py
import BigWorld, CGF
from cgf_script.managers_registrator import onAddedQuery, onRemovedQuery
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent
from GenericComponents import DynamicModelComponent
from hover_component import IsHoveredComponent

@registerComponent
class IsHighlighted(object):
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor


@registerComponent
class HighlightComponent(object):
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor
    editorTitle = 'Highlight'
    category = 'Common'
    color = ComponentProperty(type=CGFMetaTypes.VECTOR4, editorName='Color', value=(0,
                                                                                    0,
                                                                                    0,
                                                                                    1), annotations={'colorPicker': {'255Range': False, 'useAlpha': True}})
    groupName = ComponentProperty(type=CGFMetaTypes.STRING, editorName='Group name')


class HighlightManager(CGF.ComponentManager):

    @onAddedQuery(IsHoveredComponent, CGF.GameObject)
    def onHoverAdded(self, _, gameObject):
        gameObject.createComponent(IsHighlighted)

    @onRemovedQuery(IsHoveredComponent, CGF.GameObject)
    def onHoverRemoved(self, _, gameObject):
        gameObject.removeComponentByType(IsHighlighted)

    @onAddedQuery(IsHighlighted, HighlightComponent, DynamicModelComponent)
    def onDynamicModelHighlightAdded(self, _, highlightComponent, dynamicModelComponent):
        BigWorld.wgSetEdgeDetectEdgeColor(3, highlightComponent.color)
        BigWorld.wgAddEdgeDetectDynamicModel(dynamicModelComponent)
        self.__enableGroupDraw(True, highlightComponent.groupName)

    @onRemovedQuery(IsHighlighted, HighlightComponent, DynamicModelComponent)
    def onDynamicModelHighlightRemoved(self, _, highlightComponent, dynamicModelComponent):
        BigWorld.wgDelEdgeDetectDynamicModel(dynamicModelComponent)
        self.__enableGroupDraw(False, highlightComponent.groupName)

    @onRemovedQuery(HighlightComponent, DynamicModelComponent)
    def onHighlightComponentRemoved(self, _, dynamicModelComponent):
        BigWorld.wgDelEdgeDetectDynamicModel(dynamicModelComponent)

    def __enableGroupDraw(self, enable, groupName):
        highlightQuery = CGF.Query(self.spaceID, (HighlightComponent, DynamicModelComponent))
        for highlightComponent, dynamicModelComponent in highlightQuery:
            if highlightComponent.groupName and highlightComponent.groupName == groupName:
                if enable:
                    BigWorld.wgAddEdgeDetectDynamicModel(dynamicModelComponent)
                else:
                    BigWorld.wgDelEdgeDetectDynamicModel(dynamicModelComponent)