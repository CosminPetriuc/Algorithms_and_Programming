from it3.prime import get_primes_between_indices

def test_get_primes_between_indices():
    # Test a range containing no prime numbers
    my_list = [4, 6, 8, 9, 10]
    from_index = 0
    to_index = 5
    result = get_primes_between_indices(my_list, from_index, to_index)
    assert result == []

    # Test a range containing prime numbers
    my_list = [4, 7, 8, 11, 13]
    from_index = 1
    to_index = 4
    result = get_primes_between_indices(my_list, from_index, to_index)
    assert result == [7, 11, 13]

    # Test a range where both indices are out of bounds (should return an empty list)
    my_list = [4, 7, 8, 11, 13]
    from_index = -1
    to_index = 5
    result = get_primes_between_indices(my_list, from_index, to_index)
    assert result == []