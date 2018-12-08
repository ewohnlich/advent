cloth = [[0 for i in range(0, 1000)] for j in range(0, 1000)]  # matrix of counts


def iterate_map(xoffset, yoffset, width, height):
    for row in range(0, height):
        for col in range(0, width):
            cloth[yoffset + row][xoffset + col] += 1


def parse_claim(line):
    line = line.split('@ ')[-1]
    xoffset, rmdr = line.split(',')
    yoffset, rmdr = rmdr.split(': ')
    width, height = rmdr.split('x')
    return int(xoffset), int(yoffset), int(width), int(height)


with open('source.txt') as source:
    for line in source.readlines():
        iterate_map(*parse_claim(line))

    total = 0
    for row in range(0, len(cloth)):
        for col in range(0, len(cloth[row])):
            if cloth[row][col] > 1:
                total += 1
    print(total)
