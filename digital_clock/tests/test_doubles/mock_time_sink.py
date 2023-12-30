from digital_clock.base.observer import Observer
from digital_clock.base.time_source import TimeSource


class MockTimeSink(Observer):
    def __init__(self, source: TimeSource):
        self.__its_hours = None
        self.__its_minutes = None
        self.__its_seconds = None
        self.__its_source = source

    def get_hours(self):
        return self.__its_hours

    def get_minutes(self):
        return self.__its_minutes

    def get_seconds(self):
        return self.__its_seconds

    def update(self):
        self.__its_hours = self.__its_source.get_hours()
        self.__its_minutes = self.__its_source.get_minutes()
        self.__its_seconds = self.__its_source.get_seconds()
