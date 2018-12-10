circle = []

def add_value(circle, value):
    if not circle:
        circle.append(value)
        return circle
    elif value % 23 == 0:

    curr = circle.index(value-1)
    circle.insert((curr+1) % len(circle)+1, value)
    return circle

for i in range(10):
    circle = add_value(circle, i)
    print(circle)