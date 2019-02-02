from bitarray import bitarray

class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        # создаём битовый массив длиной f_len ...
        self.bitarray = bitarray(f_len)
        self.bitarray.setall(0)

    def hash1(self, str1):
        code = 0
        for c in str1:
            code += code * 17 + ord(c)
        return code % self.filter_len

    def hash2(self, str1):
        code = 0
        for c in str1:
            code += code * 223 + ord(c)
        return code % self.filter_len


    def add(self, str1):
        self.bitarray[self.hash1(str1)] = 1
        self.bitarray[self.hash2(str1)] = 1

    def is_value(self, str1):
        return self.bitarray[self.hash1(str1)] and self.bitarray[self.hash2(str1)]

