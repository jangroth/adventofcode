from collections import defaultdict
from unittest import TestCase

from aoc.day04 import ReposeRecord


class TestReposeRecord(TestCase):

    def setUp(self):
        self.rr = ReposeRecord.__new__(ReposeRecord)
        self.rr.guards = defaultdict(lambda: defaultdict(int))

    def test_should_parse_guard_change(self):
        self.assertEqual(False, self.rr._is_guard_change('[1518-08-14 00:55] wakes up'))
        self.assertEqual(False, self.rr._is_guard_change('[1518-06-07 00:33] falls asleep'))
        self.assertEqual(True, self.rr._is_guard_change('[1518-09-19 23:49] Guard #1597 begins shift'))

    def test_should_parse_sleep_start(self):
        self.assertEqual(False, self.rr._is_sleep_start('[1518-08-14 00:55] wakes up'))
        self.assertEqual(True, self.rr._is_sleep_start('[1518-06-07 00:33] falls asleep'))
        self.assertEqual(False, self.rr._is_sleep_start('[1518-09-19 23:49] Guard #1597 begins shift'))

    def test_should_parse_sleep_stop(self):
        self.assertEqual(True, self.rr._is_sleep_stop('[1518-08-14 00:55] wakes up'))
        self.assertEqual(False, self.rr._is_sleep_stop('[1518-06-07 00:33] falls asleep'))
        self.assertEqual(False, self.rr._is_sleep_stop('[1518-09-19 23:49] Guard #1597 begins shift'))

    def test_should_parse_guard_id_on_guard_change(self):
        self.assertEqual('#1597', self.rr._get_guard_id('[1518-09-19 23:49] Guard #1597 begins shift'))

    def test_should_parse_minute(self):
        self.assertEqual(55, self.rr._get_minute('[1518-08-14 00:55] wakes up'))
        self.assertEqual(33, self.rr._get_minute('[1518-06-07 00:33] falls asleep'))

    def test_should_count_sleepy_guards(self):
        self.rr._record_sleep('#1', 0, 3)
        self.rr._record_sleep('#1', 2, 4)
        self.rr._record_sleep('#2', 0, 1)

        self.assertEqual({'#1': {'0': 1, '1': 1, '2': 2, '3': 1, 'total': 5},
                          '#2': {'0': 1, 'total': 1}}, self.rr.guards)

    def test_should_parse_content(self):
        self.rr.content = [
            '[1518-11-04 00:02] Guard #99 begins shift',
            '[1518-11-04 00:36] falls asleep',
            '[1518-11-04 00:38] wakes up'
        ]

        self.rr._parse_content()

        self.assertEqual({'#99': {'36': 1, '37': 1, 'total': 2}}, self.rr.guards)

    def test_should_find_sleepiest_guard(self):
        self.rr.content = [
            '[1518-11-01 00:00] Guard #10 begins shift',
            '[1518-11-01 00:05] falls asleep',
            '[1518-11-01 00:25] wakes up',
            '[1518-11-01 00:30] falls asleep',
            '[1518-11-01 00:55] wakes up',
            '[1518-11-01 23:58] Guard #99 begins shift',
            '[1518-11-02 00:40] falls asleep',
            '[1518-11-02 00:50] wakes up',
            '[1518-11-03 00:05] Guard #10 begins shift',
            '[1518-11-03 00:24] falls asleep',
            '[1518-11-03 00:29] wakes up',
            '[1518-11-04 00:02] Guard #99 begins shift',
            '[1518-11-04 00:36] falls asleep',
            '[1518-11-04 00:46] wakes up',
            '[1518-11-05 00:03] Guard #99 begins shift',
            '[1518-11-05 00:45] falls asleep',
            '[1518-11-05 00:55] wakes up'
        ]

        self.assertEqual(('#10', 50, 24), self.rr.find_sleepiest_guard())

    def test_should_find_sleepiest_minute(self):
        self.rr.content = [
            '[1518-11-01 00:00] Guard #10 begins shift',
            '[1518-11-01 00:05] falls asleep',
            '[1518-11-01 00:25] wakes up',
            '[1518-11-01 00:30] falls asleep',
            '[1518-11-01 00:55] wakes up',
            '[1518-11-01 23:58] Guard #99 begins shift',
            '[1518-11-02 00:40] falls asleep',
            '[1518-11-02 00:50] wakes up',
            '[1518-11-03 00:05] Guard #10 begins shift',
            '[1518-11-03 00:24] falls asleep',
            '[1518-11-03 00:29] wakes up',
            '[1518-11-04 00:02] Guard #99 begins shift',
            '[1518-11-04 00:36] falls asleep',
            '[1518-11-04 00:46] wakes up',
            '[1518-11-05 00:03] Guard #99 begins shift',
            '[1518-11-05 00:45] falls asleep',
            '[1518-11-05 00:55] wakes up'
        ]

        self.assertEqual(('#99', 45, 3), self.rr.find_sleepiest_minute())

    def test_run_find_sleepiest_guard(self):
        print(ReposeRecord('../resources/aoc4.txt').find_sleepiest_guard())

    def test_run_find_sleepiest_minute(self):
        print(ReposeRecord('../resources/aoc4.txt').find_sleepiest_minute())
