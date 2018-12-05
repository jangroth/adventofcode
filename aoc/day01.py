class ChronalCalibration:
    def __init__(self, path):
        with open(path) as f:
            content = f.readlines()
        self.content = [int(x.strip()) for x in content]

    def calibrate(self):
        return sum(self.content)

    def find_first_double_frequency(self):
        unique_values = set()
        total = 0
        while True:
            for value in self.content:
                total += value
                if total in unique_values:
                    return total
                unique_values.add(total)
