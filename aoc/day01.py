class ChronalCalibration:
    def __init__(self, path):
        with open(path) as f:
            content = f.readlines()
        self.content = [int(x.strip()) for x in content]

    def calibrate(self):
        return sum(self.content)

    def find_double_frequency(self):
        

