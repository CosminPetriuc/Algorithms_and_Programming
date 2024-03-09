from it2.remove_from_index import remove

def test_remove():
    # Test removing an element from the middle of the list
    my_list = [1, 2, 3, 4, 5]
    index = 2
    remove(my_list, index)
    assert my_list == [1, 2, 4, 5]

    # Test removing the first element
    my_list = [1, 2, 3, 4, 5]
    index = 0
    remove(my_list, index)
    assert my_list == [2, 3, 4, 5]

    # Test removing the last element
    my_list = [1, 2, 3, 4, 5]
    index = 4
    remove(my_list, index)
    assert my_list == [1, 2, 3, 4]