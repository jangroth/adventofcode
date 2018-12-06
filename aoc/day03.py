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
        for patch in patches:
            self._place_patch(patch)

    def _place_patch(self, patch):
        for x in range(patch.x1, patch.x2):
            for y in range(patch.y1, patch.x2):
                self.matrix[x][y] = '1'

    def _line_to_patch(self, line):
        Patch = collections.namedtuple('Patch', ['x1', 'y1', 'x2', 'y2'])
        line_elements = line.split()
        x1 = int(line_elements[2].split(',')[0])
        y1 = int(line_elements[2].split(',')[1][:-1])
        x2 = int(line_elements[3].split('x')[0]) + x1
        y2 = int(line_elements[3].split('x')[1]) + y1
        return Patch(x1, y1, x2, y2)

    def count_overlap(self):
        pass
