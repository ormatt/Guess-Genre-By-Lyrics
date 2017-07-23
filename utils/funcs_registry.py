from collections import defaultdict
import functools


class RegistryType(type):
    _corpora_funcs = defaultdict(set)

    def __getattr__(self, item):
        return functools.partial(self.add_func, item)

    @classmethod
    def add_func(cls, name, func):
        cls._corpora_funcs[name].add(func)

    @classmethod
    def get_funcs(cls, name):
        try:
            return list(cls._corpora_funcs[name])
        except KeyError:
            return []


class RegistryClass(metaclass=RegistryType):
    __metaclass__ = RegistryType

    def __getattr__(self, item):
        return functools.partial(self.add_func, item)
