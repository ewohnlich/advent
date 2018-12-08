from prob1 import get_polymer, build_polymer


def anomalous_unit():
    lowercase = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    base_polymer = get_polymer()
    modified = []

    for char in lowercase:
        polymer = base_polymer.replace(char, '').replace(char.upper(), '')
        modified.append(len(build_polymer(polymer)))
    letter = modified.index(min(modified)) + ord('a')  # don't actually need this, but for debug
    return min(modified)


if __name__ == '__main__':
    print(anomalous_unit())
