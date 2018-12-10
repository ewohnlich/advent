def turn(circle, insertion, curr_marble, scores, curr_player):
    if insertion % 23 == 0:
        removal_idx = (curr_marble - 7) % len(circle)
        score = insertion + circle[removal_idx]
        scores[curr_player] += score
        circle.remove(circle[removal_idx])
        return removal_idx
    else:
        curr_marble = (curr_marble + 1) % len(circle) + 1
        circle.insert(curr_marble, insertion)
        return curr_marble


def play_game(num_players, threshold):
    circle = [0]
    curr_marble = 0
    scores = [0] * num_players
    for round in range(threshold):
        curr_player = round % num_players
        curr_marble = turn(circle, round + 1, curr_marble, scores, curr_player)
        round += 1
    return max(scores)


print(play_game(10, 1618))
print(play_game(13, 7999))
print(play_game(17, 1104))
print(play_game(21, 6111))
print(play_game(30, 5807))
print(play_game(459, 71320))
