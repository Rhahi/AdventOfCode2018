import numpy as np

def get_coords():
    coords = []
    with open('6.txt') as f:
        for line in f:
            coords.append([int(x) for x in line.split(',')])
    return coords

def find_min_max(coords):
    x, y = zip(*coords)

    x_min, y_min = map(min, (x, y))
    x_max, y_max = map(max, (x, y))
    width = x_max - x_min
    height = y_max - y_min
    return (x_min, y_min), (width, height)

def assign_closest(grid, offset=(0,0)):
    x_min, y_min = offset
    for index, _ in np.ndenumerate(grid):
        x1, y1 = index
        grid[x1, y1] = shortest_distance(x1+x_min, y1+y_min, coords)

    return grid

def shortest_distance(x1, y1, coords):
    index = -1
    shortest = (abs(coords[0][0]-x1) + abs(coords[0][1]-y1))

    for i, coord in enumerate(coords):
        x2, y2 = coord
        dist = distance(x1, y1, x2, y2)
        if shortest > dist:
            shortest = dist
            index = i
        elif shortest == dist:
            index = -1 #tie

    return index

def distance(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)

def distance2(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return abs(x2-x1) + abs(y2-y1)

def dangerous_region(coords, shape, offset=(0,0)):
    grid = np.full(shape=shape, fill_value = -1, dtype=np.int)
    grid = assign_closest(grid, offset)
    edge = edges(grid)
    size = 0

    for i in range(len(coords)):
        if i not in edge:
            this_size = (grid==i).sum()
            if size < this_size: size = this_size

    return size

def edges(grid):
    a = grid[0,:]
    b = grid[-1,:]
    c = grid[:,0]
    d = grid[:,-1]

    e = np.concatenate((a,b,c,d))
    f = np.unique(e)
    return f[1:]

def safe_region(coords, shape, offset=(0,0), threshold=10000):
    grid = np.zeros(shape=shape, dtype=np.int)
    x_min, y_min = offset

    for index, _ in np.ndenumerate(grid):
        x1, y1 = index
        for coord in coords:
            x2, y2 = coord
            grid[x1, y1] += distance(x1+x_min, y1+y_min, x2, y2)

    return (grid < threshold).sum()

if __name__ == '__main__':
    coords = get_coords()
    offset, shape = find_min_max(coords)
    ans1 = dangerous_region(coords, shape, offset)
    print(ans1)
    ans2 = safe_region(coords, shape, offset)
    print(ans2)