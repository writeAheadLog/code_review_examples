from digital_clock.base.observer import Observer


class Subject:
    def __init__(self):
        self.__its_observer = list()

    def register_observer(self, observer: Observer):
        self.__its_observer.append(observer)

    def notify_observers(self):
        for observer in self.__its_observer:
            observer.update()
