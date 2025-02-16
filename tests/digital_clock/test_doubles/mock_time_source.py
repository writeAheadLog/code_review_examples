from digital_clock.base.subject import Subject
from digital_clock.base.time_source import TimeSource


class MockTimeSource(TimeSource, Subject):
    def __init__(self):
        super().__init__()
        self.__its_hours = None
        self.__its_minutes = None
        self.__its_seconds = None
        self.ts_imp = Subject()

    def set_time(self, hours: int, minutes: int, seconds: int):
        self.__its_hours = hours
        self.__its_minutes = minutes
        self.__its_seconds = seconds
        self.notify_observers()

    def get_hours(self):
        return self.__its_hours

    def get_minutes(self):
        return self.__its_minutes

    def get_seconds(self):
        return self.__its_seconds
