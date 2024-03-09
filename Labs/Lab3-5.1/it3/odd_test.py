from it3.odd import get_odd_numbers_between_indices

def test_get_odd_numbers_between_indices():
    # Test a range with odd numbers only
    my_list = [1, 3, 5, 7, 9]
    from_index = 1
    to_index = 4
    result = get_odd_numbers_between_indices(my_list, from_index, to_index)
    assert result == [3, 5, 7]

    # Test a range with even and odd numbers
    my_list = [2, 3, 6, 7, 10]
    from_index = 0
    to_index = 5
    result = get_odd_numbers_between_indices(my_list, from_index, to_index)
    assert result == [3, 7]

    # Test a range with no odd numbers
    my_list = [2, 4, 6, 8, 10]
    from_index = 0
    to_index = 5
    result = get_odd_numbers_between_indices(my_list, from_index, to_index)
    assert result == []