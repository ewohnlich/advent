import re

from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt

# https://www.reddit.com/r/adventofcode/comments/a4urh5/day_10_in_only_8_iterations_with_gradient_descent/
coord = []
vel = []


def get_particles(path='source.txt'):
    with open(path) as source:
        _particles = [p.strip() for p in source.readlines() if p.strip()]
        for particle in _particles:
            xpos, ypos, xvel, yvel = list(map(int, re.findall(r'(-?\d+)', particle)))
            coord.append((xpos, ypos))
            vel.append((xvel, yvel))


def extent(_time):
    locs = coord + _time * vel
    return sum(np.max(locs, axis=0) - np.min(locs, axis=0))


p = get_particles()
coord = np.array(coord)
vel = np.array(vel)

_time = minimize(extent, 0)
round = int(np.round(_time.x))
print(round, _time.nit)

plt.plot(*(coord + round * vel).T, ls='', marker='o', color='k')
plt.gca().invert_yaxis()
plt.axis('equal')
plt.show()
