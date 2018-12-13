def get_start(sf):
    with open(sf) as source:
        tracks = source.readlines()
        tracks = [list(track.rstrip()) for track in tracks if track.strip()]
    return tracks


class TrackCar(object):
    xpos = 0
    ypos = 0
    direction = None
    last_turn = 'right'

    def __init__(self, id, x, y, direction):
        self.xpos = x
        self.ypos = y
        self.direction = direction
        self.id = id

    def __repr__(self):
        return '<{} "{}" at ({},{})>'.format(self.__class__.__name__, self.id, self.xpos, self.ypos)


def resolve_intersection(car):
    intersection_order = ['left', 'straight', 'right']
    next_turn = intersection_order[(intersection_order.index(car.last_turn) + 1) % len(intersection_order)]
    car.last_turn = next_turn
    if car.direction == '<':
        if next_turn == 'left':
            car.ypos += 1
            car.direction = 'v'
        elif next_turn == 'right':
            car.ypos -= 1
            car.direction = '^'
        else:
            car.xpos -= 1
    elif car.direction == '>':
        if next_turn == 'left':
            car.ypos -= 1
            car.direction = '^'
        elif next_turn == 'right':
            car.ypos += 1
            car.direction = 'v'
        else:
            car.xpos += 1
    elif car.direction == 'v':
        if next_turn == 'left':
            car.xpos += 1
            car.direction = '>'
        elif next_turn == 'right':
            car.xpos -= 1
            car.direction = '<'
        else:
            car.ypos += 1
    elif car.direction == '^':
        if next_turn == 'left':
            car.xpos -= 1
            car.direction = '<'
        elif next_turn == 'right':
            car.xpos += 1
            car.direction = '>'
        else:
            car.ypos -= 1


def print_track(tracks, cars):
    """ debug purposes only"""
    _tracks = []
    for track in tracks:
        _track = [t for t in track]
        _tracks.append(_track)
    for car in cars:
        _tracks[car.ypos][car.xpos] = str(car.id)
    for line in _tracks:
        print(''.join(line))
    print('')


def check_crash(cars):
    positions = []
    for car in cars:
        position = (car.xpos, car.ypos)
        if position in positions:
            return position
        else:
            positions.append(position)


def drive_car(car, tracks):
    track_pos = tracks[car.ypos][car.xpos]
    if track_pos == '+':
        resolve_intersection(car)
    else:
        if track_pos == '-':
            move = {
                '<': (-1, 0, '<'),
                '>': (1, 0, '>')
            }
        elif track_pos == '|':
            move = {
                'v': (0, 1, 'v'),
                '^': (0, -1, '^'),
            }
        elif track_pos == '\\':
            move = {
                '<': (0, -1, '^'),
                '>': (0, 1, 'v'),
                'v': (1, 0, '>'),
                '^': (-1, 0, '<')
            }
        else:  # track_pos == '/'
            move = {
                '<': (0, 1, 'v'),
                '>': (0, -1, '^'),
                'v': (-1, 0, '<'),
                '^': (1, 0, '>')
            }

        xpos, ypos, direction = move[car.direction]
        car.xpos += xpos
        car.ypos += ypos
        car.direction = direction


def zoomies(tracks, cars):
    for car in cars:
        drive_car(car, tracks)
        crash = check_crash(cars)
        if crash:
            return crash


def build_tracks(source='example.txt'):
    tracks = get_start(source)
    car_markers = '<>^v'
    cars = []
    id = 1
    for y in range(len(tracks)):
        for x in range(len(tracks[y])):
            if tracks[y][x] in car_markers:
                cars.append(TrackCar(id, x, y, tracks[y][x]))
                id += 1
    real_track = {'<': '-', '>': '-', 'v': '|', '^': '|'}
    for car in cars:
        tracks[car.ypos][car.xpos] = real_track[car.direction]

    return tracks, cars


if __name__ == '__main__':
    tracks, cars = build_tracks('source.txt')
    crash = None
    while not crash:
        crash = zoomies(tracks, cars)

    if crash:
        print('crash: {}'.format(crash))
