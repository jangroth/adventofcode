from collections import defaultdict


class ReposeRecord:
    MATRIX_SIZE = 1000

    def __init__(self, path):
        with open(path) as f:
            content = f.readlines()
        self.content = sorted([x.strip() for x in content])
        self.guards = defaultdict(lambda: defaultdict(int))

    def _parse_content(self):
        current_guard = ''
        interval_start = -1
        for line in self.content:
            if self._is_guard_change(line):
                current_guard = self._get_guard_id(line)
            elif self._is_sleep_start(line):
                interval_start = self._get_minute(line)
            else:
                interval_stop = self._get_minute(line)
                self._record_sleep(current_guard, interval_start, interval_stop)

    def _is_guard_change(self, line):
        return line.endswith('begins shift')

    def _is_sleep_start(self, line):
        return line.endswith('falls asleep')

    def _is_sleep_stop(self, line):
        return line.endswith('wakes up')

    def _get_guard_id(self, line):
        return line.split()[3]

    def _get_minute(self, line):
        return int(line.split()[1][-3:-1])

    def _record_sleep(self, guard, start, stop):
        guard_dict = self.guards[guard]
        for minute in range(start, stop):
            guard_dict['total'] += 1
            guard_dict[str(minute)] += 1

    def find_sleepiest_guard(self):
        self._parse_content()
        sorted_by_total = sorted(self.guards, key=lambda x: self.guards[x]['total'], reverse=True)
        sleepiest_guard = self.guards[sorted_by_total[0]]
        sleepiest_guard_minute = int(sorted(sleepiest_guard, key=sleepiest_guard.get, reverse=True)[1])
        return sorted_by_total[0], sleepiest_guard['total'], sleepiest_guard_minute

    def find_sleepiest_minute(self):
        self._parse_content()
        sleepy_guards = []
        for k, v in self.guards.items():
            sleepiest_minute = sorted(v, key=v.get, reverse=True)[1]
            sleepy_guards.append((k, int(sleepiest_minute), v[sleepiest_minute]))
        return sorted(sleepy_guards, key=lambda tup: tup[2], reverse=True)[0]
