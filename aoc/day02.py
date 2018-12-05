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
        for index, id1 in enumerate(self.content):
            for id2 in self.content[index + 1:]:
                is_different_by_one_character, common_part = self._are_different_by_one_character(id1, id2)
                if is_different_by_one_character:
                    return common_part

    def _are_different_by_one_character(self, texta, textb):
        if texta == textb:
            return False, None
        difference = -1
        for index, character in enumerate(texta):
            if character != textb[index]:
                if difference == -1:
                    difference = index
                else:
                    return False, None
        return True, "{}{}".format(texta[0:difference], texta[difference + 1:])
