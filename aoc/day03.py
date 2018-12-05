class SliceThePatch:
    def __init__(self, path):
        with open(path) as f:
            content = f.readlines()
        self.content = [x.strip() for x in content]

    def count_overlap(self):
        pass
