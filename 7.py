import numpy as np

def get_graph():
    graph = np.zeros(shape=(26,26), dtype=np.int)
    mentioned = set()

    with open('input/7.txt') as f:
        data = f.readlines()

    for line in data:
        before = ord(line[5]) - 65
        after = ord(line[36]) - 65 #or ord('A')
        mentioned.add(before)
        mentioned.add(after)
        graph[before][after] = 1
        #graph[0,1] means 0(A) should come before 1(B)
        #so if graph[0,:] sums to 0 then 0(A) is last.
        #if graph[:,0] sums to 0 the 0(A) is first.

    return graph, len(mentioned)

def instruction(data, length):
    graph = data
    order = ''
    #print(graph)
    for _ in range(length):
        for i in range(length):
            if graph[:,i].sum() == 0:
                graph[i,:] = 0
                graph[i,i] = 1 #mark removed
                order += chr(i+65)
                break

    return order

def multiple_workers(data, length, w):
    graph = data
    time = -1
    workleft = np.arange(26) + 61
    workers = [-1] * w

    while True:
        for index, worker in enumerate(workers):
            if worker != -1:
                #they have work!
                workleft[worker] += -1
                if workleft[worker] == 0:
                    graph[worker,:] = 0
                    graph[worker,worker] = 1
                    workers[index] = -1

        for i in range(length):
            #print(graph[:,i].sum())
            if graph[:,i].sum() == 0:
                for index, worker in enumerate(workers):
                    if worker == -1:
                        workers[index] = i
                        graph[i,i] = 1 #mark removed
                        break

        time += 1
        # exit condition
        # let's cheat
        # print(workleft.sum())
        if workleft.sum() == 0:
            return time

if __name__ == '__main__':
    graph, length = get_graph()
    print(length)
    order = instruction(graph, length)
    print(order)
    graph, length = get_graph()
    time = multiple_workers(graph, length, 5)
    print(time)