from runner import Runner
import sys

class TodayRunner(Runner):
    def parse(self, input):
        return input
    
    def part_a(self):
        pass

    def part_b(self):
        pass


test_input = """

"""

real_input = """

"""


if __name__ == "__main__":
    runner = TodayRunner(test_input, real_input)
    print(runner.run('-v' in sys.argv))

### Results

# 01: 06:38 | 09:13 (02:35)
# 02: 11:00 | 34:22 (23:22)
# 03: 04:48 | 12:56 (08:07)
# 04: 31:57 | 41:09 (09:12)
# 05: 10:08 | 26:22 (16:13)
# 06: 10:29 | 21:23 (10:54)
# 07: 17:50 | 30:12 (12:21)
# 08: 09:52 | 13:56 (04:04)
# 09: 30:41 | 58:44 (28:03)
# 10: 19:46 | 20:55 ( 1:09)
# 12: 32:17 1:17:42 (45:24)
# 13: 12:45 | 35:06 (22:21)