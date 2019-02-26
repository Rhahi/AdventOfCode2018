from time import perf_counter

def solve_part1(after):
    recipes = [3, 7]
    A = 0
    B = 1

    while len(recipes) < after + 10:
        rA = recipes[A]
        rB = recipes[B]
        r = rA + rB

        if r >= 10: recipes += [1, r-10]
        else: recipes += [r]
        
        A = (A + rA + 1)%len(recipes)
        B = (B + rB + 1)%len(recipes)

    return int("".join(map(str, recipes[after : after+10])))

def solve_part2(puzzle):
    recipes = [3, 7]
    target_gen = 128
    generation = 1
    searched = 0
    A = 0
    B = 1

    loop_time = 0
    search_time = 0
    while True:
        markA = perf_counter()
        while generation < target_gen:
            rA = recipes[A]
            rB = recipes[B]
            r = rA + rB

            if r >= 10: recipes += [1, r-10]
            else: recipes += [r]
            
            A = (A + rA + 1)%len(recipes)
            B = (B + rB + 1)%len(recipes)
            generation += 1
        target_gen *= 2
        markB = perf_counter()
        loop_time += markB - markA

        offset = max(searched - 6, 0)
        recipe_str = "".join(map(str, recipes[offset:]))
        res = recipe_str.find(puzzle)

        markC = perf_counter()
        search_time += markC - markB
        if res != -1:
            #print("loop time: {:.2f} | serach time: {:.2f}".format(loop_time, search_time))
            return res + offset
        searched = len(recipes)

if __name__ == "__main__":
    puzzle_input = "939601"
    print(solve_part1(puzzle_input))
    print(solve_part2(puzzle_input))