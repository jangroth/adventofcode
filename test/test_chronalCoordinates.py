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

        self.assertEqual('A', self.cc._find_closest_coordinate(0, 0))

    def test_find_coordinate_dot_if_tow_coordinates_are_neighbouring(self):
        self.cc.matrix = self.cc._create_empty_matrix(5)
        self.cc.matrix[2][2] = 'A'
        self.cc.matrix[0][2] = 'B'

        self.assertEqual('.', self.cc._find_closest_coordinate(0, 0))

    def test_single_chronal_generator(self):
        result = [(x, y) for x, y in self.cc._chronal_generator(2, 2, 1, 3)]
        self.assertEqual([(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (2, 1), (1, 1)], result)

    def test_double_chronal_generator(self):
        result = [(x, y) for x, y in self.cc._chronal_generator(2, 2, 2, 4)]
        self.assertEqual(
            [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (4, 3), (4, 2), (4, 1), (4, 0),
             (3, 0), (2, 0), (1, 0), (0, 0)], result)

    def test_chronal_generator_dont_go_into_negative(self):
        result = [(x, y) for x, y in self.cc._chronal_generator(0, 0, 1, 3)]
        self.assertEqual([(0, 1), (1, 1), (1, 0)], result)

    def test_chronal_generator_dont_go_over_maximum(self):
        result = [(x, y) for x, y in self.cc._chronal_generator(2, 2, 2, 3)]
        self.assertEqual([(0, 0), (0, 1), (0, 2), (0, 3), (3, 0), (2, 0), (1, 0), (0, 0)], result)

    def test_find_closest(self):
        self.cc.MATRIX_SIZE = 10
        self.cc.matrix = self.cc._create_empty_matrix(11)
        self.cc.matrix[1][1] = 'A'
        self.cc.matrix[8][3] = 'C'

        # self.assertEqual('a', self.cc._find_closest_coordinate(0, 0))
        # self.assertEqual('a', self.cc._find_closest_coordinate(1, 0))
        # self.assertEqual('a', self.cc._find_closest_coordinate(2, 0))
        self.assertEqual('a', self.cc._find_closest_coordinate(3, 0))
        self.assertEqual('a', self.cc._find_closest_coordinate(4, 0))
        self.assertEqual('.', self.cc._find_closest_coordinate(5, 0))

    def test_fill_matrix(self):
        self.cc.MATRIX_SIZE = 10
        self.cc.matrix = self.cc._create_empty_matrix(11)
        self.cc.matrix[1][1] = 'A'
        self.cc.matrix[1][6] = 'B'
        self.cc.matrix[8][3] = 'C'
        self.cc.matrix[3][4] = 'D'
        self.cc.matrix[5][5] = 'E'
        self.cc.matrix[8][9] = 'F'

        self.cc._fill_matrix()

        print(self.cc.print_matrix())
