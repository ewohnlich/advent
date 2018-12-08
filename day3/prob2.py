import re

cloth = {}


def iterate_map(xoffset, yoffset, width, height):
    for row in range(0, height):
        for col in range(0, width):
            y = str(yoffset + row)
            x = str(xoffset + col)
            if y not in cloth:
                cloth[y] = {}
            if x not in cloth[y]:
                cloth[y][x] = 0
            cloth[y][x] += 1


def parse_claim(claim):
    claim_id, xoffset, yoffset, width, height = re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', claim).groups()
    return claim_id, int(xoffset), int(yoffset), int(width), int(height)


def check_claim(xoffset, yoffset, width, height):
    for row in range(0, height):
        for col in range(0, width):
            if cloth[str(yoffset + row)][str(xoffset + col)] != 1:
                return
    return True


with open('source.txt') as source:
    claims = source.readlines()
    for line in claims:
        iterate_map(*parse_claim(line)[1:])

    for claim in claims:
        claim_id, xoffset, yoffset, width, height = parse_claim(claim)
        if check_claim(xoffset, yoffset, width, height):
            print(claim_id)
