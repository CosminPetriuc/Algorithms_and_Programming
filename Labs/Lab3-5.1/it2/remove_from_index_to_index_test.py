from it2.remove_index_to_index import remove1

def test_remove_index_to_index():
    # Test when removing a range within the list
    my_list = [1, 2, 3, 4, 5]
    from_index = 1
    to_index = 3
    remove1(my_list, from_index, to_index)
    assert my_list == [1, 5]

    # Test when removing elements at the beginning of the list
    my_list = [1, 2, 3, 4, 5]
    from_index = 0
    to_index = 2
    remove1(my_list, from_index, to_index)
    assert my_list == [4, 5]

    # Test when removing elements at the end of the list
    my_list = [1, 2, 3, 4, 5]
    from_index = 3
    to_index = 4
    remove1(my_list, from_index, to_index)
    assert my_list == [1, 2, 3]