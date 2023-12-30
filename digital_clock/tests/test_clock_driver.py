import unittest

from digital_clock.tests.test_doubles.mock_time_sink import MockTimeSink
from digital_clock.tests.test_doubles.mock_time_source import MockTimeSource


class TestClockDriver(unittest.TestCase):
    def setUp(self) -> None:
        self.source = MockTimeSource()
        self.sink = MockTimeSink(self.source)
        self.source.register_observer(self.sink)

    def test_time_change(self):
        param_list = [
            (3, 4, 5),
            (7, 8, 9)
        ]

        for p1, p2, p3 in param_list:
            with self.subTest(msg=f"Expected values - hours: {p1}, minutes: {p2}, seconds: {p3}"):
                self.source.set_time(p1, p2, p3)
                self.assert_sink_equals(self.sink, p1, p2, p3)

    def assert_sink_equals(self, sink: MockTimeSink, p1, p2, p3):
        self.assertEqual(p1, sink.get_hours())
        self.assertEqual(p2, sink.get_minutes())
        self.assertEqual(p3, sink.get_seconds())

    def test_multiple_sinks(self):
        sink2 = MockTimeSink(self.source)
        self.source.register_observer(sink2)
        self.source.set_time(12, 13, 14)
        self.assert_sink_equals(self.sink, 12, 13, 14)
        self.assert_sink_equals(sink2, 12, 13, 14)


if __name__ == '__main__':
    unittest.main()
