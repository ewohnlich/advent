def get_recipes(num):
    elves = [0, 1]  # indexes in
    recipes = [3, 7]
    while len(recipes) < num + 10:
        # add recipes
        curr = sum([recipes[elf] for elf in elves])
        new_recipes = []
        if curr == 0:
            new_recipes.append(0)
        while curr > 0:
            new_recipes.append(curr % 10)
            curr /= 10
        new_recipes.reverse()
        recipes += new_recipes

        # move
        locs = []
        for loc in elves:
            locs.append((loc + recipes[loc] + 1) % len(recipes))
        elves = locs
    return ''.join([str(i) for i in recipes[num:num+10]])


print(get_recipes(9))
print(get_recipes(5))
print(get_recipes(18))
print(get_recipes(2018))
print(get_recipes(157901))
