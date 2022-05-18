class BaseConverter:
    data = None

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def parse(self):
        raise NotImplementedError

    def to_csv(self):
        raise NotImplementedError
