from it1.add import add

def test_add():
    result1 = add(my_list=[1, 2, 3, 4], value=5)
    assert result1 == [1, 2, 3, 4, 5]
    print("Test 1 passed")

    result2 = add(my_list=[], value=1)
    assert result2 == [1]
    print("Test 2 passed")

    result3 = add(my_list=[1], value=2)
    assert result3 == [1, 2]
    print("Test 3 passed")
