def get_polymer():
    with open('source.txt') as source:
        return source.read().strip()


sample = get_polymer()


def build_polymer(base_polymer):
    polymer = []
    for unit in base_polymer:
        if polymer and unit != polymer[-1] and unit.lower() == polymer[-1].lower():
            del polymer[-1]
        else:
            polymer.append(unit)
    return ''.join(polymer)


if __name__ == '__main__':
    print(build_polymer('dabAcCaCBAcCcaDA') ) # control
    print(build_polymer('dabAcCaCBAcCcaDA'))
