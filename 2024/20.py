from collections import defaultdict
from runner import Runner
import sys
from functools import cache


test_input = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""

directions = [complex(0, 1), complex(1, 0), complex(0, -1), complex(-1, 0)]

input = test_input.split('\n')[1:-1]

graph = defaultdict(lambda: '')
width = len(input[0])
height = len(input)
for i in range(height):
    for j in range(width):
        val = input[i][j]
        if val == 'S':
            start = complex(i, j)
        if val == 'E':
            end = complex(i, j)
        graph[complex(i,j)] = val
    

@cache
def bfs(start, end):
    queue = set([start])
    seen = set([start])
    step = 0
    while len(queue):
        step += 1
        queue = set([q + d for d in directions for q in queue if graph[q+d] != '#' and (q+d) not in seen])
        if end in queue:
            return step

class TodayRunner(Runner):
    def parse(self, input):
        self.map = defaultdict(lambda: '')
        self.width = len(input[0])
        self.height = len(input)
        for i in range(self.height):
            for j in range(self.width):
                val = input[i][j]
                if val == 'S':
                    self.start = complex(i, j)
                    val == '.'
                if val == 'E':
                    self.end = complex(i, j)
                    val == '.'
                self.map[complex(i,j)] = val
            
    def cheat(self, max):
        step = 0
        queue = set([self.start])
        seen = set([self.start])
        cheat_results = defaultdict(lambda: 0)
        while step <= max and len(queue):
            ns = set([q + d for d in directions for q in queue]).difference(seen)
            for n in ns:
                if self.map[n] == '#':
                    if not self.cheats[n]:
                        cheat_2 = set([n + d for d in directions if self.map[n+d] == '.']).difference(seen)
                        for c in cheat_2:
                            total = bfs(c, self.end) + step
                            if total < max:
                                cheat_results[max-total] += 1
                                self.cheats[n].add(c)
            
            queue = [n for n in ns if self.map[n] != '#']
            step += 1
            
        print(dict(cheat_results))
        # print(dict(self.cheats))


    def part_a(self):
        max_len = bfs(self.start, self.end)
        self.cheats = defaultdict(lambda: set())
        return self.cheat(max_len)

    def part_b(self):
        pass



real_input = """

"""


if __name__ == "__main__":
    runner = TodayRunner(test_input, real_input)
    print(runner.run('-v' in sys.argv))