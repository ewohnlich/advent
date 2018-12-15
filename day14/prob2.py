def get_recipes(sequence):
    elves = [0, 1]  # indexes in recipes
    recipes = [3, 7]
    sequence = [int(s) for s in sequence]
    while sequence != recipes[-len(sequence) - 1:-1] and sequence != recipes[-len(sequence):]:
        # add recipes
        curr = sum([int(recipes[elf]) for elf in elves])
        if curr < 10:
            recipes.append(curr)
        else:
            recipes.append(int(curr / 10))
            recipes.append(curr % 10)

        # move
        locs = []
        for loc in elves:
            locs.append((loc + recipes[loc] + 1) % len(recipes))
        elves = locs
    return ''.join(map(str, recipes)).find(''.join(map(str, sequence)))


from time import time

x = time()
print('{} after {:.05f}s'.format(get_recipes('51589'), time()-x))
x = time()
print('{} after {:.05f}s'.format(get_recipes('01245'), time()-x))
print(get_recipes('01245'))
print('{} after {:.05f}s'.format(get_recipes('92510'), time()-x))
x = time()
print('{} after {:.05f}s'.format(get_recipes('59414'), time()-x))
x = time()
print('{} after {:.05f}s'.format(get_recipes('692951'), time()-x))
x = time()
print('{} after {:.05f}s'.format(get_recipes('15790'), time()-x))
x = time()
print('{} after {:.05f}s'.format(get_recipes('157901'), time()-x))  # actual puzzle input
