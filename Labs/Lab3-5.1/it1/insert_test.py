from it1.insert import insert

def test_insert():
    # Test inserting a value into the middle of the list
    my_list = [1, 2, 4, 5]
    index = 2
    value = 3
    result = insert(my_list, index, value)
    assert result == [1, 2, 3, 4, 5]

    # Test inserting a value at the beginning of the list
    my_list = [2, 3, 4, 5]
    index = 0
    value = 1
    result = insert(my_list, index, value)
    assert result == [1, 2, 3, 4, 5]

    # Test inserting a value at the end of the list
    my_list = [1, 2, 3, 4]
    index = 4
    value = 5
    result = insert(my_list, index, value)
    assert result == [1, 2, 3, 4, 5]