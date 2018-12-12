import time

import matplotlib.pyplot as plt
import numpy as np

start = time.time()


def power_level(xpos, ypos, gsn):
    rack_id = xpos + 10
    return (rack_id * ypos + gsn) * rack_id / 100 % 10 - 5


def build_grid(gsn):
    grid = np.zeros(shape=(300, 300))
    for ypos in range(0, 300):
        for xpos in range(0, 300):
            grid[xpos, ypos] = power_level(xpos, ypos, gsn)
    return grid


def get_max(grid, width=3):
    grid = np.matrix(grid)
    maxsum = 0
    pos = (1, 1)
    for ypos in range(0, len(grid) - width):
        for xpos in range(0, len(grid) - width):
            sum = grid[xpos:xpos + width, ypos:ypos + width].cumsum()
            # if _sum > maxsum:
            #     pos = (ypos, xpos)
            #     maxsum = _sum
    return (maxsum,) + pos


def run_tests():
    assert power_level(3, 5, 8) == 4
    assert power_level(122, 79, 57) == -5
    assert power_level(217, 196, 39) == 0
    assert power_level(101, 153, 71) == 4

    x = np.matrix([[4, 4, 4], [3, 3, 4], [1, 2, 4]])
    assert x.sum() == 29
    assert get_max(build_grid(18)) == (29, 33, 45)
    assert get_max(build_grid(42)) == (30, 21, 61)


if __name__ == '__main__':
    gsn = 4455
    print('Max: {}, @ ({},{})'.format(*get_max(build_grid(gsn))))  # prob1
    grid = build_grid(gsn)
    p1 = time.time()
    print(p1-start)

    supermax = []

    sums = []
    for width in range(1, 301):
        maxsum, left, top = get_max(build_grid(gsn), width)
        sums.append(maxsum)
        if maxsum == 0:  # is this actually valid?
            break
        print('Width {: 2d} max: {}, @ ({},{})'.format(width, maxsum, left, top))
        supermax.append((width, maxsum, left, top))
    print('Supermax: {}, width={}, @ ({},{})'.format(*max(supermax, key=lambda f: f[1])))  # prob2
    print(time.time() - p1)

    plt.plot(sums, linestyle='--', marker='o', color='b')
    plt.show()
