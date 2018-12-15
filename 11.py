import numpy as np

# puzzle input 3463

def power_level(x, y, puzzle):
    x = x+1
    y = y+1
    return (((x + 10) * y + puzzle) * (x + 10) ) % 1000 // 100 - 5

def power_grid(puzzle, size=300):
    grid = np.zeros(shape=(size,size), dtype=int)
    for idx in np.ndindex(grid.shape):
        x, y = idx
        grid[x,y] = power_level(x, y, puzzle)

    return grid

def subsum_grid1(data):
    grid = np.copy(data)

    for idx in np.ndindex(grid.shape):
        x, y = idx
        subsum = 0
        if x > 0:
            subsum += grid[x-1, y]
        if y > 0:
            subsum += grid[x, y-1]
        if x > 0 and y > 0:
            subsum -= grid[x-1, y-1]
        
        grid[x,y] += subsum

    return grid

def subsum_grid2(data):
    grid = np.zeros(shape=data.shape)

    for idx in np.ndindex(grid.shape):
        x, y = idx
        grid[x,y] = data[:x,:y].sum()

    return grid

def sum_size(x, y, data, size=3):
    #starts from 0,0 have to add 1 to make it 1 index start.
    return data[x+size,y+size] - data[x+size,y] - data[x, y+size] + data[x, y]

def custom_size_sum(data, size):
    xsize, ysize = data.shape
    biggest = 0
    coord = None

    for x in range(0,xsize-size):
        for y in range(0,ysize-size):
            my_size = sum_size(x, y, data, size=size)
            if my_size > biggest:
                biggest = my_size
                coord = (x+1, y+1)
    return coord, biggest

def solve_size(data, sizes=None):
    if sizes is None:
        partial_coord, partial_biggest = custom_size_sum(data, 3)
        return partial_coord, partial_biggest, 3

    else:
        biggest = 0
        coord = None
        used_size = -1
        for s in range(1,sizes+1):
            partial_coord, partial_biggest = custom_size_sum(data, s)
            if partial_biggest > biggest:
                biggest = partial_biggest
                coord = partial_coord
                used_size = s

        return coord, biggest, used_size


def coord_conv(coord, size):
    return coord[0]+size-1, coord[1]+size-1

if __name__ == "__main__":
    puzzle = 3463
    original_grid = power_grid(puzzle)
    grid = subsum_grid2(original_grid)
    print(solve_size(grid))
    print(solve_size(grid, 300))

    #print(grid)