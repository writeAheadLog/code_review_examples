import unittest
from unittest.mock import MagicMock

from modem_bridge.modem import DialModemController, HayesModem, ErniesModem, DedModemController, \
    USRoboticsModem, ModemImplementation, ModemConnectionController


def mock_path_modem_method(modem_imp: ModemImplementation):
    modem_imp.dial = MagicMock()
    modem_imp.hangup = MagicMock()
    modem_imp.send = MagicMock()
    modem_imp.receive = MagicMock()
    return modem_imp


def call_all_methods(modem_controller: ModemConnectionController):
    modem_controller.dial()
    modem_controller.send()
    modem_controller.receive()
    modem_controller.hangup()


def assert_called_correctly(modem_imp, dedicated=False):
    if dedicated:
        modem_imp.dial.assert_not_called()
        modem_imp.hangup.assert_not_called()
    else:
        modem_imp.dial.assert_called_once_with()
        modem_imp.hangup.assert_called_once_with()
    modem_imp.send.assert_called_once_with()
    modem_imp.receive.assert_called_once_with()


def run_sut_methods(modem, modem_controller: ModemConnectionController.__call__):
    modem_imp = modem()
    mock_path_modem_method(modem_imp)
    dial_mc = modem_controller(modem_imp=modem_imp)
    call_all_methods(dial_mc)
    return modem_imp


class TestModem(unittest.TestCase):
    def setUp(self) -> None:
        self.modem_list = [HayesModem, ErniesModem, USRoboticsModem]

    def test_run_dial_modem(self):
        self.is_method_called_correctly(DialModemController, dedicated=False)

    def test_run_ded_modem(self):
        self.is_method_called_correctly(DedModemController, dedicated=True)

    def is_method_called_correctly(self, modem_controller: ModemConnectionController.__call__, dedicated: bool):
        for modem in self.modem_list:
            with self.subTest(msg=f"{modem} Case"):
                modem_imp = run_sut_methods(modem, modem_controller)
                assert_called_correctly(modem_imp, dedicated)


if __name__ == '__main__':
    unittest.main()
