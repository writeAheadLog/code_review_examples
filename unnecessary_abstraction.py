from abc import ABCMeta, abstractmethod


class BaseDataSourceHook(metaclass=ABCMeta):
    pass


class RedshiftHook(BaseDataSourceHook):
    pass


class FeatureGenerator(metaclass=ABCMeta):

    def __init__(self, data_source_hook: BaseDataSourceHook):
        self.__its_hook = data_source_hook

    @abstractmethod
    def generate(self):
        pass
