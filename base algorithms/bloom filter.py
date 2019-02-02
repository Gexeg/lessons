from bitarray import bitarray

class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
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


bloom_filter = BloomFilter(32)

strings = ['0123456789', '1234567890', '2345678901','3456789012', '4567890123','5678901234',
           '6789012345','7890123456','8901234567','9012345678']

for i in strings:
    bloom_filter.add(i)

false_counter = 0
for i in strings:
    if bloom_filter.is_value(i) is False:
        false_counter +=1

print(false_counter)