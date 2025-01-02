from runner import Runner
import sys
from collections import defaultdict, Counter

class Node():
    def __init__(self, value, level):
        self.value = value
        self.level = level
        self.children = []

class TodayRunner(Runner):
    def parse(self, input):
        self.start_stones = [int(k) for k in input[0].split(' ')]
        self.saved = defaultdict(lambda: [])
    
    def blink(self):
        stones = []
        for i, s in enumerate(self.stones):
            m = str(s)
            if s == 0:
                stones.append(1)
            elif len(m) % 2 == 0:
                stones.append(int(m[:int(len(m)/2)]))
                stones.append(int(m[int(len(m)/2):]))
            else:
                stones.append(s * 2024)
        self.stones = stones


    def part_a(self):
        self.part_b()

    def blink_stone(self, s):
        m = str(s)
        if s == 0:
            return [1]
        elif len(m) % 2 == 0:
            return [int(m[:int(len(m)/2)]), int(m[int(len(m)/2):])]
        else:
            return [s * 2024]
        
    def blink_b(self):
        stones = defaultdict(lambda: 0)
        for s, v in self.stones.items():
            nxt = self.blink_stone(s)
            for n in nxt:
                stones[n] += v
        self.stones = stones


    def part_b(self):
        self.stones = Counter(self.start_stones)
        self.freqs = []
        for i in range(25):
            self.blink_b()
        return sum(self.stones.values())

test_input = """
0 0 0 1
"""

real_input = """
1750884 193 866395 7 1158 31 35216 0
"""


if __name__ == "__main__":
    runner = TodayRunner(test_input, real_input)
    print(runner.run('-v' in sys.argv))