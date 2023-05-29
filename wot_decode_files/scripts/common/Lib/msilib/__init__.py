# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/msilib/__init__.py
from _msi import *
import glob, os, re, string, sys
AMD64 = 'AMD64' in sys.version
Itanium = 'Itanium' in sys.version
Win64 = AMD64 or Itanium
datasizemask = 255
type_valid = 256
type_localizable = 512
typemask = 3072
type_long = 0
type_short = 1024
type_string = 3072
type_binary = 2048
type_nullable = 4096
type_key = 8192
knownbits = datasizemask | type_valid | type_localizable | typemask | type_nullable | type_key

class Table:

    def __init__(self, name):
        self.name = name
        self.fields = []

    def add_field(self, index, name, type):
        self.fields.append((index, name, type))

    def sql(self):
        fields = []
        keys = []
        self.fields.sort()
        fields = [None] * len(self.fields)
        for index, name, type in self.fields:
            index -= 1
            unk = type & ~knownbits
            if unk:
                print '%s.%s unknown bits %x' % (self.name, name, unk)
            size = type & datasizemask
            dtype = type & typemask
            if dtype == type_string:
                if size:
                    tname = 'CHAR(%d)' % size
                else:
                    tname = 'CHAR'
            elif dtype == type_short:
                tname = 'SHORT'
            elif dtype == type_long:
                tname = 'LONG'
            elif dtype == type_binary:
                tname = 'OBJECT'
            else:
                tname = 'unknown'
                print '%s.%sunknown integer type %d' % (self.name, name, size)
            if type & type_nullable:
                flags = ''
            else:
                flags = ' NOT NULL'
            if type & type_localizable:
                flags += ' LOCALIZABLE'
            fields[index] = '`%s` %s%s' % (name, tname, flags)
            if type & type_key:
                keys.append('`%s`' % name)

        fields = (', ').join(fields)
        keys = (', ').join(keys)
        return 'CREATE TABLE %s (%s PRIMARY KEY %s)' % (self.name, fields, keys)

    def create(self, db):
        v = db.OpenView(self.sql())
        v.Execute(None)
        v.Close()
        return


class _Unspecified:
    pass


def change_sequence(seq, action, seqno=_Unspecified, cond=_Unspecified):
    for i in range(len(seq)):
        if seq[i][0] == action:
            if cond is _Unspecified:
                cond = seq[i][1]
            if seqno is _Unspecified:
                seqno = seq[i][2]
            seq[i] = (
             action, cond, seqno)
            return

    raise ValueError, 'Action not found in sequence'


def add_data(db, table, values):
    v = db.OpenView('SELECT * FROM `%s`' % table)
    count = v.GetColumnInfo(MSICOLINFO_NAMES).GetFieldCount()
    r = CreateRecord(count)
    for value in values:
        for i in range(count):
            field = value[i]
            if isinstance(field, (int, long)):
                r.SetInteger(i + 1, field)
            elif isinstance(field, basestring):
                r.SetString(i + 1, field)
            elif field is None:
                pass
            elif isinstance(field, Binary):
                r.SetStream(i + 1, field.name)
            else:
                raise TypeError, 'Unsupported type %s' % field.__class__.__name__

        try:
            v.Modify(MSIMODIFY_INSERT, r)
        except Exception as e:
            raise MSIError('Could not insert ' + repr(values) + ' into ' + table)

        r.ClearData()

    v.Close()
    return


def add_stream(db, name, path):
    v = db.OpenView("INSERT INTO _Streams (Name, Data) VALUES ('%s', ?)" % name)
    r = CreateRecord(1)
    r.SetStream(1, path)
    v.Execute(r)
    v.Close()


def init_database(name, schema, ProductName, ProductCode, ProductVersion, Manufacturer):
    try:
        os.unlink(name)
    except OSError:
        pass

    ProductCode = ProductCode.upper()
    db = OpenDatabase(name, MSIDBOPEN_CREATE)
    for t in schema.tables:
        t.create(db)

    add_data(db, '_Validation', schema._Validation_records)
    si = db.GetSummaryInformation(20)
    si.SetProperty(PID_TITLE, 'Installation Database')
    si.SetProperty(PID_SUBJECT, ProductName)
    si.SetProperty(PID_AUTHOR, Manufacturer)
    if Itanium:
        si.SetProperty(PID_TEMPLATE, 'Intel64;1033')
    elif AMD64:
        si.SetProperty(PID_TEMPLATE, 'x64;1033')
    else:
        si.SetProperty(PID_TEMPLATE, 'Intel;1033')
    si.SetProperty(PID_REVNUMBER, gen_uuid())
    si.SetProperty(PID_WORDCOUNT, 2)
    si.SetProperty(PID_PAGECOUNT, 200)
    si.SetProperty(PID_APPNAME, 'Python MSI Library')
    si.Persist()
    add_data(db, 'Property', [
     (
      'ProductName', ProductName),
     (
      'ProductCode', ProductCode),
     (
      'ProductVersion', ProductVersion),
     (
      'Manufacturer', Manufacturer),
     ('ProductLanguage', '1033')])
    db.Commit()
    return db


def add_tables(db, module):
    for table in module.tables:
        add_data(db, table, getattr(module, table))


def make_id(str):
    identifier_chars = string.ascii_letters + string.digits + '._'
    str = ('').join([ c if c in identifier_chars else '_' for c in str ])
    if str[0] in string.digits + '.':
        str = '_' + str
    return str


def gen_uuid():
    return '{' + UuidCreate().upper() + '}'


class CAB:

    def __init__(self, name):
        self.name = name
        self.files = []
        self.filenames = set()
        self.index = 0

    def gen_id(self, file):
        logical = _logical = make_id(file)
        pos = 1
        while logical in self.filenames:
            logical = '%s.%d' % (_logical, pos)
            pos += 1

        self.filenames.add(logical)
        return logical

    def append(self, full, file, logical):
        if os.path.isdir(full):
            return
        if not logical:
            logical = self.gen_id(file)
        self.index += 1
        self.files.append((full, logical))
        return (self.index, logical)

    def commit(self, db):
        from tempfile import mktemp
        filename = mktemp()
        FCICreate(filename, self.files)
        add_data(db, 'Media', [
         (
          1, self.index, None, '#' + self.name, None, None)])
        add_stream(db, self.name, filename)
        os.unlink(filename)
        db.Commit()
        return


_directories = set()

class Directory:

    def __init__(self, db, cab, basedir, physical, _logical, default, componentflags=None):
        index = 1
        _logical = make_id(_logical)
        logical = _logical
        while logical in _directories:
            logical = '%s%d' % (_logical, index)
            index += 1

        _directories.add(logical)
        self.db = db
        self.cab = cab
        self.basedir = basedir
        self.physical = physical
        self.logical = logical
        self.component = None
        self.short_names = set()
        self.ids = set()
        self.keyfiles = {}
        self.componentflags = componentflags
        if basedir:
            self.absolute = os.path.join(basedir.absolute, physical)
            blogical = basedir.logical
        else:
            self.absolute = physical
            blogical = None
        add_data(db, 'Directory', [(logical, blogical, default)])
        return

    def start_component(self, component=None, feature=None, flags=None, keyfile=None, uuid=None):
        if flags is None:
            flags = self.componentflags
        if uuid is None:
            uuid = gen_uuid()
        else:
            uuid = uuid.upper()
        if component is None:
            component = self.logical
        self.component = component
        if Win64:
            flags |= 256
        if keyfile:
            keyid = self.cab.gen_id(keyfile)
            self.keyfiles[keyfile] = keyid
        else:
            keyid = None
        add_data(self.db, 'Component', [
         (
          component, uuid, self.logical, flags, None, keyid)])
        if feature is None:
            feature = current_feature
        add_data(self.db, 'FeatureComponents', [
         (
          feature.id, component)])
        return

    def make_short(self, file):
        oldfile = file
        file = file.replace('+', '_')
        file = ('').join(c for c in file if c not in ' "/\\[]:;=,')
        parts = file.split('.')
        if len(parts) > 1:
            prefix = ('').join(parts[:-1]).upper()
            suffix = parts[-1].upper()
            if not prefix:
                prefix = suffix
                suffix = None
        else:
            prefix = file.upper()
            suffix = None
        if len(parts) < 3 and len(prefix) <= 8 and file == oldfile and (not suffix or len(suffix) <= 3):
            if suffix:
                file = prefix + '.' + suffix
            else:
                file = prefix
        else:
            file = None
        if file is None or file in self.short_names:
            prefix = prefix[:6]
            if suffix:
                suffix = suffix[:3]
            pos = 1
            while 1:
                if suffix:
                    file = '%s~%d.%s' % (prefix, pos, suffix)
                else:
                    file = '%s~%d' % (prefix, pos)
                if file not in self.short_names:
                    break
                pos += 1
                if pos in (10, 100, 1000):
                    prefix = prefix[:-1]

        self.short_names.add(file)
        return file

    def add_file(self, file, src=None, version=None, language=None):
        if not self.component:
            self.start_component(self.logical, current_feature, 0)
        if not src:
            src = file
            file = os.path.basename(file)
        absolute = os.path.join(self.absolute, src)
        if file in self.keyfiles:
            logical = self.keyfiles[file]
        else:
            logical = None
        sequence, logical = self.cab.append(absolute, file, logical)
        self.ids.add(logical)
        short = self.make_short(file)
        full = '%s|%s' % (short, file)
        filesize = os.stat(absolute).st_size
        attributes = 512
        add_data(self.db, 'File', [
         (
          logical, self.component, full, filesize, version,
          language, attributes, sequence)])
        if file.endswith('.py'):
            add_data(self.db, 'RemoveFile', [
             (
              logical + 'c', self.component, '%sC|%sc' % (short, file),
              self.logical, 2),
             (
              logical + 'o', self.component, '%sO|%so' % (short, file),
              self.logical, 2)])
        return logical

    def glob(self, pattern, exclude=None):
        files = glob.glob1(self.absolute, pattern)
        for f in files:
            if exclude and f in exclude:
                continue
            self.add_file(f)

        return files

    def remove_pyc(self):
        add_data(self.db, 'RemoveFile', [
         (
          self.component + 'c', self.component, '*.pyc', self.logical, 2),
         (
          self.component + 'o', self.component, '*.pyo', self.logical, 2)])


class Binary:

    def __init__(self, fname):
        self.name = fname

    def __repr__(self):
        return 'msilib.Binary(os.path.join(dirname,"%s"))' % self.name


class Feature:

    def __init__(self, db, id, title, desc, display, level=1, parent=None, directory=None, attributes=0):
        self.id = id
        if parent:
            parent = parent.id
        add_data(db, 'Feature', [
         (
          id, parent, title, desc, display,
          level, directory, attributes)])

    def set_current(self):
        global current_feature
        current_feature = self


class Control:

    def __init__(self, dlg, name):
        self.dlg = dlg
        self.name = name

    def event(self, event, argument, condition='1', ordering=None):
        add_data(self.dlg.db, 'ControlEvent', [
         (
          self.dlg.name, self.name, event, argument,
          condition, ordering)])

    def mapping(self, event, attribute):
        add_data(self.dlg.db, 'EventMapping', [
         (
          self.dlg.name, self.name, event, attribute)])

    def condition(self, action, condition):
        add_data(self.dlg.db, 'ControlCondition', [
         (
          self.dlg.name, self.name, action, condition)])


class RadioButtonGroup(Control):

    def __init__(self, dlg, name, property):
        self.dlg = dlg
        self.name = name
        self.property = property
        self.index = 1

    def add(self, name, x, y, w, h, text, value=None):
        if value is None:
            value = name
        add_data(self.dlg.db, 'RadioButton', [
         (
          self.property, self.index, value,
          x, y, w, h, text, None)])
        self.index += 1
        return


class Dialog:

    def __init__(self, db, name, x, y, w, h, attr, title, first, default, cancel):
        self.db = db
        self.name = name
        self.x, self.y, self.w, self.h = (x, y, w, h)
        add_data(db, 'Dialog', [(name, x, y, w, h, attr, title, first, default, cancel)])

    def control(self, name, type, x, y, w, h, attr, prop, text, next, help):
        add_data(self.db, 'Control', [
         (
          self.name, name, type, x, y, w, h, attr, prop, text, next, help)])
        return Control(self, name)

    def text(self, name, x, y, w, h, attr, text):
        return self.control(name, 'Text', x, y, w, h, attr, None, text, None, None)

    def bitmap(self, name, x, y, w, h, text):
        return self.control(name, 'Bitmap', x, y, w, h, 1, None, text, None, None)

    def line(self, name, x, y, w, h):
        return self.control(name, 'Line', x, y, w, h, 1, None, None, None, None)

    def pushbutton(self, name, x, y, w, h, attr, text, next):
        return self.control(name, 'PushButton', x, y, w, h, attr, None, text, next, None)

    def radiogroup(self, name, x, y, w, h, attr, prop, text, next):
        add_data(self.db, 'Control', [
         (
          self.name, name, 'RadioButtonGroup',
          x, y, w, h, attr, prop, text, next, None)])
        return RadioButtonGroup(self, name, prop)

    def checkbox(self, name, x, y, w, h, attr, prop, text, next):
        return self.control(name, 'CheckBox', x, y, w, h, attr, prop, text, next, None)