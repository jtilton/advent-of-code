from runner import Runner
import sys
from collections import defaultdict

class TodayRunner(Runner):
    def parse(self, input):
        self.map = defaultdict(lambda: '')
        self.height = len(input)
        self.width = len(input[0])
        for i in range(len(input)):
            for j in range(len(input[0])):
                self.map[(i, j)] = input[i][j]
                if input[i][j] == '^':
                    self.start = (i, j)
        
    def full_path(self):
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        turns = 0

        loc = self.start
        seen = set([loc])
        while self.map[loc] != '':
            direction = directions[turns % 4]
            next_loc = (loc[0] + direction[0], loc[1] + direction[1])
            if self.map[next_loc] == '':
                break
            elif self.map[next_loc] != '.' and self.map[next_loc] != '^':
                turns += 1
            else:
                loc = next_loc
                seen.add((loc))
        return (seen, len(seen))

    def part_a(self):
        (_, seen_count) = self.full_path()
        return seen_count
    
    def part_b(self):
        (seen, _) = self.full_path()
        loops = 0
        for (i, j) in seen:
            new_map = self.map.copy()
            new_map[(i, j)] = '#'
            if self.run_iteration(new_map):
                loops += 1
        return loops

    def run_iteration(self, map):
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        turns = 0

        loc = self.start
        seen = [set(), set(), set(), set()]
        while map[loc] != '':
            di = turns % 4
            direction = directions[di]
            next_loc = (loc[0] + direction[0], loc[1] + direction[1])
            if map[next_loc] == '':
                break
            elif map[next_loc] != '.' and map[next_loc] != '^':
                turns += 1
            else:
                loc = next_loc
                if loc in seen[di]:
                    if loc == self.start:
                        return False
                    return True
                else:
                    seen[di].add(loc)
        return False


test_input = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

real_input = """
.......................#...................#....#..#......#.................#.#..#........................#.#..............#.....#
................#.#.......#..#.......#.................................................................................#.##.......
............#..............#......................#...#.....#...#..........##.........#.....#.....................................
..#...#......................................#............................#..................#..........#..#......................
....#........#.#....................#..........#.....#.............#..#............................#..................#......#....
..........................................................#................#............................................#.........
..#............................#.....#...........................#...........#........##...........................#..#...........
.....................#...........................#.#..............#......................................#.........#....#.....#...
.#...#.#.................#....................#...............................................................#.#..........#......
....#....................................#...........................................#.....#..........#...........................
.......................#..........#..............#......#....#.......#........................................#.#.................
......#...........................................................#...#............#.................#............................
.......#.................#..#.....................#...............................................................................
..............#....................#.#..........#........#......#................#.................#..........#...................
#.#.......................................#.........................#...................................#.........................
...#.........................................................................................#................#..................#
#.....#....#............................................................#.........................#..................#.#..........
.#.....#.#.......#.#..................#.#......................#.......#.....#..#..................##.....#.......#...#...........
....#.........#.................................#..........#........#...............#................#...................#....#...
.................#...............#...#.................#.................................................#........................
....#...#...............................#..................................................#..........#................#.....#....
...........#........#....#.......#...#..........#...............#.....#.....#.....#..........#....................................
............#.........#.................#................#.................#.#..................................................#.
............#......................................#...................................................................#..........
...........#....#.....................................................................................#............#..........#...
..........#........................................#.............#.................#........................#..#.......#........#.
......#.............................#.................##..................................#.....................#.................
.#.................................#.............................................#.................##.....#..............#......#.
.........................#..............................#..........#...........#....#................#......................#.....
.......#...................#......##........................#.........#...........................................................
......................................................................##...........#................#.............................
....#...................................##...............................................#........................................
...##.....#..#........#.................#..............................................................#..........................
........##......#....................#..............................#......................#...................#..................
.........................................................#.......................................................#.#..............
..........#.............................#.........#...............#................#.#.........#..........................#.#.....
....................#...................#..#.......................................................#..........#...............#...
...........................................................#........................#.........#........#..........................
.......#..............#......#.................................#...................##...........................#.........#.......
#...#...............................................................................................................#.............
................................#..#....#............#...........#..................#.............................#...............
....................#..............#.........#.................................#.............#..##................................
#...#..................................................................................#.....#...........#........................
........#...........#........#...#..................#.....#....#.........#.........................#...........................#..
.............#...#...................................................................#...........#................................
.............#........................................#...#.............#..............................#..#.........#.............
...#.................................................................................#.............#..........................##..
...#..............................................................................................................................
................#.........#..................................#...................#................................................
...#................#...#.#.....................#...........#..................................#........#....#......#.............
..........................#.....................#..#...................................##........................................#
#........................#...............................................#........#..#..........#...........................#.....
.#............#.#..............................................................#...........#......................................
......#..................................................................#.......#..............................#...#....#........
........#........................#.........#.............#.....#..................................................................
...............................................................................#...........................................#......
........................#..................................#.....................................................#................
............................................................#..........................#.................#.......................#
.....................#..#.........................#..............#.............................#........#..............##......#..
.....................#.................................................#.......#............#........................#.......#....
......................#.....................................................#......#............................#.................
................................................................#...#..##..#.....................................#...............#
..............#..............................................................................................#....................
............................................#......#..........#...............................................................#...
....#.................................#..................................................................#..........##..#.........
............#.....#................................................................................#..........#.........#.........
.....................#......................................#.........#....................................................#....#.
.........................#...............................#...............................#....................#...................
.#.....................#.#.......................................#....#...........#.......................#.......................
.....................................................#.#..#......................................................................#
#..........#..........................#............................#.............#..................#.............#...........#...
........#.........................................................................................................................
..........#.............#.........................................#................................................#..............
...........#................................#.................#...........................#.............................#.........
..................#.........................................#.#..................#...#...........#.......#..#.....................
........................................................#...#.......................................................#.............
.........................................................................#.......#..#.....#.......................................
............#..............................................................#.........#..............#.............#...............
#...#..........................................#...........#.....#.....................................#...............#..........
...........................#............#.........................................................................................
...#..........................................#.......................................................................#...........
..............#......#.....#.....................#..........................#.....................................................
.........................#....#...................#...#.......#..............................#........................#...........
.............................#............^.#................................................#......#..#.#...........#............
....................................................................................#...#.#...................................#...
.......................#..............................##..............................................#...........................
......................#...................................................#..........................................#............
......#........................................................................#.....................................#............
.......................#.............................#........................#...........#...........#............#...........#..
....#...............#..#......#....#..................#.............#.......#...............#.......................#.............
............#...#..................#..............................................................................................
....#.......#.................#.......................................................#..#......#.................................
.........#......#..........#......................#.....................#..................#.#....................................
...............##.......................................................#...#.............................#.......#...............
........................................................##...................#...#............#......#............................
...........#...#..............#.............................................................#...................#............#....
...............................................#.....#.....#......................................................................
.#....................#...#........#....................#.#.........#..........#................................#................#
.............#.....#..#....................................#.#...........#.................................................#..#.#.
......#.....................................#....................................................................#................
............................................................##......#.....................#.......#.....................#...#.....
.#.......#......................#.................................................................................................
................#....#......................#.........#...................#........#.......##.....#...............................
..#....#....................#............................................................#.#......#............#.....#.#....#.....
.................................#.................................................#.......#......................................
..................#...........#....#.....................#......#...............#..................#....................##........
.##...............................................#............#...........................#......................................
.............#...........#...........................#..#.......#...#..........#......................#..........#................
.......#...................................#.................#....#..............................................................#
........#....................................................#.................#.....#.........#.#................................
................#.................................#.....................#.....#.....#............................##...............
..............................................##.................#..##........#...........#............#..........................
....#......................................#...............................................................................#......
..#..............#.#................#..#..............#.......................................#.#.......#..............#......#..#
.....#..............................................................................................................#.......#.....
..#.......#.#..........#.......#..................................#..........#.......#.................#...........#...........#..
...............#.....#................#............#................#............#.....#.#........#...............................
....#.....................#................#.....................................#......................#.#.......#....#..........
........#...............#...#.....................................................#........#.........#.........#..................
...#......#..........................#.....#..........................##.......#....#.............................................
.............#................................#............................#.....#.......#......#................................#
.......................#............#..........................#..................................................................
.................................................#..............#...#...........................#.................................
......#...................#..............................................................................................#....#..#
....................................#......#.....................#..............#.......#...................#.....................
............#...................................#...........#........#........#...........................................##......
#...........#..........................#....................................#.........#................................#..........
......##..#...............................................................#...............................#.........#.............
.......................#.....#.........................#...#.........................#.....#..........#.#...#.....................
.......................#..#.....#.....#..........................#.........#.....#....................#.....#....................#
"""


if __name__ == "__main__":
    runner = TodayRunner(test_input, real_input)
    print(runner.run('-v' in sys.argv))