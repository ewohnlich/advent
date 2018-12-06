import colorsys
import os


def get_coords():
    with open('source.txt') as source:
        coords = []
        for coord in source.readlines():
            x, y = coord.split(',')
            coords.append((int(x.strip()), int(y.strip())))
    return coords


html_block = '<div style="height:{size}px; width: {size}px; background-color: #{color}; margin:0; padding: 0; display: inline-block"></div>'
block_size = 3
sample = [
    (1, 1),  # A*
    (1, 6),  # B*
    (8, 3),  # C*
    (3, 4),  # D
    (5, 5),  # E
    (8, 9),  # F*
]


def get_boundaries(coords):
    xmin = min(coords, key=lambda x: x[0])
    xmax = max(coords, key=lambda x: x[0])
    ymin = min(coords, key=lambda y: y[1])
    ymax = max(coords, key=lambda y: y[1])
    return xmin[0], xmax[0], ymin[1], ymax[1]


def get_manhattan(coord1, coord2):
    x = abs(coord1[0] - coord2[0])
    y = abs(coord1[1] - coord2[1])
    return x + y


def get_closest_coord(coords, x, y):
    manhattans = [get_manhattan(coord, (x, y)) for coord in coords]
    if manhattans.count(min(manhattans)) == 1:
        coord_idx = manhattans.index(min(manhattans))
        return coord_idx


def get_color(idx, num_coords):
    """ We create colors at intervals of int(0xffffff) / input_length
        Black (#000000) is reserved for double matches. Other colors are interval * idx + interval
    """
    num_colors = num_coords + 1  # num coords + 1 for black border
    interval = 1 / float(num_colors)
    r, g, b = colorsys.hsv_to_rgb(idx * interval, 1.0, 1.0)

    color = "{0:02x}{1:02x}{2:02x}".format(int(r * 255), int(g * 255), int(b * 255))
    return color


def calc_areas(coords):
    if os.path.exists('output.html'):
        os.remove('output.html')
    output = open('output.html', 'a')  # filled in
    areas = [0] * len(coords)
    xmin, xmax, ymin, ymax = get_boundaries(coords)

    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):
            if (x, y) in coords:
                areas[coords.index((x, y))] += 1
                # list of coordinates
                output.write(html_block.format(color='ffffff', size=block_size))
            else:
                coord_idx = get_closest_coord(coords, x, y)
                if coord_idx is not None:
                    areas[coord_idx] += 1
                    # closest coordinate color
                    output.write(html_block.format(color=get_color(coord_idx, len(coords)), size=block_size))
                else:
                    # one or more coordinate points are equidistant
                    output.write(html_block.format(color='000000', size=block_size))
        output.write('<br/>')

    # check boundaries for finiteness
    def wipe_area(x, y):
        cidx = get_closest_coord(coords, x, y)
        if cidx:
            areas[cidx] *= 0

    for y in range(ymin, ymax + 1):
        x = xmin - 1
        wipe_area(x, y)
    for y in range(ymin, ymax + 1):
        x = xmax - 1
        wipe_area(x, y)
    for x in range(xmin - 1, xmax + 2):  # include corner cases
        y = ymin - 1
        wipe_area(x, y)
    for x in range(xmin - 1, xmax + 2):  # include corner cases
        y = ymax - 1
        wipe_area(x, y)
    print max(areas)
    output.close()


if __name__ == '__main__':
    calc_areas(get_coords())
