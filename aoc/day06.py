import string
from collections import defaultdict


class ChronalCoordinates:
    MATRIX_SIZE = 10

    def __init__(self, path):
        with open(path) as f:
            content = f.readlines()
        self.content = sorted([x.strip() for x in content])
        self.matrix = self._create_empty_matrix(self.MATRIX_SIZE)

    def _create_empty_matrix(self, size):
        return [['0' for _ in range(size)] for _ in range(size)]

    def _place_coordinates(self):
        for index, coordinate in enumerate(self.content):
            row, column = [int(x) for x in coordinate.replace(' ', '').split(',')]
            self.matrix[row][column] = 'C{}'.format(index)

    def _find_closest_coordinate(self, row, column):
        if self.matrix[row][column].isupper():
            return self.matrix[row][column]
        radius = 1
        closest_coordinates = []
        while True:
            for test_row, test_column in self._chronal_generator(row, column, radius, self.MATRIX_SIZE):
                if self.matrix[test_row][test_column].startswith('C'):
                    closest_coordinates.append(self.matrix[test_row][test_column][1:])
            if not closest_coordinates:
                radius += 1
            elif len(closest_coordinates) == 1:
                return closest_coordinates[0]
            else:
                return '.'

    def _fill_matrix(self):
        for row in range(self.MATRIX_SIZE):
            for column in range(self.MATRIX_SIZE):
                closest_coordinate = self._find_closest_coordinate(row, column)
                self.matrix[row][column] = closest_coordinate

    def _remove_non_candidates(self):
        non_candidates = {'.'}
        for i in range(self.MATRIX_SIZE):
            non_candidates.add(self.matrix[0][i])
            non_candidates.add(self.matrix[self.MATRIX_SIZE - 1][i])
            non_candidates.add(self.matrix[i][0])
            non_candidates.add(self.matrix[i][self.MATRIX_SIZE - 1])
        for row in range(self.MATRIX_SIZE):
            for column in range(self.MATRIX_SIZE):
                current_spot = self.matrix[row][column]
                if current_spot in non_candidates or current_spot.startswith('C'):
                    self.matrix[row][column] = None

    def find_largest_area(self):
        self._place_coordinates()
        self._remove_non_candidates()
        finites = defaultdict(int)
        for row in range(self.MATRIX_SIZE):
            for column in range(self.MATRIX_SIZE):
                value = self.matrix[row][column]
                if value:
                    finites[value] += 1
        return sorted(finites.items(), key=lambda x: x[1], reverse=True)[0]

    def _chronal_generator(self, row, column, distance, max):
        current_dir = 'southeast'
        current_column = column
        current_row = row - distance
        is_complete = False
        while not is_complete:
            print(current_row, current_column)
            if 0 <= current_row < max and 0 <= current_column < max:
                yield current_row, current_column
            if current_dir == 'southeast':
                if current_column < column + distance:
                    current_row += 1
                    current_column += 1
                else:
                    current_dir = 'southwest'
            if current_dir == 'southwest':
                if current_row < row + distance:
                    current_row += 1
                    current_column -= 1
                else:
                    current_dir = 'northwest'
            if current_dir == 'northwest':
                if current_column > column - distance:
                    current_row -= 1
                    current_column -= 1
                else:
                    current_dir = 'northeast'
            if current_dir == 'northeast':
                if current_row > row - distance and current_row != row - distance + 1 and current_column != column - 1:
                    current_row -= 1
                    current_column += 1
                else:
                    is_complete = True

    def print_matrix(self):
        for column in range(11):
            for row in range(11):
                print(self.matrix[row][column], end='', flush=True)
            print()
