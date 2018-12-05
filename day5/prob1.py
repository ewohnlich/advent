def get_polymer():
    with open('source.txt') as source:
        return source.read().strip()


sample = get_polymer()


def traverse(polymer):
    idx = 0
    while idx < len(polymer):
        if idx + 1 == len(polymer):
            return polymer
        if polymer[idx] != polymer[idx + 1] and polymer[idx].lower() == polymer[idx + 1].lower():
            polymer = polymer[:idx] + polymer[min(idx + 2, len(polymer)):]
            if idx != 0:
                idx -= 1  # go back a step if not already at the beginning. Previous unit might now catalyze
        else:
            idx += 1
    return polymer


if __name__ == '__main__':
    print traverse('dabAcCaCBAcCcaDA')  # control
    print len(traverse(sample))
