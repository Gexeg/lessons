from datetime import datetime
import hashlib, random, timeit


class Block:
    def __init__(self):
        self.hash = None
        self.previous_block_hash = None
        self.index = None
        self.created_at = None
        self.data = None
        self.nonce = None


class Blockchain:
    def __init__(self, first_block_data):
        self.chain = []
        self.attempts_to_form_hash = []
        self.hash_reference_last_digits = '0'

        first_block = Block()
        first_block.hash = '00000'
        first_block.index = '1'
        first_block.created_at = datetime.now()
        first_block.data = str(first_block_data)

        self.chain.append(first_block)
        self.attempts_to_form_hash.append(1)

    def hash_fun_without_nonce(self, data_for_hashing):
        hash_data = str(data_for_hashing).encode('utf-8')
        hash_code = hashlib.md5(hash_data).hexdigest()
        return hash_code

    def hash_fun_with_nonce(self, data_for_hashing):
        nonce = random.random()
        hash_data = (str(data_for_hashing) + str(nonce)).encode('utf-8')
        hash_code = hashlib.md5(hash_data).hexdigest()
        number_of_last_digits = len(self.hash_reference_last_digits)
        attempts_to_form_hash = 1
        while hash_code[-number_of_last_digits:] != self.hash_reference_last_digits:
            nonce = random.random()
            hash_data = (str(data_for_hashing) + str(nonce)).encode('utf-8')
            hash_code = hashlib.md5(hash_data).hexdigest()
            attempts_to_form_hash += 1
        return nonce, hash_code, attempts_to_form_hash

    def add_new_block(self, data_for_block):
        current_date = datetime.now()
        previous_block_hash = self.chain[-1].hash
        new_block_index = len(self.chain) + 1
        data_for_hashing = str(previous_block_hash) + str(data_for_block) + str(current_date) + str(new_block_index)
        nonce_hash_attempts = self.hash_fun_with_nonce(data_for_hashing)

        new_block = Block()
        new_block.hash = nonce_hash_attempts[1]
        new_block.previous_block_hash = previous_block_hash
        new_block.index = new_block_index
        new_block.created_at = current_date
        new_block.data = data_for_block
        new_block.nonce = nonce_hash_attempts[0]

        self.chain.append(new_block)
        self.attempts_to_form_hash.append(nonce_hash_attempts[2])
        return current_date

    def find_block_by_hash(self, necessary_hash):
        for block in self.chain:
            if block.hash == necessary_hash:
                return block
        return False

    def find_damaged_block(self):
        for block in self.chain[1:]:
            hash_must_be = self.hash_fun_without_nonce(str(block.previous_block_hash) + str(block.data) + str(block.created_at) + str(block.index) + str(block.nonce))
            if hash_must_be != block.hash:
                damaged_block = block
                return damaged_block


bitcoin_killer = Blockchain('start chain')
time_for_add_block1 = timeit.Timer(lambda: bitcoin_killer.add_new_block('Hello, chain!')).timeit(number=100)
bitcoin_killer.hash_reference_last_digits = '00'
time_for_add_block2 = timeit.Timer(lambda: bitcoin_killer.add_new_block('blah')).timeit(number=100)
bitcoin_killer.hash_reference_last_digits = '000'
time_for_add_block3 = timeit.Timer(lambda: bitcoin_killer.add_new_block('blah-blah')).timeit(number=100)
bitcoin_killer.hash_reference_last_digits = '0000'
time_for_add_block4 = timeit.Timer(lambda: bitcoin_killer.add_new_block('blah-blah-blah')).timeit(number=100)
bitcoin_killer.hash_reference_last_digits = '00000'
time_for_add_block5 = timeit.Timer(lambda: bitcoin_killer.add_new_block('blah-blah-blah-blah')).timeit(number=10)

time_list = [0]
time_list.append(time_for_add_block1 / 100)
time_list.append(time_for_add_block2 / 100)
time_list.append(time_for_add_block3 / 100)
time_list.append(time_for_add_block4 / 100)
time_list.append(time_for_add_block5 / 10)
complexity = ''

for index in range(len(time_list)):
    print('При сложности',complexity, 'время формирования: ', time_list[index])
    print()
    complexity += '0'

print('Проверка цепи: ', bitcoin_killer.find_damaged_block())
