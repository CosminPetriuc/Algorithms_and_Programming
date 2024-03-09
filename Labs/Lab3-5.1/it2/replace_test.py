from it2.replace import replace

def test_replace():
    # Test replacing a single occurrence of the old value in the middle of the list
    my_list = [1, 2, 3, 2, 5]
    old_value = 2
    new_value = 4
    replace(my_list, old_value, new_value)
    assert my_list == [1, 4, 3, 2, 5]

    # Test replacing the old value that occurs at the beginning of the list
    my_list = [2, 3, 4, 2, 5]
    old_value = 2
    new_value = 1
    replace(my_list, old_value, new_value)
    assert my_list == [1, 3, 4, 2, 5]

    # Test replacing the old value at the end of the list
    my_list = [1, 2, 3, 4, 2]
    old_value = 2
    new_value = 5
    replace(my_list, old_value, new_value)
    assert my_list == [1, 2, 3, 4, 5]