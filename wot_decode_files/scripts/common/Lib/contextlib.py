# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/contextlib.py
import sys
from functools import wraps
from warnings import warn
__all__ = [
 'contextmanager', 'nested', 'closing']

class GeneratorContextManager(object):

    def __init__(self, gen):
        self.gen = gen

    def __enter__(self):
        try:
            return self.gen.next()
        except StopIteration:
            raise RuntimeError("generator didn't yield")

    def __exit__(self, type, value, traceback):
        if type is None:
            try:
                self.gen.next()
            except StopIteration:
                return

            raise RuntimeError("generator didn't stop")
        else:
            if value is None:
                value = type()
            try:
                self.gen.throw(type, value, traceback)
                raise RuntimeError("generator didn't stop after throw()")
            except StopIteration as exc:
                return exc is not value
            except:
                if sys.exc_info()[1] is not value:
                    raise

        return


def contextmanager(func):

    @wraps(func)
    def helper(*args, **kwds):
        return GeneratorContextManager(func(*args, **kwds))

    return helper


@contextmanager
def nested(*managers):
    warn('With-statements now directly support multiple context managers', DeprecationWarning, 3)
    exits = []
    vars = []
    exc = (None, None, None)
    try:
        try:
            for mgr in managers:
                exit = mgr.__exit__
                enter = mgr.__enter__
                vars.append(enter())
                exits.append(exit)

            yield vars
        except:
            exc = sys.exc_info()

    finally:
        while exits:
            exit = exits.pop()
            try:
                if exit(*exc):
                    exc = (None, None, None)
            except:
                exc = sys.exc_info()

        if exc != (None, None, None):
            raise exc[0], exc[1], exc[2]

    return


class closing(object):

    def __init__(self, thing):
        self.thing = thing

    def __enter__(self):
        return self.thing

    def __exit__(self, *exc_info):
        self.thing.close()