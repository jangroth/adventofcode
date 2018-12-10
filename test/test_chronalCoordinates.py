from unittest import TestCase

from aoc.day06 import ChronalCoordinates


class TestChronalCoordinates(TestCase):
    def setUp(self):
        self.cc = ChronalCoordinates.__new__(ChronalCoordinates)

    def test_create_empty_matrix(self):
        self.assertEqual([['0', '0'],
                          ['0', '0']], self.cc._create_empty_matrix(2))
        self.assertEqual([['0', '0', '0'],
                          ['0', '0', '0'],
                          ['0', '0', '0']], self.cc._create_empty_matrix(3))

    def test_find_coordinate_if_coordinate_for_coordinate(self):
        self.cc.matrix = self.cc._create_empty_matrix(3)
        self.cc.matrix[0][0] = 'A'

        self.assertEqual('A', self.cc._find_closest_coordinate(0, 0))

    def test_find_coordinate_A_if_coordinate_is_neighbouring(self):
        self.cc.matrix = self.cc._create_empty_matrix(3)
        self.cc.matrix[1][1] = 'A'

        self.assertEqual('a', self.cc._find_closest_coordinate(0, 0))

    def test_find_coordinate_dot_if_two_coordinates_are_neighbouring(self):
        self.cc.matrix = self.cc._create_empty_matrix(5)
        self.cc.matrix[2][0] = 'A'
        self.cc.matrix[0][2] = 'B'

        self.assertEqual('.', self.cc._find_closest_coordinate(0, 0))

    def test_single_chronal_generator(self):
        result = [(x, y) for x, y in self.cc._chronal_generator(2, 2, 1, 4)]
        self.assertEqual([(1, 2), (2, 3), (3, 2), (2, 1)], result)

    def test_double_chronal_generator(self):
        result = [(x, y) for x, y in self.cc._chronal_generator(2, 2, 2, 5)]
        self.assertEqual(
            [(0, 2), (1, 3), (2, 4), (3, 3), (4, 2), (3, 1), (2, 0), (1, 1)], result)

    def test_chronal_generator_dont_go_into_negative(self):
        result = [(x, y) for x, y in self.cc._chronal_generator(0, 0, 1, 3)]
        self.assertEqual([(0, 1), (1, 0)], result)

    def test_chronal_generator_dont_go_over_maximum(self):
        result = [(x, y) for x, y in self.cc._chronal_generator(2, 2, 2, 3)]
        self.assertEqual([(0, 2), (2, 0), (1, 1)], result)

    def test_find_closest(self):
        self.cc.MATRIX_SIZE = 10
        self.cc.matrix = self.cc._create_empty_matrix(11)
        self.cc.matrix[1][1] = 'A'
        self.cc.matrix[8][3] = 'C'
        self.cc.matrix[5][5] = 'E'

        self.assertEqual('a', self.cc._find_closest_coordinate(0, 0))
        self.assertEqual('a', self.cc._find_closest_coordinate(1, 0))
        self.assertEqual('a', self.cc._find_closest_coordinate(2, 0))
        self.assertEqual('a', self.cc._find_closest_coordinate(3, 0))
        self.assertEqual('a', self.cc._find_closest_coordinate(4, 0))
        self.assertEqual('.', self.cc._find_closest_coordinate(5, 0))
        self.assertEqual('c', self.cc._find_closest_coordinate(6, 0))

    def test_fill_matrix(self):
        self.cc.MATRIX_SIZE = 11
        self.cc.matrix = self.cc._create_empty_matrix(11)
        self.cc.matrix[1][1] = 'A'
        self.cc.matrix[1][6] = 'B'
        self.cc.matrix[8][3] = 'C'
        self.cc.matrix[3][4] = 'D'
        self.cc.matrix[5][5] = 'E'
        self.cc.matrix[8][9] = 'F'

        self.cc._fill_matrix()

        self.assertEqual([['a', 'a', 'a', 'a', '.', 'b', 'b', 'b', 'b', 'b', 'b'],
                          ['a', 'A', 'a', 'a', '.', 'b', 'B', 'b', 'b', 'b', 'b'],
                          ['a', 'a', 'a', 'd', 'd', '.', 'b', 'b', 'b', 'b', 'b'],
                          ['a', 'a', 'd', 'd', 'D', 'd', '.', '.', '.', '.', '.'],
                          ['a', 'a', 'd', 'd', 'd', 'e', 'e', 'e', 'e', 'f', 'f'],
                          ['.', '.', 'e', 'e', 'e', 'E', 'e', 'e', 'e', 'f', 'f'],
                          ['c', 'c', 'c', 'c', 'e', 'e', 'e', 'e', 'f', 'f', 'f'],
                          ['c', 'c', 'c', 'c', 'c', 'e', 'e', 'f', 'f', 'f', 'f'],
                          ['c', 'c', 'c', 'C', 'c', 'c', '.', 'f', 'f', 'F', 'f'],
                          ['c', 'c', 'c', 'c', 'c', 'c', '.', 'f', 'f', 'f', 'f'],
                          ['c', 'c', 'c', 'c', 'c', 'c', '.', 'f', 'f', 'f', 'f']], self.cc.matrix)

    def test_remove_non_candidates(self):
        self.cc.MATRIX_SIZE = 11
        self.cc.matrix = self.cc._create_empty_matrix(11)
        self.cc.matrix[1][1] = 'A'
        self.cc.matrix[1][6] = 'B'
        self.cc.matrix[8][3] = 'C'
        self.cc.matrix[3][4] = 'D'
        self.cc.matrix[5][5] = 'E'
        self.cc.matrix[8][9] = 'F'

        self.cc._fill_matrix()
        self.cc._remove_non_candidates()

        self.assertEqual([[None, None, None, None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None, None, None, None],
                          [None, None, None, 'd', 'd', None, None, None, None, None, None],
                          [None, None, 'd', 'd', None, 'd', None, None, None, None, None],
                          [None, None, 'd', 'd', 'd', 'e', 'e', 'e', 'e', None, None],
                          [None, None, 'e', 'e', 'e', None, 'e', 'e', 'e', None, None],
                          [None, None, None, None, 'e', 'e', 'e', 'e', None, None, None],
                          [None, None, None, None, None, 'e', 'e', None, None, None, None],
                          [None, None, None, None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None, None, None, None]], self.cc.matrix)

    def test_find_largest_area(self):
        self.cc.MATRIX_SIZE = 11
        self.cc.matrix = self.cc._create_empty_matrix(11)
        self.cc.matrix[1][1] = 'A'
        self.cc.matrix[1][6] = 'B'
        self.cc.matrix[8][3] = 'C'
        self.cc.matrix[3][4] = 'D'
        self.cc.matrix[5][5] = 'E'
        self.cc.matrix[8][9] = 'F'

        self.cc._fill_matrix()

        self.assertEqual(('e', 16), self.cc.find_largest_area())

    def test_run_find_largest_area(self):
        print(ChronalCoordinates('../resources/aoc6.txt').find_largest_area())
