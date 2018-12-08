def get_data(source='source.txt'):
    with open(source) as source:
        data = [int(i) for i in source.read().split(' ')]
    data.reverse()
    return data


def build_tree(data):
    sum = 0
    num_children = data.pop()
    num_metadata = data.pop()
    for child in range(num_children):
        sum += build_tree(data)
    for meta in range(num_metadata):
        sum += data.pop()
    return sum


if __name__ == '__main__':
    print(build_tree(get_data()))
