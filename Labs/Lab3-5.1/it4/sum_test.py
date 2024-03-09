from it4.sum import sum

def test_sum():
    # Test sum of a range with positive integers
    my_list = [1, 2, 3, 4, 5]
    from_index = 1
    to_index = 3
    result = sum(my_list, from_index, to_index)
    assert result == 9  # (2 + 3 + 4)

    # Test sum of a range with both positive and negative integers
    my_list = [-2, 0, 3, -1, 4]
    from_index = 0
    to_index = 4
    result = sum(my_list, from_index, to_index)
    assert result == 4  # (-2 + 0 + 3 - 1 + 4)

    # Test sum of a range with all negative integers
    my_list = [-1, -2, -3, -4, -5]
    from_index = 2
    to_index = 4
    result = sum(my_list, from_index, to_index)
    assert result == -12  # (-3 + -4 + -5)\