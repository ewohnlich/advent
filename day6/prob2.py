from prob1 import get_coords, get_manhattan, get_boundaries

def get_distances(coords, x, y):
    total = 0
    for coord in coords:
        total += get_manhattan(coord, (x,y))
    return total


if __name__ == '__main__':
    coords = get_coords()
    threshold = 10000
    area = 0

    xmin, xmax, ymin, ymax = get_boundaries(coords)
    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):
            distances = get_distances(coords, x, y)
            if distances < threshold:
                area += 1
    print area
