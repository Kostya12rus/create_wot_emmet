# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_asserts.py
from ..fixer_base import BaseFix
from ..fixer_util import Name
NAMES = dict(assert_='assertTrue', assertEquals='assertEqual', assertNotEquals='assertNotEqual', assertAlmostEquals='assertAlmostEqual', assertNotAlmostEquals='assertNotAlmostEqual', assertRegexpMatches='assertRegex', assertRaisesRegexp='assertRaisesRegex', failUnlessEqual='assertEqual', failIfEqual='assertNotEqual', failUnlessAlmostEqual='assertAlmostEqual', failIfAlmostEqual='assertNotAlmostEqual', failUnless='assertTrue', failUnlessRaises='assertRaises', failIf='assertFalse')

class FixAsserts(BaseFix):
    PATTERN = "\n              power< any+ trailer< '.' meth=(%s)> any* >\n              " % ('|').join(map(repr, NAMES))

    def transform(self, node, results):
        name = results['meth'][0]
        name.replace(Name(NAMES[str(name)], prefix=name.prefix))