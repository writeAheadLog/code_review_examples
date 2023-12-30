from abc import ABCMeta, abstractmethod


class TimeSource(metaclass=ABCMeta):
    @abstractmethod
    def get_hours(self):
        pass

    @abstractmethod
    def get_minutes(self):
        pass

    @abstractmethod
    def get_seconds(self):
        pass
