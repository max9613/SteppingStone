import os

# Manages an experiment.
# Stores printouts and saves them to an experiment file.
# Requires explanation of an experiment before starting.
class Experiment:

    # Constructor.
    def __init__(self, directory_path, naming_convention, default_print_stream, description):
        list = os.listdir(directory_path)
        self.name = f'{naming_convention}_{len(list)}'
        self.directory_path = directory_path
        self.print_stream = default_print_stream
        self.description = description
        self.log = []


    # Start experiment
    @staticmethod
    def start_experiment(directory_path, naming_convention, default_print_stream):
        description = input('Please enter a brief description of this experiment:\n')
        return Experiment(directory_path, naming_convention, default_print_stream, description)

    # Prints to default print stream and logs the string.
    def print(self, message, end='\n'):
        self.log.append(message)
        self.print_stream(message, end=end)

    # Saves the experiment description and logs.
    def save(self):
        file = open(f'{self.directory_path}\\{self.name}.text', 'w')
        file.write(f'Experiment description:\n{self.description}\n\nLogs:\n')
        for m in self.log:
            file.write(f'{m}\n')
        file.close()
