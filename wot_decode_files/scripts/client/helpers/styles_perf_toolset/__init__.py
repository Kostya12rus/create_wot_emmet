# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/styles_perf_toolset/__init__.py
import sys
from . import styles_overrider
from . import report_generator
g_stylesOverrider = styles_overrider.StylesOverrider()
g_reportGenerator = report_generator.ReportGenerator()

def setup():
    applyStylesFlag = '--applyStyles'
    if applyStylesFlag in sys.argv:
        path = sys.argv[sys.argv.index(applyStylesFlag) + 1]
        g_stylesOverrider.loadStylesConfig(path)
    generateReportFlag = '--generateReport'
    if generateReportFlag in sys.argv:
        location = sys.argv[sys.argv.index(generateReportFlag) + 1]
        g_reportGenerator.setLocation(location)


__all__ = ('styles_overrider', 'report_generator', 'g_stylesOverrider', 'g_reportGenerator',
           'setup')