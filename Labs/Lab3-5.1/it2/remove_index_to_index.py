def remove1(my_list, from_index, to_index):
    result = []
    for i in range(0, from_index):
        result.append(my_list[i])
    for i in range(to_index + 1, len(my_list)):
        result.append(my_list[i])
    for i in range(0, len(result)):
        my_list[i] = result[i]
    i = len(my_list) - 1
    while len(my_list) != len(result):
        my_list.pop(i)
        i -= 1