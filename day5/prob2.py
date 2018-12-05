from prob1 import get_polymer, traverse


def anomalous_unit():
    lowercase = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    modified = []

    for char in lowercase:
        polymer = get_polymer().replace(char, '').replace(char.upper(), '')
        modified.append(len(traverse(polymer)))
    letter = modified.index(min(modified)) + ord('a')  # don't actually need this, but for debug
    return min(modified)


if __name__ == '__main__':
    print anomalous_unit()
