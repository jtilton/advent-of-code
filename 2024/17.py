from runner import Runner
import sys

class TodayRunner(Runner):
    def parse(self, input):
        self.a = int(input[0].split(': ')[1])
        self.b = int(input[1].split(': ')[1])
        self.c = int(input[2].split(': ')[1])

        self.program = [int(v) for v in input[4].split(': ')[1].split(',')]
    
    def basic_compute(self, limit = None):
        output = []
        i = 0
        while i < len(self.program) and (not limit or len(output) < limit):
            opcode = self.program[i]
            operand = self.program[i+1]

            co = operand
            if operand == 4:
                co = self.a
            elif operand == 5:
                co = self.b
            elif operand == 6:
                co = self.c

            match opcode:
                case 0:
                    self.a = int(self.a/(2**co))
                    i += 2
                case 1:
                    self.b = self.b ^ operand
                    i += 2
                case 2:
                    self.b = co % 8
                    i += 2
                case 3:
                    if self.a != 0:
                        i = operand
                    else:
                        i += 2
                case 4:
                    self.b = self.b ^ self.c
                    i += 2
                case 5:
                    output.append(co % 8)
                    i += 2
                case 6:
                    self.b = int(self.a/(2**co))
                    i += 2
                case 7:
                    self.c = int(self.a/(2**co))
                    i += 2

        return ','.join([str(v) for v in output])
    
    def part_a(self):
        return self.basic_compute()
        target = '2,4,1,2,7,5,0,3,1,7,4,1,5,5,3,0'
        mid = 2978368709872*64
        i = 0
        while True:
            self.a = mid + i
            output = self.basic_compute()
            if output == target:
                return mid + i
            
            self.a = mid - i
            output = self.basic_compute()
            if output == target:
                return mid - i
            i += 1

        



    def compute(self):
        output_i = 0
        i = 0
        while i < len(self.program):
            opcode = self.program[i]
            operand = self.program[i+1]

            co = operand
            if operand == 4:
                co = self.a
            elif operand == 5:
                co = self.b
            elif operand == 6:
                co = self.c

            match opcode:
                case 0:
                    self.a = int(self.a/(2**co))
                    i += 2
                case 1:
                    self.b = self.b ^ operand
                    i += 2
                case 2:
                    self.b = co % 8
                    i += 2
                case 3:
                    if self.a != 0:
                        i = operand
                    else:
                        i += 2
                case 4:
                    self.b = self.b ^ self.c
                    i += 2
                case 5:
                    if self.program[output_i] != co % 8:
                        return False
                    else:
                        output_i += 1
                        i += 2
                case 6:
                    self.b = int(self.a/(2**co))
                    i += 2
                case 7:
                    self.c = int(self.a/(2**co))
                    i += 2

        return output_i == len(self.program)
    
    def part_b(self):
        # a = 8**15
        return
        a = 0
        while True:
            if a % 10000 == 0:
                print(a)
            self.a = a
            if self.compute():
                return a
            a += 1



test_input = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
"""

test_input = """
Register A: 190615597431823
Register B: 0
Register C: 0

Program: 2,4,1,2,7,5,0,3,1,7,4,1,5,5,3,0
"""


real_input = """
Register A: 158329674399744
Register B: 0
Register C: 0

Program: 2,4,1,2,7,5,0,3,1,7,4,1,5,5,3,0
"""

# b = a % 8     2,4
# b = b ^ 2     1,2
# c = a / 2^b   7,5
# a = a / 8     0,3
# b = b ^ 7     1,7
# b = b ^ c     4,1
# out: b % 8    5,5
# jump 0        3,0



if __name__ == "__main__":
    runner = TodayRunner(test_input, real_input)
    print(runner.run('-v' in sys.argv))