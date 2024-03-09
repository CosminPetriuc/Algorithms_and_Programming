def get_odd_numbers_between_indices(my_list, from_index, to_index):
    odd_numbers = []
    for index in range(from_index, to_index):
        if from_index >= 0 and to_index < len(my_list):
            if my_list[index] % 2 != 0:
                odd_numbers.append(my_list[index])
    return odd_numbers