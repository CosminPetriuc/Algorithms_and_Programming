from it4.max import max

def test_max():
    # Test a range with positive integers
    my_list = [5, 7, 2, 9, 3, 12]
    from_index = 1
    to_index = 4
    result = max(my_list, from_index, to_index)
    assert result == 9  # Maximum value in the range (7, 2, 9, 3)

    # Test a range with both positive and negative integers
    my_list = [-5, -7, 0, 12, -3, -9]
    from_index = 1
    to_index = 5
    result = max(my_list, from_index, to_index)
    assert result == 12  # Maximum value in the range (-7, 0, 12, -3, -9)

    # Test a range with a single element
    my_list = [4]
    from_index = 0
    to_index = 0
    result = max(my_list, from_index, to_index)
    assert result == 4  # The single element is the maximum