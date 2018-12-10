from collections import deque


def turn(circle, insertion, scores, curr_player):
    if insertion % 23 == 0:
        circle.rotate(7)
        scores[curr_player] += insertion + circle.pop()
        circle.rotate(-1)
    else:
        circle.rotate(-1)
        circle.append(insertion)


def play_game(num_players, threshold):
    circle = deque([0])
    scores = [0] * num_players
    for round in range(threshold):
        curr_player = round % num_players
        turn(circle, round + 1, scores, curr_player)
        round += 1
    return max(scores)


print(play_game(10, 25))
print(play_game(10, 1618))
print(play_game(13, 7999))
print(play_game(17, 1104))
print(play_game(21, 6111))
print(play_game(30, 5807))
print(play_game(459, 7132000))
