from fnmatch import fnmatch
import os
import os.path as path
from constants import MODULE_PATTERN
from functools import reduce
import imp


def get_dir_content(s, _):
    return s, map(lambda fn: path.join(s['modules_dir'], fn),
                  os.listdir(s['modules_dir']))


def filter_only_files(s, dir_content):
    return s, filter(lambda fn: path.isfile(path.join(s['modules_dir'], fn)),
                     dir_content)


def filter_by_pattern(s, dir_files):
    return s, filter(lambda fn:
                     fnmatch(path.basename(fn), MODULE_PATTERN),
                     dir_files)


def import_modules(s, dir_filtered_files):
    return s, map(lambda fn:
                  imp.load_source(path.splitext(path.basename(fn))[0], fn),
                  dir_filtered_files)


def get_objects(s, imported_modules):
    return s, map(lambda mod:
                  getattr(mod, s['class_name']),
                  imported_modules)


def objects_from_modules(modules_dir, class_name, args=None):
    s = {'modules_dir': modules_dir,
         'class_name': class_name,
         'args': args if args is not None else list()}

    return reduce(lambda func_a, func_b: func_b(*func_a),
                  [get_dir_content,
                   filter_only_files,
                   filter_by_pattern,
                   import_modules,
                   get_objects],
                  (s, None))[1]
