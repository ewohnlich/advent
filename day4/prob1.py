import re


def get_guards():
    with open('source.txt') as source:
        entries = source.readlines()
        entries = sorted([entry.strip() for entry in entries])

    guards = {}
    curr_guard = None
    start_time = '0'

    for entry in entries:
        timestamp, action = re.match(r'\[(.*)\] (.*)', entry).groups()
        if action.startswith('Guard'):
            curr_guard = re.match(r'(.*)#(\d+)', action).groups()[-1]
        elif action == 'falls asleep':
            start_time = timestamp[-2:]
        elif action == 'wakes up':
            end_time = timestamp[-2:]
            duration = int(end_time) - int(start_time)
            if curr_guard not in guards:
                guards[curr_guard] = {'total': 0, 'ranges': []}
            guards[curr_guard]['total'] += duration
            guards[curr_guard]['ranges'].append(start_time + '-' + end_time)
    return guards


def get_max_guard(guards):
    def get_total(guard):
        return guard[1]['total']

    return max(guards.items(), key=get_total)


def get_guard_minutes(sleep_times):
    _minutes = [0] * 60
    for sleep_range in sleep_times['ranges']:
        start = int(sleep_range[:2])
        end = int(sleep_range[3:])
        for minute in range(start, end):
            _minutes[minute] += 1
    return _minutes


if __name__ == '__main__':
    guard_id, stimes = get_max_guard(get_guards())
    minutes = get_guard_minutes(stimes)
    max_minute = minutes.index(max(minutes))
    print int(guard_id) * max_minute
