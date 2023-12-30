from abc import ABCMeta, abstractmethod


class Modem(metaclass=ABCMeta):
    @abstractmethod
    def dial(self):
        pass

    @abstractmethod
    def hangup(self):
        pass

    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def receive(self):
        pass


class DedicatedModem(metaclass=ABCMeta):
    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def receive(self):
        pass


class ModemImplementation(metaclass=ABCMeta):
    @abstractmethod
    def dial(self):
        pass

    @abstractmethod
    def hangup(self):
        pass

    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def receive(self):
        pass


class ModemConnectionController(Modem, DedicatedModem, metaclass=ABCMeta):
    def __init__(self, modem_imp: ModemImplementation):
        self.__its_modem_imp = modem_imp

    @abstractmethod
    def dial(self):
        pass

    @abstractmethod
    def hangup(self):
        pass

    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def receive(self):
        pass

    def _dial_imp(self):
        self.__its_modem_imp.dial()

    def _hangup_imp(self):
        self.__its_modem_imp.hangup()

    def _send_imp(self):
        self.__its_modem_imp.send()

    def _receive_imp(self):
        self.__its_modem_imp.receive()


class DedModemController(ModemConnectionController):
    def dial(self):
        pass

    def hangup(self):
        pass

    def send(self):
        self._send_imp()

    def receive(self):
        self._receive_imp()


class DialModemController(ModemConnectionController):
    def dial(self):
        self._dial_imp()

    def hangup(self):
        self._hangup_imp()

    def send(self):
        self._send_imp()

    def receive(self):
        self._receive_imp()


class HayesModem(ModemImplementation):
    def dial(self):
        pass

    def hangup(self):
        pass

    def send(self):
        pass

    def receive(self):
        pass


class ErniesModem(ModemImplementation):
    def dial(self):
        pass

    def hangup(self):
        pass

    def send(self):
        pass

    def receive(self):
        pass


class USRoboticsModem(ModemImplementation):
    def dial(self):
        pass

    def hangup(self):
        pass

    def send(self):
        pass

    def receive(self):
        pass