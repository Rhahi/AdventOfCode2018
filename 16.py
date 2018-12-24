from collections import defaultdict

def get_data():
    part1 = []
    part2 = []

    with open('input/16.txt') as f:
        data = f.readlines()

    for i in range(0, len(data), 4):
        if data[i+3] == '\n':
            inst = list(map(int, data[i+1][:-1].split(' ')))
            before = list(map(int, data[i][9:-2].split(',')))
            after = list(map(int, data[i+2][9:-2].split(',')))
            part1.append([inst, before, after])
        else:
            break

    for j in range(i, len(data)):
        if data[j] != '\n':
            inst = list(map(int, data[j][:-1].split(' ')))
            part2.append(inst)

    return part1, part2

class TIS100:
    def __init__(self, init=[0,0,0,0]):
        self.r = init.copy()
        self.fnc = [
            self.addr, self.addi,
            self.mulr, self.muli, 
            self.banr, self.bani,
            self.borr, self.bori,
            self.setr, self.seti,
            self.gtir, self.gtri, self.gtrr,
            self.eqir, self.eqri, self.eqrr]
        self.valid = [False] * len(self.fnc)
        self.untested = True
        self.identified_function = None

    def set_reg(self, reg):
        self.r = reg #attach to external memory

    def __repr__(self):
        return repr(self.r)

    def addr(self, a, b, c):
        self.r[c] = self.r[a] + self.r[b]

    def addi(self, a, v2, c):
        self.r[c] = self.r[a] + v2

    def mulr(self, a, b, c):
        self.r[c] = self.r[a] * self.r[b]

    def muli(self, a, v2, c):
        self.r[c] = self.r[a] * v2

    def banr(self, a, b, c):
        self.r[c] = self.r[a] & self.r[b]

    def bani(self, a, v2, c):
        self.r[c] = self.r[a] & v2

    def borr(self, a, b, c):
        self.r[c] = self.r[a] | self.r[b]

    def bori(self, a, v2, c):
        self.r[c] = self.r[a] | v2

    def setr(self, a, _, c):
        self.r[c] = self.r[a]

    def seti(self, v1, _, c):
        self.r[c] = v1

    def gtir(self, v1, b, c):
        self.r[c] = 1 if v1 > self.r[b] else 0

    def gtri(self, a, v2, c):
        self.r[c] = 1 if self.r[a] > v2 else 0

    def gtrr(self, a, b, c):
        self.r[c] = 1 if self.r[a] > self.r[b] else 0

    def eqir(self, v1, b, c):
        self.r[c] = 1 if v1 == self.r[b] else 0

    def eqri(self, a, v2, c):
        self.r[c] = 1 if self.r[a] == v2 else 0

    def eqrr(self, a, b, c):
        self.r[c] = 1 if self.r[a] == self.r[b] else 0

    def test(self, inst, before, after):
        hits = 0
        for idx, f in enumerate(self.fnc):
            self.r = before.copy()
            f(*inst)
            if self.r != after:
                self.valid[idx] = False
            elif self.untested:
                self.valid[idx] = True
                hits += 1
            else:
                hits += 1
        self.untested = False
        return hits
    
    def valid_debug(self):
        a = ["#" if i else '.' for i in self.valid]
        print("Matches:", self.count(), a)

    def id(self):
        if self.count() == 1:
            self.identified_function = self.fnc[self.index()]

    def call(self, a, b, c):
        self.identified_function(a, b, c)
        return self.r.copy()

    def count(self):
        return self.valid.count(True)
    
    def index(self):
        return self.valid.index(True)

    def invalidiate(self, idx):
        if self.count() > 1:
            self.valid[idx] = False

def sample_test(samples, opcodes):
    multiple_match_count = 0
    for sample in samples:
        instruction, before, after = sample
        n = instruction[0]
        inst = instruction[1:]

        mc = opcodes[n].test(inst, before, after)
        multiple_match_count += 1 if mc >= 3 else 0

    return multiple_match_count

def identify(opcodes):
    for _ in range(len(opcodes)):
        for v in opcodes.values():
            if v.count() == 1:
                idx = v.index()
                v.id()
                for vv in opcodes.values():
                    vv.invalidiate(idx)

def run(instructions, opcodes):
    reg = [0,0,0,0]
    for o in opcodes.values():
        o.set_reg(reg)

    for inst in instructions:
        n = inst[0]
        i = inst[1:]
        opcodes[n].call(*i)

    return reg[0]

if __name__ == "__main__":
    samples, instructions = get_data()
    opcodes = defaultdict(TIS100)
    res1 = sample_test(samples, opcodes)
    print(res1)
    identify(opcodes)
    res2 = run(instructions, opcodes)
    print(res2)