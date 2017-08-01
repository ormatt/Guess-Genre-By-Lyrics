from fnmatch import fnmatch
import os
import os.path as path
from constants import MODULE_PATTERN, SCRIPT_DIR
from functools import reduce
import imp


def _get_dir_content(s, _):
    return s, map(lambda fn: path.join(s['modules_dir'], fn),
                  os.listdir(s['modules_dir']))


def _filter_only_files(s, dir_content):
    return s, filter(lambda fn: path.isfile(path.join(s['modules_dir'], fn)),
                     dir_content)


def _filter_by_pattern(s, dir_files):
    return s, filter(lambda fn:
                     fnmatch(path.basename(fn), MODULE_PATTERN),
                     dir_files)


def _import_modules(s, dir_filtered_files):
    return s, map(lambda fn:
                  imp.load_source(path.splitext(path.basename(fn))[0], fn),
                  dir_filtered_files)


def _get_objects(s, imported_modules):
    return s, map(lambda mod:
                  getattr(mod, s['class_name']),
                  imported_modules)


def objects_from_modules(modules_dir, object_name, args=None):
    s = {'modules_dir': modules_dir,
         'class_name': object_name,
         'args': args if args is not None else list()}

    return reduce(lambda func_a, func_b: func_b(*func_a),
                  [_get_dir_content,
                   _filter_only_files,
                   _filter_by_pattern,
                   _import_modules,
                   _get_objects],
                  (s, None))[1]


def imports_from_modules(modules_dir, args=None):
    s = {'modules_dir': modules_dir,
         'args': args if args is not None else list()}

    return reduce(lambda func_a, func_b: func_b(*func_a),
                  [_get_dir_content,
                   _filter_only_files,
                   _filter_by_pattern,
                   _import_modules],
                  (s, None))[1]
