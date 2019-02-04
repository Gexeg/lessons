import os

class Neuron:
    def __init__(self):
        self.weight_coefficients = []
        self.limit = 35

        for coefficients in range(10):
            coefficient = []
            for i in range(10):
                coefficient.append(0)
            self.weight_coefficients.append(coefficient)

    def training(self, path_for_training_directory):
        files_for_training = self.collect_file_names_for_training(path_for_training_directory)

        number_of_right_choices = 0
        for file_name in files_for_training:
            if '_yes' in file_name:
                number_of_right_choices += 1

        for cycle in range(10000):
            right_choices = 0
            right_file_names = []
            for file_name in files_for_training:
                is_right_symbol = self.file_check(file_name)
                if is_right_symbol:
                    if '_yes' in file_name:
                        right_file_names.append(file_name)
                        right_choices += 1
                        continue
                    if '_no' in file_name:
                        self.lowering_weight_coefficients(file_name)
                        continue
                if is_right_symbol is False:
                    if '_yes' in file_name:
                        self.increase_weight_coefficients(file_name)
                        continue
            if right_choices == number_of_right_choices:
                current_cycle = cycle
                return current_cycle, right_file_names

    def collect_file_names_for_training(self, path_for_training_directory):
        files = os.listdir(path_for_training_directory)
        for file_index in range(len(files)):
            files[file_index] = str(path_for_training_directory) + files[file_index]
        return files

    def file_check(self, file_name):
        with open(str(file_name), 'r') as file:
            line_index = 0
            total_score = 0
            for line in file:
                sign_index = 0
                for sign in line.strip():
                    score = self.weight_coefficients[line_index][sign_index] * int(sign)
                    total_score += score
                    sign_index += 1
                line_index += 1
            return total_score > self.limit

    def lowering_weight_coefficients(self, file_name):
        with open(str(file_name), 'r') as file:
            line_index = 0
            for line in file:
                sign_index = 0
                for sign in line.strip():
                    self.weight_coefficients[line_index][sign_index] -= int(sign)
                    sign_index += 1
                line_index += 1
            return

    def increase_weight_coefficients(self, file_name):
        with open(str(file_name), 'r') as file:
            line_index = 0
            for line in file:
                sign_index = 0
                for sign in line.strip():
                    self.weight_coefficients[line_index][sign_index] += int(sign)

                    sign_index += 1
                line_index += 1
            return





new_neuron = Neuron()

print(new_neuron.training(os.path.abspath('neural_network') + '/files_for_task/'), '\n')

for line_of_coefficients in new_neuron.weight_coefficients:
    print(line_of_coefficients)