from collections import defaultdict


class ChronalCoordinates:
    MATRIX_SIZE = 10

    def __init__(self, path):
        with open(path) as f:
            content = f.readlines()
        self.content = sorted([x.strip() for x in content])
        self.matrix = self._create_empty_matrix(self.MATRIX_SIZE)

    def _create_empty_matrix(self, size):
        return [[' ' for _ in range(size)] for _ in range(size)]

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
                print(test_row, test_column, radius, self.matrix[test_row][test_column].startswith('C'))
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
        directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        current_dir = 0
        current_row, current_column = row - distance, column
        while current_dir < 4:
            current_row += directions[current_dir][0]
            current_column += directions[current_dir][1]
            if 0 <= current_row < max and 0 <= current_column < max:
                yield current_row, current_column

            if (
                    (current_dir == 0 and current_row == row) or
                    (current_dir == 1 and current_column == column) or
                    (current_dir == 2 and current_row == row) or
                    (current_dir == 3 and current_column == column)
            ):
                current_dir += 1

    def print_matrix(self):
        for row in range(11):
            for column in range(11):
                print(':{} '.format(self.matrix[row][column]), end='', flush=True)
            print()
