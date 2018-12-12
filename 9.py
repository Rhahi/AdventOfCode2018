import numpy as np
from io import StringIO

def get_info(example = None):
    if example == None:
        with open('9.txt') as f:
            data = f.read().split()
    else:
        data = example.read().split()

    players = int(data[0])
    marbles = int(data[6])

    return players, marbles

def solve_game(players, marbles):
    cursor = 0
    circle = [0]
    score = np.zeros(players)
    for i in range(1, marbles + 1): #1 ~ marbles
        current_player = i % players
        if i % 23 != 0:
            new_cursor = wrap_forward(len(circle), cursor)
            circle.insert(new_cursor, i)
        else:
            new_cursor = wrap_backward(len(circle), cursor)
            plus_score = circle.pop(new_cursor)
            score[current_player] += i + plus_score

            print("p: {}\ti: {}\t| {}\t{}\t{}".format(plus_score, i, cursor, new_cursor, len(circle)))
                
            
        
        cursor = new_cursor

    return max(score)

def wrap_forward(length, cursor_before):
    return 1 + (cursor_before + 1) % length

def wrap_backward(length, cursor_before):
    return (cursor_before - 7) % length

if __name__ == "__main__":
    players, marbles = get_info()
    #high_score = solve_game(players, marbles)
    high_score = solve_game(10, 1618)
    print(high_score)