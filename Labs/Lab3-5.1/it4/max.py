def max(my_list, from_index, to_index):
    maxx = my_list[from_index]
    for index in range(from_index + 1, to_index + 1):
        if my_list[index] > maxx:
            maxx = my_list[index]
    return maxx