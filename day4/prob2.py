from prob1 import get_guards, get_guard_minutes

if __name__ == '__main__':
    highest_max_count = 0
    minute_for_max_guard = None
    guard2_id = None
    guards = get_guards()
    for guard_id in guards:
        guard_mins = get_guard_minutes(guards[guard_id])
        guard_max_count = max(guard_mins)
        guard_max_minute = guard_mins.index(guard_max_count)
        if guard_max_count > highest_max_count:
            guard2_id = guard_id
            highest_max_count = guard_max_count
            minute_for_max_guard = guard_max_minute
    print int(guard2_id) * minute_for_max_guard
