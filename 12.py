def get_info():
    with open('12.txt') as f:
        initial = f.readline()[15:-1]
        f.readline()
        data = f.readlines()
    
    all_patterns = []
    for pattern in data:
        p_from = pattern[0:5]
        p_to = pattern[9]
        all_patterns.append((p_from, p_to))
    return initial, all_patterns

def extend_pots(pots):
    """Append '.' in the string to make sure leading and following pots are empty.
    Return resulting pots and front-adjustments made.
    """
    adjust = 0

    while pots[0:4] != "....":
        pots = '.' + pots
        adjust += 1
    while pots[-4:] != '....':
        pots = pots + '.'

    return pots, adjust

def pass_generation(pots, patterns):
    """Pass single generation.
    Return resulting pot position and its adjustment made to zero-index offset.
    """
    pots, adjust = extend_pots(pots)
    next_pots = ''

    pattern, change = zip(*patterns)
    for pos in range(0,len(pots) - 4):
        try:
            idx = pattern.index(pots[pos:pos+5])
        except ValueError:
            # if the change is not defined, assume it is '.'
            # built for example case.
            next_pots += '.'
        else:
            next_pots += change[idx]
    result = pots[0:2] + next_pots + pots[-2:]
    return result, adjust

def score_pots(pots, offset=0):
    """Get pots configuration and return its score.
    """
    answer = 0

    for idx, char in enumerate(pots):
        if char == '#': answer += idx - offset
    return answer

def solve_part_1(pots, patterns, generations):
    """Get pots and patterns and return the next pot state.
    """
    offset = 0
    for _ in range(generations):
        pots, adjust_offset = pass_generation(pots, patterns)
        offset += adjust_offset

    return score_pots(pots, offset)

def solve_part_2(pots, patterns, generations):
    """Get pots and patterns and return the next pot state.
    More general solution which yields part 1 as well.
    """
    offset = 0
    score = 0
    prev_score = 0
    prev_diff = 0
    consecutive = 0 #number of same diff occuring consecutively

    #print("Gen\tScore\tDiff")
    for gen in range(1, generations + 1):
        pots, adjust_offset = pass_generation(pots, patterns)
        offset += adjust_offset
        score = score_pots(pots, offset)
        diff = score - prev_score
        #print("{}\t{}\t{}".format(gen, score, diff))
        if diff == prev_diff:
            consecutive += 1
        else:
            consecutive = 0
        prev_score = score
        prev_diff = diff
        if consecutive > 5:
            break
            
    return calculate_score_at(gen, generations, score, diff)

def calculate_score_at(current, target, score, diff):
    return (target-current) * diff + score

if __name__ == "__main__":
    pots, patterns = get_info()
    ans1 = solve_part_1(pots, patterns, 20)
    print('Answer1:', ans1)
    ans2 = solve_part_2(pots, patterns, 50000000000)
    print('Answer2:', ans2)