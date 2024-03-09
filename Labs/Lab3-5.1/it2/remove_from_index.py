def remove(my_list, index):
    if index < 0 or index > len(my_list) - 1:
        print("Choose a valid index!!!")
        return
    my_list.pop(index)