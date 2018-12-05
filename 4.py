import numpy as np

def sample():
    with open('AdventOfCode/4.txt') as f:
        for line in f:
            pass

def timetable():
    guards = {}

    with open('AdventOfCode/4.txt') as f:
        lines = f.readlines()
        lines.sort()
        
        x = ''
        sleep = 0

        for line in lines:
            min = int(line[15:17]) #very very bad practice!!
            info = line[25:30].rstrip()
            if info[0] == '#':
                #update the current guard
                x = info
                #add empty data if no previous data present
                if info not in guards:
                    #print('new', end=' ')
                    guards[info] = np.zeros(60, dtype=np.int)
                    #I don't know why they don't average, but just sum

            elif info[0] == 'a':
                sleep = min
            elif info[0] == 'u':
                guards[x][sleep:min] += 1
                #print('guard {} sleeps from {} to {}'.format(x, sleep, min))
                #print(guards[x][1:31])

    return guards

def sleepyguard_minute(guards):
    sleepyhead = ''
    sleepysum = 0

    for k, v in guards.items():
        if np.sum(v) > sleepysum:
            sleepyhead = k
            sleepysum = np.sum(v)
    
    sleepyminute = np.argmax(guards[sleepyhead])
    return sleepyhead, sleepyminute

def sleepyminute_guard(guards):
    lists = []
    for k, v in guards.items():
        best = np.max(v)
        time = np.argmax(v)
        candidate = False
        if np.count_nonzero(v == best) == 1:
            candidate = True
            for k2, v2 in guards.items():
                if v2[time] > best:
                    #this is not the answer
                    candidate = False
                    break
        if candidate:
            lists.append((k, time, guard_number(k) * time, guards[k][time]))
    print(lists)
    # for each guard, get their finiest minute
    # for each guard's finest minute, compare it with other guards' counts
    # if they pass both tests, they are good.
    # the answer is probably with the highest minute.

def guard_number(guard):
    return int(guard[1:])

guards = timetable()
sleepyhead, minute = sleepyguard_minute(guards)
print(guard_number(sleepyhead) * minute)

sleepyminute_guard(guards)
#guard_of_the_minute, sleepyminute = sleepyminute_guard(guards)
#print(guard_number(guard_of_the_minute) * sleepyminute)

# [1518-03-17 00:04] Guard #769 begins shift
# [1518-03-17 00:29] falls asleep
# [1518-03-17 00:47] wakes up
# [1518-03-17 00:50] falls asleep
# [1518-03-17 00:51] wakes up
# [1518-03-18 00:02] Guard #2039 begins shift
# [1518-03-18 00:29] falls asleep
# [1518-03-18 00:50] wakes up
# [1518-03-19 00:00] Guard #769 begins shift
# [1518-03-19 00:42] falls asleep
# [1518-03-19 00:55] wakes up

# [1
# 1 1 1 2 2
# 3 3 3 3 3
# 3 3 5 5 5
# 5 5 5 5 5
# 5 5 5 5 5
# 5 6 5 5 5
# 3 3 2 2 2
# 2 2 2 3 3
# 4 6 6 7 8
# 8 7 6 5 5
# 5 5 4 5 5
# 6 3 1 0]