from unittest import TestCase

from aoc.day01 import ChronalCalibration


class TestChronalCalibration(TestCase):

    def test_calibrate(self):
        chronal_calibration = ChronalCalibration.__new__(ChronalCalibration)
        chronal_calibration.content = [1, -1, 0]
        self.assertEqual(0, chronal_calibration.calibrate())

    def test_double_frequency(self):
        chronal_calibration = ChronalCalibration.__new__(ChronalCalibration)
        chronal_calibration.content = [1, -2, 3, 1]
        self.assertEqual(2, chronal_calibration.find_first_double_frequency())

    def test_run_calibrate(self):
        print("Calibrate: {}".format(ChronalCalibration('../resources/aoc1.txt').calibrate()))

    def test_find_first_double_frequency(self):
        print("First duplicate frequency: {}".format(ChronalCalibration('../resources/aoc1.txt').find_first_double_frequency()))
