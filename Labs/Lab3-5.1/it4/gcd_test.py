from it4.gcd import get_gcd_between_indices

def test_get_gcd_between_indices():
    # Test a valid range with a GCD
    my_list = [12, 18, 24, 36, 48, 60]
    from_index = 1
    to_index = 4
    result = get_gcd_between_indices(my_list, from_index, to_index)
    assert result == 12

    # Test a valid range with no GCD (all numbers are coprime)
    my_list = [7, 11, 13, 17, 19]
    from_index = 0
    to_index = 4
    result = get_gcd_between_indices(my_list, from_index, to_index)
    assert result == 1

    # Test a valid range with a single element
    my_list = [5]
    from_index = 0
    to_index = 0
    result = get_gcd_between_indices(my_list, from_index, to_index)
    assert result == 5