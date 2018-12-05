from unittest import TestCase

from aoc.day01 import ChronalCalibration


class TestChronalCalibration(TestCase):

    def test_calibrate(self):
        chronal_calibration = ChronalCalibration.__new__(ChronalCalibration)
        chronal_calibration.content = [1, -1, 0]
        self.assertEqual(chronal_calibration.calibrate(), 0)

    def test_double_frequency(self):
        chronal_calibration = ChronalCalibration.__new__(ChronalCalibration)
        chronal_calibration.content = [1, -1, 0]
        self.assertEquals(chronal_calibration.find_double_frequency(), 0)

    def test_run_calibrate(self):
        print(ChronalCalibration('../resources/aoc1.txt').calibrate())


