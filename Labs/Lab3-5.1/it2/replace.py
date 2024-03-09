def replace(my_list, old_value, new_value):
    for i in range(0, len(my_list)):
        if (my_list[i] == old_value):
            my_list[i] = new_value
            break