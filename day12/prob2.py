from prob1 import generation, count_pots, get_pots

if __name__ == '__main__':
    """ Only reason this works is because it looks like after N generations each successive generation produces
        the same amount of new plants. After this point it's just a matter of arithmetic. Checking the last
        three values for equivalent diffs works in this case, what is the better way?
    """
    pots, rules = get_pots('source.txt')
    min_range = 0
    count = count_pots(pots, min_range)
    last = count
    last2 = 0
    last3 = -1
    gen = 0
    while count-last != last-last2 or count-last != last2-last3:  # repeating
        pots, new_min = generation(pots, rules)
        min_range += new_min

        last3 = last2
        last2 = last
        last = count
        count = count_pots(pots, min_range)
        gen += 1
    val = count + (50e9 - gen) * (count - last)
    print(long(val))


