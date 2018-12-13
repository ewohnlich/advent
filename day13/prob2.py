from prob1 import build_tracks, drive_car


def resolve_crashes(cars):
    crashes = set()
    positions = {}
    for car in cars:
        position = (car.xpos, car.ypos)
        if position in positions:
            crashes.add(car.id)
            crashes.add(positions[position].id)
        else:
            positions[position] = car
    return crashes


def zoomies(tracks, cars):
    crashes = set()
    for car in sorted(cars, key=lambda _car: (_car.xpos, _car.ypos)):
        drive_car(car, tracks)
        crashes = crashes.union(resolve_crashes(cars))
    cars[:] = [car for car in cars if car.id not in crashes]
    if len(cars) == 1:
        return cars[0]


if __name__ == '__main__':
    tracks, cars = build_tracks('source.txt')
    last_car = None
    while not last_car:
        last_car = zoomies(tracks, cars)

    print('last car: {}'.format(last_car))
