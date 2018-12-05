import collections


class InventoryManagement:
    def __init__(self, path):
        with open(path) as f:
            content = f.readlines()
        self.content = [x.strip() for x in content]

    def checksum(self):
        factor_twos = 0
        factor_threes = 0
        for id in self.content:
            counted_id = collections.Counter(id)
            counted_id_values = counted_id.values()
            if 2 in counted_id_values:
                factor_twos += 1
            if 3 in counted_id_values:
                factor_threes += 1
        return factor_twos * factor_threes

    def common_letters(self):
        pass
