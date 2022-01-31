# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/ny_vignette_settings_switcher.py
import BigWorld
_NY_VIGNETTE_INTENSITY = 0.7
_VIEWS_TO_VIGNETTE_CHANGE = {
 'hangar',
 'heroVehiclePreviewPage',
 'vehiclePreviewPage',
 'ny_navigation'}
_defaultVignetteIntensity = None

def _isVignetteView(viewName):
    return viewName in _VIEWS_TO_VIGNETTE_CHANGE


def checkVignetteSettings(viewName):
    global _defaultVignetteIntensity
    vignetteSettings = BigWorld.WGRenderSettings().getVignetteSettings()
    if _defaultVignetteIntensity is None:
        _defaultVignetteIntensity = vignetteSettings.w
    vignetteSettings.w = _NY_VIGNETTE_INTENSITY if _isVignetteView(viewName) else _defaultVignetteIntensity
    BigWorld.WGRenderSettings().setVignetteSettings(vignetteSettings)
    return