from random import randint
import os

class FileOperations:
    """Объект, взаимодействующий со структурой данных"""
    def __init__(self, files_storage_structure):
        self.files_storage = files_storage_structure

    def summ_from_random_files(self):
        """метод, выбирающий 2 случайных файла из списка доступных. Перед выполнением с помощью
        методов класса-исключения проводятся проверки на наполненность хранилища и корректность файлов"""
        cheks = Storage_exceptions()
        if cheks.check_storage(self.files_storage):
            first_file_name = cheks.check_file(self.choose_random_file())
            second_file_name = cheks.check_file(self.choose_random_file())
            with open(str(first_file_name), 'r') as first_file:
                with open(str(second_file_name), 'r') as second_file:
                    sum = 0
                    for line in first_file:
                        sum = sum + int(line)
                    for line in second_file:
                        sum = sum + int(line)
                    return sum

    def fill_storage(self, number_of_files):
        """Метод, наполняющий хранилище файлами, заполненными случайными числами"""
        for file in range(number_of_files):
            self.create_file()

    def create_file(self):
        file_name = len(self.files_storage.file_names_with_path)
        with open(self.files_storage.absolute_path + str(file_name), 'wt+') as new_file:
            for line in range(3):
                new_file.write(str(randint(0, 100)) + '\n')
            self.insert_file_in_storage(file_name)

    def insert_file_in_storage(self, file_name):
        self.files_storage.file_names_with_path.append(str(self.files_storage.absolute_path) + str(file_name))


    def choose_random_file(self):
        return self.files_storage.file_names_with_path[randint(0, len(self.files_storage.file_names_with_path))]

    def change_storage(self, new_storage):
        self.files_storage = new_storage


class FilesStorage:
    def __init__(self, absolute_path):
        """Структура данных, хранящая в себе информацию о пути до директории содержащей файлы и
        файлах, помещенных в эту директорию"""
        self.absolute_path = absolute_path
        self.file_names_with_path = []


class Storage_exceptions:
    """класс исключений, содержащий метод, проверяющий наполненнойсть хранилища и метод-обертку
    для проверки файлов перед открытием"""
    def check_storage(self, storage):
        if len(storage.file_names_with_path) == 0:
            raise BaseException("В хранилище еще нет файлов")
        return True

    def check_file(self, file_name):
        try:
            with open(str(file_name), 'r') as file:
                for line in file:
                    if int(line):
                        pass
            return file_name
        except:
            raise BaseException('Ошибка при открытии файла ', file_name)


storage = FilesStorage(os.path.abspath('files_storage') + '/files_storage')
file_operations = FileOperations(storage)
file_operations.fill_storage(15)
print(file_operations.summ_from_random_files())




