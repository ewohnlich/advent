import re
import time
start = time.time()

def cloud_key(x, y):
    return '{},{}'.format(x, y)


def get_particles(path='example.txt'):
    with open(path) as source:
        _particles = [p.strip() for p in source.readlines() if p.strip()]
    particles = [
        map(int, re.match(r'position=<([- ]*\d*),([- ]*\d*)> velocity=<([- ]*\d*),([- ]*\d*)>', particle).groups())
        for particle in _particles]
    cloud = {}
    for particle in particles:
        xpos, ypos, xvel, yvel = particle
        ckey = cloud_key(xpos, ypos)
        cloud.setdefault(ckey, [])
        cloud[ckey].append((xvel, yvel))
    return cloud


def progress(cloud):
    new_cloud = {}
    for ckey in cloud.keys():
        pairs = cloud.pop(ckey)
        for pair in pairs:
            xvel, yvel = pair
            xpos, ypos = map(int, ckey.split(','))
            new_key = cloud_key(xpos + xvel, ypos + yvel)
            new_cloud.setdefault(new_key, [])
            new_cloud[new_key].append((xvel, yvel))
    return new_cloud


def print_particles(cloud, second, threshold):
    particles = [map(int, ckey.split(',')) for ckey in cloud.keys()]
    xmin = min(particles, key=lambda particle: particle[0])[0]
    xmax = max(particles, key=lambda particle: particle[0])[0]
    ymin = min(particles, key=lambda particle: particle[1])[1]
    ymax = max(particles, key=lambda particle: particle[1])[1]
    lineval = ['vvv{}vvv({})\n'.format(second, time.time()-start)]
    if (ymax-ymin) <= threshold:
        for y in range(ymin, ymax + 1):
            for x in range(xmin, xmax + 1):
                ck = cloud_key(x, y)
                lineval.append(ck in cloud and '#' or ' ')
            lineval.append('\n')
        print ''.join(lineval)


if __name__ == '__main__':
    cloud = get_particles('source.txt')
    threshold = 20

    print_particles(cloud, 0, threshold)
    for i in range(0, 2 ** 15):
         cloud = progress(cloud)
         print_particles(cloud, i+1, threshold)
