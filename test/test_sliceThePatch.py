from unittest import TestCase

from aoc.day03 import SliceThePatch


class TestSliceThePatch(TestCase):

    def test_count_overlap(self):
        slice_the_patch = SliceThePatch.__new__(SliceThePatch)
        slice_the_patch.content = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']

        self.assertEqual(4, slice_the_patch.count_overlap())
