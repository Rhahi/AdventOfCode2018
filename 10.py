from io import StringIO
import numpy as np

def get_info(example = None):
    if example is None:
        with open('input/10.txt') as f:
            lines = f.readlines()
    else:
        return np.array([( 9,  1, 0,  2),( 7,  0,-1,  0),( 3, -2,-1,  1),( 6, 10,-2, -1),( 2, -4, 2,  2),(-6, 10, 2, -2),( 1,  8, 1, -1),( 1,  7, 1,  0),(-3, 11, 1, -2),( 7,  6,-1, -1),(-2,  3, 1,  0),(-4,  3, 2,  0),(10, -3,-1,  1),( 5, 11, 1, -2),( 4,  7, 0, -1),( 8, -2, 0,  1),(15,  0,-2,  0),( 1,  6, 1,  0),( 8,  9, 0, -1),( 3,  3,-1,  1),( 0,  5, 0, -1),(-2,  2, 2,  0),( 5, -2, 1,  2),( 1,  4, 2,  1),(-2,  7, 2, -2),( 3,  6,-1, -1),( 5,  0, 1,  0),(-6,  0, 2,  0),( 5,  9, 1, -2),(14,  7,-2,  0),(-3,  6, 2, -1)])
    
    data = []
    for line in lines:
        xpos = int(line[10:16])
        ypos = int(line[18:24])
        xvel = int(line[36:38])
        yvel = int(line[40:42])
        data.append((xpos, ypos, xvel, yvel))

    return np.array(data)

def vertical_score(data):
    current = np.copy(data)
    best = np.inf
    time = 0
    while True:
        high_y = max(current[:,1])
        low_y = min(current[:,1])
        current[:,0:2] += current[:,2:4]
        score = high_y - low_y
        time += 1
        if best > score:
            best = score
        else:
            current[:,0:2] -= 2 * current[:,2:4]
            return current, time - 2
    
def print_msg(data):
    data = np.copy(data)
    high_x = max(data[:,0])
    low_x = min(data[:,0])
    high_y = max(data[:,1])
    low_y = min(data[:,1])

    data[:,0] -= low_x
    data[:,1] -= low_y

    width = high_x - low_x
    height = high_y - low_y
    
    grid = np.zeros(shape=(height + 1, width + 1))
    for dot in data:
        x = dot[0]
        y = dot[1]

        grid[y,x] = 1

    return grid

if __name__ == '__main__':
    data = get_info()
    raw_text, time = vertical_score(data)
    message = print_msg(raw_text)
    print(time)
    print(grid)