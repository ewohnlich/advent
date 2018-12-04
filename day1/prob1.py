with open('source1.txt') as source:
    frqs = source.readlines()
    print sum([int(i) for i in frqs])
