import re
import numpy as np
import time

def unpack_list():
    spec = []

    with open('input/3.txt') as f:
        for line in f:
            spec.append(unpack(line))
    return spec

def unpack(text):
    regex = re.compile(r"#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)")
    match = regex.match(text)
    
    num = int(match.group(1))
    left = int(match.group(2))
    top = int(match.group(3))
    width = int(match.group(4))
    height = int(match.group(5))
    #better way to pack this?
    return num, left, top, width, height

def overlap(data):
    fabric = np.zeros(shape=(1000,1000))
    # 15 seconds
    
    for line in data:
        num, l, t, w, h = line
        sheet = np.ones(shape=(h,w))
        sheet = np.pad(sheet, ((t, 1000-h-t), (l, 1000-w-l)), mode='constant', constant_values=0)
        fabric += sheet

    return fabric

def overlap_alt(data):
    fabric = np.zeros(shape=(1000,1000))
    # 11 seconds
    for line in data:
        n, l, t, w, h = line
        sheet = np.ones(shape=(h,w))
        top = np.zeros(shape=(t,1000))
        bottom = np.zeros(shape=(1000-t-h,1000))
        left = np.zeros(shape=(h,l))
        right = np.zeros(shape=(h,1000-l-w))

        sheet = np.concatenate((left, sheet), axis=1)
        sheet = np.concatenate((sheet, right), axis=1)
        sheet = np.concatenate((top, sheet), axis=0)
        sheet = np.concatenate((sheet, bottom), axis=0)
        fabric += sheet

    return fabric

def overlap_fast(data):
    fabric = np.zeros(shape=(1000,1000))
    #wow, less than a second!!!
    for line in data:
        n, l, t, w, h = line

        # I think I can use slicing to make array operation faster
        # but I don't know how exactly it works.
        # I'm just confused if it's height first or width first :P

        fabric[t+1:t+1+h, l+1:l+1+w] += 1

    return fabric

def count_overlap(sheet):
    return np.count_nonzero(sheet > 1)

def find_unique(data, sheet):
    for line in data:
        n, l, t, w, h = line

        #find sum of subarray
        # if that sum is w*h it is valid

        subsum = np.sum(sheet[t+1:t+1+h, l+1:l+1+w])
        if subsum == w*h:
            return n
    return -1

if __name__ == "__main__":
    data = unpack_list()
    sheet = overlap_fast(data)
    print(count_overlap(sheet))
    print(find_unique(data, sheet))
