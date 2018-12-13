def get_start(sf):
    with open(sf) as source:
        tracks = source.readlines()
        tracks = [list(track.rstrip()) for track in tracks if track.strip()]
    return tracks


car_headings = '<^>v'  # turning right


class TrackCar(object):
    xpos = 0
    ypos = 0
    direction = None
    last_turn = 2

    def __init__(self, id, x, y, direction):
        self.xpos = x
        self.ypos = y
        self.direction = direction
        self.id = id

    def __repr__(self):
        return '<{} "{}" at ({},{})>'.format(self.__class__.__name__, self.id, self.xpos, self.ypos)


def resolve_intersection(car):
    """ get orientation based on ordering of right turns as defined by car_headings
        left is negative, right is positive
    """
    this_turn = (car.last_turn + 1) % 3 - 1  # -1 left, 0 straight, 1 right
    car.last_turn = this_turn + 1  # reset to [0,1,2]
    car.direction = car_headings[(car_headings.index(car.direction) + this_turn) % 4]
    if car.direction == '<':
        car.xpos -= 1
    elif car.direction == '>':
        car.xpos += 1
    elif car.direction == 'v':
        car.ypos += 1
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

    cars = []
    id = 1
    for y in range(len(tracks)):
        for x in range(len(tracks[y])):
            if tracks[y][x] in car_headings:
                cars.append(TrackCar(id, x, y, tracks[y][x]))
                id += 1
    real_track = {'<': '-', '>': '-', 'v': '|', '^': '|'}
    # remove the cars
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
