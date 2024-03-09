def insert(my_list, index, value):
    if index < 0 or index > len(my_list) - 1:
        print("Choose a valid index!!!")
        return
    my_list.insert(index, value)
    return my_list

#insert function adds a number to a specific index in the list
#my_list = it's the list that we want to add a number to it
#index = the index that we want to add a number to it
#value = the number that we want to add to the list