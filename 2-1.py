def checksum():
    two = 0
    three = 0

    with open('input/2.txt') as f:
        lines = f.readlines()
        for line in lines:
            two_check = 0
            three_check = 0

            for c in line:
                cnt = line.count(c) 
                if cnt == 2:
                    two_check = 1
                elif cnt == 3:
                    three_check = 1
            
            two += two_check
            three += three_check

    return two * three

def match():
    with open('AdventOfCode/2.txt') as f:
        lines = f.readlines()
        # for every line except for last
        # compare with remaining lines
        # check if they have only 1 difference

        for idx in range(len(lines) - 1):
            for line in lines[idx + 1:]:
                if difference(lines[idx], line) == 1:
                    return lines[idx], line
            


def difference(str1, str2):
    if len(str1) != len(str2):
        return -1
    
    diff = len(str1)

    for i in range(len(str1)):
        if str1[i] == str2[i]:
            diff -= 1

    return diff