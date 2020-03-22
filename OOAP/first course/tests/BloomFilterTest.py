import pytest
from BloomFilter import BloomFilter

def test_filter():
    bloom_filter = BloomFilter(32)

    strings = ['0123456789', '1234567890', '2345678901','3456789012', '4567890123','5678901234',
            '6789012345','7890123456','8901234567','9012345678']

    for string in strings:
        bloom_filter.add(string)

    for string in strings:
        assert bloom_filter.in_filter(string)
