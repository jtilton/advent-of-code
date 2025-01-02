from collections import defaultdict
from runner import Runner
import sys

class TodayRunner(Runner):
    def parse(self, input):
        self.map = defaultdict(lambda: '')
        self.width = len(input[0])
        for i in range(len(input)):
            if input[i] == '':
                self.instructions = ''.join(input[i+1:])
                self.height = i
                return
            for j in range(len(input[0])):
                if input[i][j] == '@':
                    self.start = complex(i, j)
                    self.map[complex(i,j)] = '.'
                else:
                    self.map[complex(i,j)] = input[i][j]
    
    def direction(self, char):
        match char:
            case '<':
                return complex(0, -1)
            case '>':
                return complex(0, 1)
            case '^':
                return complex(-1, 0)
            case 'v':
                return complex(1, 0)

    def move_one(self, pos, d):
        start = pos
        while True:
            pos += d
            if self.map[pos] == '#':
                return start
            elif self.map[pos] == 'O':
                continue
            elif self.map[pos] == '.':
                self.map[start + d] = '.'
                if pos != start + d:
                    self.map[pos] = 'O'
                return start + d
        
    def gps(self, pos):
        return int(100*pos.real + pos.imag)

    def part_a(self):
        original = self.map.copy()
        pos = self.start
        for i in self.instructions:
            d = self.direction(i)
            pos = self.move_one(pos, d)
        
        gps = 0
        for (p, v) in self.map.items():
            if v == 'O':
                gps += self.gps(p)
        self.map = original
        return gps

    def expand_char(self, char):
        match char:
            case '#':
                return '##'
            case 'O':
                return '[]'
            case '.':
                return '..'
            
    def b_map(self, pos):
        return self.input[int(pos.real)][int(pos.imag)]
    
    def b_map_set(self, pos, val):
        self.input[int(pos.real)][int(pos.imag)] = val

    def move_one_horiz(self, pos, d):
        start = pos
        while True:
            pos += d
            if self.b_map(pos) == '#':
                return start
            elif self.b_map(pos) in '[]':
                continue
            elif self.b_map(pos) == '.':
                if pos != start + d:
                    x = pos
                    while x != start:
                        self.b_map_set(x, self.b_map(x-d))
                        x -= d
                return start + d
    
    def box_info(self, pos):
        r = int(pos.real)
        c = int(pos.imag)
        if self.input[r][c] == '[':
            twin = (r, c+1)
            return (set([(r,c), twin]), (c, c+1))
        elif self.input[r][c] == ']':
            twin = (r, c-1)
            return (set([(r,c), twin]), (c-1, c))

    def get_next_row_boxes(self, pos, d):
        (b, (rs, re)) = self.box_info(pos)
        for c in range(rs, re+1):
            r = int(pos.real) + d
            if self.input[r][c] in '[]':
                new_boxes = self.get_next_row_boxes(complex(r, c), d)
                if new_boxes == -1:
                    return -1
                b = b.union(new_boxes)
            elif self.input[r][c] == '#':
                return -1
        return b

    def move_one_vert(self, pos, d):
        start = pos
        pos += complex(d, 0)
        val = self.b_map(pos)
        if val =='#':
            return start
        elif val in '[]':
            boxes = self.get_next_row_boxes(pos, d)
            if boxes == -1:
                return start
        elif val == '.':
            return pos
        for (r, c) in sorted(boxes, reverse=(d == 1)):
            self.input[r+d][c] = self.input[r][c]
            self.input[r][c] = '.'
        return pos

    def gps_b(self):
        gps = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.input[i][j] == '[':
                    gps += 100*i + j
        return gps

    def part_b(self):
        self.input = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row += [c for c in self.expand_char(self.map[(complex(i,j))])]
            self.input.append(row)

        self.width *= 2

        pos = complex(self.start.real, self.start.imag*2)
    
        for i in self.instructions:
            d = self.direction(i)
            if d.real == 0:
                pos = self.move_one_horiz(pos, d)
            else:
                pos = self.move_one_vert(pos, int(d.real))

        self.print_b(pos)
        return self.gps_b()

    def print_b(self, pos=None):
        for i in range(self.height):
            line = ''
            for j in range(self.width):
                val = self.b_map(complex(i,j))
                if pos == complex(i, j):
                    line += '@'
                else:
                    line += val
            print(line)

    def print(self, pos=None):
        for i in range(self.height):
            line = ''
            for j in range(self.width):
                val = self.b_map[complex(i,j)]
                if pos == complex(i, j):
                    line += '@'
                else:
                    line += val
            print(line)

test_input = """
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""

real_input = """
##################################################
#.....OO..O..O.O..#....OOO..O...OO.....O....O....#
#.O#...#OO.....O.O.O....#..OO..OO.##.#......O#.#.#
#.....O.............O..O....OO#...O..O.......O...#
#...O..#..........#....O..#...O.OOO....OO........#
#O.##..OO....#O..OO#..#.#...OO.O....O#..O.O.O..OO#
#......#..O..O#.OOOO.O.OO...O#.OOO...#...#....OOO#
#.#......O.OO......OO.O.O....#.....O.O.O.OO.##OO.#
#.....OO..OOO...O........O...OO.O....O.O.....O...#
#..O#...O#.....OO...OO.OO.OO..........OOO.#.#..O.#
#....O....#.O......O......O#.OO.O..#O...#......OO#
#......O.#O...OO.....O..........#......O.O.......#
#O..#O#O.OO..O.O.#...#.O...O.#OO.....O.OO#OOO..O.#
#...OO#...OO..O..#.OO.##....O.O....#OO.O.........#
#..#.........O....OOO..#O..OOO.O....O.O...O......#
#.OO......O..O#.......O.O...OO........#.....O..O.#
#OO...O..O..O.O.OOO.........OO.....O.O.......O..##
#O...OOO......O........O#...........O.....O.OO..O#
#..OO.....#..O..#.OOO...O..O#....O.OO.#...O......#
#....#.O##.O..O...OO.O.O#.O.O#.#O.#O.OO...O......#
#O....O....O..O..##O....O.....O.O..OO..OOO.OO....#
#O.......O..#O.......O..O...O....O...OO.OO.#.....#
##.OO.OO#.O#.O.OO..OOO.O...#..#...O...O..#...O...#
#.O...O..#..OO.O..O..#O.OO...OOO.OO..O....O.....##
#.O..OO..O.OO#...O...OOO@..O.#O.OO.OO.....OO..O.O#
#..O....OO..#O..O.O.O...O..OO....OO..OO.#.#.O....#
#.##...O.O...OOOO.O.O..O.O..#O#.O..O.OO#..O......#
#OOO#..#.#.O##.....OO.O.O..#O..O...O.....OO....OO#
#..O.O...#........O..O.#....OOOO.....#..#O...O..##
#...O....OO......O.OO..O#O.O...#........O.O.#..O.#
#.....OO...#OO.O.OO.O#.O.O.#..........#...O....O.#
#..OO..#O.O..OO.O.O.O...O.O..OO.OO..OO.....O...O.#
##O.....O.#.O........O...OO..O#..........#....#O##
#.#O.....O.....O.OO.OOO.O............O.O...O#.#O.#
#.O..#.O....#.........#..OO.OO.#..OO.O.O.O.....O.#
#....OO#....O.O...O...O..O#..O.....O....O..O...O.#
#O...OO.O..#..O........O..#O.O#..#O#...O...O..#.##
#............O..#..#.O...O.##OO.....O.O..#.OO#.O.#
#....O....#........#O..O.O...............O.#..#..#
#O....OO...OO...#...O.....O.#O#.............O..O##
#..OOO......OOOO#.OO...OO#.O..O........OO.O.....O#
##.OOOO#..O.O......O......O....O...OO.OO.OOO.....#
#.O.#.#.O.#......O..OOO#O#OO..O...#O.O#.O..#.O...#
#O.OO..#OO......#.#.O#..O.O....OO....#O...O......#
#.O#...O...OO.O..O#..OO...#.O.O...O#.##O#....OOOO#
#..#........O..O...OO.#.....O..O...O#.OO..O.....O#
#.#.#.O....O..O..O...O.O.O..#..O.O..#...O..O.....#
#O.O....OO..O..O..O....O..O.OO...O.O.....O.#....##
#.OO....OO.....OO.......O...O..O.OO#..OO...O.O.#O#
##################################################

v^^<<<<<^^>v^>><v^<^<v><^^v<^^<>>^^^<^^>v>>>v>v>>^^<^>>^>><^<<v^^<^v><v^><><v^^<<^>v^v^v>v<<vv<^^<vvv>>>v<>v>v<^>>v<>^><vv>^^vv<v<^^vv^v^<v<>>vvv>vv>>v<^v<v<><<^>^<vv^<^>vv>vv<><>vvvv>^v^^<v>vv<^<v>><vv><>><>>v>^v^^v><v>>v>^<vv^v>v<v^>>^><<<<><^>v><v<>>v>^^^><v>^>v<v^>>^^<vv^>^><^>v>><v^>^>><v<^>>>^^<<>^v<>>^>><v<<>^^><<><^>><<>v<^^v>v^<><^><<^v^^>^>vv^^<^^v<v^v><<v<>^vv<<^<>^v^v^<^^v<^^v^<<v>>v>vv<^<>v>v<^^><v<>>^>v^^^^><>>v>^<^>^^^v^>>>vv>^<vv>^<>^<v<v<vv>>v><>>^<v^^^v>>v<<v>^v<v^<>>v<^v<<vvv<^v>v^^><<^^<v^><^v<<>>v><v^<>>^v^^^^^><>><^^^v<^v><v<>>^vv^^<>v<<<<^vv^<<>^^<<>vv^vv<v^<^v<>><<v<v<<^v>>^>vvv>>>^vv<<<v<>v^>^>vv^>v<v<<><v^<^v<>v><<^<v<^<^^v^vvvv^>^v^>vv<v>^v><<vv^<v<<^v>>vv>v<><v^>^<^><^><><^<^<<>^v^^<<v^>^^><><<>v^><>vv<<v^<<vvv>>^^>><>v><^vv<v>>vv<^><v<v^^v>>><v^vv^vvv^>v>v^^<>^^>><^><^v>^>v<<v<^>vv>^<v^<^^vvvv><<v^<^^><v^>^^<^vv>^<v>>v><<^v<v<<>>^><<v^vv<>^v><>^<<>^<<><>v^<><<<^>><>^><v>>>>><^<^<vvvvvv>vv>>vv>^>><v><^<<>>vv^v<^>^^^^v<<v>>>v<<^<<<<v<^vv>^<>><v>^<^v>>v><<>>^v
<v<<<><vv^^<>^<>^<^v<><^v>>vv^v<^^<v<><^><^>^^^v^v>^><^<<vv>v^v^<^>^^^^<^><^v^vv<^v<v><>>>^^<v^v^<<^^^^^><v<>><>^<v^<<^v<<^>>vv<^<<><<^^^^v>><>^v<^v<>v^^^^<<vv<v<<<<v<<>^<^^<v<^^>^v^^>>vv><<>><<<^^v^v<^v>><^v^>^^^<>^><v^vv>v<v^v>>v^^v^>v>^v^^^<<v^<v>^vv>v>^^v^v>>^^<<v^vv^v^v<v<<<>>><><><<^^>vv^<<<>^v<>v<<<<<>^^^v><v<<^v<<^v^>><v<<>vv><<<v><v^<<vv<v>v^^>^^^<v^v>vv><v<^v^>v<>^^<v>^<<>>>><>>>>v^^v<>^>><<vvv<^>v<^>>vv>^<^^^^<<^>>v<>>^<><^^><><>>^>v<v<>^^>>>v^^<><>^v<<><<^><<v<v<v<><^^v<v<><^>><v>^v>>v<<>vv^>v<<^>>v><^^^>>>^>^>vv^^v<>^>^v<<<v^<<<^v>>v><^>v^>v^>v<<<vv>^>vvv<<v^vv><^vv>^>^^^>>><>v>>>^<>v^v><vv<><^>^>>>^v^vv<<>^>^^^<<><<^^vvv^v>v^><>^^^<<>>>>^vvv><>><vvv<><>^<<^<<>>^^<^^^^>^v<<<^>v>vv^^v^^>^v>^v^vv<^^<>^^^<><^^vv>v<<>^<^vv>>>>>^^<>>vvv^v<<^vv>>>^v<<<vv>vv<^^>^v><>>><>v^v>^>^><vv^><>>><>v>>vvv<><vvv<v^^^<v^>^vv>^v<<><vvvvv^>v>v^^v>><v><>>>v^><^v<>><<>><^><v^vv<^vv<^>v<<<<^<>vv<v><vvvv<>v^v^v^>^><v^>>><<<^>>vv^v>vv^^<^<^v<vv><v>>v>^^^^^v^^><<vv^vv^^>v^vv^<<<><^<<<<^vv>><^>>>><<v
vvv^^<><<>><v<>v^>vv>>vv><><^<><v><<^>>vvv<><>>^<<>^v>^v>>><v<><v^vvv<^>>>v>v<vv^^^v<^<^v^<><v<<^<^^^><^v<>vvv>>><<^v<v>v<vv<^>^><>v<<v<<^<>vvv>v<^>v^v^vv>^v<<><^>vvv<v<<<^^>^v>>vv>>^v><^^<^^><<v^^>>>>v^><<v><vvv^>v^<v<<v>>><<^<v<v<<<v^^<><v^<<^<vv^^^^vvv^>v^<vv<>v<<<v^<>v<v<^<<^>><>^^^v^>v^v^v>v^<vv<v^<^>v>v<>>>^>><^<<<^v<^v^v^^^^^><v<<>v>><><>^<>>v<v^^v<^><<>><^^v><<v^<v>^v>v>^^><^^^>>^<^<<<<^^>>^^vv^^<vvv^v<^<vv^<^v<>><v^^v>^^^^v<<<v><<<v>v<^^^<^^>v<^>>v^v>^^<v<v>^v<v<<<^v>^^<<>>>>>^<^vv<<>>^vv^>^>>^>v>>>>^>v>^v<<v<^<>^<vv<v<>v^v>>^v^>^<vv<^v^^v^<<<><<<>vv^v^<<^^^v^^<<<>>>vv>v^<<^<><^^>>v>^v<v<<>>^^^v>^>^<<<vv<<^vvv>v<<v^v^><v><^v><<v<vvv<^<v<<vvv>>v^^^<v^<^v>><<^><<<>v>>><<<^<^^^^v<<^^>^><^^vv>v>>><vv><vv^>vvv>^<>>^>^^<vv<^<<v<v^v<v<^v<>><^><^<vvv<>>>^^<>v^vv^>v^>vvv^>^<^><<<<^v>v^v^<<<>>^<>^<v>^v>><<>><^^v<^^^v<>^^<vv<>v><^v^>v^v<v>>>^>v<^v^^v>^v<v^vv^v<<vv>v>>>>^vvv^v<<v>>^vv>v^>><^v^v<><^<v<^^<v^>vvvv>v<>>vvvvv>v<<>v<^<^^>^^v^v<^^^^v<>^^v><^><v>v^<^v<^<v^^^<>vv>>>>>^vv><^^<v<vv>
<^^><<>>v><<<vv^>vvv^^^>>v^>>^><v^v^>>>^<^<>v>><<<v^<>v^<vv>^<v>^>v^^<^<^v^v><><v<v^<><>^v^><^^>><>v>><v^^^^>v^^v>^>^>^>^^^>v^^<>v^>>v<<^^^^>>^><<v^><v^v<^>^v^<^<v<<<vv<^vv^^<<^v>>v>>^^^>v^v<>v^<^v><^>^<>^v<^>vv^>^v>^^<^>v>^^<>^v^vv><v<v>><^vv><^^vv><><v>><^v>^v^vv>>><v<v><v>v^v<^v<>^^v<>^^>^^^^^>>><^<>>v>vvvv<^<<^^>^><^^<<>v<<v<>v^<^<>>v>^v>>^v>>v>^<^>v>v<vv>^v<v^>v>^vv^v^v>v<<v>>v><>>>^<v><^^^^^^>^><<<^<^><v<>v>>v>v<><<<<>v<v<<^v^^^v><<<>^>^v^><<<^>><^>v^^>><^<^^v<v>v^>v^>vv^v><^<^><>^^v^<<^v>v><><>vv^^<^v<>>^^><>^^^v<v><><vv<v^>>^>v<v^>v^^^><v^v^<v><<><<v^v<>><v^<><^<vv>^v^>>v^<v^vv^v^vv^vv<<>^vvvv^^vv^^<^v>v^v<<<v>>^>v<><vv>>v<v<^vvvv<^v><<v^><>>^^<><><^<v>>^v^v^<<v<>^>v<>>v^>v>v>^v^^><>^<><>^^^><><<^<>^<>^>v<><>><v><v^>v^^vv^><^><<>v>v<^vv<>^v<v>>^^^<v<^v^^^^<<><vv<<v^>vv^><<^^^<<>^>v^>v^vv>>v<<>vv<v^>v^>vvvv^>^<vvvv^<>^<<vv<<<<v<v<>>^<<^<>v>>v><^^<v>>><<v>vv^v^^^^^^^^v>^^^^v<<^v^<^<<<v>><>>v<>^^^^>^><v^<>^v<v<>>v^v^^>vvv^^v><^v>v>v>>^>>v><>>v<^>>><^<<>^>vv<<><v>^^^<<v^<>^^<v^^<v<
^v^v>v<<^v><v<<<^<v<vv>^><^^>>vv<^<>>>>^^v^>v^^v^^<<<<v<<^vv<<><^<<^<>v><^v<>>>^^v><>>v^v<v>^>v<^^>>^>v^<^<<<v^v^^>^^<<^^^v^<v<^vv>vv>vvv^>^v>v<^v>^vv<><v<><v<>>>>><^<>^>>^vvv>v^>v<<<<^v>>v>^vvv<>^^^v>^v^>>^^<^^^^><^^^v<<><>^v>><v<<v^^<><v^>v<v><><<<v<vv<v>^v^^>vv>^^<^<><<v^^v^><^><^<>^<>^>^^<vvvvv<<v>>>vv>>v>vvv><^<><^<<<>><>vv>>^v^^^^<>v><^^^^>>v^vv^<<>v>v<^<<^v<><^^^^<<^<<^vv><<v>v^v>^<>vv^vv^v^><>v>>>^^^>>vv>^>v<v>v<>v>v><v>^^v^vv><vv^<>^>^<vv<<<^<^<<><>^^><v<>v><vv>v>v<<>^>><<>v<^<vv><><^^vv<vv<^>>v^<>v<^^<^^v^^<<v>v>^><v<><v<^^^>><v>v^vv^>vv^>^^>^<<<<>>><>v<><<v^<><v^^<vv>v^vv<<<^v>>v>v>^>^^><>vv<^vv>>v><<vvvv>vv^>>v><<<^<^^<^<v<v>>>^v^v^v>^>^>>>>^^vv>^>v^^>>><>^^^v<^>v<>^<>v<^<v<v>>><>vv^<<<^^^><^v^vv<^>v<vv>v^>>><v^>>>^<<<v>^^^>^<v>^<<<^v>^^^>v>vv>vv<<^<^><>>v><><^v^>^v><^>^vvvv^<><>^>^vv><>v>>v<>^>>>^v^vv^>^>^<^^<v>v>^^>vv>>vv^<v<<^<v^^vv<^>^^<><<v>^^>v><>v^v^<vv>^v<^^><>^<>>v^vvvvv^^<<<>v>v^^^<v<^<><v>vv^v^<<^<<^v<<^v^v><>^><^<^v>vv<^^v<v<^><v<^v><^vvvvvv<^<^^v^^v>v^>>v>>^<v>
v>^^<>v>^v^><^><>vv^<v^^^^><<<v<>^<<^^vvv<><^v><>>v><>><v<vv^><><v>v^v^^><><>^^v<<vv<^<v^^<^<v<^<>^^^vv>v^>vvv>^<<^>v<>^v<<v^<><v<v^v><^<v^^^v<>>^^vv>^^v>^vv><v^<v<>>><>v<v<<v>v>>>^><>>>>^^>>^v<vv>>v^><><^^^^vvv<^>vvv^>v<>^<<v<<>^<>v<<v<v<^<^^<^<>v<<<^><vv<>v^v^>v>><>v>v<<<<v^v^<><^><><vv><^^^><v><v>>v<<<^v>vv^^^<v<><<>v<v^<<<<^>>>>^^^v^<><v<<^<^^<^<v>v>v<>^v<<v^v<v<v^>>>>vv^>><v<^v<v<^>v>^>v^v<vv^<v^><><<^>^><<<>><<v><>^<^<<><v><v<>vvv<<<vvv<><v^v^^v^vv<^<<<vv<><>vvv<<vv^^v^>>^<v>>v<<vvv^<>v>^<^<<^>>>^<<><>^^^<>>v>v>>^vv<v><^>>vv><><v>>v>^vv>^v^<v>v^>>v^^^>v^^>v>>v^<>vvvv>v<<<^^v>>vvv<>v>^vv^^<<vv>^<<>vv<^vv<^^<>v^>>>^v^vv<^<^^<>>^^<^<>vvvv^<>^^^<^^vvv^v<<^^>v^>v^>v><v>^^v>^vv>v^vv>>>v>>><<v>^v<v>^v<<<v>^^<v>>>>>>>>^<vv^<<v<vv^v^vv>><^^<>v^<>^vv>><>^<^^>><<^v<>^>^v>v>v^<^v^>><<<>>v>><><v><v>^>^^^><<v>v^<^^>^>^^<<^vv<>v^^>^<^><>^^<v>><^><v<v>^vv<>^v>^^^^<v>><^vv<><>v>v>vv^><>>^v<v^v>v^>^<><vv^vv>v^^^<^>>v^>^<v>^^v><v>^>vv<<<v>^<v^^^<^>v<v>>^^v><>vv>^^><vv^^^>^v^^<<v>>>><vv>v^^<v>vv<><>
>^><<^^v<<>v^^v<^<^<<vv>^<<v<>>^^^<>^<<vv<^v>^^v<>v^^<^<^v<vv^<>><>v>^<^<v>v^vvvv^^>^v^>><<><v^^>^<<^>^<v><v^><<<vv>vvv>v^>v>^v^<v^><v>^>vv<^^v>^>^v>>vv<<>>><v>>><>^><>vv^v>v><v<<<v<vv<^v>>v>>><<>^>>>^^^><v>^vvv>>v>^^v^<v^^<>vv^v^^<^^>^<v>^>vv^^^v^<<^>>><><<^>>>vv><><^>^v>><>v<vvv^v<vv>^v>v>v^^><<^^>v>vv<<^>v<>v><^<v^>v<vvv>v>v<v^^v<<<v^v^>>><<<>>>v^><>>v>^<^v^>>v>^<v<v<vv<^^^v<><^>>vv>>v<v>>^<^v<>vv>^^vv<>><v<v<^^<>^v<<<^>^v^^v<<v^v><^^^^<^<v>^v^^v<<<><v>^^^v^>^<vv^^v>v<<<^>v>>^^^>v<>><<<><<<^<>v<v<><^^>^v^<<v<^vvv>^>v>v^v<>>^<v<<v<v<^<v>v>^<^<>^^<>>vv^^>v^<v<v>^^<vv<^^^^>^>^<>^^v<^^v<^><vv>>>v^^vv<>>><v>v^v^^><<<v<^v>vv^<^^<<>^><<^>>^^>v^<^^v^v>>^^v<^v<v<>><<>^>^<>>>>><^v^<>^<>>^v>^<><>v<vv^v>v^<<v^v^v^^>><>>^^<v>^v^vv<^vvvvv><>v>><<<><^vvv<<^><<v<v<<><>>><vv>v><>v^>>^v^<>>^^^>>v<^^^>vv>v>^<^>^^>^<<<vv><<v^<<<^v^<>>^<^>vvvvv>^^<<v>>vv^v><^<^v>>^<^><<><<>v><v^>><^^v^^<<<>vv<>^^^v^v<v<<>^^>^^>^>^>v>>^<<<<v><>v^^^<v<><^^^<>v^^<v^v^>vv^>><^v<v^^v^>>^v><^<^^>v<v<>^v>>^<v<^^>>v^<v^><^>^>^v
vv^^^v>^vv^v^<<^<v<<^><^><^v>>v^<^>vvv>v<>v^<^><^>v^>^<<<^^>>v<^>^>>^>vv<><>^<<^<<^vv<>^>v^^^^v^v>>^><<v^^^v^>>^^^vv>v>^>v>^<<<><v^>^<^^v><v^^vv>vv<v<<^^<<>>^v^>><^>vvv^^<^v>^<<>v<^v^>>>^><<^>^^vv^>vv>^v^<v^<>^<vvv>^v^v>v>^<v>><>><<^>>^<^<vvv>>>>v><<^>vv<v>^vv^<<>^vv<<>>>>vv<<^v^>^>v>vvv^>v<^v>^>^v^<<^<<<>^<v^v>><^>v>>>^>>^v^>v<<v>^>^<^vv^v<<>v><>^v^><<><vv><><vv<^v>^^v^^<>><>^^v<^v>>>vv<><<vv><<^^^<vv>>>^^>^>v^>>^><^<vv>v<^<>v^><<<>vv><<<v>v><>v><vvv>vv>v>v<<<<v>v<^<>v^<^<^>^^^^v>v><^^vv^^^^>>>>>>v^><<^<^v>>v^<v>v>><><v><><>>vv^>>vv<v<^vv<>^^<v>><>^v<>^^v<><>>^^^<v>>v>>v<>>^><<<^v^^>>v<v<^v><^v<^<v^<>vv>>^^>>^v<^><^vvvvv<v<^<><<>v>>v>vvv>>>^v>>>v^v^^v^<vv^^<^><<>^<<>>>vvv^v^<v>>><vvv<v<><v>^^^v<^><v><^^>^v>^^>^<vv<^v<>^v^^^>^^>v>^^<^^^<^^>>v><<<<<>>>v>>>^vv^^>><vv^^>vvvv^vv>^^vv<<<<<vv<v^v>vv^>>v<^<<><v<^vv>>^>vv^vv^<^^^^<^<>>^<<^<><^^<><v<^>vvv^>^>>>>>^v><>^<>^v^<><>^>v><^^<<<v<^^v<^><^<>vv^<>^v<>vv<><>^<^>^^^>><^v^>^<v>><vv^vv>v>>>v^<^<^>v<^v<^v<^>v^^^v><>^>^vv>>>>^<vv>^><<<<<^>>^vv
v>^vv<>>>>^^<>>^><^<vv>>v<>v<^<>>^>^<<><v<v><v<<>v<^v<<vv^>>>v>^>><v<v<><>v<^>>vv<v><<^<^v^v<^v>>><^^>v<>>><v><v^^>vvvv^<v><<v^<<^^^<v>^<<<<^^v^<^^><^<><>>^^>vv^<v<>^><^v>^<v^><^<v<^v^^^<>>v>v<<>^^>>>^<<^v^>^^<v>v^>^^vvv<^v<><v^<^><^vvv>>v<v<v><v>^<v<><<^v>v>>v>>^vv^v^v^<v^><<^vv<>v^>vv><<<v^^<v^v<>^>v<^v>^v>><vv<<^vv>vvvv^v^^^vv^v>>^^v><^<v^^>v^>^<>^<^v<^vv<v<>v^^vv^^v>^vv>>><^v>^<>>v<^^v<>vv>^>v<^^vv<^<v^^<<^v>>^^<v^^>v>><v^v^^<<^<>v^<>><v>v^^>>vv>^^vvv<v^^>^v><<vv^>>^v>>^^<vv>>^^<v^<>^<^><^>>^^^><v^v<><^^>><vv><>^<^^^>^<vvv<><<^><^vvv<^<^>^<>vv^<<>v^^<vv^<v<v>v^>^<><<v><v<>^vv^>>^<^^>v<<v>>>v^>^>>v<v>v>v<<^<v^^<<<<^>v<>>v<><v<v<v<<<>^><v^^>^<vvvvv>>vv<v<^^<v<^v^^^><<<vv<vv>>v<<^<v<<<<>^vv<<><vv<v>^<<><<>>v<<v>>>^v^>>><>v>v<^<^<vv<<<v><^>^^^<>^^v<vv>v>>>^v>>^>>^><v>><^^<<>>v<^^>><^v>><^>vv^^^<vv^>^^><^<vv><<<><<><>>>v>^v^<v^<^>>^>vv>v<^<>vv><><<^>v>v^vv<>^>vvvv<>^<<v<^v<^>^>>>^v><^<^^^^^>v>v<vv^<>^>vv<<<<<v^^<^<v<^v^v^v>v^><<<^v<v<<^<v^^>v>^>^v^<v>><^v^>v<v^><^>>>^><<^^v^^^v>>><^vv>>
>>>vvv<^vv>^<>v^vv^><>v^>><>^^^<>>v<^>^v>vv<>^vv^vv^vv>v<^^v^v^<v>>><^>^^^<<<<<^<vv>^<^vv><v>v<>^vv>>^<vv>><><^^<^><^v<vvv<><^<^<^^^>^^>^^^>v>>><^>^<vv<^>><^>>^>^<<^<>v^>^>>>v>^^<vvv><^^>vv^><<<v>><^<v^^>^<v><v^><<^v^^>^<><<<^><>v>^<^>>^v<^^^<>vv>^<^<^^v^v>>vv<>v<v<<^^^vvv><v>vvv^>><v<<v^<<<v^v><>^vv<^><>^v><>v><>v><>^v>vv>><^v^^^<<>v<vv>v<><<^>>v<^^^v^v^vv>>><><vvvv<^<>>vvvv>v^>^vv^v^<v^^>v<v>>v>v><><<>^^^<><>^^<<>^v<v<^^<>^v^^<>vv<v^^^v>>v><<^v>^<^>>^v^>^<<<<v<^<^^vv>v^v^>^<<<<v>v<vv<v<><<^v<<^>><^v<v>><>^<<<^<^^>><<>^^^^^>v<><<<<v^v<v>>^^>>vv^<v><^>>vv^<^<^><v^<vv><vv^^>^^>^^<v<>vv<^v<v>>^>^vv^^v<<>><v<v<<v^<^v^^<v><<>><vv<^v^v<^<v<<^vv<><<<>v^^<v<><<>>vv<^><<^^vv<<<vvv>vvvv>v>v^v^>vvv^^v>^>^^<><v>^<v^>^><^v^<<<>v^^>^^<^^<<v><^vvv>>^^v>^<v<^<^^<v<vvv^vvvv>>^v<>>^<v<>^^^^<<v<v^>^><<<<vv<^v^v<vv^<^v<<>><v^^^v>^v<vv<>>v^><<<><v>^^^<>>^<vvv^^>v^^<^<>v^^<>v<>><>^>vv<<vv<v<vv^v>v<<<>^><vv<v<>>><>>v<><^><>>v^^>><>vv>^<<><^^v<<^^><>>^^>v>v<><<<>^>>^^><<vvv>><^^^<^<<>vv>>v<><^>v>vvv^<><>>v^^
v^^<<^<<<v^v>>vvv^<<>v^^><^^^v><vvvv^^<>^>>vv<<<^vv<>>^v>^<v<>>^^>^^<<><^v<>v>>>^v<>^vv^^<<<<v^>^>>^^v>><<<^v^^^v><>vv^^><>v>v^<^v<v^v>><^v<><^<^>^<^vvv^<^^^<<<^<>>><<^>^vv^<<<><<^>^<vvv^>v<vvv<<<^v>>^<<v<^<<<><v^^v>>vv^><^>^v>^><^<>^<<^<v^<^v^^v><><<vv^<^><><>^<^<^v>vv^>>vv<>><v^<<v^^<>^v><^^^>^^>>>v><><vv^v>^v>v<>^vvv<^^^^>><^<<v<<^>^<>><vv^v^>^v^v<v^>v>v>>v^^v<>v>v<^<^<v>>^>v<v^v>><<><^<^v>^<^v^v^<v>><<<<vv<><><><>^vv^^^><v<^^><<^^>>v^v^^vv<>v<^vvv^v>^>^<<<^v^^vvv<^^v>^v<^>>>>>>^v^><><<^>^<>vvv^v<<<vv^v>^^^vv^<vvv>^vvv>>^v>^vv>v>v<^v>vvv^^>^<>^>>vvv<>>>^^v^<>^vv^^vv^v>v<^v^>vv<^<<<v^v<^vv<<vv>v>^>v^v<^^v^^^^>v<^v>><^><<^^>^^<^^^<>v>>vv^^^v>v>v^>>^>v>v>^^v<<<<<vv<>^<v><<>^<v>>v<v><vv<<^>^<>>^<v<^>>v>>v<v>vvv^^vv>><^<vvvvvv^>^<^^>^<v>>>>><^>><>>^^>v><>>^>vv>vvv<<<><<v^<^^<>^>^^>^<vv>^^^^>vv>v>^^>v>>v^vv^^^v^>>>^^<<v>v<<>v>^vv>^v><v<^v^^<^<v><>^>>>v^>^v><<v>>^<<><><^>vv>>^^v>^>>^v<><^^v<^v^v>vv<^<><<v>>^><<^<<<<^^v<<<^^^^>^v><^vv>>^>>v^v>v<v<v<<^<v>><<>^<v<^^vv^^^^v^v>><^vvv^>^^v^<^<<<
<<>^<v>>><^v>v<v>^v^^<<^vv>>>><v>^<^<^v^>^^vv<v<vvv^vvv^^^<v>>>vv<v<<^v^><>><v^<v^v^^^vv^^<<<v>v<^>>v^>^vvv>>^^^v^vvv>>vv^v><v<>>^^vv<<<v<^<^v<v>>v^^>vv^><^<v>^<>^>v^v>v>v<<<<v^v<>^v<>>>v<>^^<><^^<^<<vv><>v^^>>>v><v<^vv<^<<v>v^><<^^vv<>^vvvv>^>v><>^vvv<v^><<^>^><<<vv<v^^<>>^<v>^<v^v^^<<<vv<^>>^^><>><v<><><>v<^^<^vv^>v<^<<vvvv^^vv<>^^><v><<<<^>v<<^<<v><<><v<<<<vv<^<<<>^v^v>>><vv^<<<v>><<^<^^><v<>^>vvv>>^><>vvv><<>^vv><>^<>>>v^>vv>vv^^^v<^v><<vvv<^v^v>v<vv>^<v^>><v^^<<>^><<v^v>^><v^vv>^<vv>^>^vvv^>><v^<^vv^<>>v>^>>>>^v<>vv^^><^v<<><^>v^v^v>>v^<v><v^>^v>>>>v><<<<<vv^<^>v^<^<^v<>>v^<<v^^<^><v^vv<>^vv<^>^v<^^v^v^v<v<^><<^><vvv^v^<><^><^v>vv^^<v^>vv^<>vvvv^vv>>^<>v^<>><><v<v<^v>^>>^^vv<>^<<v^^<v<v^<^>^>>^<v<>v^^^<<v^vvv><<<><^vv<^>vvv^<<^v>^^>^^<>v^>>^^<v^<>v>^^v^^>v>^^>^vv^<v>>^^vv><>v><<^><^<^<^v<>^v<>v^^<^>>^<>^<vv>>^vv^<<^v>>><v^^><v><>>v<v^>>>v^v<v>>v^vv^v>v>^<>v^>^>v><>^vv<^^^^<v^><^<^^><<<<<<vv^v<>^>v<>^v^>v<<<v<<v^^v>v^<v<>>vvvv><<^^<v<^>>v^v^<^v^<<>vv>^>v>^<>v^^v<>>vv^<<^v<<>v<^<<vv
>^>^>><<<>^<^^^>v>v<v<<^^^^^<^<v<^>>^>>^>vv<v<v>^<>vv^<>^<<>^^v<vv>^^<vv<>v><v^<><v<<^>v>v>^^<<>v>v><v^>v>vv^v^<v^v>^^<<v^vv>>><>^>><v<^<>><><^^>v>>^>vv<^^<<^<<>><^^>v<<>^<^><<vv<vvv><^v><<v^<>vv^v>^>>>vvv><^<<<<<^^>^^<>>^>v>v>>^v>v^<v^v^^v^v^vv>^^^<v^^v^>^v^>^^v>^v>^v>^<^^v>^>^<>v<vv^v>^<vv>^^vv<<^>>>>vvv<<v^>^^<>v^^^v<^><v^^<vv<^v<><>^^^<v>><>^<^v^>v^v>^<v<<<v^><v^<v<^v<v><v<^>><^>>v^v^<^v<v>vv>vv<>>^^vvvv^v^^v<^>>v<>v>^<^>vv<<>^^^v>v<v^v<<<><v>v>vvv>v<<<>^<>><<>^^v>>v<v<><^v>vv>^><<<>^>><v^v>^vv<vv^^>v<^^<<<>v^>v<><^>v>>>^^^v<><<v>>>>>><^v<>><^>^><^^v<^v><>>><^^>^<<<v<<<<>^v^^<v>^>vvv<v><v<^vvv>^^^^^v^><>v^^^<<^^v><v<^^><v^>>v<<<v>>^<<^<v<><<v>>v^<^<>v<^><<v^><<<>>>vvv^^><v^<<^^<vv^^>^><<^>^<v><>v>>><vvv<>v^^^<<v^v<>>><^v<^v<><<^v><^vv^^^^^>vvv<v>v^<>^v^>^^<vv>>>>>>^<^<^<v><v^>^<v>>><<>vv^v>v><><<><<<^<v<>><<v<^v<>v<>^<>^v^^v^>vvv>^<v>^^<<><v<v><^^^><v<^>>v><><^<<^^>>v<^v<v>v>>>v<<v^<<<>^^<v^<>^v<^v^<vv<><v>v><<<>^^^>^^^>^^^<v>^>v^<^^^<^v^<^>^<>v<>>^^>v^<v^v>><^^<v>^v>>^^v<v>>^<<>><
^<^v><v><^^<><^<^>v^^>>v^^^<^<v^<<v>vv<v^>>vv<><>^v<><^vv<vvv>^>vv>^<>><^<<<^>^^v<<<^<v>v<<>>^>^<<v>>>>>v<>vvv<vv>>^><<v<vv^^>v<<vv>^^<^>v^>v>^^<>><v^^^^<^>v^<^><><^v^^vv^<v><<^>>v>v^vv>><<v<v<v^^<v<><^><^<><>^v>><<>>^^^^^><>v^^<<^^>v<<<<^v<<<>^<v<^v^^<<^^^<^v<>><>>v<v^^v<^v^^>v>^>v^v<^^^v^>><>^>vv^<^>^v>^>v^>>v>v>>^^^>>^>v^<v^^^^>^v^v<<>>v><v^<vv^v<v^<>v>v^>^^<>><<v>>>>><<^vv>^<>^v<v^^<>>v<^>v>><v^>^<><vv>vv>v<><^><v^^v^>v<^<^>>v^>v<<^v^><v^^><^^>><<<>^<<<>v^>^^^^>>^><<^^v^><^^<^>^<<^^>v>>>v^<><^<<<>^<<^^^<v<v<<^^vv>v^><^>^>^^v^>>^>><<>^^>v>>^><v><vvv^<vv^>^<><<><><>^^<<>^^<>^>v><>>v<<>><>^^^<<<v<^>>v^><^^^^^^v^^^^>>v<<<><>^^vvvv<v<>vvv>^>v^^^>vv>>><^>^^<<v^<>>><^^<^^v><>>^<^>>v<v>^^vv^^v<<v^v>^<>v^<^>><^<v>v^<^<>><^^<^^^>^^<^><><^>v><v^vv^<^>>>^>v^^^<><^v><>^<>^v^><^>^^>>>^<vv<<^><>><<^<v>v>vv<<vv^^v>>^^^v^^>^>^^<<<^<><vv>v<v<><<><<^<v^>>^^>>^^vvv<v^<><vv>^<^><v^vvv<<<<v><>^>^<><v^v<^^vv<<>>^^>><<<><^>><<>^>>^<v<<vvv><<v^^v^^><<<vv^v^>^<v<><><>v>^^v>>v^<v>^<<^<vv<v<>>vv<<v^^><v<v>^^v
>>vvv<v<^v<<v><>^vvv^>^^v<<v<v>v><>^<v<<>v<<<v^^^<^<v^>^<><v>^v>^v>vvv<v^><v<^<^vv^<^^<<<^^<><<v^<v<><>v>v><>^^v><>><^><^^^><<>>vv^v>vv><>v^<<^<>^v^^>vvv<^>v>^v>^v><vv^<^v>v^v<^v<<^><<<>^vvv>>^v<<v>^v>vv<^^>>^vvv><v<><vvv>^>v<^^^^^vv>^<<^<<>^<<<>v>v^<^v>^>v^<<<>><^><>vv^vv^<<vv>^v^>v<<<v>><<^>vvvv^<^>><vvv<^v<v<^^v^v^v><^v>v>v<><><<>vv^^v>><v<><>v<^v>^<>vvv>^>v><<v<^>v>v>>^><^^><<<vv<v^v^vv>><vv<<^^v^vvv<^v>v><><>>v>><><<^>><v<^^^v^>vv><>^^<<^>v>><v^>^><><><^v^v^<<vv><^<vv^vv^^<^^^v>>v^^^>vvvv^<>vvv<<^<^v^^<^v>vv>>^>v^><<<>>^vv<vv<>><v>>v^<v<>v>^vv<>>vv>>v^<^<v<<vvv^^^v<vvv>><<>>^v<<>^v<>v>>><<v<<v<<<>vv>^v<<>>v<<vvv<v>v^>>v<^<>^^v><^^>^vvvv<^^v<^><^^<>v^>>vv>^^^>v>^^>v^>v<<>^<v^>>v^vv<vvv>v<vv>vv<>v><<^^>vvv>>>>v^v>>><^^^v<v^><<^><>><<><^><>><^>^^vv^^>v^><v>v>>vv^>^>^<vv^<v>^<<<^^<>v<<v^><<>v<v^><v^><vv^^>vv^v^^><v^v^<<>v<>^vv^v<<v<>v^v>v^v^>vv><><>>>vvv>v>><>vv<^^<<>v>v>v^v<^<v<>>^v<>v><>><v<<^>^><<<^v>v^vv<vvv<v>^>>>^<vvvv><vv^<^vv<<^>^^v<^>^>v<<^vv<<<>^v>v<><>>^^<<v^><^^>><>v>^^v<<
<<><^v^<vvv>^>><^^><>^^^<>>^>^>><v^vv^>^^v<>vv>><>v>v>v<^>><>v<v<v^^<<vv>^>v>>vv>>>v^<>^>v^<<>^^^vv<<^vvv>^v<v^<^^vv><v<<<^^<v^>^v<^>^v^<>v<^<^<vvv<v<^^>^v>>>v^^^^>vvv^>>>^v^<>>^<<><vvv<>v>>^^>^<^>>v^v^>>vv^^vv<^<^v<<<v<^^^><<<^^<>v<<>>>^<^>v>^<>v>^^v^v^>>^<>>^<vv<<^<<<<^^vv^v>>^vv>v^^<<<vv^><v^^><<^<>^v<^^>v>><vv^^v>>v^><^v^<^<<v>^><>v^vv^<<<^v^<^<^vvvv^^vv><^^v>>v^vv<<>>>vv><^>^v>>^v<<>>><>v>^>><v^><^><v^v<>>>>v><v^v>v^>vvvv^^^<>^>vv^vv<<v><>>>v<v<v<<>v>^v<>v>^v<^><>>v^vvv<>v<v^>vv<vv^^>><<<<^v^^v^v<>^<^<^<v<^v^><^>v<^>^<^<<<^^>v<^<^v<^v^<v>^<>v<v>^v<^v^>>^><v^^v^v><vv>v<<v<vv^^^<<<>v>^<<<v>v<v<<vv^v^vv>>><>v>v^^<><v><>^>^^^<>^^>^^>>><^<v>^>^>^^^<>v<vv<^^v^^^<^<<^>>>^^^><><v^v^<<v^<><^<v^^v>>^v^<^^>^>>v^><v<^v^>^>>^vv^<v^>^<>^>^v>><>>vvvvv<^<<v^<>v<><><<>^v>>v>>>>^>^<^vv>><<><<><<v<^^<<v^>^<<><v<<<^><^v<vv>^v>^<<v^vv<vv><<v<^vv^v<<^<>^^^v>>v<^^>v<^><<^v>>>><v<<>><>v^>v<v^^v^<><^<^><v>^<>^^>^^^<^>^v^^v>v<>><<v<<v^^v<><^^vvv<<<v<><><v<v>v^^<^v<vv>^<><v<v>^>^vv<>v<<^<>^<v<vv<<<^<<><v<^v
v^><v>>v><v>^>v><<>v^^>v><^^><^>>^vv><vvv^>v^<^^<>^<<>>>^^>^>><><<>vv<<^<<>v><>>v>^v>>^>>v<v^v<v^^v><<><>v<v>^<^<v^v^>>v^<vv^<^<vv^^><^^^v>vv>>^vvvv^^<<vvv^>^^>vv>^>^^^^^^^^v<v<>>^<v<><^>^vv>vv<<<<v>vvv^<v^v<v>>><<v<<^>>^v>vvv<v>>v<^^v>>v>v>vvv>v<><<<<<<^<^v<^>><><<<>v^>>v<<<^<^><v<<>>>v>v<>^^>>v>^><v<><<<v><>^vv<^^>>^vv^>^v^^^vvv^<<^<^<<v<^v<v<v><>>>^<v>^>>v^vv<>><>v<>><<<<>><v^>v^<^<>v^<v^^^>>^>^v<^^<<>^<^vv>v<<v<v><^^^v>vv<>><>v<v<v^<<v^<vv<<v^^<^vvvv^<>^^<^^<>v<v>^>>^v><<v<^v<v^v>^^>^v^<<<^>vv>>^<v^<<<<^<^^>v^<^><>^v^<><^v>><><<^v<^>v^v<><v^^^<v>v>><v<<^^vvv^><^>>>^<^^^v^><^>>vvv^>^<>v<^^<<<<^^^<<<<^>v<>v<<v^vv<^>>vv<v^<^^v<vvv^vv<v<^vv<v<<v^vv>>v>v<>>>>v^^<^^v><v<>v>vv^v>vv^<v<v<v^v<<>>v^v><^v<^vv^^<>^v^v<v^<<v^<>^^v>><>^v>^<>>v>v>v>^^v>v^>>v^v>^v^>vv^<<^^><^^>>^^vvvv>^v>>^^<<^v><^<^^><>vvv>>^^>^<<^^>vv>><<^<<^v>^>^>^<><>>vvvv^>v<<>>v^v>v^v^<<<<v<<^^>^<v<^^v<>v<^<<^^v^>^<^>v^^^^v^<v^>v^>>>vv^vv<<v<<^v^v^vv^<^<>^<vv^^><^<<<^>^<^^^v<vv<v^^>>v^>^>^<<^>v<>^^^>v^^vv<v<v<vv^>>vv>^^>>>v>
v<<v>^<>>v>v<><^^v^^<^<>><<><<v<^^>><>^>v<>v^v<v>><^><>^^>v<<^><><v>v<^^>^>^>>vv<<<^^><v<v^<v^><v>v>^^^<^<v>>>^v^>>>><<>^><>>v^v^v>>^^v<>v>>v><>>vv<vv^<^>><<^v>>^^v^<^v^>^<^^<<v^<v>vv^^^<<<>^<^>^^^^>v<<<<^<><<^<^>^v<^v<^v<v>^>^^><v>>^^><>vv^^^<>v<v><<<^vv>vv<<^>>^>><<^v<>^>>^>^<>^>vvv<v<vv<v^<^>vv>v^v>>>v<^<>v^<v>^v^<v^<vvvv>>vv>>^>><>^^><^>^>><^^<>^<<v><<vv<^<>^^^><^^<<>>><^v^>><>v^^<vvv<>vv><^^>><>>v<v^vv><v^>>vv>^><^v<v<<^^^>^<^<v><>v>^<><v^^^^^vvv<>^<<><vv<^v^^>vvv><<^v>^^>^v^vv<^<<><vv^><^^v>^>v^v^vvv>^vv^<^^v>v<vv>^<v^v<^^v^^<>^<vv<vv><<vvv<<<^<>^vvvv^v<^>^<<>v<v>vv<^<vv^^^<^v^v<<v<<v<vv>v^<<v^<^<<>>v^v<^^v<><<<<v<^<<>v<vv<><^v>^v<v^>>v<v^>>v><<<v<v>><>^vv^>>^>v>><>>vvvv<<v^^vv^v>^<^v^<vv<^<>^<^<<^<>>v^><v>v<>><^<>^<>>>v>>vv^^<<^^vv><v><^v<>v<^^v<<^v>^^^v>v^>v>^^^v^<v>>vv>>>^^<v<v^^<^<^^^vv^<^^>^^^><v^^^><^v>^v^>>>^>>v<<><>v^<<<^^v^v<>vv<^v>><>^<>^^<>>><^<>>v^v<<>v<>^v<<<v^v<>vv<<<v<v<><^v>v<<>^^>v>><>>>^><v^v^>v<v>^<^<vv^<<>>>^^^v^<v^v<^^v^vv<><<^v>^^^vvv^<>v>>^^v<^><^v>>v^>v^^v
<^>vvv^^v^^^vvv>><>^^<v>^^v^<<^v>^vvv^^<<>><>>v^v<^<<^^>^v<>^vv>>>v<^<<^^v^v>^>^<><vv<>>v<>^<^v<^<^<>>v>><^^^^v>>vv<^^v^<>^^><>vvv^<v>v<>>^<vv<v<v^>v>>>^v>^^<vv^<<^>^><vv^v<^<>vv<<^<v^>vv<>^v^v>^^^<>>v<v<^>vvvv^>^^v<>^<<><v<>^<^^<^<^><v^^>v<^v>v^>>v<>vv^<v>^^^><vv^v^v<<v<>^^v>v>^^v>v><v>vv<vv^><v<v^^^><^<v<^^^^^>v^><>v>^v>v^<v<>>v>><^<<^>^^^^>>v>>>^><<>v<^^<<><><>>>>^vv<v<>vv^<<<^>>vv>^<vv><^>><<<^>v<v<^^<^>>v>v>^vv<^>v>>^vv<^>>v^<<<<<^><vvv>^^<>>><^^<<<<><>v^^v^^^>^<><v>><vvv<^><<^<v>^^>v>>^>>>v><^v^vv^>^<v^<^><v<>><^vv^><>>^>vvvv<<v>>>>^^vv^<<vv^v^<>>^v<>^v^>v^><>><<^^<<v<>^^<<^vv>v<<>>>>>><><^^^v<<<<v^<^><>v><vv^^v>v^v>>v<vv>v^v<<v><<^v<^v><>^v^^<>v>v<^^^><^><^vv^^>vv>>^><v><<<<>>^vvvvvv>^^vvvv^v><^>^>v>^>^>^v<^^<^>v>v<v^v><<<v^>^<<<>^^^<v>^>^<^>><^<<vv>^^v><<^^<><><^>v^v^>v^><>^<^<><<<<v<<><v^>^^v^^<<>^v<vv>>>^^<v^^v^><v>vv><>^v^^v^>><v>^^v<^<^><^v>^><v^vv>^^>^>v<<^v<^>v^>^^<v>^>v^^^>^v^v<>^^>^^>v<v<^<^<v^<v<v><v>^<^v>^^^>>><<v<^v^^v^>>v<v^^^^>^^<^<<<v^<v^^^v^v>>^<vv>vv^>>>v>><<<^v
>v><<v^<<^v^<<vv><>>><v<>>><<>v>^^>^^<v>>>v><><<^<^v>v^vv^v<vv>>vvv^v<<<<v<<<<<^><>^><^v^^<v^>vvv<>^vv<^^^>><^^v^<<<<^^<v>><vv<>^<v>^^v>vv>><<>^>v<>^vv<^^<<<>>^<^>>^<^><vvvv>v^v^<v^^v^<>^<>^v^^v^^<><v<^<>>vvv^v^v>^v^>v>^>><^>^<>v<v<v<>^^<>^vv><<<>^<vv<<vv^<^^v>>^<>v>^^<<><><v<>>v<<v^vv^<>v>>v^<v^<^^<v<^<^<^v<>v^<>vv>^>>><<><^vv<><<v<v>v<^v<^^vv<vv^>^<><^>^v>^>>^>^><<^v^^>v<<^^>v>v>^<>>v<v^><v<^v<v><><<^^vv>>>v^<^v^^>><^>>>><><^^<>^v>^<^><^^^^<>^v^^v>v^>>v>v>^^^v^><>vv<v^^<>>^^>>v<>^^>v<>><><v<>v<^^>^v^><<><<v><^^>v<vvv^^v<^<>><<vv>^>><^vvv>v>>^<v^><<^^>>>><<>v^^>>>>>v><><^^<v<v^v<<v>><>^><vv^^>>>>v^^>^^vvv>><>>^^<>>v^^>vvv<v>>>v^^^<<vv>^<^^<><v^v>vv<<>v^<><<>>^>^^v<v>>><^>vv<^vv>>v><<v^<v<><v^^vv<^<vv<>v<><vv><v>>v<>><^>>v>vv>^vv<^^^><>v^>^v<vv<>^>^vv^>>^><v>v^><^<^>^v^>vvv<<>>vvv<>><>>v^v><^<v>v^<^<<v^v<^^^^^^<vv<>>^>>v><^^<^><>>^^^>v^<>>v><<>>v>^>v<vv>v<<v^vv^v^vv>v>v^^v^^v<^^^<><^v>^v><v<<^^>>>^<v<^<><>^^^^^v^>vv<>>^^^<vv<>v^>^v^>>>vv<v>^>^<>^v^>>vv^>^v<<<^>v><^<<>>^>v>>v>^<v><^v>>^
"""


if __name__ == "__main__":
    runner = TodayRunner(test_input, real_input)
    print(runner.run('-v' in sys.argv))