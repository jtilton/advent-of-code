from runner import Runner
import sys

class TodayRunner(Runner):
    def parse(self, input):
        return input
    
    # To be called after self.parse
    def exec(self, input):
        print(input)


test_input = """

"""

real_input = """

"""


if __name__ == "__main__":
    runner = TodayRunner(test_input, real_input)
    runner.run('-v' in sys.argv)

### Results

# 01: 06:38 | 09:13 (02:35)
# 02: 11:00 | 34:22 (23:22)
# 03: 04:48 | 12:56 (08:07)
# 04: 31:57 | 41:09 (09:12)
# 05: 10:08 | 26:22 (16:13)