from prob1 import get_data


def build_tree(data):
    value = 0
    num_children = data.pop()
    num_metadata = data.pop()
    meta_index = {}
    if not num_children:
        for meta in range(num_metadata):
            value += data.pop()

    for child in range(num_children):
        meta_index[child + 1] = build_tree(data)
    if num_children:
        for meta in range(num_metadata):
            value += meta_index.get(data.pop()) or 0

    return value


if __name__ == '__main__':
    print(build_tree(get_data('source.txt')))
