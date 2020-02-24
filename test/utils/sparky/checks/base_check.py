import abc


class BaseCheck(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def do(self):
        return False

    @abc.abstractmethod
    def tell(self):
        return False
