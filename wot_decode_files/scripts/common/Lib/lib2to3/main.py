# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/main.py
from __future__ import with_statement
import sys, os, difflib, logging, shutil, optparse
from . import refactor

def diff_texts(a, b, filename):
    a = a.splitlines()
    b = b.splitlines()
    return difflib.unified_diff(a, b, filename, filename, '(original)', '(refactored)', lineterm='')


class StdoutRefactoringTool(refactor.MultiprocessRefactoringTool):

    def __init__(self, fixers, options, explicit, nobackups, show_diffs, input_base_dir='', output_dir='', append_suffix=''):
        self.nobackups = nobackups
        self.show_diffs = show_diffs
        if input_base_dir and not input_base_dir.endswith(os.sep):
            input_base_dir += os.sep
        self._input_base_dir = input_base_dir
        self._output_dir = output_dir
        self._append_suffix = append_suffix
        super(StdoutRefactoringTool, self).__init__(fixers, options, explicit)

    def log_error(self, msg, *args, **kwargs):
        self.errors.append((msg, args, kwargs))
        self.logger.error(msg, *args, **kwargs)

    def write_file(self, new_text, filename, old_text, encoding):
        orig_filename = filename
        if self._output_dir:
            if filename.startswith(self._input_base_dir):
                filename = os.path.join(self._output_dir, filename[len(self._input_base_dir):])
            else:
                raise ValueError('filename %s does not start with the input_base_dir %s' % (
                 filename, self._input_base_dir))
        if self._append_suffix:
            filename += self._append_suffix
        if orig_filename != filename:
            output_dir = os.path.dirname(filename)
            if not os.path.isdir(output_dir):
                os.makedirs(output_dir)
            self.log_message('Writing converted %s to %s.', orig_filename, filename)
        if not self.nobackups:
            backup = filename + '.bak'
            if os.path.lexists(backup):
                try:
                    os.remove(backup)
                except os.error as err:
                    self.log_message("Can't remove backup %s", backup)

            try:
                os.rename(filename, backup)
            except os.error as err:
                self.log_message("Can't rename %s to %s", filename, backup)

        write = super(StdoutRefactoringTool, self).write_file
        write(new_text, filename, old_text, encoding)
        if not self.nobackups:
            shutil.copymode(backup, filename)
        if orig_filename != filename:
            shutil.copymode(orig_filename, filename)

    def print_output(self, old, new, filename, equal):
        if equal:
            self.log_message('No changes to %s', filename)
        else:
            self.log_message('Refactored %s', filename)
            if self.show_diffs:
                diff_lines = diff_texts(old, new, filename)
                try:
                    if self.output_lock is not None:
                        with self.output_lock:
                            for line in diff_lines:
                                print line

                            sys.stdout.flush()
                    else:
                        for line in diff_lines:
                            print line

                except UnicodeEncodeError:
                    warn("couldn't encode %s's diff for your terminal" % (
                     filename,))
                    return

        return


def warn(msg):
    print >> sys.stderr, 'WARNING: %s' % (msg,)


def main(fixer_pkg, args=None):
    parser = optparse.OptionParser(usage='2to3 [options] file|dir ...')
    parser.add_option('-d', '--doctests_only', action='store_true', help='Fix up doctests only')
    parser.add_option('-f', '--fix', action='append', default=[], help='Each FIX specifies a transformation; default: all')
    parser.add_option('-j', '--processes', action='store', default=1, type='int', help='Run 2to3 concurrently')
    parser.add_option('-x', '--nofix', action='append', default=[], help='Prevent a transformation from being run')
    parser.add_option('-l', '--list-fixes', action='store_true', help='List available transformations')
    parser.add_option('-p', '--print-function', action='store_true', help='Modify the grammar so that print() is a function')
    parser.add_option('-v', '--verbose', action='store_true', help='More verbose logging')
    parser.add_option('--no-diffs', action='store_true', help="Don't show diffs of the refactoring")
    parser.add_option('-w', '--write', action='store_true', help='Write back modified files')
    parser.add_option('-n', '--nobackups', action='store_true', default=False, help="Don't write backups for modified files")
    parser.add_option('-o', '--output-dir', action='store', type='str', default='', help='Put output files in this directory instead of overwriting the input files.  Requires -n.')
    parser.add_option('-W', '--write-unchanged-files', action='store_true', help='Also write files even if no changes were required (useful with --output-dir); implies -w.')
    parser.add_option('--add-suffix', action='store', type='str', default='', help="Append this string to all output filenames. Requires -n if non-empty.  ex: --add-suffix='3' will generate .py3 files.")
    refactor_stdin = False
    flags = {}
    options, args = parser.parse_args(args)
    if options.write_unchanged_files:
        flags['write_unchanged_files'] = True
        if not options.write:
            warn('--write-unchanged-files/-W implies -w.')
        options.write = True
    if options.output_dir and not options.nobackups:
        parser.error("Can't use --output-dir/-o without -n.")
    if options.add_suffix and not options.nobackups:
        parser.error("Can't use --add-suffix without -n.")
    if not options.write and options.no_diffs:
        warn("not writing files and not printing diffs; that's not very useful")
    if not options.write and options.nobackups:
        parser.error("Can't use -n without -w")
    if options.list_fixes:
        print 'Available transformations for the -f/--fix option:'
        for fixname in refactor.get_all_fix_names(fixer_pkg):
            print fixname

        if not args:
            return 0
    if not args:
        print >> sys.stderr, 'At least one file or directory argument required.'
        print >> sys.stderr, 'Use --help to show usage.'
        return 2
    if '-' in args:
        refactor_stdin = True
        if options.write:
            print >> sys.stderr, "Can't write to stdin."
            return 2
    if options.print_function:
        flags['print_function'] = True
    level = logging.DEBUG if options.verbose else logging.INFO
    logging.basicConfig(format='%(name)s: %(message)s', level=level)
    logger = logging.getLogger('lib2to3.main')
    avail_fixes = set(refactor.get_fixers_from_package(fixer_pkg))
    unwanted_fixes = set(fixer_pkg + '.fix_' + fix for fix in options.nofix)
    explicit = set()
    if options.fix:
        all_present = False
        for fix in options.fix:
            if fix == 'all':
                all_present = True
            else:
                explicit.add(fixer_pkg + '.fix_' + fix)

        requested = avail_fixes.union(explicit) if all_present else explicit
    else:
        requested = avail_fixes.union(explicit)
    fixer_names = requested.difference(unwanted_fixes)
    input_base_dir = os.path.commonprefix(args)
    if input_base_dir and not input_base_dir.endswith(os.sep) and not os.path.isdir(input_base_dir):
        input_base_dir = os.path.dirname(input_base_dir)
    if options.output_dir:
        input_base_dir = input_base_dir.rstrip(os.sep)
        logger.info('Output in %r will mirror the input directory %r layout.', options.output_dir, input_base_dir)
    rt = StdoutRefactoringTool(sorted(fixer_names), flags, sorted(explicit), options.nobackups, not options.no_diffs, input_base_dir=input_base_dir, output_dir=options.output_dir, append_suffix=options.add_suffix)
    if not rt.errors:
        if refactor_stdin:
            rt.refactor_stdin()
        else:
            try:
                rt.refactor(args, options.write, options.doctests_only, options.processes)
            except refactor.MultiprocessingUnsupported:
                print >> sys.stderr, "Sorry, -j isn't supported on this platform."
                return 1

        rt.summarize()
    return int(bool(rt.errors))