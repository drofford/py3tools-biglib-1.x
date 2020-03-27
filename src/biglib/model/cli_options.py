import logging

import attr


@attr.s
class Options:
    as_parsed = attr.ib(default=attr.Factory(dict))
    original = attr.ib(default=attr.Factory(dict))
    computed = attr.ib(default=attr.Factory(dict))

    def __attrs_post_init__(self):
        if self.as_parsed is not None:
            v = vars(self.as_parsed)
            if len(v) > 0:
                self.original = v

    def __getitem__(self, key):
        try:
            return self.computed[key]
        except KeyError:
            return self.original[key]

    def __setitem__(self, key, val):
        self.computed[key] = val

    def get(self, key):
        try:
            return self.computed[key]
        except KeyError:
            return self.original[key]

    def put(self, key, val):
        self.computed[key] = val
