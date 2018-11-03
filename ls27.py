from datetime import datetime
import hashlib, random


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
        nonce = random.randint(0, 100000)
        hash_data = (str(data_for_hashing) + str(nonce)).encode('utf-8')
        hash_code = hashlib.md5(hash_data).hexdigest()
        number_of_last_digits = len(self.hash_reference_last_digits)
        attempts_to_form_hash = 1
        while hash_code[-number_of_last_digits:] != self.hash_reference_last_digits:
            nonce = random.randint(0, 100000)
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
        self.hash_reference_last_digits += '0'
        return current_date

    def find_block_by_hash(self, necessary_hash):
        for block in self.chain:
            if block.hash == necessary_hash:
                return block
        return False

    def check_all_chain(self):
        for block in self.chain[1:]:
            hash_must_be = self.hash_fun_without_nonce(str(block.previous_block_hash) + str(block.data) + str(block.created_at) + str(block.index) + str(block.nonce))
            if hash_must_be != block.hash:
                damaged_block = block
                return damaged_block
        return True

bitcoin_killer = Blockchain('start chain')
bitcoin_killer.add_new_block('Hello, chain!')
bitcoin_killer.add_new_block('blah')
bitcoin_killer.add_new_block('blah-blah')
bitcoin_killer.add_new_block('blah-blah-blah')

for index in range(len(bitcoin_killer.chain)):
    print(' Данные блока: ',bitcoin_killer.chain[index].data)
    print(' хеш: ', bitcoin_killer.chain[index].hash)
    print(' Попыток на формирование хеша: ', bitcoin_killer.attempts_to_form_hash[index])
    print()

print(bitcoin_killer.check_all_chain())