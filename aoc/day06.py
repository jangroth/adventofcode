class ChronalCoordinates:
    MATRIX_SIZE = 10

    def __init__(self, path):
        with open(path) as f:
            content = f.readlines()
        self.content = sorted([x.strip() for x in content])
        self.matrix = self._create_empty_matrix(self.MATRIX_SIZE)

    def _create_empty_matrix(self, size):
        return [['0' for _ in range(size)] for _ in range(size)]

    def _find_closest_coordinate(self, row, column):
        if self.matrix[row][column].isupper():
            return self.matrix[row][column]
        is_complete = False
        radius = 1
        closest_coordinates = []
        while not is_complete:
            for row, column in self._chronal_generator(row, column, radius, self.MATRIX_SIZE):
                if self.matrix[row][column].isupper():
                    closest_coordinates.append(self.matrix[row][column].lower())
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

    def find_largest_area(self):
        pass

    def _chronal_generator(self, row, column, distance, max):
        current_dir = 'east'
        current_column = column - distance
        current_row = row - distance
        is_complete = False
        while not is_complete:
            if 0 <= current_row < max and 0 <= current_column < max:
                yield current_row, current_column
            if current_dir == 'east':
                if current_column < column + distance:
                    current_column += 1
                else:
                    current_row += 1
                    current_dir = 'south'
            elif current_dir == 'south':
                if current_row < row + distance:
                    current_row += 1
                else:
                    current_column -= 1
                    current_dir = 'west'
            elif current_dir == 'west':
                if current_column > column - distance:
                    current_column -= 1
                else:
                    current_row -= 1
                    current_dir = 'north'
            elif current_dir == 'north':
                if current_row > row - distance:
                    current_row -= 1
                else:
                    is_complete = True

    def print_matrix(self):
        for column in range(11):
            for row in range(11):
                print(self.matrix[row][column], end='', flush=True)
            print()
