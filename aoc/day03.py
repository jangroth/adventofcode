import collections


class SliceThePatch:
    MATRIX_SIZE = 100

    def __init__(self, path):
        with open(path) as f:
            content = f.readlines()
        self.content = [x.strip() for x in content]
        self.patches = [self._line_to_patch(x) for x in self.content]
        self.matrix = self._create_empty_matrix(1000)

    def _create_empty_matrix(self, size):
        return ['0' * size for _ in range(size)]

    def _place_patches(self):
        for patch in self.patches:
            self._place_patch(patch)

    def _place_patch(self, patch):
        for row in range(patch.y1, patch.y2):
            for column in range(patch.x1, patch.x2):
                this_square = self.matrix[row][column]
                if this_square == '0':
                    self.matrix[row] = self.matrix[row][:column] + '1' + self.matrix[row][column + 1:]
                elif this_square == '1':
                    self.matrix[row] = self.matrix[row][:column] + '2' + self.matrix[row][column + 1:]

    def _line_to_patch(self, line):
        Patch = collections.namedtuple('Patch', ['id', 'x1', 'y1', 'x2', 'y2'])
        line_elements = line.split()
        id = int(line_elements[0][1:])
        x1 = int(line_elements[2].split(',')[0])
        y1 = int(line_elements[2].split(',')[1][:-1])
        x2 = int(line_elements[3].split('x')[0]) + x1
        y2 = int(line_elements[3].split('x')[1]) + y1
        return Patch(id=id, x1=x1, y1=y1, x2=x2, y2=y2)

    def count_overlap(self):
        self._place_patches()
        return sum([line.count('2') for line in self.matrix])
