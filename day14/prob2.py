def get_recipes(sequence):
    elves = [0, 1]  # indexes in
    recipes = '37'
    while sequence not in ''.join([str(i) for i in recipes[:-10]]):
        # add recipes
        curr = sum([int(recipes[elf]) for elf in elves])
        new_recipes = []
        if curr == 0:
            new_recipes.append(0)
        while curr > 0:
            new_recipes.append(curr % 10)
            curr /= 10
        new_recipes.reverse()
        recipes += ''.join(map(str,new_recipes))

        # move
        locs = []
        for loc in elves:
            locs.append((loc + int(recipes[loc]) + 1) % len(recipes))
        elves = locs
    return ''.join(map(str, recipes)).find(sequence)


print(get_recipes('51589'))
print(get_recipes('515891'))
print(get_recipes('01245'))
print(get_recipes('92510'))
print(get_recipes('59414'))
print(get_recipes('692951'))
print(get_recipes('157901'))
