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

    def _find_components(self, text):
        return ''.join(sorted(list(set(x for x in text.lower()))))

    def _react(self, text):
        for position in range(1, len(text)):
            if self._is_match(text[position - 1: position + 1]):
                return self._react("{}{}".format(text[0:position - 1], text[position + 1:]))
        return text


    def react_polymer(self):
        return self._react(self.content[0])

    def improve_polymer(self):
        print("Reacting base polymer.")
        base = self._react(self.content[0])
        print("Done, length: {}".format(len(base)))
        result = {}
        for component in self._find_components(base):
            print('Testing {}'.format(component))
            candidate = base.replace(component, '').replace(component.upper(), '')
            candidate_reacted = self._react(candidate)
            result[component] = len(candidate_reacted)
            print('...Done, result {}'.format(len(candidate_reacted)))
        return sorted(result.items(), key=lambda x: x[1])[0]


