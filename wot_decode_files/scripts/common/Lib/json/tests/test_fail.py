# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/json/tests/test_fail.py
from json.tests import PyTest, CTest
JSONDOCS = [
 '"A JSON payload should be an object or array, not a string."', 
 '["Unclosed array"', 
 '{unquoted_key: "keys must be quoted"}', 
 '["extra comma",]', 
 '["double extra comma",,]', 
 '[   , "<-- missing value"]', 
 '["Comma after the close"],', 
 '["Extra close"]]', 
 '{"Extra comma": true,}', 
 '{"Extra value after close": true} "misplaced quoted value"', 
 '{"Illegal expression": 1 + 2}', 
 '{"Illegal invocation": alert()}', 
 '{"Numbers cannot have leading zeroes": 013}', 
 '{"Numbers cannot be hex": 0x14}', 
 '["Illegal backslash escape: \\x15"]', 
 '[\\naked]', 
 '["Illegal backslash escape: \\017"]', 
 '[[[[[[[[[[[[[[[[[[[["Too deep"]]]]]]]]]]]]]]]]]]]]', 
 '{"Missing colon" null}', 
 '{"Double colon":: null}', 
 '{"Comma instead of colon", null}', 
 '["Colon instead of comma": false]', 
 '["Bad value", truth]', 
 "['single quote']", 
 '["\ttab\tcharacter\tin\tstring\t"]', 
 '["tab\\   character\\   in\\  string\\  "]', 
 '["line\nbreak"]', 
 '["line\\\nbreak"]', 
 '[0e]', 
 '[0e+]', 
 '[0e+-1]', 
 '{"Comma instead if closing brace": true,', 
 '["mismatch"}', 
 '["A\x1fZ control characters in string"]']
SKIPS = {1: 'why not have a string payload?', 
   18: "spec doesn't specify any nesting limitations"}

class TestFail(object):

    def test_failures(self):
        for idx, doc in enumerate(JSONDOCS):
            idx = idx + 1
            if idx in SKIPS:
                self.loads(doc)
                continue
            try:
                self.loads(doc)
            except ValueError:
                pass
            else:
                self.fail(('Expected failure for fail{0}.json: {1!r}').format(idx, doc))

    def test_non_string_keys_dict(self):
        data = {'a': 1, (1, 2): 2}
        self.assertRaises(TypeError, self.dumps, data)
        self.assertRaises(TypeError, self.dumps, data, indent=True)


class TestPyFail(TestFail, PyTest):
    pass


class TestCFail(TestFail, CTest):
    pass