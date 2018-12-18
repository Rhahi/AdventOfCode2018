def twice():
    freq = 0
    freq_list = set([0])
    
    while True:
        with open('input/1.txt') as f:
            for line in f:
                freq += int(line)
                if freq in freq_list:
                    return freq
                else: freq_list.add(freq)

print(twice())