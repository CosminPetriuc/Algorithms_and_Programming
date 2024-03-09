def sum(my_list, from_index, to_index):
    sum = 0
    for i in range(from_index, to_index+1):
        sum += my_list[i]
    return sum
