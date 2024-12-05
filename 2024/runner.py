class Runner():
    def __init__(self, test_input, real_input):
        self.test_input = test_input
        self.real_input = real_input

    def parse(self, input):
        return input

    def exec(self, input):
        pass

    def run(self, is_test_run):
        if is_test_run:
            input = self.test_input
        else:
            input = self.real_input
        parsed_input = self.parse(input.split('\n')[1:-1])

        result = self.exec(parsed_input)
        print(result)
