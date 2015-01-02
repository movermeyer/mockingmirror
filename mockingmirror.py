import mock

__version__ = "0.dev0"

class ReturnValueNotSet(object):
    __slots__=[]
    def __str__(self):
        return "RETURN_VALUE_NOT_SET"

RETURN_VALUE_NOT_SET = ReturnValueNotSet()


class Invocation(object):
    def __init__(self, mirror, expected_args, expected_kargs,
                 expected_count=slice(None,None,None)):
        self.mirror = mirror
        self.expected_count = expected_count
        self.mirror.mock.return_value = RETURN_VALUE_NOT_SET

    def __call__(self, side_effect):
        self.mirror.mock.side_effect = side_effect

    def __setitem__(self, invocation_count, return_value):
        self.mirror.mock.return_value = return_value

    def __getitem__(self, invocation_count):
        return Invocation(self.mock, expected_count)

class Mirror(object):
    def __init__(self, name=None, parent=None, mirrors=None):
        if mirrors is None:
            mirrors = []
        self.mock = mock.NonCallableMock()
        self.name = name
        self.parent = parent
        self.spec = set()
        self.mirrors = mirrors
        self.mirrors.append(self)
        self.is_callable = False
        self.mock = mock.NonCallableMock()
        if name is not None:
            setattr(self.parent.mock, self.name, self.mock)

    def __getattr__(self, name):
        mirror = Mirror(name, self, self.mirrors)
        object.__setattr__(self, name, mirror)
        self.spec.add(name)
        return mirror

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)
        if name != "mock":
            setattr(self.mock, name, value)

    def __call__(self, *expected_args, **expected_kargs):
        if not self.is_callable:
            self.is_callable = True
            self.mock = mock.Mock()
            setattr(self.parent.mock, self.name, self.mock)
        return Invocation(self, expected_args, expected_kargs)

    def freeze(self):
        self.mock.mock_add_spec(list(self.spec), False)

    def freezeall(self):
        for mirror in self.mirrors:
            mirror.freeze()

def mirrored(setup):
    def wrap_setup(self):
        self.mirror = Mirror()
        self.mock = self.mirror.mock
        setup(self, self.mirror, self.mock)
        self.mirror.freezeall()
    return wrap_setup
