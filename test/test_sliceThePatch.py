import collections
from unittest import TestCase

from aoc.day03 import SliceThePatch


class TestSliceThePatch(TestCase):

    def test_convert_line_to_patch(self):
        slice_the_patch = SliceThePatch.__new__(SliceThePatch)
        Patch = collections.namedtuple('Patch', ['id', 'x1', 'y1', 'x2', 'y2'])

        self.assertEqual(Patch(1, 0, 0, 1, 1), slice_the_patch._line_to_patch('#1 @ 0,0: 1x1'))
        self.assertEqual(Patch(2, 1, 1, 2, 2), slice_the_patch._line_to_patch('#2 @ 1,1: 1x1'))
        self.assertEqual(Patch(3, 1, 3, 5, 7), slice_the_patch._line_to_patch('#3 @ 1,3: 4x4'))

    def test_create_empty_matrix(self):
        slice_the_patch = SliceThePatch.__new__(SliceThePatch)

        self.assertEqual(['00', '00'], slice_the_patch._create_empty_matrix(2))
        self.assertEqual(['000', '000', '000'], slice_the_patch._create_empty_matrix(3))

    def test_place_single_patch(self):
        slice_the_patch = SliceThePatch.__new__(SliceThePatch)
        slice_the_patch.matrix = slice_the_patch._create_empty_matrix(4)
        Patch = collections.namedtuple('Patch', ['id', 'x1', 'y1', 'x2', 'y2'])

        slice_the_patch._place_patch(Patch(1, 1, 1, 3, 3))

        self.assertEqual(['0000', '0110', '0110', '0000'], slice_the_patch.matrix)

    def test_place_another_single_patch(self):
        slice_the_patch = SliceThePatch.__new__(SliceThePatch)
        slice_the_patch.content = ['#1 @ 3,2: 5x4']
        slice_the_patch.patches = [slice_the_patch._line_to_patch(x) for x in slice_the_patch.content]
        slice_the_patch.matrix = slice_the_patch._create_empty_matrix(9)

        slice_the_patch._place_patches()

        self.assertEqual(['000000000', '000000000', '000111110', '000111110', '000111110', '000111110', '000000000', '000000000', '000000000'], slice_the_patch.matrix)

    def test_place_double_patch(self):
        slice_the_patch = SliceThePatch.__new__(SliceThePatch)
        slice_the_patch.matrix = slice_the_patch._create_empty_matrix(4)
        Patch = collections.namedtuple('Patch', ['id', 'x1', 'y1', 'x2', 'y2'])

        slice_the_patch._place_patch(Patch(1, 1, 1, 3, 3))
        slice_the_patch._place_patch(Patch(2, 1, 1, 3, 3))

        self.assertEqual(['0000', '0220', '0220', '0000'], slice_the_patch.matrix)

    def test_count_overlap(self):
        slice_the_patch = SliceThePatch.__new__(SliceThePatch)
        slice_the_patch.content = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
        slice_the_patch.patches = [slice_the_patch._line_to_patch(x) for x in slice_the_patch.content]
        slice_the_patch.matrix = slice_the_patch._create_empty_matrix(10)

        self.assertEqual(4, slice_the_patch.count_overlap())

    def test_run_count_overlap(self):
        print(SliceThePatch('../resources/aoc3.txt').count_overlap())
