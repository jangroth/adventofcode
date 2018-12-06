import collections
from unittest import TestCase

from aoc.day03 import SliceThePatch


class TestSliceThePatch(TestCase):

    def setUp(self):
        self.stp = SliceThePatch.__new__(SliceThePatch)
        self.Patch = collections.namedtuple('Patch', ['id', 'x1', 'y1', 'x2', 'y2'])
        self.stp.overlapping_patches = set()

    def test_convert_line_to_patch(self):
        self.assertEqual(self.Patch(1, 0, 0, 1, 1), self.stp._line_to_patch('#1 @ 0,0: 1x1'))
        self.assertEqual(self.Patch(2, 1, 1, 2, 2), self.stp._line_to_patch('#2 @ 1,1: 1x1'))
        self.assertEqual(self.Patch(3, 1, 3, 5, 7), self.stp._line_to_patch('#3 @ 1,3: 4x4'))

    def test_create_empty_matrix(self):
        self.assertEqual(['00', '00'], self.stp._create_empty_matrix(2))
        self.assertEqual(['000', '000', '000'], self.stp._create_empty_matrix(3))

    def test_place_single_patch(self):
        self.stp.matrix = self.stp._create_empty_matrix(4)
        self.stp._place_patch(self.Patch(3, 1, 1, 3, 3))

        self.assertEqual(['0000', '0330', '0330', '0000'], self.stp.matrix)

    def test_place_another_single_patch(self):
        self.stp.content = ['#1 @ 3,2: 5x4']
        self.stp.patches = [self.stp._line_to_patch(x) for x in self.stp.content]
        self.stp.matrix = self.stp._create_empty_matrix(9)

        self.stp._place_patches()

        self.assertEqual(['000000000', '000000000', '000111110', '000111110', '000111110', '000111110', '000000000', '000000000', '000000000'], self.stp.matrix)

    def test_place_double_patch(self):
        self.stp.matrix = self.stp._create_empty_matrix(4)

        self.stp._place_patch(self.Patch(1, 1, 1, 3, 3))
        self.stp._place_patch(self.Patch(2, 1, 1, 3, 3))

        self.assertEqual(['0000', '0##0', '0##0', '0000'], self.stp.matrix)

    def test_count_overlap(self):
        self.stp.content = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
        self.stp.patches = [self.stp._line_to_patch(x) for x in self.stp.content]
        self.stp.matrix = self.stp._create_empty_matrix(10)

        self.assertEqual(4, self.stp.count_overlap())

    def ignroe_test_find_non_overlapping_patches(self):
        self.stp.content = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
        self.stp.patches = [self.stp._line_to_patch(x) for x in slice_the_patch.content]
        self.stp.matrix = self.stp._create_empty_matrix(10)

        self.assertIn('#3', self.stp.find_non_overlapping_patches())

    def test_run_count_overlap(self):
        print(SliceThePatch('../resources/aoc3.txt').count_overlap())
