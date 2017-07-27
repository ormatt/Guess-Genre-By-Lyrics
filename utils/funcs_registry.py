from collections import defaultdict
import functools


def with_metaclass(mcls):
    """
    Metaclass wrapper as Python 2 and 3 use different syntax for metaclasses
    :param mcls: Metaclass for the given class 
    :return: Wrapper that creates a class from the metaclass
    """
    def wrapper(cls):
        attributes = cls.__dict__.copy()
        return mcls(cls.__name__, cls.__bases__, attributes)
    return wrapper


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


@with_metaclass(RegistryType)
class RegistryClass():
    def __getattr__(self, item):
        return functools.partial(self.add_func, item)
