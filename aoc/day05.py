import sys


class AlchemicalReduction:
    def __init__(self, path):
        with open(path) as f:
            content = f.readlines()
        self.content = [x.strip() for x in content]
        sys.setrecursionlimit(50000)

    def _is_match(self, two_letters):
        first = two_letters[0]
        second = two_letters[1]
        return first != second and (first.islower() and second == first.upper() or first.isupper() and second == first.lower())

    def _react(self, text):
        for position in range(1, len(text)):
            if self._is_match(text[position - 1: position + 1]):
                return self._react("{}{}".format(text[0:position - 1], text[position + 1:]))
        return text

    def react_polymer(self):
        return self._react(self.content[0])
