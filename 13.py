def get_info():
    with open('13.txt') as f:
        data = f.readlines()
    
    carts = []
    cartset = "^>v<"
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char in cartset:
                carts.append(Cart(x, y, cartset.index(char))) #append direction, coordinate, state
    
    return carts, data

class Cart:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.state = 0

    def __repr__(self):
        return "({}, {}) {}".format(self.x, self.y, ["up", "right", "down", "left"][self.direction])

    def __ge__(self, other): #>=
        return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other): #<=
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other): #>
        return self.y > other.y or (self.y == other.y and self.x > other.x)

    def __lt__(self, other): #<
        return self.y < other.y or (self.y == other.y and self.x < other.x)

    def __eq__(self, other): #==
        return self.y == other.y and self.x == other.x

    def __ne__(self, other): #!=
        return not self.__eq__(other)

    def check_collision(self, other):
        if other is self: return False
        else: return self.__eq__(other)

    def deflect(self, tile):
        if   tile == '/':
            if   self.direction == 0: self.direction = 1 # up > right
            elif self.direction == 1: self.direction = 0 # right > up
            elif self.direction == 2: self.direction = 3 # down > left
            elif self.direction == 3: self.direction = 2 # left > down
        elif tile == '\\':
            if   self.direction == 0: self.direction = 3 # up > left
            elif self.direction == 1: self.direction = 2 # right > down
            elif self.direction == 2: self.direction = 1 # down > right
            elif self.direction == 3: self.direction = 0 # left > up

    def turn(self):
        if self.state == 0:
            self.direction = (0,1,2,3)[self.direction - 1]
        elif self.state == 2:
            self.direction = (0,1,2,3,0)[self.direction + 1]

        self.state += 1 #0: left, 1: straight, 2: right
        if self.state > 2:
            self.state = 0
    
    def move(self, grid):
        # look up next tile
        dx, dy = ( (0,-1),(1,0),(0,1),(-1,0) )[self.direction]
        self.x += dx
        self.y += dy
        next_tile = grid[self.y][self.x]
        self.deflect(next_tile)
        
        if next_tile == '+':
            self.turn()

    def info(self):
        return (self.x, self.y)

def first_collision(cart_list, grid):
    collision = False
    address = None
    time = 0

    while not collision:
        cart_list.sort()
        for cart in cart_list:
            cart.move(grid)
            for i in cart_list:
                if cart.check_collision(i):
                    collision = True
                    address = (cart.x, cart.y)
                    break
        time += 1
    return address

def last_collision(cart_list, grid):
    time = 0

    while len(cart_list) > 1:
        cart_list.sort()
        todelete = []

        for cart in cart_list:
            cart.move(grid)
            for i in cart_list:
                if cart.check_collision(i):
                    todelete = [cart, i]
                    break

        for item in todelete:
            cart_list.remove(item)
        time += 1

    address = (cart_list[0].x, cart_list[0].y)
    return address, time

if __name__ == "__main__":
    cart_list, grid = get_info()
    print(first_collision(cart_list, grid))

    cart_list, grid = get_info()
    print(last_collision(cart_list, grid))
    
        
