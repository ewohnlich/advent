def get_twice(frqs, curr=0):
    for frq in frqs:
        curr += int(frq)
        if curr in unique_frqs:
            return curr
        unique_frqs.add(curr)
    return get_twice(frqs, curr)


unique_frqs = set([0])
with open('source1.txt') as source:
    frqs = source.readlines()
    print get_twice(frqs)
