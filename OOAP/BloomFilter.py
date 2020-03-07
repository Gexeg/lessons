'''
abstract class BloomFilter<T>

    // КОНСТРУКТОР
    // постусловие: создан новый фильтр с длинной фильтра = f_len
    public BloomFilter<T> BloomFilter(int f_len);

    // КОМАНДА
    // поместить значение в фильтр
    // постусловие: значение помещено
    public void add(str value)

    // очистить фильтр
    // постусловие: фильтр очищен
    public void clear()

    // ЗАПРОС
    // значение присутствует?
    public bool in_filter(str value)
'''
from bitarray import bitarray


class BloomFilter():

    def __init__(self, f_len):
        self.filter_len = f_len
        self.clear()

    def clear(self):
        self.bitarray = bitarray(self.filter_len)
        self.bitarray.setall(0)

    def _hash1(self, str1):
        code = 0
        for c in str1:
            code += code * 17 + ord(c)
        return code % self.filter_len

    def _hash2(self, str1):
        code = 0
        for c in str1:
            code += code * 223 + ord(c)
        return code % self.filter_len

    def add(self, str1):
        self.bitarray[self._hash1(str1)] = 1
        self.bitarray[self._hash2(str1)] = 1

    def in_filter(self, str1):
        return self.bitarray[self._hash1(str1)] and self.bitarray[self._hash2(str1)]
