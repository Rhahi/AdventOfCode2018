from io import StringIO

def get_tree_raw(example = None):
    if example == None:
        with open('8.txt') as f:
            data = f.read().split()
    else:
        data = example.read().split()
    return list(map(int, data))

def solve_tree(tree):
    num_children = tree[0]
    num_metadata = tree[1]

    head = 2 # size of head
    size = head + num_metadata # header, metadata
    child_metadata = []
    child_size = 0

    for _ in range(num_children):
        offset, new_metadata = solve_tree(tree[head + child_size:])
        child_size += offset
        child_metadata += new_metadata

    size += child_size # header, children, metadata
    metadata = tree[head+child_size : head+child_size+num_metadata]

    return size, metadata + child_metadata

def solve_tree_2(tree):
    num_children = tree[0]
    num_metadata = tree[1]
    
    value = 0
    head = 2 # size of head
    size = head + num_metadata # header, metadata
    child_data = []
    child_size = 0

    for _ in range(num_children):
        offset, child_value = solve_tree_2(tree[head + child_size:])
        child_size += offset
        child_data.append(child_value)

    size += child_size # header, children, metadata
    metadata = tree[head+child_size : head+child_size+num_metadata]
    if num_children == 0:
        value = sum(metadata)
    else:
        for v in metadata:
            if v <= num_children and v != 0:
                print(child_data)
                value += child_data[v-1]
    return size, value

if __name__ == '__main__':
    example = StringIO("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2")
    #data = get_tree_raw(example)
    data = get_tree_raw()
    #print(data[0:10], data[-1])
    size, metadata = solve_tree(data)
    print(len(data)==size, sum(metadata))
    size, value = solve_tree_2(data)
    print(len(data)==size, value)
    