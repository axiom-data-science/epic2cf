#!python
# coding=utf-8

__version__ = '0.0.1'

import logging
logger = logging.getLogger("epic2cf")
logger.addHandler(logging.NullHandler())
logger.addHandler(logging.StreamHandler())

from epic2cf.data import epic_map


class DotDict(object):
    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def get(self, key):
        return getattr(self, key, None)

    def __repr__(self):
        import pprint
        return pprint.pformat(vars(self), indent=2)


class mapping(object):
    @staticmethod
    def get(epic_code):
        try:
            epic_code = int(epic_code)
        except ValueError:
            logger.error("EPIC code '{0}'' could not be converted to an integer.".format(epic_code))
            return None

        epic = epic_map.get(epic_code)
        if epic is not None:
            return DotDict(**epic)
        else:
            logger.error("EPIC code {0} not recognized".format(epic_code))
            return None
