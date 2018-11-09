class Neuron:
    def __init__(self):
        self.weight = []
        self.limit = 35

        for coefficients in range(10):
            coefficient = []
            for i in range(10):
                coefficient.append(0)
            self.weight.append(coefficient)

    def file_check(self):
        file_name = input('Пожалуйста, введите имя файла: ')
        with open('/home/gex/files_for_task/' + str(file_name), 'r') as file:
            line_index = 0
            total_score = 0
            for line in file:
                sign_index = 0
                for sign in line.strip():
                    score = self.weight[line_index][sign_index] * int(sign)
                    total_score += score
                    sign_index += 1
                line_index += 1
            return total_score > self.limit



new_neuron = Neuron()

print(new_neuron.file_check())