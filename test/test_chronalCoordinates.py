from unittest import TestCase

from aoc.day06 import ChronalCoordinates


class TestChronalCoordinates(TestCase):
    def setUp(self):
        self.cc = ChronalCoordinates.__new__(ChronalCoordinates)

    def test_create_empty_matrix(self):
        self.assertEqual([[' ', ' '],
                          [' ', ' ']], self.cc._create_empty_matrix(2))
        self.assertEqual([[' ', ' ', ' '],
                          [' ', ' ', ' '],
                          [' ', ' ', ' ']], self.cc._create_empty_matrix(3))

    def test_place_coordinates(self):
        self.cc.MATRIX_SIZE = 10
        self.cc.matrix = self.cc._create_empty_matrix(11)
        self.cc.content = ['1, 1', '8, 3', '5, 5']

        self.cc._place_coordinates()

        self.assertEqual('C0', self.cc.matrix[1][1])
        self.assertEqual('C1', self.cc.matrix[8][3])
        self.assertEqual('C2', self.cc.matrix[5][5])

    def test_single_chronal_generator(self):
        result = [(x, y) for x, y in self.cc._chronal_generator(2, 2, 1, 4)]
        self.assertEqual([(2, 3), (3, 2), (2, 1), (1, 2)], result)

    def test_double_chronal_generator(self):
        result = [(x, y) for x, y in self.cc._chronal_generator(2, 2, 2, 5)]
        self.assertEqual(
            [(1, 3), (2, 4), (3, 3), (4, 2), (3, 1), (2, 0), (1, 1), (0, 2)], result)

    def test_chronal_generator_dont_go_into_negative(self):
        result = [(x, y) for x, y in self.cc._chronal_generator(0, 0, 1, 3)]
        self.assertEqual([(0, 1), (1, 0)], result)

    def test_chronal_generator_dont_go_over_maximum(self):
        result = [(x, y) for x, y in self.cc._chronal_generator(2, 2, 2, 3)]
        self.assertEqual([(2, 0), (1, 1), (0, 2)], result)

    def test_find_coordinate_if_starting_at_coordinate(self):
        self.cc.matrix = self.cc._create_empty_matrix(3)
        self.cc.content = ['0, 0']
        self.cc._place_coordinates()

        self.assertEqual('C0', self.cc._find_closest_coordinate(0, 0))

    def test_find_coordinate_if_coordinate_is_neighbouring(self):
        self.cc.matrix = self.cc._create_empty_matrix(3)
        self.cc.content = ['0, 1']
        self.cc._place_coordinates()

        self.assertEqual('0', self.cc._find_closest_coordinate(0, 0))

    def test_find_coordinate_dot_if_two_coordinates_are_neighbouring(self):
        self.cc.matrix = self.cc._create_empty_matrix(5)
        self.cc.content = ['2, 0', '0, 2']
        self.cc._place_coordinates()

        self.assertEqual('.', self.cc._find_closest_coordinate(0, 0))

    def test_find_closest(self):
        self.cc.MATRIX_SIZE = 10
        self.cc.matrix = self.cc._create_empty_matrix(11)
        self.cc.content = ['1, 1', '8, 3', '5, 5']
        self.cc._place_coordinates()

        self.assertEqual(['0', '0', '0', '0', '0', '.', '1'], [self.cc._find_closest_coordinate(x, y) for x, y in [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)]])

    def test_fill_matrix(self):
        self.cc.MATRIX_SIZE = 11
        self.cc.matrix = self.cc._create_empty_matrix(11)
        self.cc.content = ['1, 1', '1, 6', '8, 3', '3, 4', '5, 5', '8, 9']
        self.cc._place_coordinates()

        self.cc._fill_matrix()

        self.assertEqual([['0', '0', '0', '0', '.', '1', '1', '1', '1', '1', '1'],
                          ['0', 'C0', '0', '0', '.', '1', 'C1', '1', '1', '1', '1'],
                          ['0', '0', '0', '3', '3', '.', '1', '1', '1', '1', '1'],
                          ['0', '0', '3', '3', 'C3', '3', '.', '.', '.', '.', '.'],
                          ['0', '0', '3', '3', '3', '4', '4', '4', '4', '5', '5'],
                          ['.', '.', '4', '4', '4', 'C4', '4', '4', '4', '5', '5'],
                          ['2', '2', '2', '2', '4', '4', '4', '4', '5', '5', '5'],
                          ['2', '2', '2', '2', '2', '4', '4', '5', '5', '5', '5'],
                          ['2', '2', '2', 'C2', '2', '2', '.', '5', '5', 'C5', '5'],
                          ['2', '2', '2', '2', '2', '2', '.', '5', '5', '5', '5'],
                          ['2', '2', '2', '2', '2', '2', '.', '5', '5', '5', '5']], self.cc.matrix)

    def test_remove_non_candidates(self):
        self.cc.MATRIX_SIZE = 11
        self.cc.content = ['1, 1', '1, 6', '8, 3', '3, 4', '5, 5', '8, 9']
        self.cc.matrix = self.cc._create_empty_matrix(11)
        self.cc._place_coordinates()
        self.cc._fill_matrix()

        self.cc._remove_non_candidates()

        self.assertEqual([[None, None, None, None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None, None, None, None],
                          [None, None, None, '3', '3', None, None, None, None, None, None],
                          [None, None, '3', '3', None, '3', None, None, None, None, None],
                          [None, None, '3', '3', '3', '4', '4', '4', '4', None, None],
                          [None, None, '4', '4', '4', None, '4', '4', '4', None, None],
                          [None, None, None, None, '4', '4', '4', '4', None, None, None],
                          [None, None, None, None, None, '4', '4', None, None, None, None],
                          [None, None, None, None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None, None, None, None]], self.cc.matrix)

    def test_find_largest_area(self):
        self.cc.MATRIX_SIZE = 11
        self.cc.content = ['1, 1', '1, 6', '8, 3', '3, 4', '5, 5', '8, 9']
        self.cc.matrix = self.cc._create_empty_matrix(11)
        self.cc._place_coordinates()
        self.cc._fill_matrix()

        self.assertEqual(('4', 16), self.cc.find_largest_area())

    def test_run_find_largest_area(self):
        print(ChronalCoordinates('../resources/aoc6.txt').find_largest_area())
