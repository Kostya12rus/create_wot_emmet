# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/multiprocessing/process.py
__all__ = [
 'Process', 'current_process', 'active_children']
import os, sys, signal, itertools
try:
    ORIGINAL_DIR = os.path.abspath(os.getcwd())
except OSError:
    ORIGINAL_DIR = None

def current_process():
    global _current_process
    return _current_process


def active_children():
    _cleanup()
    return list(_current_process._children)


def _cleanup():
    for p in list(_current_process._children):
        if p._popen.poll() is not None:
            _current_process._children.discard(p)

    return


class Process(object):
    _Popen = None

    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}):
        count = _current_process._counter.next()
        self._identity = _current_process._identity + (count,)
        self._authkey = _current_process._authkey
        self._daemonic = _current_process._daemonic
        self._tempdir = _current_process._tempdir
        self._parent_pid = os.getpid()
        self._popen = None
        self._target = target
        self._args = tuple(args)
        self._kwargs = dict(kwargs)
        self._name = name or type(self).__name__ + '-' + (':').join(str(i) for i in self._identity)
        return

    def run(self):
        if self._target:
            self._target(*self._args, **self._kwargs)

    def start(self):
        _cleanup()
        if self._Popen is not None:
            Popen = self._Popen
        else:
            from .forking import Popen
        self._popen = Popen(self)
        del self._target
        del self._args
        del self._kwargs
        _current_process._children.add(self)
        return

    def terminate(self):
        self._popen.terminate()

    def join(self, timeout=None):
        res = self._popen.wait(timeout)
        if res is not None:
            _current_process._children.discard(self)
        return

    def is_alive(self):
        if self is _current_process:
            return True
        else:
            if self._popen is None:
                return False
            else:
                returncode = self._popen.poll()
                if returncode is None:
                    return True
                _current_process._children.discard(self)
                return False

            return

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def daemon(self):
        return self._daemonic

    @daemon.setter
    def daemon(self, daemonic):
        self._daemonic = daemonic

    @property
    def authkey(self):
        return self._authkey

    @authkey.setter
    def authkey(self, authkey):
        self._authkey = AuthenticationString(authkey)

    @property
    def exitcode(self):
        if self._popen is None:
            return self._popen
        else:
            return self._popen.poll()

    @property
    def ident(self):
        if self is _current_process:
            return os.getpid()
        else:
            return self._popen and self._popen.pid

    pid = ident

    def __repr__(self):
        if self is _current_process:
            status = 'started'
        elif self._parent_pid != os.getpid():
            status = 'unknown'
        elif self._popen is None:
            status = 'initial'
        elif self._popen.poll() is not None:
            status = self.exitcode
        else:
            status = 'started'
        if type(status) in (int, long):
            if status == 0:
                status = 'stopped'
            else:
                status = 'stopped[%s]' % _exitcode_to_name.get(status, status)
        return '<%s(%s, %s%s)>' % (type(self).__name__, self._name,
         status, self._daemonic and ' daemon' or '')

    def _bootstrap(self):
        global _current_process
        from . import util
        try:
            self._children = set()
            self._counter = itertools.count(1)
            try:
                sys.stdin.close()
                sys.stdin = open(os.devnull)
            except (OSError, ValueError):
                pass

            _current_process = self
            util._finalizer_registry.clear()
            util._run_after_forkers()
            util.info('child process calling self.run()')
            try:
                self.run()
                exitcode = 0
            finally:
                util._exit_function()

        except SystemExit as e:
            if not e.args:
                exitcode = 1
            elif isinstance(e.args[0], (int, long)):
                exitcode = int(e.args[0])
            else:
                sys.stderr.write(str(e.args[0]) + '\n')
                sys.stderr.flush()
                exitcode = 1
        except:
            exitcode = 1
            import traceback
            sys.stderr.write('Process %s:\n' % self.name)
            sys.stderr.flush()
            traceback.print_exc()

        util.info('process exiting with exitcode %d' % exitcode)
        return exitcode


class AuthenticationString(bytes):

    def __reduce__(self):
        from .forking import Popen
        if not Popen.thread_is_spawning():
            raise TypeError('Pickling an AuthenticationString object is disallowed for security reasons')
        return (
         AuthenticationString, (bytes(self),))


class _MainProcess(Process):

    def __init__(self):
        self._identity = ()
        self._daemonic = False
        self._name = 'MainProcess'
        self._parent_pid = None
        self._popen = None
        self._counter = itertools.count(1)
        self._children = set()
        self._authkey = AuthenticationString(os.urandom(32))
        self._tempdir = None
        return


_current_process = _MainProcess()
del _MainProcess
_exitcode_to_name = {}
for name, signum in signal.__dict__.items():
    if name[:3] == 'SIG' and '_' not in name:
        _exitcode_to_name[-signum] = name