#In aA, a and A react, leaving nothing behind.
#In abBA, bB destroys itself, leaving aA. As above, this then destroys itself, leaving nothing.
#In abAB, no two adjacent units are of the same type, and so nothing happens.
#In aabAAB, even though aa and AA are of the same type, their polarities match, and so nothing happens.
from string import ascii_lowercase as list_lowercase
import time


def polymer(p = None):
    if p is None:
        with open('AdventOfCode/5.txt') as f:
            p = f.readline()
            #p = 'bCaAcb'

    cur = 0

    while True:
        if react(p[cur], p[cur + 1]):
            #print( p[max(cur-10,0):cur], p[cur:cur+2], p[cur+2:min(cur+10,len(p))] )
            p = p[:cur] + p[cur+2:]
            if cur > 0: cur += -1
        else:
            cur += 1

        if end_of_string(p, cur):
            break

    return p.strip()

def end_of_string(str, cur):
    if cur + 1 >= len(str): return True
    else: return False

def remove_letter(p, a):
    q = p.replace(a.lower(), '') #don't need to do lower; redundancy lowercase
    #print(len(q))
    r = q.replace(a.upper(), '')
    #print(len(r))
    return r

def react(a, b):
    if abs(ord(a) - ord(b)) == 32:
        return True
    else:
        return False

def polymer_shrink(p):
    num = len(p)
    candidate = p

    for letter in list_lowercase:
        q = remove_letter(p, letter)
        r = polymer(q)
        #print(len(r), end='\n\n')
        a = len(r)
        if num > a:
            num = a
            candidate = r
    return candidate


if __name__ == '__main__':
    start = time.perf_counter()

    p = polymer()
    print(len(p))
    q = polymer_shrink(p)
    print(len(q))
    
    end = time.perf_counter()
    print(end-start)