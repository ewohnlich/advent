PLANT = '#'
EMPTY = '.'


def get_pots(source_file='example.txt'):
    pots = ''
    rules = {}
    with open(source_file) as source:
        for input in source.readlines():
            if input.strip():
                if not pots:
                    pots = input.strip().split(': ')[-1]
                else:
                    config, dest = input.strip().split(' => ')
                    rules[config] = dest

    return pots, rules


def generation(pots, rules):
    new_pots = []
    min_range = pots[0] == PLANT and -1 or 0  # always start with an empty pot on edge, to allow for expansion
    max_range = pots[-1] == PLANT and len(pots) + 1 or len(pots)
    for idx in range(min_range, max_range):
        rule = []
        for i in range(-2 + idx, 3 + idx):
            if i < 0 or i >= len(pots):
                rule.append(EMPTY)
            else:
                rule.append(pots[i])
        rule = ''.join(rule)
        new_pots.append(rules.get(rule) or EMPTY)
    return ''.join(new_pots), min_range


def count_pots(pots, min_range):
    return sum([idx + min_range for idx, val in enumerate(pots) if val == PLANT])


if __name__ == '__main__':
    pots, rules = get_pots('source.txt')
    min_range = 0
    for i in range(20):
        pots, new_min = generation(pots, rules)
        min_range += new_min
    print(count_pots(pots, min_range))
