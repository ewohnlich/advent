with open('source.txt') as source:
    box_ids = source.readlines()

doubles = 0
triples = 0
for box_id in box_ids:
    double = False
    triple = False
    box_id = box_id.strip()
    for char in box_id:
        if box_id.count(char) == 2:
            double = True
        elif box_id.count(char) == 3:
            triple = True
    if double:
        doubles += 1
    if triple:
        triples += 1

print(doubles * triples)
