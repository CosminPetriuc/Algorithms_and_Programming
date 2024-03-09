from it3.prime import get_primes_between_indices
from it4.sum import sum
from it1.add import add
from it1.insert import insert
from it2.remove_from_index import remove
from it2.remove_index_to_index import remove1
from it2.replace import replace
from it3.odd import get_odd_numbers_between_indices
from it4.max import max
from it4.gcd import get_gcd_between_indices
from it5.filter_prime import filter_prime

def read_from_file(file_name):
    data = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                try:
                    number = int(line.strip())
                    data.append(number)
                except ValueError:
                    print(f"Data in the file: {line.strip()}")
        return data
    except FileNotFoundError:
        print("File not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def write_to_file(file_name, data):
    try:
        with open(file_name, 'w') as file:
            for number in data:
                file.write(str(number) + "\n")
            print(f"Data written to {file_name}")
    except Exception as e:
        print(f"An error occurred: {e}")

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 0
while x != 14:
    print("1: Add a number at the end of the list." '\n'
          "2: Insert a number at the index." '\n'
          "3: Remove a number at the index." '\n'
          "4: Remove numbers between two given index." '\n'
          "5: Replace a number." '\n'
          "6: Get prime number between the two given index." '\n'
          "7: Get odd number between two given index." '\n'
          "8: Sum of elements between two given index." '\n'
          "9: Get greatest common divisor of elements between two given index." '\n'
          "10: Get maximum of elements between the two given index." '\n'
          "11: Keep only prime numbers and remove the other elements." '\n'
          "12: Read current list from file." '\n'
          "13: Write the current list to file." '\n'
          "0: Exit")
    x = int(input("Choose a option: "))
    if x == 1:
        value = int(input("Choose a value: "))
        add(my_list, value)
    elif x == 2:
        index = int(input("Choose an index: "))
        value = int(input("Choose a value: "))
        insert(my_list, index, value)
    elif x == 3:
        index = int(input("Choose an index: "))
        remove(my_list, index)
    elif x == 4:
        from_index = int(input("Choose an index: "))
        to_index = int(input("Choose another index: "))
        remove1(my_list, from_index, to_index)
    elif x == 5:
        old_value = int(input("Choose a value from list: "))
        new_value = int(input("Choose a new value: "))
        replace(my_list, old_value, new_value)
    elif x == 6:
        from_index = int(input("Choose an index:"))
        to_index = int(input("Choose another index: "))
        get_primes_between_indices(my_list, from_index, to_index)
    elif x == 7:
        from_index = int(input("Choose an index: "))
        to_index = int(input("Choose another index: "))
        get_odd_numbers_between_indices(my_list, from_index, to_index)
    elif x == 8:
        from_index = int(input("Choose an index: "))
        to_index = int(input("Choose another index: "))
        print("Sum is:",sum(my_list, from_index, to_index))
    elif x == 9:
        from_index = int(input("Choose an index: "))
        to_index = int(input("Choose another index: "))
        print("GCD is: ",get_gcd_between_indices(my_list, from_index, to_index))
    elif x == 10:
        from_index = int(input("Choose an index: "))
        to_index = int(input("Choose another index: "))
        print("Max is: ", max(my_list, from_index, to_index))
    elif x == 11:
        filter_prime(my_list)
    elif x == 12:
        file_name = "input.txt"
        my_list = read_from_file(file_name)
    elif x == 13:
        file_name = "output.txt"
        my_list = write_to_file(file_name, my_list)
    elif x == 0:
        exit(print("PaPaPa"))
    print(my_list)
